from sqlalchemy import Column, Integer, ForeignKey, String, Date

from src.medopedia.domain.MedopediaEntry import MedopediaEntry


class Vehicle(MedopediaEntry):
    __tablename__ = 'vehicle'
    id = Column(Integer, ForeignKey('medopedia_entries.id'), primary_key=True)
    model_name = Column(String)
    manufacturer = Column(String)
    date_of_birth = Column(Date)
    __mapper_args__ = {
        'polymorphic_identity': 'vehicle'
    }
