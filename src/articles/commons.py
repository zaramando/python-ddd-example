from typing import List

import pydantic


class ValueObject(pydantic.BaseModel):
    class Config:
        frozen = True


class Request(pydantic.BaseModel):
    class Config:
        frozen = True


class DomainEvent(pydantic.BaseModel):
    ...


class AggregateRoot(pydantic.BaseModel):
    _events: List[DomainEvent]

    def record_event(self, event: DomainEvent) -> None:
        self._events.append(event)

    def pull_events(self) -> List[DomainEvent]:
        events = self._events.copy()
        self._events.clear()
        return events

