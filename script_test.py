import unittest
from script import score, bestScore, hiLo

class TestStringMethods(unittest.TestCase):

    def test_result1(self):
        self.assertEqual( score(["2","3"]) , [5])

    def test_result1a(self):
        self.assertEqual( score(["D","3"]) , [13])

    def test_result1b(self):
        self.assertEqual( score(["3","3","5","5","10"]) , [26])

    def test_result2(self):
        self.assertEqual( score(["A","A"]) , [2, 12, 22])

    def test_result3(self):
        self.assertEqual( score(["K","A"]) , [11, 21])

    def test_result4(self):
        self.assertEqual( score(["A","9"]) , [10, 20])

    def test_result4a(self):
        self.assertEqual( score(["A","2"]) , [3, 13])

    def test_result4b(self):
        self.assertEqual( score(["A","2","3"]) , [6, 16])       

    def test_result4c(self):
        self.assertEqual( score(["A","2","3","4"]) , [10, 20])     

    def test_result5(self):
        self.assertEqual( score(["A","9","A"]) , [11, 21, 31])

# ------------------------------------------------------------------
    def test_result6a(self):
        self.assertEqual( bestScore([11]) , 11)

    def test_result6b(self):
        self.assertEqual( bestScore([26]) , 26)

    def test_result6(self):
        self.assertEqual( bestScore([11, 21, 31]) , 21)

# ------------------------------------------------------------------
    def test_result7(self):
        self.assertEqual( hiLo(["A","2","3"],["3","7","10"]) , 1)



    # def test_split(self):
    #     s = 'hello world'
    #     self.assertEqual(s.split(), ['hello', 'world'])
    #     # check that s.split fails when the separator is not a string
    #     with self.assertRaises(TypeError):
    #         s.split(2)

if __name__ == '__main__':
    unittest.main()