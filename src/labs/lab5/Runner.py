from shared.interfaces.RunnerInterface import RunnerInterface
from labs.lab5 import init

class Runner(RunnerInterface):
    @staticmethod
    def run():
        init.main()

if __name__ == '__main__':
    Runner().run()