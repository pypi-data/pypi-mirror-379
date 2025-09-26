from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional
from passlib.hash import sha256_crypt


@dataclass
class User:
    id: int
    created_at: datetime = field(default_factory=datetime.now)
    last_login_at: datetime = field(default_factory=datetime.now)
    login_id: str = field(default="")
    position: str = field(default="직원")
    name: str = field(default="")
    password: str = field(default="")
    is_active: int = field(default=1)
    permission: str = field(default="worker")
    password_valid_by: Optional[datetime] = None
    password_reuse_count: int = field(default=0)
    is_temporary: int = field(default=0)
    audit_logs: List = field(default_factory=list)

    # Password encryption function
    @property
    def hashed_password(self):
        return sha256_crypt.encrypt(self.password)

    @hashed_password.setter
    def hashed_password(self, raw_password):
        self.password = sha256_crypt.encrypt(raw_password)

    # Password verification
    def verify_password(self, password):
        return sha256_crypt.verify(password, self.password)

    def __repr__(self):
        return f"<User(name={self.name}, login_id={self.login_id})>"
