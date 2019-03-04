from lib.cli.base import Cli

from lib.modules import nslookup

class nslookupCli(Cli):
  def start(self):
    self.dryrun_nslookup(self.data)
    self.require_confirmation()
    self.realrun_nslookup(self.data)

  def dryrun_nslookup(self, data):
    print('Debug Dryrun...')
    nslookup.dryrun_nslookup(data, 'a', 'debug')

  def realrun_nslookup(self, data):
    print('Debug start...')
    nslookup.run_nslookup(data, 'a', 'debug')
    print('Debug complete.')
