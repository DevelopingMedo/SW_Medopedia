from abc import ABC, abstractmethod

from src.medopedia.domain import MedopediaEntry


class MedopediaRepository(ABC):
    @abstractmethod
    def create_entry(self, entry: MedopediaEntry) -> None:
        pass

    @abstractmethod
    def get_entry(self, entry_id: str) -> MedopediaEntry:
        pass

    @abstractmethod
    def update_entry(self, entry: MedopediaEntry) -> None:
        pass

    @abstractmethod
    def delete_entry(self, entry_id: str) -> None:
        pass