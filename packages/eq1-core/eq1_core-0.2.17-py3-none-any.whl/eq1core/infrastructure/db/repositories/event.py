from sqlalchemy import and_
from datetime import datetime
from typing import List, Optional
from eq1core.logger import AppLogger
from eq1core.infrastructure.db import SessionLocal
from eq1core.infrastructure.db.repositories.common import CommonRepo
from eq1core.infrastructure.db.models import EventModel, EventUserType, EventStatusType
from eq1core.infrastructure.db.mapper import to_domain


class EventRepo(CommonRepo):
    db_session = SessionLocal
    model = EventModel

    @classmethod
    @to_domain
    def create_new_event(cls,
                         command: str,
                         data: str):
        with cls.db_session() as session:
            event = EventModel(
                command=command,
                data=data,
                status=EventStatusType.WAIT.value,
                publisher=EventUserType.INSPECTION.value,
                subscriber=EventUserType.CLIENT.value,
                created_at=datetime.now(),
                updated_at=datetime.now()
            )

            session.add(event)
            session.commit()

            return event

    @classmethod
    @to_domain
    def get_all(cls, hide_done: bool = True, hide_deleted: bool = True) -> List[EventModel]:
        with cls.db_session() as session:
            query_filters = []

            if hide_done:
                query_filters.append(EventModel.status != 'DONE')
                query_filters.append(EventModel.status != 'done')
                # TODO : notin_ ['DONE', 'done'] 구문으로 변경. 테스트 필요.

            if hide_deleted:
                query_filters.append(EventModel.is_deleted == 0)

            return session.query(EventModel).filter(and_(True, *query_filters)).all()

    @classmethod
    @to_domain
    def get_new_events(cls, target: str = "inspection") -> List[EventModel]:
        try:
            with cls.db_session() as session:
                query_filters = [
                    EventModel.status == EventStatusType.WAIT.value,
                    EventModel.subscriber == target
                ]

                events = session.query(EventModel).order_by(
                    EventModel.id.desc()
                ).filter(and_(True, *query_filters)).all()

                return events

        except Exception as e:
            AppLogger.write_error(cls, f"get_new_events. Error : {e}")
            return []

    @classmethod
    @to_domain
    def mark_done_event(cls, event_id: int):
        with cls.db_session() as session:
            event = session.query(EventModel).filter(EventModel.id == event_id).first()
            event.status = EventStatusType.DONE.value
            session.commit()

            return event

    @classmethod
    @to_domain
    def mark_fail_event(cls, event_id: int):
        with cls.db_session() as session:
            event = session.query(EventModel).filter(EventModel.id == event_id).first()
            event.status = EventStatusType.FAIL.value
            session.commit()

            return event

    # @classmethod
    # def mock_reset_summary(cls):
    #     import json
    #     from app.ui_event.event import UIEventCommand
    #     with cls.db_session() as session:
    #         event = EventModel(
    #             command=str(UIEventCommand.RESET_SUMMARY.name),
    #             data=json.dumps({"time": f"{datetime.now()}"}),
    #             status=EventStatusType.WAIT.value,
    #             publisher=EventUserType.CLIENT.value,
    #             subscriber=EventUserType.INSPECTION.value,
    #             created_at=datetime.now(),
    #             updated_at=datetime.now()
    #         )

    #         session.add(event)
    #         session.commit()

    #         return event

    # @classmethod
    # def get_last_reset_summary_time(cls) -> Optional[datetime]:
    #     from app.ui_event.event import UIEventCommand
    #     with cls.db_session() as session:
    #         query_filters = [EventModel.command == str(UIEventCommand.RESET_SUMMARY.name)]
    #         event = session.query(EventModel).filter(and_(*query_filters)).order_by(EventModel.id.desc()).first()

    #         if event is None:
    #             return None

    #         return event.created_at
