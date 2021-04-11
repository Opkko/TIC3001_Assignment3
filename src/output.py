import os
from collections import deque

dirPath = os.path.dirname(os.path.realpath(__file__))
filePath = os.path.join(dirPath, "Output1.txt")

class Output:
    def __init__(self, filename, result):
        self.__filename = filename
        self.__result = result
        self.__getresult()

    def __getresult(self):
        with open(filePath, "a+") as file:
            file.write(self.__filename + "\n")
            for line in self.__result:
                file.write("{line}\n".format(line=line))
            file.close()