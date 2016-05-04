# -*- coding: utf-8 -*-

from assignment3 import Variable, Variables, Constraint, Constraints, BinaryCSP
from p1_is_complete import is_complete
from p2_is_consistent import is_consistent

def select_unassigned_variable(csp):
	"""Selects the next unassigned variable, or None if there is no more unassigned variables
	(i.e. the assignment is complete).

	For P3, *you do not need to modify this method.*
	"""
	return next((variable for variable in csp.variables if not variable.is_assigned()))


def order_domain_values(csp, variable):
	"""Returns a list of (ordered) domain values for the given variable.

	For P3, *you do not need to modify this method.*
	"""
	return [value for value in variable.domain]


def inference(csp, variable):
	"""Performs an inference procedure for the variable assignment.

	For P3, *you do not need to modify this method.*
	"""
	return True


def backtracking_search(csp):
	"""Entry method for the CSP solver.  This method calls the backtrack method to solve the given CSP.

	If there is a solution, this method returns the successful assignment (a dictionary of variable to value);
	otherwise, it returns None.

	For P3, *you do not need to modify this method.*
	"""
	if backtrack(csp):
		return csp.assignment
	else:
		return None


def backtrack(csp):
	"""Performs the backtracking search for the given csp.

	If there is a solution, this method returns True; otherwise, it returns False.
	"""

	# TODO implement this
	#pass

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





