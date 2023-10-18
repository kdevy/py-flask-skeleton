import datetime
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.types import DateTime, String
from sqlalchemy import func, text
from bootstrap import db
from flask_login import UserMixin

class User(UserMixin, db.Model):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(256))
    email: Mapped[str] = mapped_column(String(256))
    password: Mapped[str] = mapped_column(String(256))
    created_dt: Mapped[datetime.datetime] = mapped_column(DateTime, nullable=False, server_default=func.now())
    updated_dt: Mapped[datetime.datetime] = mapped_column(DateTime, nullable=True, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
