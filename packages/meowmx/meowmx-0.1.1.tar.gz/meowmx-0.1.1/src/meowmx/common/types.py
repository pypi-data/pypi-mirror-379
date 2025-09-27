from dataclasses import dataclass
import typing as t

from sqlalchemy.orm import Session


@dataclass
class NewEvent:
    event_type: str
    json: t.Dict[str, t.Any]


@dataclass
class NewEventRow:
    aggregate_id: str
    event_type: str
    json: t.Dict[str, t.Any]
    version: int


@dataclass
class RecordedEvent:
    aggregate_type: str
    aggregate_id: str
    id: int
    event_type: str
    json: t.Dict[str, t.Any]
    tx_id: int
    version: int


@dataclass
class SubCheckpoint:
    last_tx_id: int
    last_event_id: int


SessionMaker = t.Callable[[], Session]

EventHandler = t.Callable[[Session, RecordedEvent], None]
