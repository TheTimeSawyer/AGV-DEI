class Node(object):
    def __init__(self,lat,long,cnodes):
        self.lat=lat
        self.long=long
        self.cnodes=cnodes.copy()
    
    def __str__(self):
        return(str(self.lat)+" + "+str(self.long)+"+"+self.cnodes)
        
    def dist(self,other):
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
        
        '''The final distanceis calculated using the 
        distance formula in coordinate geometry.'''
    
