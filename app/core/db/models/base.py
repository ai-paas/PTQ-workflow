import uuid

from sqlalchemy import orm


class Base(orm.DeclarativeBase):
    """
    Base datebase model
    """

    pk: orm.Mapped[uuid.UUID] = orm.mapped_column(
        primary_key=True,
        default=uuid.uuid4,
    )
