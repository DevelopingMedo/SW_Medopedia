from sqlalchemy import Column, Integer, ForeignKey, String, Date

from src.medopedia.domain.MedopediaEntry import MedopediaEntry


class Planet(MedopediaEntry):
    __tablename__ = 'planet'
    id = Column(Integer, ForeignKey('medopedia_entries.id'), primary_key=True)
    name = Column(String)
    min_temperature = Column(String)
    max_temperature = Column(Date)
    __mapper_args__ = {
        'polymorphic_identity': 'planet'
    }
