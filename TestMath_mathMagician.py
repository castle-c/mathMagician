import unittest
from mathMagician import *

class TestMagician(unittest.TestCase):


  @classmethod
  def setUp(self):
    self.magic = Magician()


  def test_integer_creation(self):
    self.assertEqual(self.magic.create_integers(5), [1,2,3,4,5])


  def test_fibonacci_creation(self):
    self.assertEqual(self.magic.create_fibonacci(5), [1,2,3,5])


  # def test_primes_creation(self):
  #   self.assertEqual(self.magic.create_primes(12), [2,3,5,7])





if __name__ == '__main__':
  unittest.main()
