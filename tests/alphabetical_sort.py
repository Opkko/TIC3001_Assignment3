from output import Output

class AlphabetSort:
    def __init__(self, keyWordList, filename, shifted):
        self.__keyWordList = keyWordList
        self.filename = filename
        self.__shifted = shifted
        self.__result = []
        self.__iswordinlist()
        self.__getsorted()
        self.__calloutput()

    def __iswordinlist(self):
        for word in self.__keyWordList:
             for i in range(0, len(self.__shifted)):
                if self.__shifted[i][0].casefold() == word.casefold():
                    self.__appendshiftedlist(self.__shifted[i])
        

    def __appendshiftedlist(self, shifted):   
        jointostring = ' '.join(shifted) 
        self.__result.append(jointostring)


    def __getsorted(self):
        return self.__result.sort(key=str.casefold)
    
    def __calloutput(self):
        if len(self.__result) >= 1:
            Output(self.filename, self.__result)