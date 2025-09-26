from sqlalchemy import and_
from typing import List, Optional
from eq1core.infrastructure.db import SessionLocal
from eq1core.infrastructure.db.models import VisionPresetModel
from eq1core.infrastructure.db.repositories.common import CommonRepo


class VisionPresetRepo(CommonRepo):
    db_session = SessionLocal
    model = VisionPresetModel
