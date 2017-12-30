import unittest
from strategy import matcher

strategy1 = { 
    "L" : {
        "bet" : 1,
        "L" : {
            "bet" : 2,
            "L" : { 
                "bet" : 31,
                "W" : { 
                    "bet" : 41,
                    "W" : {
                        "bet": 51
                    },
                    "L" : {
                        "bet": 52
                    }
                },
                "L" : {  
                    "bet" : 42,
                    "W" : {
                        "bet": 53
                    },
                    "L" : {
                        "bet": 54
                    }
                }  
            },
            "W" : { 
                "bet" : 32,
                "W" : {
                    "bet" : 43,
                    "W" : {
                        "bet": 55
                    },
                    "L" : {
                        "bet": 56
                    }
                },
                "L" : {
                    "bet" : 44,
                    "W" : {
                        "bet": 57
                    },
                    "L" : {
                        "bet": 58
                    }
                }
            }
        }
    }
}

class TestStringMethods(unittest.TestCase):
    def test_level01(self):
        self.assertEqual( matcher(["W"] ,strategy1), 0 )

    def test_level02(self):
        self.assertEqual( matcher(["W","L"] ,strategy1), 1 )

    def test_level03(self):
        self.assertEqual( matcher(["W","L","W"] ,strategy1), 0 )

    def test_level04(self):
        self.assertEqual( matcher(["W","L","W","L"] ,strategy1), 1 )

    def test_level05(self):
        self.assertEqual( matcher(["W","L","L","W"] ,strategy1), 32 )

    def test_level2(self):
        self.assertEqual( matcher(["W","L","W","L","L"] ,strategy1), 2 )

    def test_level31(self):
        self.assertEqual( matcher(["W","L","W","L","L","W"] ,strategy1), 32 )

    def test_level32(self):
        self.assertEqual( matcher(["W","L","L","L"] ,strategy1), 31 )

    def test_level41(self):
        self.assertEqual( matcher(["W","L","L","L","W"] ,strategy1), 41 ) 

    def test_level42(self):
        self.assertEqual( matcher(["W","L","L","W","W"] ,strategy1), 43 ) 

    def test_level51(self):
        self.assertEqual( matcher(["W","L","L","L","W","L"] ,strategy1), 52 ) 

    def test_level52(self):
        self.assertEqual( matcher(["W","L","L","L","W","W"] ,strategy1), 51 ) 

    def test_level53(self):
        self.assertEqual( matcher(["W","L","L","W","W","L"] ,strategy1), 56 ) 

    def test_level54(self):
        self.assertEqual( matcher(["W","L","L","W","W","W"] ,strategy1), 55 ) 

if __name__ == '__main__':
    unittest.main()