import yaml
import subprocess
import sys

def start(file):
  f = open(file, "r+")
  data = yaml.load(f)
  dryrun_thrim(data)
  require_confirmation()
  realrun_thrim(data)

def require_confirmation():
  while True:
    choice = input('Run Thrim? [y/N]: ').lower()
    if choice in ['y', 'yes']:
      return True
    elif choice in ['n', 'no']:
      print('Thrim end...')
      sys.exit()

def dryrun_thrim(data):
  print('Thrim Dryrun...')
  dryrun_nslookup(data, 'a', 'debug')

def realrun_thrim(data):
  print('Thrim start...')
  run_nslookup(data, 'a', 'debug')
  print('Thrim complete.')

def dryrun_nslookup(data, type, option):
  option_configs = data[type][option]

  for i in range(len(option_configs)):
    site = option_configs[i]['site']
    port = option_configs[i]['port']
    print('[Dryrun] nslookup -type=' + type + ' -' + option + ' -port=' + str(port) + ' ' + site)

def run_nslookup(data, type, option):
  option_configs = data[type][option]

  for i in range(len(option_configs)):
    site = option_configs[i]['site']
    port = option_configs[i]['port']
    command = ['nslookup', '-type={}'.format(type), '-{}'.format(option), '-port={}'.format(port), site]
    print('[Running] nslookup -type=' + type + ' -' + option + ' -port=' + str(port) + ' ' + site)
    subprocess.run(command)
