import unittest
from cameltosnake import camel_to_snake

class Test_CaseSwitch(unittest.TestCase):

    # Ich muss mir noch überlegen, was ich haben möchte. Sollen auch die Namen, die nicht umgewandelt werden müssen aufgenommen?
    def test_basic_cameltosnake(self):
        input = ["unusual.txt", "testFile.txt"]
        expected = ["test_file.txt"]
        result = camel_to_snake(input)
        self.assertEqual(expected,result)

    def test_edge_camletosnake(self):
        input = [None, 0, "Testfile.txt", "testFile.txt"]
        expected = ["test_file.txt"]
        result = camel_to_snake(input)
        self.assertEqual(expected, result)


if __name__ == "__main__":
    unittest.main()
        