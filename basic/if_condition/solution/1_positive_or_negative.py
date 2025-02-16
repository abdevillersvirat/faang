# Write a program to find a given number is positive negative or zero.
#If the number is positive you should print POSITIVE , or if the number 
# is negative you should print NEGATIVE or if the number is 0 you 
# should print ZERO.
#Complete the function below and store your result in ans variable
def positive_or_negative(num):
   #Practise yourself : write your code here 
   ans = ""
   if num > 0:
       ans = "POSITIVE"
   elif num < 0:
        ans = "NEGATIVE"
   else:
        ans = "ZERO"
   return ans
import unittest

class Test(unittest.TestCase):
    def test_positive_or_negative(self):
        num = 5
        actual = positive_or_negative(num)
        expected = "POSITIVE"
        self.assertEqual(actual, expected)
    def test_positive_or_negative(self):
        num = -2
        actual = positive_or_negative(num)
        expected = "NEGATIVE"
        self.assertEqual(actual, expected)
    def test_positive_or_negative(self):
        num = 0
        actual = positive_or_negative(num)
        expected = "ZERO"
        self.assertEqual(actual, expected)
unittest.main(verbosity=2)
