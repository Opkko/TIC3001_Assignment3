from input import Input
from main import main
import unittest
import filecmp
import timeit
import time
import sys
import os

dirPath = os.path.dirname(os.path.realpath(__file__))
outputPath = os.path.join(dirPath, "Output1.txt")


class TestCase1(unittest.TestCase):
    def test_compareresults(self):
        # keyWordList = ["science", "Computer"]
        keyWordList = []
        keyWord = "science"
        filePath = os.path.join(dirPath, "testcases/Test1/ListOfFiles.in")
        # print(filePath)
        outputTestPath = os.path.join(dirPath, "testcases/Test1/Output1.txt")
        # os.remove("Output1.txt")
        for i in range(2):
            if len(keyWordList) == 0:
                keyWordList.append(keyWord)
                self.input = Input(filePath, keyWordList)
            else:
                keyWord = "Computer"
                keyWordList.append(keyWord)
                if len(keyWordList) > 1:
                    with open(outputPath, "w") as file:
                        file.close()
                self.input = Input(filePath, keyWordList)
        self.assertTrue(filecmp.cmp(outputPath, outputTestPath, shallow=False))

class TestCase2(unittest.TestCase):
    def test_compareresults(self):
        keyWordList = []
        keyWord = "science"
        filePath = os.path.join(dirPath, "testcases/Test1/ListOfFiles.in")
        outputTestPath = os.path.join(dirPath, "testcases/Test1/Output1.txt")
        # os.remove("Output1.txt")
        for i in range(2):
            if len(keyWordList) == 0:
                keyWordList.append(keyWord)
                self.input = Input(filePath, keyWordList)
            else:
                keyWord = "science"
                keyWordList.append(keyWord)
                if len(keyWordList) > 1:
                    with open(outputPath, "w") as file:
                        file.close()
                self.input = Input(filePath, keyWordList)
        self.assertTrue(filecmp.cmp(outputPath, outputTestPath, shallow=False))

class TestCase3(unittest.TestCase):
    def test_compareresults(self):
        keyWordList = []
        keyWord = "science"
        filePath = os.path.join(dirPath, "testcases/Test3/ListOfFiles.in")
        outputTestPath = os.path.join(dirPath, "testcases/Test3/Output3.txt")
        # os.remove("Output1.txt")
        for i in range(2):
            if len(keyWordList) == 0:
                keyWordList.append(keyWord)
                self.input = Input(filePath, keyWordList)
            else:
                keyWord = "Computer"
                keyWordList.append(keyWord)
                if len(keyWordList) > 1:
                    with open(outputPath, "w") as file:
                        file.close()
                self.input = Input(filePath, keyWordList)
        self.assertTrue(filecmp.cmp(outputPath, outputTestPath, shallow=False))


# class TestCase3(unittest.TestCase):
#     def test_compareresults(self):
#         keyWordList = ["science", "Computer"]
#         filePath = os.path.join(dirPath, "ListOfFiles.in")
#         print(filePath)
#         outputTestPath = os.path.join(dirPath, "testcases/Test3/Output1.txt")
#         for i in range(len(keyWordList)):
#             self.input = Input(filePath, keyWordList[i])
#             self.assertTrue(filecmp.cmp(outputPath, outputTestPath, shallow=False))

# class TestCase4(unittest.TestCase):
#     def test_compareresults(self):
#         filePath = os.path.join(dirPath, "testcases/Test4/Titles4.txt")
#         ignoredWordsFilePath = os.path.join(dirPath, "testcases/Test4/Ignored4.txt")
#         requiredWordsFilePath = os.path.join(dirPath, "testcases/Test4/Required4.txt")
#         outputTestPath = os.path.join(dirPath, "testcases/Test4/Output4.txt")
#         self.input = Input(filePath, ignoredWordsFilePath, requiredWordsFilePath)
#         self.assertTrue(filecmp.cmp(outputPath, outputTestPath, shallow=False))

# class TestCase5(unittest.TestCase):
#     def test_compareresults(self):
#         filePath = os.path.join(dirPath, "testcases/Test5/Titles5.txt")
#         ignoredWordsFilePath = os.path.join(dirPath, "testcases/Test5/Ignored5.txt")
#         requiredWordsFilePath = os.path.join(dirPath, "testcases/Test5/Required5.txt")
#         outputTestPath = os.path.join(dirPath, "testcases/Test5/Output5.txt")
#         self.input = Input(filePath, ignoredWordsFilePath, requiredWordsFilePath)
#         self.assertTrue(filecmp.cmp(outputPath, outputTestPath, shallow=False))

# class TestCase6(unittest.TestCase):
#     def test_compareresults(self):    
#         filePath = os.path.join(dirPath, "testcases/Test6/Titles6.txt")
#         ignoredWordsFilePath = os.path.join(dirPath, "testcases/Test6/Ignored6.txt")
#         requiredWordsFilePath = os.path.join(dirPath, "testcases/Test6/Required6.txt")
#         outputTestPath = os.path.join(dirPath, "testcases/Test6/Output6.txt")
#         self.input = Input(filePath, ignoredWordsFilePath, requiredWordsFilePath)
#         self.assertTrue(filecmp.cmp(outputPath, outputTestPath, shallow=False))

if __name__ == '__main__':
    unittest.main()