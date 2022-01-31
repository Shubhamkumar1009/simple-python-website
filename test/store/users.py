import unittest
import store.users as users
from data.config.config import Config


class UsersTest(unittest.TestCase):

    def setUp(self) -> None:
        self.config = Config(password_secret='really-long-password-secret-for-generating-a-hash')
        self.correct_hash = 'aafef08cd8566e96c04898c3db3e5559'
        self.correct_password = 'password'
        self.wrong_password = 'password1'

    def test_password_hash_stays_same(self):
        assert self.correct_hash == users.calculate_password_hash(self.config, self.correct_password)
        assert self.correct_hash == users.calculate_password_hash(self.config, self.correct_password)

    def test_password_verification(self):
        assert users.verify_hash(self.config, self.correct_password, self.correct_hash)
        assert not users.verify_hash(self.config, self.wrong_password, self.correct_hash)

    def test_password_hashes_are_different(self):
        assert users.calculate_password_hash(self.config, self.correct_password) != users.calculate_password_hash(self.config, self.wrong_password)

    def test_generate_hash(self):
        password = 'admin-password'
        hash = users.calculate_password_hash(self.config, password)
        print(f'Generated a MD5 hash for "{password}" => {hash}')
        assert True