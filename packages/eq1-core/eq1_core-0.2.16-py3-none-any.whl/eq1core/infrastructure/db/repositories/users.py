
from eq1core.infrastructure.db import SessionLocal
from eq1core.infrastructure.db.models import UserModel
from eq1core.infrastructure.db.repositories.common import CommonRepo


class UserRepo(CommonRepo):
    db_session = SessionLocal
    model = UserModel
