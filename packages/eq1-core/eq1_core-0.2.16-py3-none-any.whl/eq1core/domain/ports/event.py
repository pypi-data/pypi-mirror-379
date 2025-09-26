from datetime import datetime
from typing import List, Optional, Protocol, Dict
from abc import ABC, abstractmethod
from eq1core.domain.entities.event import Event
from eq1core.domain.ports.common import CommonPort


class EventPort(CommonPort[Event], Protocol):
    def create_new_event(self, command: str, data: str) -> Event:
        ...

    def get_all(self, hide_done: bool = True, hide_deleted: bool = True) -> List[Event]:
        ...

    def get_new_events(self, target: str = "inspection") -> List[Event]:
        ...

    def mark_done_event(self, event_id: int) -> Optional[Event]:
        ...

    def mark_fail_event(self, event_id: int) -> Optional[Event]:
        ...

    def mock_reset_summary(self) -> Event:
        ...

    def get_last_reset_summary_time(self) -> Optional[datetime]:
        ...
