import fire
import run
import absorb
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from test import test_require_confirmation

class Thrim(object):
  def hello(self):
    return 'Hello, Thrim!'
  def run(self, f='config.yml'):
    run.start(f)
  def absorb(self):
    absorb.start()
  def test(self):
    test_require_confirmation()

def main():
  fire.Fire(Thrim)

if __name__ == '__main__':
  fire.Fire(Thrim)
