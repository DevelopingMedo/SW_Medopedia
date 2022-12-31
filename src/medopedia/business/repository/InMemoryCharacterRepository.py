from src.medopedia.domain import Character
from src.medopedia.extapi.interface.repository.CharacterRepository import CharacterRepository


class InMemoryCharacterRepository(CharacterRepository):
    def __init__(self):
        self.characters = []

    def create_entry(self, entry: Character) -> None:
        self.characters.append(entry)

    def get_entry(self, entry_id: str) -> Character:
        for character in self.characters:
            if character.id == entry_id:
                return character
        raise ValueError(f"Character with id {entry_id} not found")

    def update_entry(self, entry: Character) -> None:
        for i, character in enumerate(self.characters):
            if character.id == entry.id:
                self.characters[i] = entry
                return
        raise ValueError(f"Character with id {entry.id} not found")

    def delete_entry(self, entry_id: str) -> None:
        for i, character in enumerate(self.characters):
            if character.id == entry_id:
                del self.characters[i]
                return
        raise ValueError(f"Character with id {entry_id} not found")