import fire
from lib.cli import thrim_cli

class Thrim(object):
  def hello(self):
    return 'Hello, Thrim!'

  def run(self, f='config.yml'):
    thrim = thrim_cli.thrimCli(f)
    thrim.start()

def main():
  fire.Fire(Thrim)

if __name__ == '__main__':
  fire.Fire(Thrim)