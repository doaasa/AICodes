loc_A, loc_B = (0, 0), (1, 0)

def TableDrivenAgentProgram(table):
    """
    [Figure 2.7]
    This agent selects an action based on the percept sequence.
    It is practical only for tiny domains.
    To customize it, provide as table a dictionary of all
    {percept_sequenceaction} pairs.
    """
    percepts = []

    def program(percept):
        percepts.append(percept)
        action = table.get(tuple(percepts))
        return action

    return program
table = {((loc_A, 'Clean'),):'Right',
             ((loc_A, 'Dirty'),) :'Suck',
             ((loc_B, 'Clean'),) :'Left',
             ((loc_B, 'Dirty'),):'Suck',
             ((loc_A, 'Dirty'), (loc_A, 'Clean')): 'Right',
             ((loc_A, 'Clean'), (loc_B, 'Dirty')) :'Suck',
             ((loc_B, 'Clean'), (loc_A, 'Dirty')) :'Suck',
             ((loc_B, 'Dirty'), (loc_B, 'Clean')): 'Left',
             ((loc_A, 'Dirty'), (loc_A, 'Clean'), (loc_B, 'Dirty')) :'Suck',
             ((loc_B, 'Dirty'), (loc_B, 'Clean'), (loc_A, 'Dirty')) :'Suck'}
program1 = TableDrivenAgentProgram(table)
print(program1((loc_A, 'Clean')))



