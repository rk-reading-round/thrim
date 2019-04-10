import unittest

try:
  from run import require_confirmation
except FileNotFoundError:
  pass

class TestRequireConfirmation(unittest.TestCase):
  def test_require_confirmation(self):
    print("hello")

if __name__ == "__main__":
    unittest.main()