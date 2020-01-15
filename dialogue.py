# main py
from lib.util import *;


class Dialogue():
    def __init__(self):
        print("init class");

    def run(self):
        print(util.add(3,4));
        print("task begin!");

if __name__ == "__main__":
    main = Dialogue();
    main.run();
