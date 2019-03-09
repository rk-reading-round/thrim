import platform
from lib.cli.base import Cli
from lib.modules import iptables

class thrimCli(Cli):
  def start(self):
    self.dryrun_thrim(self.data)
    self.require_confirmation()

    try:
      self.realrun_thrim(self.data)
    except FileNotFoundError:
      print('[Error] command iptables not found')

  def dryrun_thrim(self, data):
    print('Thrim Dryrun...')
    iptables.dryrun_iptables(data, 'input', 'accept')
    iptables.dryrun_iptables(data, 'input', 'drop')
    iptables.dryrun_iptables(data, 'output', 'accept')
    iptables.dryrun_iptables(data, 'output', 'drop')

  def realrun_thrim(self, data):
    print('Thrim start...')
    iptables.run_iptables(data, 'input', 'accept')
    iptables.run_iptables(data, 'input', 'drop')
    iptables.run_iptables(data, 'output', 'accept')
    iptables.run_iptables(data, 'output', 'drop')
    print('Thrim complete.')
