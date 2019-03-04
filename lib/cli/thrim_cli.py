import yaml
import subprocess
import sys

from cli import Cli

class thrimCli(Cli):
  def __init__(self, *args):
    self.options = args

  def start(self):
