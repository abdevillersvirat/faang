# Write a program with print "HI" when a number is divisible by 3, "HELLO" when a number 
# is divisible by 5, "HOW ARE YOU" when a number is divisible by both 3 and 5
#If the number is divisible by 3 you should return the ans variable set to "HI".
#If the number is divisible by 5 you should return the ans variable set to "HELLO".
#If the number is divisible by both 3 & 5 you should return the ans variable set to "HOW ARE YOU" 
#If the input number is 0 or not divisible by both 3 and  you should return the ans variable set 
# to "INVALID NUMBER"
#Complete the function below and store your result in ans variable
def divisible_by_3or5(num):
    ans = " "
   #
    if num == 0:
        ans = "INVALID NUMBER"
    

        if num%3 == 0 and num%5 == 0:
            ans = "HOW ARE YOU"
        elif num%3 == 0:
            ans = "HI"
        elif num%5 == 0:
            ans = "HELLO"
        else:
            ans = "INVALID NUMBER"

    return ans

    
import unittest

class Test(unittest.TestCase):
    def test_divisible_by_3or5(self):
        num = 5
        actual = divisible_by_3or5(num)
        expected = "HELLO"
        self.assertEqual(actual, expected)
    def test_divisible_by_3or5(self):
        num = 2
        actual = divisible_by_3or5(num)
        expected = "INVALID NUMBER"
        self.assertEqual(actual, expected)
    def test_divisible_by_3or5(self):
        num = 0
        actual = divisible_by_3or5(num)
        expected = "INVALID NUMBER"
        self.assertEqual(actual, expected)
    def test_divisible_by_3or5(self):
        num = 15
        actual = divisible_by_3or5(num)
        expected = "HOW ARE YOU"
        self.assertEqual(actual, expected)
    def test_divisible_by_3or5(self):
        num = 6
        actual = divisible_by_3or5(num)
        expected = "HI"
        self.assertEqual(actual, expected)
    
unittest.main(verbosity=2)


