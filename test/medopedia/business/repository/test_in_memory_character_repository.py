import unittest
from datetime import datetime

from src.medopedia.business.repository.InMemoryCharacterRepository import InMemoryCharacterRepository
from src.medopedia.domain import Character


class InMemoryCharacterRepositoryTest(unittest.TestCase):

    def test_create_character(self):
        repo = InMemoryCharacterRepository()

        # Erstelle einen neuen Charakter
        character = Character(firstname="Han",
                              lastname="Solo",
                              date_of_birth=datetime(year=29, month=5, day=25),
                              is_before_battle_of_yavin=True)

        # Speichere den Charakter in der Repository
        repo.create_entry(character)

        # Stelle sicher, dass der Charakter in der Repository gespeichert wurde
        self.assertIn(character, repo.characters)


if __name__ == '__main__':
    unittest.main()
