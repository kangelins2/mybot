from sqlalchemy.orm import declarative_base, Mapped, mapped_column

Base = declarative_base()

class BaseORM(Base):
    __abstract__ = True


class Email(BaseORM):
    __tablename__ = '__emails__'

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str]
