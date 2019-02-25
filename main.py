import fire
import run

class Thrim(object):
  def hello(self):
    return 'Hello, Thrim!'
  def run(self, f='config.yml'):
    run.start(f)

if __name__ == '__main__':
  fire.Fire(Thrim)