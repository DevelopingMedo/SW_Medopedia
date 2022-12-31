from dataclasses import dataclass
from typing import Any

from sqlalchemy import Column, Integer, ForeignKey, String, Date, Boolean

from src.medopedia.domain.MedopediaEntry import MedopediaEntry


@dataclass
class Character(MedopediaEntry):
    __tablename__ = 'character'
    id = Column(Integer, ForeignKey('medopedia_entry.id'), primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    date_of_birth = Column(Date)
    is_before_battle_of_yavin = Column(Boolean)

    __mapper_args__ = {
        'polymorphic_identity': 'character'
    }

    def __init__(self, first_name, last_name, date_of_birth, is_before_battle_of_yavin):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.is_before_battle_of_yavin = is_before_battle_of_yavin
        self.first_name = first_name
