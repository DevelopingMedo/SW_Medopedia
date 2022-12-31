from src.medopedia.domain import Character
from src.medopedia.extapi.interface.repository.MedopediaRepository import MedopediaRepository


class CharacterRepository(MedopediaRepository):


    def create_entry(self, entry: Character) -> Character:
        pass

    def get_entry(self, entry_id: str) -> Character:
        pass

    def update_entry(self, entry: Character) -> Character:
        pass

    def delete_entry(self, entry: Character):
        pass