from collections import deque
from alphabetical_sort import AlphabetSort

class CircularShift:
    lst = []
    tmp = []
    y = []
    def __init__(self, listOfFiles, keyWordList):
        self.__listOfFiles = listOfFiles
        self.__keyWordList = keyWordList
        self.__shifted = []
        self.__lst = [] #---- this new lst
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
                    
                    CircularShift.lst.append(self.filename)
                    CircularShift.y = self.__shifted[:]

                    CircularShift.lst.append(self.__shifted[:])
                    self.__shifted.clear() #--- this is for each file
                    CircularShift.y.clear()
                 
                except IOError:
                    print("File not accessible")
           
        else:
            for self.filename in self.__listOfFiles:
                CircularShift.tmp = self.lst_splitting(CircularShift.lst, self.filename)
                self.__callalphabetsort(self.filename, CircularShift.tmp)
                    
    def lst_splitting(self, lst, filename):
        tmplst = []
        print("what is lst in split")
        print(lst)
        print(filename)
        for i in range(len(lst)):
            print (i) #len = 4
            print("what is i in if ")
            print(lst[i])
            if filename == lst[i]:
                print("before append tmplst")
                print(tmplst)
                tmplst += lst[i+1]
                print("tmpLst is")
                print(tmplst)
                break
        return tmplst
    
    def __callalphabetsort(self, filename, shifted):
        AlphabetSort(self.__keyWordList, filename, shifted)
