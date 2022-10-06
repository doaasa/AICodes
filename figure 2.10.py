'''
location_A=(0,0)
location_B= (0,1)

percept=((0,1), "Clean")
rules={ (location_A,"Dirty") : "Suck",(location_B,"Dirty") : "Suck",
       (location_A, 'Clean'):'Right', (location_B, 'Clean'):'Left'}

def intrerpretInput(percept):
     return percept
    
def Rule_Match(state , rules):
    return rules[state]  #ازاى نقدر نرجع الكي والفاليز مع بعض من الفانكشن
    
def SimpleReflexAgent(percept):
    state= intrerpretInput(percept)
    rule= Rule_Match(state, rules)
    action=rule
    return action


print(SimpleReflexAgent(percept))
    
'''

location_A=(0,0)
location_B= (0,1)

percept=((0,1), "Clean")
rules={ (location_A,"Dirty") : "Suck",(location_B,"Dirty") : "Suck",
       (location_A, 'Clean'):'Right', (location_B, 'Clean'):'Left'}

def intrerpretInput(percept):
     return percept
    
def Rule_Match(state , rules):
    x= rules.pop(state)
    return x  #ازاى نقدر نرجع الكي والفاليز مع بعض من الفانكشن
    
def SimpleReflexAgent(percept):
    state= intrerpretInput(percept)
    rule= Rule_Match(state, rules)
    action=rule
    return action


print(SimpleReflexAgent(percept))
    
