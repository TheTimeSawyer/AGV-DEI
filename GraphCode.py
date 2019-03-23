class Node(object):
    def __init__(self,ind,lat,long,cnodes):
        self.ind=ind
        self.lat=lat
        self.long=long
        self.cnodes=cnodes.copy()
    
    def __str__(self):
        return(str(self.lat)+"  "+str(self.long)+"  "+str(self.cnodes))
        
    def dist(self,other):
        if other.ind in self.cnodes:
            
            x=((self.lat-other.lat)*111000)
            
            ''' 111000m is Approximate for Regions around Agra,
            where this vehicle is being tested'''
            
            longdist= (math.cos((self.lat)*math.pi/180))*111.321
            
            '''This is a formula for measuring approximate
            distances between longitudes. This is valid only 
            when tha latitudes of initial and final position 
            are not very far apart.'''
            
            y=((self.long-other.long)*longdist)
            return pow((x**2)-(y**2),0.5)
        else:            
            return None


# dummy node             
class AdjNode: 
    def __init__(self, data): 
        self.vertex = data 
        self.next = None
# Random values of latitude and longitude.
n0 = Node(0,65.5,128.26,[1])
n1 = Node(1,65.5,128.26,[0,2,3])
n2 = Node(2,65.5,128.26,[1])
n3 = Node(3,65.5,128.26,[2,4])
n4 = Node(4,65.5,128.26,[3])

lnodes = [n0,n1,n2,n3,n4]

class Graph: 
    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [None] * self.V 
  
    # Function to add an edge in an undirected graph 
    def add_edge(self, src, dest): 
        # Adding the node to the source node 
        node = AdjNode(dest) 
        node.next = self.graph[src] 
        self.graph[src] = node 
  
        # Adding the source node to the destination as 
        # it is the undirected graph 
        node = AdjNode(src) 
        node.next = self.graph[dest] 
        self.graph[dest] = node 
  
    # Function to print the graph 
    def print_graph(self): 
        for i in range(self.V): 
            print("Adjacency list of vertex {}\n head".format(i), end="") 
            temp = self.graph[i] 
            while temp: 
                print(" -> {}".format(temp.vertex), end="") 
                temp = temp.next
            print(" \n") 
''' This code creates a graph of indices and a 
separate list which stores the data of each node(latitude
and longitude). The '''            




g = Graph(5)

#How to create a graph by specifying its edges.
#This is an example, specific to our chosen path.

g.add_edge(0,1)
g.add_edge(1,2)
g.add_edge(1,3)
g.add_edge(3,4)


g.print_graph()
#How to access the node data from the nodes list.
print (lnodes[0])
