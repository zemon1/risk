#Jeff Haak
#Risk Board
import networkx as nx
import matplotlib.pyplot as plt
from copy import deepcopy as dc

class Board:

    __slots__ = ["gui", "colors", "initialGraph", "troops", "countries", "groups", "graph"]

    def __init__(self, gui=False):
        self.colors = ["b", "g", "r", "k", "y", "c"]
        self.graph = {}
        self.troops = {}
        self.countries = []
        self.groups = {}
        self.gui = gui
        #self.graph = nx.Graph()
        self.nxgraph = nx.house_graph()

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
                            self.troops[i-1] = {"player":-1, "count":-1}
                            self.nxgraph.add_node(i-1)

                
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
                        #try to append the country number to list in groups
                        try:                            
                            self.groups[int(item)]["list"].append(count)
                        #If the key doesn't exist make one.
                        except KeyError:
                            self.groups[int(item)] = {"name":line[i+1], "list":[count], "bonus":[int(line[i+2])]}
                    
                    elif i == groupLoc or i == groupLoc+1:
                        pass                       
                            
                    #These are the actual connections
                    elif not i == 0:
                        if item == '1' or item == '2':
                            if not i - 1  == count:
                                conns.append(i - 1)
                                self.nxgraph.add_edge(i - 1, count)
                    
                    conns.sort()        
                    self.graph[count]["paths"] = conns
                            
                        
                            
            
            count += 1
        
        #print "Graph:", self.nxgraph[14]
        for key in self.graph.keys():
            print key, self.graph[key]
            
        print "\n"
        #print "\n\n\n\n", self.groups

                     
        #print "Graph:", self.graph.edges()

        pos = nx.spring_layout(self.nxgraph, scale=.5)

        for key in self.groups.keys():
            colorKey = self.colors[key%len(self.colors)]
            #print colorKey
            
            nx.draw_networkx_nodes(self.nxgraph, pos
                                  , nodlist=self.groups[key]["list"]
                                  , node_color=colorKey
                                  , node_size=500)

        nx.draw_networkx_edges(self.nxgraph, pos)

        if self.gui:
            #nx.draw(self.nxgraph)
            plt.axis('off')
            plt.show()

    def getBoard(self):
        return dc(self.graph)

    
    
if __name__ == "__main__":
    board = Board()
    board.importMap("topBot.csv")
    ng = board.getBoard()

    print ng[0]
    ng[0] = []
    print ng[0]
    print board.graph[0]
