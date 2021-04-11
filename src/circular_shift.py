from collections import deque
from alphabetical_sort import AlphabetSort

class CircularShift:
    lst = []
    tmp = []
    shifted = []
    def __init__(self, listOfFiles, keyWordList):
        self.__listOfFiles = listOfFiles
        self.__keyWordList = keyWordList
        self.__shifted = []
        self.__getshifted()

    def __getshifted(self):
        if len(self.__keyWordList) == 1:
            for self.filename in self.__listOfFiles:
                try:
                    with open(self.filename) as file:
                        lines = [line.strip() for line in file]
                        for line in lines:
                            wordlist = line.split(" ")
                            self.deq = deque(wordlist)

                            for i in range(0, len(self.deq)):
                                self.deq.rotate()
                                self.__shifted.append(list(self.deq))
                    self.__callalphabetsort(self.filename, self.__shifted)
                    self.__storekwicindex()
                 
                except IOError:
                    print("File not accessible")
           
        else:
            for self.filename in self.__listOfFiles:
                CircularShift.tmp = self.__lstsplitting(CircularShift.lst, self.filename)
                self.__callalphabetsort(self.filename, CircularShift.tmp)

    def __storekwicindex(self):
        CircularShift.lst.append(self.filename)
        CircularShift.shifted = self.__shifted[:]

        CircularShift.lst.append(self.__shifted[:])
        self.__shifted.clear() #--- this is for each file
        CircularShift.shifted.clear()


    def __lstsplitting(self, lst, filename):
        tmplst = []
        for i in range(len(lst)):
            if filename == lst[i]:
                tmplst += lst[i+1]
                break
        return tmplst
    
    def __callalphabetsort(self, filename, shifted):
        AlphabetSort(self.__keyWordList, filename, shifted)
