import unittest

from parser import Parser


class TestParser(unittest.TestCase):
    def test_file_reader(self):
        people = Parser.read_file("data.csv")
        assert len(people) == 4
        assert people["outroemail@hotmail.com"]["first_name"] == "vinicius"
        assert people["outroemail@hotmail.com"]["last_name"] == "agostini"
        assert people["outroemail@hotmail.com"]["birth"] == "19960603"
        assert people["outroemail@hotmail.com"]["gender"] == "masculino"

    def test_file_reader_raises_on_wrong_extension(self):
        self.assertRaises(RuntimeError, Parser.read_file, "data.tsv")


if __name__ == "__main__":
    unittest.main()
