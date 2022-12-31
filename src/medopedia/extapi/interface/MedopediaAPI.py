from abc import ABC, abstractmethod


class MedopediaAPI(ABC):
    @abstractmethod
    def search_for_character(self, search: str) -> str:
        pass
