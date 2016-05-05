# -*- coding: utf-8 -*-

from collections import deque
from assignment3 import Variable, Variables, Constraint, Constraints, BinaryCSP
from p1_is_complete import is_complete
from p2_is_consistent import is_consistent

def ac3(csp, arcs=None):
	"""Executes the AC3 or the MAC (p.218 of the textbook) algorithms.

	If the parameter 'arcs' is None, then this method executes AC3 - that is, it will check the arc consistency
	for all arcs in the CSP.  Otherwise, this method starts with only the arcs present in the 'arcs' parameter
	in the queue.

	Note that the current domain of each variable can be retrieved by 'variable.domains'.

	This method returns True if the arc consistency check succeeds, and False otherwise."""

	queue_arcs = deque(arcs if arcs is not None else csp.constraints.arcs())

	# TODO implement this
	#pass

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
		





def revise(csp, xi, xj):
	# You may additionally want to implement the 'revise' method.

	revised = False

	for di in xi.domain:

		satisfactory = False

		''' get constraints '''
		constraints = csp.constraints[xi]
		for constraint in constraints:
			if (constraint.var2 == xj):
				for dj in xj.domain:

					if (constraint.is_satisfied(di, dj)):
						satisfactory = True

					reverseConstraint = constraint._flip()
					if (reverseConstraint.is_satisfied(dj, di)):
						satisfactory = True
	
		if (satisfactory == False):
			(xi.domain).remove(di)
			revised = True
	return revised


