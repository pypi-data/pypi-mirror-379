# smeller/utils/events.py
from typing import Callable, Dict, List, Any

class Event:
    """Represents an event."""
    def __init__(self, name: str, data: Any = None):
        self.name = name
        self.data = data

class EventHandler:
    """Manages event subscriptions and publishing."""

    def __init__(self):
        self._subscribers: Dict[str, List[Callable[[Event], Any]]] = {}

    def subscribe(self, event_name: str, callback: Callable[[Event], Any]) -> None:
        """Subscribes a callback to an event."""
        if event_name not in self._subscribers:
            self._subscribers[event_name] = []
        self._subscribers[event_name].append(callback)

    def unsubscribe(self, event_name: str, callback: Callable[[Event], Any]) -> None:
        """Unsubscribes a callback from an event."""
        if event_name in self._subscribers:
            self._subscribers[event_name].remove(callback)

    async def publish(self, event: Event) -> None:
        """Publishes an event to all subscribers."""
        event_name = event.name
        if event_name in self._subscribers:
            for callback in self._subscribers[event_name]:
                try:
                    await callback(event)  # Вызываем асинхронно
                except Exception as e:
                    print(f"Error in event handler for {event_name}: {e}")