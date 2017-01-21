'''
About: this program is an implementation of Karger's randomized algorithm for finding 'min cut'
estimation in a Graph

This is a canonical example of Randomized Algorithms

Run for [n^2*log(n)] epochs to get the anwer with very high probability

Read more about here: https://www.cs.princeton.edu/courses/archive/fall13/cos521/lecnotes/lec2final.pdf

@author - Apurva Dubey
'''

import os
import random
from collections import Counter

#os.chdir('C:/Users/')

class Graph():
    '''
    Class to instantiate a graph and its associated methods
    '''
    def __init__(self,in_name, in_vertices = [], in_adjDict = {}):
        self.name = in_name
        self.vertices = in_vertices
        self.adjDict = in_adjDict
        
    def setVertices(self,in_vertex_list):
        self.vertices = [str(i) for i in in_vertex_list]

    def setAdjacencyDict(self,in_adj_key,in_adj_list):
        self.adjDict[in_adj_key] = in_adj_list

    def numVertex(self):
        return len(self.vertices)

    def mergeVertex(self,u,v):
        '''
        Function to merge two nodes of a graph into a super node
        '''
        # fist, add the merged super-node to the set of vertices
        self.vertices.append(str(u)+'-'+str(v))

        tmp = self.adjDict[u] + self.adjDict[v]
        tmp = [t for t in tmp if t not in [u,v]]        
        self.adjDict[str(u)+'-'+str(v)] = tmp

        # then remove the two vertices from the list of vertices
        tmp = [t for t in self.vertices if t not in [u,v]]
        self.vertices = tmp
        
        del self.adjDict[u]
        del self.adjDict[v]
           
        # change the reference of u and v to supernode (uv)
        for x in self.adjDict[str(u)+'-'+str(v)]:
            tmp = [i if i not in [u,v] else str(u)+'-'+str(v) for i in self.adjDict[x]]
            self.adjDict[x] = tmp
            
    def _about(self):
        return "Graph name is: %s; Number of vertices: %d" % (self.name, len(self.vertices))

    def __str__(self):
        return self._about()
    
def graphReduce(in_graph):
    '''
    This function takes as input a Graph, and repeatedly contracts the graph
    till there are two nodes left

    The two nodes left are used to determin the number of "lines" connecting the two
    left super-nodes
    '''
    while in_graph.numVertex() > 2:
        # Randomly choose two nodes that we would like to collapse into a super-node
        u = random.choice(in_graph.adjDict.keys())
        v = random.choice(in_graph.adjDict[u])

        # Merge the two vertices into a super-node
        in_graph.mergeVertex(u,v)

    # Return the number of "lines" connecting the remaing two super-nodes
    return len((in_graph.adjDict[(list(in_graph.adjDict.keys())[0])]))

def mostCommon(lst):
    '''
    Function to find the most common element in the list
    '''
    data = Counter(lst)
    return data.most_common(1)[0][0]

def example():
    '''
    Run a dummy example to check the correctness of the implementation
    '''

    g = Graph('MyGraph')
    g.setVertices(['a','b','c','d','e','f'])
    g.setAdjacencyDict('a',['c','d'])
    g.setAdjacencyDict('b',['c'])
    g.setAdjacencyDict('c',['a','b','e','f'])
    g.setAdjacencyDict('d',['a','e'])
    g.setAdjacencyDict('e',['d','c','f'])
    g.setAdjacencyDict('f',['c','e'])

    graphReduce(g)
    
    print (g)
    print (g.vertices)
    print (g.adjDict)
    print len((g.adjDict[(list(g.adjDict.keys())[0])]))

    print "--------------------------"

def readFile(f):
    '''
    Function to parse the input file
    '''
    file_pointer = open(f, 'r')

    tmp = [i.split("\n")[0].split("\t")[:-1] for i in  file_pointer.readlines()]
    input_array = [[str(r) for r in row] for row in tmp]

    return input_array

if __name__=="__main__":

    # array to store the number of min cuts in each epoch
    minCuts = []

    # read the file
    input_file = 'Week4_kargerMinCut.txt'
    a = readFile(input_file)

    # run the code for 1000 epochs
    for i in range(0,1000):
        print "epoch i:", i

        # adjacency list, and vertices
        in_adjDict = {r[0]:r[1:] for r in a}
        in_vertices = list(in_adjDict.keys())

        # instantiate graph
        kargerGraph = Graph('MyGraph'+str(i),in_vertices,in_adjDict)

        # append the number of min cuts returned in the epoch
        minCuts.append(graphReduce(kargerGraph))

    
    print minCuts

    # get the most frequent occurance of min cut, which will be the probabilistically best answer
    print mostCommon(minCuts)
    

