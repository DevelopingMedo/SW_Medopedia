from sqlalchemy import Column, Integer, String, Date, ForeignKey, Enum
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class MedopediaEntry(Base):
    __tablename__ = 'medopedia_entry'
    id = Column(Integer, primary_key=True)
    type = Column(Enum('character', 'planet', name='entry_type'))
    created_at = Column(Date)
    description = Column(String)
