import fire
import run

class Thrim(object):
  def hello(self):
    return 'Hello, Thrim!'
  def run(self):
    run.start()

if __name__ == '__main__':
  fire.Fire(Thrim)