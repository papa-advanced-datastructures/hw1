from python.rolling_hash import PreviousHash, RollingHash


class TestRollingHash:
    def test_no_previous_hash(self):
        string = 'a'
        hashed = RollingHash(string=string).run()
        assert hashed == 97

    def test_two_characters(self):
        string = 'ab'
        hashed = RollingHash(string=string).run()
        assert hashed == 9798

    def test_use_previous_hash(self):
        string = 'bc'
        hashed = RollingHash(string=string, previous_hash=PreviousHash(string='ab', value=9798)).run()
        assert hashed == 9899
