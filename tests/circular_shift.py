from collections import deque
from alphabetical_sort import AlphabetSort
import os


dirPath = os.path.dirname(os.path.realpath(__file__))

class CircularShift:
    lst = []
    tmp = []
    shifted = []
    def __init__(self, listOfFiles, keyWordList,filePathTitle):
        # print("what is files")
        # print(listOfFiles)
        self.filePathTitle = filePathTitle
        self.__listOfFiles = listOfFiles
        self.__keyWordList = keyWordList
        self.__shifted = []
        self.__getshifted()

    
    def __getshifted(self):
        if len(self.__keyWordList) == 1:
            # print("came in if now")
            flag = False
            for self.filename in self.__listOfFiles:

                try:
                    with open( self.filePathTitle + "/" + self.filename) as file:
 

                        lines = [line.strip() for line in file]
                        if lines == []:
                            flag = True
                        else :
                            flag = False
                        for line in lines:
                            wordlist = line.split(" ")
                            self.deq = deque(wordlist)
                            for i in range(0, len(self.deq)):
                                self.deq.rotate()
                                self.__shifted.append(list(self.deq))
                    self.__callalphabetsort(self.filename, self.__shifted)
                    self.__storekwicindex()
                    if flag == True:
                        CircularShift.lst.clear()
                except IOError:
                    print("File not accessible")
           
        else:
            # print("came to else")
            for self.filename in self.__listOfFiles:
                CircularShift.tmp = self.__lstsplitting(CircularShift.lst, self.filename)
                # print("what is tmp")
                # print(CircularShift.tmp)
                self.__callalphabetsort(self.filename, CircularShift.tmp)
            CircularShift.lst.clear()
    def __storekwicindex(self):
        CircularShift.lst.append(self.filename)
        CircularShift.shifted = self.__shifted[:]

        CircularShift.lst.append(self.__shifted[:])
        self.__shifted.clear() #--- this is for each file
        CircularShift.shifted.clear()


    def __lstsplitting(self, lst, filename):
        tmplst = []
        # print("what is lst in split")
        # print(lst)
        # print(filename)
        for i in range(len(lst)):
            # print (i) #len = 4
            # print("what is i in if ")
            # print(lst[i])
            if filename == lst[i]:
                # print("before append tmplst")
                # print(tmplst)
                tmplst += lst[i+1]
                # print("tmpLst is")
                # print(tmplst)
                break
        return tmplst

    # def filePath(self) :

    
    def __callalphabetsort(self, filename, shifted):
        AlphabetSort(self.__keyWordList, filename, shifted)
