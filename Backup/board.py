#Jeff Haak
#Risk Board

class Board:

    __slots__ = ["graph", "troops", "countries", "groups"]

    def __init__(self):
        self.graph = {}
        self.troops = {}
        self.countries = []
        self.groups = {}

    def importMap(self, fileName):
        countryCodeLoc = -1
        groupLoc = -1
        
        #Read in the file and make a board.
        with open(fileName, 'r') as theFile:
            lines = theFile.readlines()

        count = 0
        for line in lines:
            line = line.strip().split(',')

            #Title line, holds the index of country code, and group name
            if count == 0 and len(self.countries) == 0:
                for i in range(0,len(line)):
                    item = line[i]
                    #if its not the first empty cell
                    if not item == "":
                        #if it is the Country Code Column save it
                        if item == "cc":
                            countryCodeLoc = i
                        elif item == "group":
                            groupLoc = i
                        else:
                            self.countries.append(item)
                            self.graph[i-1] = {"name": item, "paths":[]}

                
                print "CC:", countryCodeLoc
                print "Group:", groupLoc
                #print "Graph:", self.graph
                #print line
                #print self.countries
                count -= 1
            else:
                conns = []
                for i in range(0,len(line)):
                    item = line[i]
                    if i == countryCodeLoc:
                        pass
                    elif i == groupLoc:
                        pass
                    #These are the actual connections
                    elif not i == 0:
                        if item == '1' or item == '2':
                            conns.append(i)
                            
                    self.graph[count]["paths"] = conns
                            
                        
                            
            
            count += 1
            
        print "Graph:", self.graph

if __name__ == "__main__":
    board = Board()
    board.importMap("topBot.csv")
