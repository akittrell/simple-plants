from sqlalchemy import Column, Integer, String

from base import Base


class Plants(Base):
    __tablename__ = "plants"

    id = Column(Integer, primary_key=True)
    common_name = Column(String, index=True)
    genus = Column(String)
    family_name = Column(String)
