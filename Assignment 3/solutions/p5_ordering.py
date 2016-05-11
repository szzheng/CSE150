# -*- coding: utf-8 -*-

def select_unassigned_variable(csp):
    """Selects the next unassigned variable, or None if there is no more unassigned variables
    (i.e. the assignment is complete).

    This method implements the minimum-remaining-values (MRV) and degree heuristic. That is,
    the variable with the smallest number of values left in its available domain.  If MRV ties,
    then it picks the variable that is involved in the largest number of constraints on other
    unassigned variables.
    """

    #variable used to store the current best choice possibl;e
    nextVar = None;
    #variable used to represent the number of possible moves a variable will
    #have
    minDom = 9999999;
    
   
    
    #if the variable is already assigned ignore it
    for v in csp.variables:
        if v.is_assigned():
            continue

     #but if theres a tie we need to break by comparing the number of constraints
        if minDom == len(v.domain):
            num = 0;
            for cons in csp.constraints:
                if cons.var1 == v or cons.var2 ==v:
                    num +=1;
                if cons.var1 == nextVar or cons.var1 == nextVar:
                    num -=1;

            if num>0:
                nextVar =v;
        
            
   

        # if the length of the variables domain is less than the
        #earliers variables it will have less possible moves
        #so switch
        if minDom > len(v.domain):
            nextVar = v;
            minDom = len(v.domain);

    if nextVar:
        return nextVar
    else:
        return None
        
  


def order_domain_values(csp, variable):
    """Returns a list of (ordered) domain values for the given variable.

    This method implements the least-constraining-value (LCV) heuristic; that is, the value
    that rules out the fewest choices for the neighboring variables in the constraint graph
    are placed before others.
    """

    #list for constraints
    varsConstraints = [];
    #list of those effected by constraints
    others = [];
    #list of moves and their counts
    moves= [];
    
    #get all constraints on this variable
    # get any other variable that would be affected by a move
    for con in csp.constraints:
        if con.var1 == variable :
            varsConstraints.append(con);
            others.append(con.var2)
        elif con.var2 == variable:
            varsConstraints.append(con);
            others.append(con.var1);

    #check if the value is in any of the other variables domains
    # if it is we keep a count of how many times it appears and
    #record that count with its corresponding value in a list

    for x in range (0, len(variable.domain)):
        appearence = 0;
        for o in others:
            if variable.domain[x] in o.domain:
                appearence += 1;

        moves.insert(x,appearence);

    tempMove = 0;
    tempIndex = 0;
    listofmoves = []
    list2 = []
    for x in range (0,len(variable.domain)):
        tempMove = min(moves)
       
        tempIndex = moves.index(tempMove)
        moves[tempIndex] = 9999999999;
        listofmoves.append(variable.domain[tempIndex])
      

    list2 = listofmoves[::-1]
    return listofmoves
    
        
    


    # TODO implement this
    pass
