# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 15:21:56 2022

@author: Electronica Care
"""

import agent as a
import random as random
import agents as agents


loc_A, loc_B = (0, 0), (1, 0)

class VaccumAgent:
    def __init__(self):
        self.status= {loc_A: random.choice(['Clean', 'Dirty']),
                       loc_B: random.choice(['Clean', 'Dirty'])}
        
    def percept (self , agent):
        return (agent.location , self.status[agent.location])
    def AgentLocation(self, agent, action):
        if agent.location == loc_B :
            action = 'Right'

        elif  agent.location== loc_A:
            action= "left"
    
    def RandLocation(self):
        return random.choice([loc_A, loc_B])
    
print("State of the Environment: {}.".format(VaccumAgent().status))


      
        
        