from collections import deque
from threading import RLock
from typing import Callable, Deque, Dict, List, Type

from loguru import logger

from .common import BaseCallback, Event, FunctionTypes

logger.remove()
moduvent_logger = logger.bind(source="moduvent_sync")


class Callback(BaseCallback):
    def call(self):
        if self.func_type in [
            FunctionTypes.BOUND_METHOD,
            FunctionTypes.FUNCTION,
            FunctionTypes.STATICMETHOD,
        ]:
            self.func(self.event)
        else:
            moduvent_logger.exception(
                f"Unknown function type for {self.func.__qualname__}"
            )

    def copy(self):
        # shallow copy
        return Callback(func=self.func, event=self.event)

    def __eq__(self, value):
        if isinstance(value, Callback):
            return self.func == value.func and self.event == value.event
        return super().__eq__(value)


# We say that a subscription is the information that a method wants to be called back
# and a registration is the process of adding a method to the list of callbacks for a particular event.
class EventManager:
    def __init__(self):
        self._subscriptions: Dict[Type[Event], List[Callback]] = {}
        self._callqueue: Deque[Callback] = deque()
        self._subscription_lock = RLock()
        self._callqueue_lock = RLock()

    def _verbose_callqueue(self):
        moduvent_logger.debug(f"Callqueue ({len(self._callqueue)}):")
        for callback in self._callqueue:
            moduvent_logger.debug(f"\t{callback}")

    def _process_callqueue(self):
        moduvent_logger.debug("Processing callqueue...")
        with self._callqueue_lock:
            while self._callqueue:
                callback = self._callqueue.popleft()
                moduvent_logger.debug(f"Calling {callback}")
                try:
                    callback.call()
                except Exception as e:
                    moduvent_logger.exception(f"Error while processing callback: {e}")
                    continue
        moduvent_logger.debug("End processing callqueue.")

    def _register_callback(self, callback: Callback):
        with self._subscription_lock:
            self._subscriptions.setdefault(callback.event, []).append(callback)

    def verbose_subscriptions(self):
        moduvent_logger.debug("Subscriptions:")
        for event_type, callbacks in self._subscriptions.items():
            moduvent_logger.debug(f"{event_type.__qualname__} ({len(callbacks)}):")
            for callback in callbacks:
                moduvent_logger.debug(f"\t{callback}")

    def register(self, func: Callable[[Event], None], event_type: Type[Event]):
        callback = Callback(func=func, event=event_type)
        self._register_callback(callback)
        moduvent_logger.debug(f"Registered {callback}")

    def subscribe(self, *event_types: Type[Event]):
        """This is used as a decorator to register a simple function."""

        def decorator(func: Callable[[Event], None]):
            for event_type in event_types:
                self.register(func=func, event_type=event_type)
            return func

        return decorator

    def remove_callback(self, func: Callable[[Event], None], event_type: Type[Event]):
        """Remove a callback from the list of subscriptions."""
        if event_type not in self._subscriptions:
            return
        with self._subscription_lock:
            for callback in self._subscriptions.get(event_type, []):
                if callback.func == func:
                    self._subscriptions[event_type].remove(callback)
                    moduvent_logger.debug(f"Removed {callback}")

    def remove_function(self, func: Callable[[Event], None]):
        """Remove all callbacks for a function."""
        with self._subscription_lock:
            for callbacks in self._subscriptions.values():
                for callback in callbacks:
                    if callback.func == func:
                        callbacks.remove(callback)
        moduvent_logger.debug(f"Removed all callbacks for {func}")

    def clear_event_type(self, event_type: Type[Event]):
        with self._subscription_lock:
            if event_type in self._subscriptions:
                del self._subscriptions[event_type]
                moduvent_logger.debug(f"Cleared all subscriptions for {event_type}")

    def emit(self, event: Event):
        event_type = type(event)
        moduvent_logger.debug(f"Emitting {event}")

        if event_type in self._subscriptions:
            callbacks = self._subscriptions[event_type]
            moduvent_logger.debug(
                f"Processing {event_type.__qualname__} ({len(callbacks)} callbacks)"
            )
            for callback in callbacks:
                callback_copy = callback.copy()
                callback_copy.event = event
                self._callqueue.append(callback_copy)

            self._verbose_callqueue()
            self._process_callqueue()


def subscribe_method(*event_types: List[Type[Event]]):
    """Tag the method with subscription info."""
    # Validate that all event_types are subclasses of Event
    for event_type in event_types:
        if not isinstance(event_type, type) or not issubclass(event_type, Event):
            raise TypeError(
                f"subscribe_method decorator expects Event subclasses, got {event_type!r}."
            )

    def decorator(func):
        if not hasattr(func, "_subscriptions"):
            func._subscriptions = []  # note that function member does not support type hint
        func._subscriptions.extend(event_types)
        moduvent_logger.debug(f"{func.__qualname__}._subscriptions = {event_types}")
        return func

    return decorator


class EventMeta(type):
    """Define a new class with events info gathered after class creation."""

    def __new__(cls, name, bases, attrs):
        new_class = super().__new__(cls, name, bases, attrs)

        _subscriptions: Dict[Type[Event], List[Callable[[Event], None]]] = {}
        for attr_name, attr_value in attrs.items():
            # find all subscriptions of methods
            if hasattr(attr_value, "_subscriptions"):
                for event_type in attr_value._subscriptions:
                    _subscriptions.setdefault(event_type, []).append(attr_value)

        new_class._subscriptions = _subscriptions
        return new_class


class EventAwareBase(metaclass=EventMeta):
    """The base class that utilize the metaclass."""

    def __init__(self, event_manager):
        self.event_manager: EventManager = event_manager
        # trigger registrations
        self._register()

    def _register(self):
        moduvent_logger.debug(f"Registering callbacks of {self}...")
        for event_type, funcs in self._subscriptions.items():
            for func in funcs:
                callback = Callback(func=getattr(self, func.__name__), event=event_type)
                self.event_manager._register_callback(callback)
