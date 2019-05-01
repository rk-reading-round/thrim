import unittest

from run import dryrun_iptables

class TestDryrunIptalbles(unittest.TestCase):
    def test_command(self):
        data = {}