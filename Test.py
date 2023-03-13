import unittest

from prog1 import summation 

class Testsum(unittest.Testcase):
  def test_list_int(self):
    data = [23,32]
    result = summation(data)
    self.assertEqual(result,55)
    
if __name__ == '__main__':
  unittest.main()
