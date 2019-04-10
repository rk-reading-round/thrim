import unittest
import contextlib

from run import require_confirmation

class redirect_stdin(contextlib._RedirectStream):
    _stream = "stdin"

class TestRequireConfirmation(unittest.TestCase):
  def _calFUT(self):
    return require_confirmation()
  
  def test_yes(self):
    from io import StringIO
    buf = StringIO()
    buf.write("y")
    buf.seek(0)

    with redirect_stdin(buf):
      actual = self._calFUT()
    self.assertTrue(actual)
    
  def test_no(self):
    from io import StringIO
    buf = StringIO()
    buf.write("n")
    buf.seek(0)

    try:
      with redirect_stdin(buf):
        actual = self._calFUT()
    except SystemExit as e:
      self.assertEqual(e.code, None)

if __name__ == "__main__":
    unittest.main()