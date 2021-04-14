from circular_shift import CircularShift

class Input:
    def __init__(self, inputFile, keyWordList,filePathTitle):
        self.__inputFile = inputFile
        self.__keyWordList = keyWordList
        self.__listOfFiles = self.__getfiles()
        self.filePathTitle = filePathTitle
        self.__callcircularshift()
        

    def __getfiles(self):
        try:
            with open(self.__inputFile) as file:
                files = [line.strip() for line in file]
                return files
        except IOError:
            print("File not accessible")

    def __callcircularshift(self):
        CircularShift(self.__listOfFiles, self.__keyWordList, self.filePathTitle)