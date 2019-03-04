import yaml
import subprocess
import sys

class Cli():
  def __init__(self, file):
    self.f = open(file, "+r")
    self.data = yaml.load(self.f)

  def require_confirmation(self):
    while True:
      choice = input('Run Thrim? [y/N]: ').lower()
      if choice in ['y', 'yes']:
        return True
      elif choice in ['n', 'no']:
        print('Thrim end...')
        sys.exit()
