import unittest
import sys
from io import StringIO

from run import dryrun_iptables

class TestDryrunIptalbles(unittest.TestCase):
  def setUp(self):
    self.captor = StringIO()
    sys.stdout = self.captor

  def tearDown(self):
    sys.stdout = sys.__stdout__

  def test_dryrun(self):
    """sample data
    """
    data = {
      'input': {
        'accept': [
          {'src': '22.22.22.22/32',
           'protocol': 'tcp',
           'in_interface': 'eth0'
          }
        ]
      }
    }
    chain = "input"
    target = "accept"

    expect = "iptables -A INPUT -j ACCEPT -s 22.22.22.22/32 -p tcp -i eth0\n"
    dryrun_iptables(data, chain, target)

    self.assertEqual(expect, self.captor.getvalue())

if __name__ == "__main__":
  unittest.main()