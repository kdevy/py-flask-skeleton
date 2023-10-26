import datetime
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.types import DateTime
from sqlalchemy import func, text
from bootstrap import db

class ManagementSheetRow(db.Model):
    __tablename__ = "management_sheet_row"

    id: Mapped[int] = mapped_column(primary_key=True)
    management_sheet_id: Mapped[int] = mapped_column(nullable=False, comment="管理表ID")
    sort: Mapped[int] = mapped_column(nullable=False, server_default="1", comment="並び順")
    creator_id: Mapped[int] = mapped_column(nullable=True, comment="作成者ID")
    updator_id: Mapped[int] = mapped_column(nullable=True, comment="更新者ID")
    created_dt: Mapped[datetime.datetime] = mapped_column(DateTime, nullable=False, server_default=func.now(), comment="作成日時")
    updated_dt: Mapped[datetime.datetime] = mapped_column(DateTime, nullable=True, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"), comment="更新日時")
