from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Float, DateTime
from datetime import datetime

class Base(DeclarativeBase):
    pass

class Comidas(Base):
    __tablename__ = 'alimentos'
    id: Mapped[int] = mapped_column(primary_key=True)
    nome_alimento: Mapped[str] = mapped_column(String(255))
    preparo: Mapped[str] = mapped_column(String(255))
    kcal: Mapped[float] = mapped_column(Float)
    proteina: Mapped[float] = mapped_column(Float)
    lipidios: Mapped[float] = mapped_column(Float)
    carboidratos: Mapped[float] = mapped_column(Float)
    fibra: Mapped[float] = mapped_column(Float)

class Refeicao(Base):
    __tablename__ = 'refeicao'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    data_horario: Mapped[datetime] = mapped_column(DateTime)
    comidas: Mapped[str] = mapped_column(String(255), nullable=True)
    proteina: Mapped[float] = mapped_column(Float, nullable=True)
    lipidios: Mapped[float] = mapped_column(Float, nullable=True)
    carboidratos: Mapped[float] = mapped_column(Float, nullable=True)
    fibra: Mapped[float] = mapped_column(Float, nullable=True)
    total_caloria: Mapped[float] = mapped_column(Float)
