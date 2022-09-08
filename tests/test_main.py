from pathlib import Path
from uuid import uuid4

from main import Main


class TestMain:
    def test_parses_args(self):
        string_1_filename = Path(f'file1_{uuid4().hex}.txt')
        string_2_filename = Path(f'file2_{uuid4().hex}.txt')
        try:
            with open(string_1_filename, 'w') as f:
                f.write('arbitrary')
            with open(string_2_filename, 'w') as f:
                f.write('arbitrary2')
            substrings = Main([None, string_1_filename, string_2_filename, '9']).run()
            assert substrings == {(0, 0)}
        finally:
            string_1_filename.unlink(missing_ok=True)
            string_2_filename.unlink(missing_ok=True)
