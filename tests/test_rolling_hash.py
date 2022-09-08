from python.rolling_hash import PreviousHash, RollingHash


class TestRollingHash:
    def test_no_previous_hash(self):
        string = 'a'
        hashed = RollingHash(string_to_add=string).run()
        assert hashed == 98

    def test_two_characters(self):
        string = 'ab'
        hashed = RollingHash(string_to_add=string).run()
        assert hashed == 9899

    def test_use_previous_hash(self):
        previous_hash = PreviousHash(
            first_character='a',
            value=RollingHash(string_to_add='ab').run(),
            window_size=2
        )
        hashed = RollingHash(string_to_add='c', previous_hash=previous_hash).run()
        assert hashed == 9901
