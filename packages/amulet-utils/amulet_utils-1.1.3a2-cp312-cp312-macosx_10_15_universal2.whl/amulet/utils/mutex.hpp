#pragma once

#include <chrono>
#include <condition_variable>
#include <list>
#include <map>
#include <mutex>
#include <optional>
#include <stdexcept>
#include <string>
#include <thread>
#include <tuple>
#include <type_traits>

#include <amulet/utils/dll.hpp>
#include <amulet/utils/task_manager/cancel_manager.hpp>

namespace {

template <template <typename...> class Template, typename T>
struct is_specialization_of : std::false_type { };

template <template <typename...> class Template, typename... Args>
struct is_specialization_of<Template, Template<Args...>> : std::true_type { };

}

namespace Amulet {

// An exception raised in some deadlock cases.
class AMULET_UTILS_EXPORT_EXCEPTION Deadlock : public std::runtime_error {
public:
    using std::runtime_error::runtime_error;
    Deadlock()
        : Deadlock("Deadlock")
    {
    }
};

enum class ThreadAccessMode {
    Read, // This thread can only read.
    ReadWrite // This thread can read and write.
};

enum class ThreadShareMode {
    Unique, // Other threads can't run in parallel.
    SharedReadOnly, // Other threads can only read in parallel.
    SharedReadWrite // Other threads can read and write in parallel.
};

// This is a custom mutex implementation that prioritises acquisition order and allows parallelism where possible.
// The acquirer can define the required permissions for this thread and permissions for other parallel threads.
// It also supports cancelling waiting through a CancelManager instance.
// The mutex is compatible with std::lock_guard, std::unique_lock and std::shared_lock.
class OrderedMutex {
protected:
    using LockMode = std::pair<ThreadAccessMode, ThreadShareMode>;
    struct ThreadState {
        std::thread::id id;
        std::optional<LockMode> state; // The current lock mode. Empty if unlocked.
    };

    std::mutex mutex;
    std::condition_variable condition;
    // The number of threads that are reading
    size_t read_count = 0;
    // The number of threads that are writing
    size_t write_count = 0;
    // The number of locked threads blocking reading
    size_t blocking_read_count = 0;
    // The number of locked threads blocking writing
    size_t blocking_write_count = 0;
    // The threads that currently hold the lock.
    std::list<ThreadState> locked_threads;
    // The pending threads in the order the lock call was made.
    std::list<ThreadState> pending_threads;
    // Lookup from thread id to the iterator in locked_threads or pending_thread.
    std::map<std::thread::id, std::list<ThreadState>::iterator> threads;

    template <
        bool ReturnBool,
        bool Blocking,
        ThreadAccessMode DesiredThreadAccessMode,
        ThreadShareMode DesiredThreadShareMode,
        class... Args>
    std::conditional_t<ReturnBool, bool, void> _lock_imp(Args... args_pack)
    {
        // Lock the state.
        std::unique_lock lock(mutex);

        // Get the thread id
        auto id = std::this_thread::get_id();

        // Check for a deadlock.
        if (threads.find(id) != threads.end()) {
            throw Deadlock("Deadlock encountered.");
        }

        auto is_needed_self_state = [&]() -> bool {
            if constexpr (DesiredThreadAccessMode == ThreadAccessMode::Read) {
                return blocking_read_count == 0;
            } else {
                static_assert(DesiredThreadAccessMode == ThreadAccessMode::ReadWrite);
                return blocking_write_count == 0;
            }
        };

        auto is_needed_other_state = [&]() -> bool {
            if constexpr (DesiredThreadShareMode == ThreadShareMode::Unique) {
                return read_count == 0;
            } else if constexpr (DesiredThreadShareMode == ThreadShareMode::SharedReadOnly) {
                return write_count == 0;
            } else {
                static_assert(DesiredThreadShareMode == ThreadShareMode::SharedReadWrite);
                return true;
            }
        };

        // Is mutex in a lockable state.
        auto is_needed_state = [&]() -> bool {
            return is_needed_self_state() && is_needed_other_state();
        };

        auto set_state = [&]() {
            if constexpr (DesiredThreadAccessMode == ThreadAccessMode::Read) {
                read_count++;
            } else {
                static_assert(DesiredThreadAccessMode == ThreadAccessMode::ReadWrite);
                read_count++;
                write_count++;
            }
            if constexpr (DesiredThreadShareMode == ThreadShareMode::Unique) {
                blocking_read_count++;
                blocking_write_count++;
            } else if constexpr (DesiredThreadShareMode == ThreadShareMode::SharedReadOnly) {
                blocking_write_count++;
            } else {
                static_assert(DesiredThreadShareMode == ThreadShareMode::SharedReadWrite);
            }
        };

        if (pending_threads.empty() && is_needed_state()) {
            // mutex can be locked without blocking. Lock it.
            set_state();
            auto it = locked_threads.insert(locked_threads.end(), { id, std::make_pair(DesiredThreadAccessMode, DesiredThreadShareMode) });
            threads.emplace(id, it);
            if constexpr (ReturnBool) {
                return true;
            }
        } else if constexpr (Blocking) {
            // Wait until the mutex can be locked.

            // Unpack the args
            auto args = std::tie(args_pack...);
            AbstractCancelManager& cancel_manager = std::get<std::tuple_size_v<decltype(args)> - 1>(args);

            // Create the lock state
            auto it = pending_threads.insert(pending_threads.end(), { id, std::nullopt });
            threads.emplace(id, it);

            auto is_lockable = [&]() -> bool {
                return pending_threads.begin() == it && is_needed_state();
            };

            // If the state does not get locked it must be erased.
            auto erase_state = [&]() -> void {
                threads.erase(it->id);
                pending_threads.erase(it);

                // Notify other threads if the top pending thread changes.
                if (it == pending_threads.begin()) {
                    condition.notify_all();
                }
            };

            // Function to lock the mutex.
            auto lock_state = [&]() -> void {
                // Update the mutex state
                set_state();

                // Move the thread state
                locked_threads.splice(locked_threads.end(), pending_threads, pending_threads.begin());
                it->state = std::make_pair(DesiredThreadAccessMode, DesiredThreadShareMode);

                // Notify other threads that the top pending thread changed.
                condition.notify_all();
            };

            auto token = cancel_manager.register_cancel_callback([&]() -> void {
                condition.notify_all();
            });

            auto unregister_cancel = [&]() -> void {
                cancel_manager.unregister_cancel_callback(token);
            };

            if constexpr (ReturnBool) {
                static_assert(std::tuple_size_v<decltype(args)> == 2);
                const auto& timeout = std::get<0>(args);
                using TimeoutT = std::remove_cvref_t<decltype(timeout)>;

                auto wait = [&](std::unique_lock<std::mutex>& _lck, decltype(timeout) _timeout, std::function<bool()> _pred) -> bool {
                    if constexpr (is_specialization_of<std::chrono::duration, TimeoutT>::value) {
                        return condition.wait_for(_lck, _timeout, _pred);
                    } else {
                        static_assert(is_specialization_of<std::chrono::time_point, TimeoutT>::value);
                        return condition.wait_until(_lck, _timeout, _pred);
                    }
                };

                auto result = wait(lock, timeout, [&] { return cancel_manager.is_cancel_requested() || is_lockable(); });
                unregister_cancel();
                if (result && !cancel_manager.is_cancel_requested()) {
                    lock_state();
                    return true;
                } else {
                    erase_state();
                    return false;
                }
            } else {
                // Wait until this is at the top of the queue and the mutex is unlocked.
                condition.wait(lock,
                    [&] {
                        if (cancel_manager.is_cancel_requested()) {
                            erase_state();
                            unregister_cancel();
                            throw TaskCancelled();
                        }
                        return is_lockable(); });

                unregister_cancel();
                lock_state();
            }
        } else if constexpr (ReturnBool) {
            return false;
        }
    }

    template <bool ReturnBool, bool Blocking, ThreadAccessMode DesiredThreadAccessMode, ThreadShareMode DesiredThreadShareMode, class... TimeoutTs>
    std::conditional_t<ReturnBool, bool, void> _lock(TimeoutTs... timeout, AbstractCancelManager& cancel_manager)
    {
        return _lock_imp<ReturnBool, Blocking, DesiredThreadAccessMode, DesiredThreadShareMode, TimeoutTs..., AbstractCancelManager&>(timeout..., cancel_manager);
    }

    template <bool ReturnBool, bool Blocking, ThreadAccessMode DesiredThreadAccessMode, ThreadShareMode DesiredThreadShareMode>
    std::conditional_t<ReturnBool, bool, void> _lock()
    {
        return _lock_imp<ReturnBool, Blocking, DesiredThreadAccessMode, DesiredThreadShareMode>();
    }

public:
    // Constructors
    OrderedMutex() = default;
    OrderedMutex(const OrderedMutex&) = delete;
    OrderedMutex(OrderedMutex&&) = delete;

    // Destructor
    ~OrderedMutex() = default;

    // Locks the mutex in the requested mode (default is read write unique).
    // Blocks until the mutex is acquired or the task is cancelled through the cancel manager.
    // If the task is cancelled before the mutex is acquired, TaskCancelled is thrown.
    // Thread safe.
    template <ThreadAccessMode DesiredThreadAccessMode = ThreadAccessMode::ReadWrite, ThreadShareMode DesiredThreadShareMode = ThreadShareMode::Unique>
    void lock(AbstractCancelManager& cancel_manager = global_VoidCancelManager)
    {
        _lock<false, true, DesiredThreadAccessMode, DesiredThreadShareMode>(cancel_manager);
    }

    // Tries to lock the mutex in the requested mode (default is read write unique).
    // Immediately returns true if the mutex was locked and false if it wasn't.
    // Thread safe
    template <ThreadAccessMode DesiredThreadAccessMode = ThreadAccessMode::ReadWrite, ThreadShareMode DesiredThreadShareMode = ThreadShareMode::Unique>
    bool try_lock()
    {
        return _lock<true, false, DesiredThreadAccessMode, DesiredThreadShareMode>();
    }

    // Like try_lock but with a timeout duration.
    // Returns true if the mutex was locked and false if it was not locked within the duration or if the task was cancelled.
    // Thread safe.
    template <ThreadAccessMode DesiredThreadAccessMode = ThreadAccessMode::ReadWrite, ThreadShareMode DesiredThreadShareMode = ThreadShareMode::Unique, class Rep, class Period>
    bool try_lock_for(const std::chrono::duration<Rep, Period>& timeout_duration, AbstractCancelManager& cancel_manager = global_VoidCancelManager)
    {
        return _lock<true, true, DesiredThreadAccessMode, DesiredThreadShareMode, const std::chrono::duration<Rep, Period>&>(timeout_duration, cancel_manager);
    }

    // Like try_lock but with a timeout time.
    // Returns true if the mutex was locked and false if it was not locked before the timeout time or if the task was cancelled.
    // Thread safe.
    template <ThreadAccessMode DesiredThreadAccessMode = ThreadAccessMode::ReadWrite, ThreadShareMode DesiredThreadShareMode = ThreadShareMode::Unique, class Clock, class Duration>
    bool try_lock_until(const std::chrono::time_point<Clock, Duration>& timeout_time, AbstractCancelManager& cancel_manager = global_VoidCancelManager)
    {
        return _lock<true, true, DesiredThreadAccessMode, DesiredThreadShareMode, const std::chrono::time_point<Clock, Duration>&>(timeout_time, cancel_manager);
    }

    // Unlock the mutex.
    // Must be called by the thread that locked it.
    // Thread safe.
    void unlock()
    {
        // Lock the state.
        std::unique_lock lock(mutex);

        // Get the thread id
        auto id = std::this_thread::get_id();

        // Find the thread state
        auto it = threads.find(id);

        // Ensure that the mutex is locked in the same mode by the thread.
        if (it == threads.end() || !it->second->state.has_value()) {
            throw std::runtime_error("This mutex is not locked by this thread.");
        }

        switch (it->second->state->first) {
        case ThreadAccessMode::Read:
            read_count--;
            break;
        case ThreadAccessMode::ReadWrite:
            read_count--;
            write_count--;
            break;
        default:
            break;
        }

        switch (it->second->state->second) {
        case ThreadShareMode::Unique:
            blocking_read_count--;
            blocking_write_count--;
            break;
        case ThreadShareMode::SharedReadOnly:
            blocking_write_count--;
            break;
        default:
            break;
        }

        // Remove the thread state
        locked_threads.erase(it->second);
        threads.erase(it);

        // Wake up pending threads
        condition.notify_all();
    }

    // SharedTimedLockable

    // An alias to lock<ThreadAccessMode::Read, ThreadShareMode::SharedReadOnly>
    void lock_shared()
    {
        lock<ThreadAccessMode::Read, ThreadShareMode::SharedReadOnly>();
    }

    // An alias to try_lock<ThreadAccessMode::Read, ThreadShareMode::SharedReadOnly>
    bool try_lock_shared()
    {
        return try_lock<ThreadAccessMode::Read, ThreadShareMode::SharedReadOnly>();
    }

    // An alias to unlock
    void unlock_shared()
    {
        unlock();
    }

    // An alias to try_lock_for<ThreadAccessMode::Read, ThreadShareMode::SharedReadOnly>
    template <class Rep, class Period>
    bool try_lock_shared_for(const std::chrono::duration<Rep, Period>& timeout_duration, AbstractCancelManager& cancel_manager = global_VoidCancelManager)
    {
        return try_lock_for<ThreadAccessMode::Read, ThreadShareMode::SharedReadOnly, Rep, Period>(timeout_duration, cancel_manager);
    }

    // An alias to try_lock_until<ThreadAccessMode::Read, ThreadShareMode::SharedReadOnly>
    template <class Clock, class Duration>
    bool try_lock_shared_until(const std::chrono::time_point<Clock, Duration>& timeout_time, AbstractCancelManager& cancel_manager = global_VoidCancelManager)
    {
        return try_lock_until<ThreadAccessMode::Read, ThreadShareMode::SharedReadOnly, Clock, Duration>(timeout_time, cancel_manager);
    }
};

template <
    ThreadAccessMode DesiredThreadAccessMode = ThreadAccessMode::ReadWrite,
    ThreadShareMode DesiredThreadShareMode = ThreadShareMode::Unique>
class OrderedLockGuard {
private:
    OrderedMutex& mutex;

public:
    OrderedLockGuard(OrderedMutex& mutex)
        : mutex(mutex)
    {
        mutex.lock<DesiredThreadAccessMode, DesiredThreadShareMode>();
    }
    ~OrderedLockGuard()
    {
        mutex.unlock();
    }
};

} // namespace Amulet
