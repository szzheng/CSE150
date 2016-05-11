# -*- coding: utf-8 -*-

from collections import deque
from p1_is_complete import is_complete
from p2_is_consistent import is_consistent
from p3_basic_backtracking import select_unassigned_variable, order_domain_values


def inference(csp, variable):
    """Performs an inference procedure for the variable assignment.

    For P6, *you do not need to modify this method.*
    """
    return ac3(csp, csp.constraints[variable].arcs())


def backtracking_search(csp):
    """Entry method for the CSP solver.  This method calls the backtrack method to solve the given CSP.

    If there is a solution, this method returns the successful assignment (a dictionary of variable to value);
    otherwise, it returns None.

    For P6, *you do not need to modify this method.*
    """
    if backtrack(csp):
        return csp.assignment
    else:
        return None


def backtrack(csp):
    """Performs the backtracking search for the given csp.

    If there is a solution, this method returns True; otherwise, it returns False.
    """

    ''' Initial completion check '''
    complete = is_complete(csp)
    if (complete):
		return complete

    #print len(csp.variables) + " length"
    currentVariable = select_unassigned_variable(csp)

    if not(currentVariable is None):
		#print str(currentVariable.name)
		for dv in order_domain_values(csp, currentVariable):
			domainValue = dv
			#print "domainValue: " + str(domainValue)

			if (is_consistent(csp, currentVariable, domainValue)):

				#print "assign"
				csp.variables.begin_transaction()

				''' assign variable '''

				currentVariable.assign(domainValue)

				result = backtrack(csp)
				if not(result == False):
					return True

				csp.variables.rollback()

    return False



def ac3(csp, arcs=None):
    """Executes the AC3 or the MAC (p.218 of the textbook) algorithms.

    If the parameter 'arcs' is None, then this method executes AC3 - that is, it will check the arc consistency
    for all arcs in the CSP.  Otherwise, this method starts with only the arcs present in the 'arcs' parameter
    in the queue.

    Note that the current domain of each variable can be retrieved by 'variable.domains'.

    This method returns True if the arc consistency check succeeds, and False otherwise.  Note that this method does not
    return any additional variable assignments (for simplicity)."""

    queue_arcs = deque(arcs if arcs is not None else csp.constraints.arcs())

    ''' Execute AC3'''
    if (arcs == None):
		#print "AC3"
		queue_arcs = deque(csp.constraints.arcs())


    while (queue_arcs):

		arc = queue_arcs.popleft()
		if revise(csp, arc[0], arc[1]):
			if not(arc[0].domain):
				return False

				''' get constraints '''
				constraints = csp.constraints[arc[1]]
				for constraint in constraints:
					neighbor = constraint.var2
					queue_arcs.append((neighbor, arc[0]))

    return True
