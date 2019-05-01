import unittest
import iptc
import subprocess

from run import run_iptables

class TestRunIptables(unittest.TestCase):
	def tearDown(self):
		subprocess.run(["iptables", "--flush"])

	def test_thrim_run(self):
		#sample data
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

		#testrun run_iptables
		run_iptables(data, chain, target)
		actual = []
		table = iptc.Chain(iptc.Table(iptc.Table.FILTER), 'INPUT')
		actual.append(table.rules[0].target.name)
		actual.append(table.rules[0].src)
		actual.append(table.rules[0].protocol)
		actual.append(table.rules[0].in_interface)

		expect = ['ACCEPT', '22.22.22.22/255.255.255.255', 'tcp', 'eth0']

		self.assertEqual(expect, actual)

if __name__ == "__main__":
  unittest.main()