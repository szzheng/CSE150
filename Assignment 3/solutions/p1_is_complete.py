# -*- coding: utf-8 -*-

from assignment3 import Variable, Variables, Constraint, Constraints, BinaryCSP


def is_complete(csp):
	"""Returns True when the CSP assignment is complete, i.e. all of the variables in the CSP have values assigned."""

	# Hint: The list of all variables for the CSP can be obtained by csp.variables.
	# Also, if the variable is assigned, variable.is assigned() will be True.
	# (Note that this can happen either by explicit assignment using variable.assign(value),
	# or when the domain of the variable has been reduced to a single value.)

	# TODO implement this
	
	''' Get the variables '''
	variablesList = (csp.variables)._variable_list

	complete = True

	''' Loop through variables, incomplete as soon as one is not assigned '''
	for v in variablesList:
		#currentVariable = variablesList.pop(0)
		currentVariable = v

		if not(currentVariable.is_assigned()): 
			complete = False
			return complete


	return complete 
	