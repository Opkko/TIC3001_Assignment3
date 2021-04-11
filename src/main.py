import os
from input import Input
import sys
from pathlib import Path

def main():
    preInput = ""
    dirPath = os.path.dirname(os.path.realpath(__file__))
    filePath = os.path.join(dirPath, sys.argv[1])
    outputfilePath = os.path.join(dirPath, "Output1.txt")
    keyWordList = []

    if Path(filePath).is_file():
      while True:
        keyWord = input('userinput:')
        preInput = keyWord 
        if len(keyWord.split(" ")) == 1 :        
          if len(keyWordList) == 0 or len(keyWordList) == 1 and keyWord != 'q':
            keyWordList.append(keyWord)
          elif len(keyWordList) > 1 and keyWord in keyWordList and keyWord != 'q':
            print("Please key in different User Input")
            continue
          elif len(keyWordList) > 1 and keyWord not in keyWordList and keyWord != 'q':
            keyWordList.append(keyWord)
          if len(keyWordList) > 1:
            with open(outputfilePath, "w") as file:
              file.close()
          if keyWord == 'q':
            with open(outputfilePath, "w") as file:
              file.close()
            break
          else:
            Input(filePath, keyWordList)
    else:
      print ("File not exist")
      exit()


if __name__== "__main__":
  main()