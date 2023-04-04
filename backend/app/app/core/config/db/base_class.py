from sqlalchemy.ext.declarative import declarative_base, declared_attr

@declarative_base()
class Base:
    id: Any
    __name__: str
    # Automatically generated __tablename__
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()
