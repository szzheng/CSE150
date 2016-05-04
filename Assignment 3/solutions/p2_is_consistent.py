# -*- coding: utf-8 -*-

from assignment3 import Variable, Variables, Constraint, Constraints, BinaryCSP

def is_consistent(csp, variable, value):
    """Returns True when the variable assignment to value is consistent, i.e. it does not violate any of the constraints
    associated with the given variable for the variables that have values assigned.

    For example, if the current variable is X and its neighbors are Y and Z (there are constraints (X,Y) and (X,Z)
    in csp.constraints), and the current assignment as Y=y, we want to check if the value x we want to assign to X
    violates the constraint c(x,y).  This method does not check c(x,Z), because Z is not yet assigned."""

    # TODO implement this
    
    ''' get constraints '''
    constraints = csp.constraints[variable]

    consistent = True

    ''' loop through neighbors '''
    for i in constraints:

    	currentConstraint = i

    	var1 = currentConstraint.var1    # Should be variable
    	var2 = currentConstraint.var2


    	if (var2.is_assigned()):

    		val2 = var2.value
    		if not(currentConstraint.is_satisfied(value, val2)):
    			consistent = False
    			return consistent

    		reverseCurrentConstraint = currentConstraint._flip()
    		if not(reverseCurrentConstraint.is_satisfied(val2, value)):
    			consistent = False
    			return consistent

    return consistent

