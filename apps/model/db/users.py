from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from apps.model import Base

class Users(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, index=True,
                                    autoincrement=True)
    name: Mapped[str] = mapped_column(String(64))
    cash_balance: Mapped[float]
