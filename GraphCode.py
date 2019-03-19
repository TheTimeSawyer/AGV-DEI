class AdjNode(object):
    def __init__(self,lat,longi):
        self.lat=lat
        self.longi=longi
        self.next=None
    
    def __str__(self):
        return(str(self.lat)+" + "+str(self.longi)+"+"+self.cnodes)
        
    def dist(self,other):
        x=((self.lat-other.lat)*111000)
        
        ''' 111000m is Approximate for Regions around Agra,
        where this vehicle is being tested'''
        
        longdist= (math.cos((self.lat)*math.pi/180))*111.321
        
        '''This is a formula for measuring approximate
        distances between longitudes. This is valid only 
        when tha latitudes of initial and final position 
        are not very far apart.'''
        
        y=((self.longi-other.longi)*longdist)
        return pow((x**2)-(y**2),0.5)
        
        '''The final distanceis calculated using the 
        distance formula in coordinate geometry.'''




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

