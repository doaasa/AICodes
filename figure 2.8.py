location_A= (0,0)
location_B =(0,1)


def ReflexVaccumAgent(state , location):**
   if(state == "Dirty"):
       return "Suck"
   elif (location == location_A):
       return "Right"
   elif (location == location_B):
       return "Left"  
    
        
   
        
    

print (ReflexVaccumAgent("Dirty", location_B))


    
