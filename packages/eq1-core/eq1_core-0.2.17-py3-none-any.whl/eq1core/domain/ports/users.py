from abc import ABC, abstractmethod
from typing import Protocol, List, Optional
from eq1core.domain.entities.users import User
from .common import CommonPort


class UserPort(CommonPort[User], Protocol):
    def get_user_by_id(self, user_id: int) -> Optional[User]:
        ...

    def get_all_users(self) -> List[User]:
        ...

    def create_user(self, user_data: dict) -> User:
        ...

    def update_user(self, user_id: int, user_data: dict) -> Optional[User]:
        ...

    def delete_user(self, user_id: int) -> bool:
        ...
