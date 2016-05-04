# -*- coding: utf-8 -*-

__author__ = 'Dan'
__email__ = 'daz040@eng.ucsd.edu'

from assignment2 import Player, State, Action

import pickle

'''
1. Check for the self.is_time_up() condition often in your code (searching through the game
tree, for example). You can check it anywhere within the Player class methods.
2. Once the self.is_time_up() becomes True, your code should finish up and return the move
as quickly as possible. There will only be about one second (1 second) allocated for this
portion, so it should only do “quick” operations to finish up (such as calculating the best
move from the tree you’ve searched.)
'''

class CustomPlayer(Player):
	"""The custom player implementation.
	"""

	def __init__(self):
		"""Called when the Player object is initialized. You can use this to
		store any persistent data you want to store for the  game.

		For technical people: make sure the objects are picklable. Otherwise
		it won't work under time limit.
		"""


		transposition_table = {}
		pass


	player = None
	transposition_table = {}
	action = None

	def alphabetaIterative(self, state):

		global action
		global depth_limit
		global changed 
		global transposition_table
		global nonTerminal
		global maxDepth

		maxDepth = 0
		changed = False

		stateString = ""
		for i in state.board:
			stateString += str(i)
		stateString += str(state.player_row)

		limit = 2

		
		while not(self.is_time_up == True):
			transposition_table = {}
			maxDepth = 0
			print "ITERATING again"
			nonTerminal = False
			value = self.maxValue(state, limit * -1, limit, 0)
			print "MAX DEPTH REACHED is " + str(maxDepth)
			depth_limit += 1

			# after we search and nothing has changed, we break out
			if (nonTerminal == False):
				break
		
		#print "TIME's UP"
		#value = self.maxValue(state, limit * -1, limit, 0)
		#depth_limit += 1

		bestAction = transposition_table.get(stateString, None)
		if (bestAction is None):
			return None
		else:
			return bestAction[0]

	def maxValue(self, state, alpha, beta, depth):
		
		global maxDepth
		if (depth > maxDepth):
			maxDepth = depth
		global nonTerminal
		stateString = ""
		for i in state.board:
			stateString += str(i)
		stateString += str(state.player_row) 

		#if (stateString == "11110111100"):
			#if not(transposition_table):
				#print "GOOD"

		#if (depth_limit == 35 or depth_limit == 36):
			#print stateString

		# If we're at the depth limit, stop
		# Apply utility function if we're at terminal node, apply evaluation function if we're not
		if (depth >= depth_limit):
			# Terminal test
			if (state.is_terminal()): 
				#print "Applying utility"
				utility = state.utility(player)
				"Applying utility for " + stateString + " " + str(utility) 
				transposition_table[stateString] = (None, utility, depth)
				return utility

			else:
				#print "Applying evaluation"
				#changed = True
				value = self.evaluate(state, player.row)
				"Applying valuefor " + stateString + " " + str(value)
				transposition_table[stateString] = (None, value, depth)
				nonTerminal = True
				return value

		# We're not at the depth limit, handle terminality anyways
		# Terminal test
		if (state.is_terminal()): 
			
			utility = state.utility(player)
			"Applying utility not at depth limit for " + stateString + " " + str(utility)
			transposition_table[stateString] = (None, utility, depth)
			return utility

		# Otherwise we expand the node

		# Past lowest possible utility, effectively negative infinite
		utility = -2

		# Get the actions from this state
		actions = state.actions()

		# No best action yet, will be set recursively on the way up
		bestAction = None 

		# No available actions, repeat state but switch players
		if not(actions):
			nextState = State(state.board, state.opponent_row, state.player)
			utility = self.minValue(nextState, alpha, beta, depth + 1)
			transposition_table[stateString] = (None, utility, depth)

			if (utility >= beta):
				return utility

			if (utility > alpha):
				alpha = utility

		# Actions available, start from low to high index, find the best one


		bestAction = transposition_table.get(stateString, None)
		if (bestAction is None):
			while (actions):
				
				currentAction = actions.pop(0)
				nextState = state.result(currentAction)

				utilityTmp = self.minValue(nextState, alpha, beta, depth + 1)

				#if (stateString == "11110111100"):
				#	print str(utilityTmp)
				if (utilityTmp > utility):

				#	if (stateString == "11110111100"):
				#		print "WHOANELLY"
					utility = utilityTmp
					bestAction = currentAction
					transposition_table[stateString] = (bestAction, utility, depth)

				'''
				# tie break
				if (utility == utilityTmp):
					bestAction = transposition_table.get(stateString, None)
					index = bestAction[0].index
					if (currentAction.index < index):
						print "tiebreaking"
						bestAction = currentAction
						transposition_table[stateString] = (bestAction, utility)'''

				if (utility >= beta):
					return utility

				if (utility > alpha):
					alpha = utility

			return utility
		else:
			
			if (depth < bestAction[2]):
				#print "REEXPLORING at " + stateString
				while (actions):
					currentAction = actions.pop(0)
					nextState = state.result(currentAction)

					utilityTmp = self.minValue(nextState, alpha, beta, depth + 1)
					if (utilityTmp > utility):
						utility = utilityTmp
						bestAction = currentAction
						#if (nonTerminal == True):
							#print "UPDATING"
						#print "REUPDATING at " + stateString
						transposition_table[stateString] = (bestAction, utility, depth)

					# tie break
					if (utility == utilityTmp):
						bestAction = transposition_table.get(stateString, None)
						index = bestAction[0].index
						if (currentAction.index < index):
							print "tiebreaking"
							bestAction = currentAction
							transposition_table[stateString] = (bestAction, utility, depth)

					
					if (utility >= beta):
						return utility

					if (utility > alpha):
						alpha = utility

				#print "utility " + str(utility) + "bestaction 1: " + str(bestAction[1])
				return utility
			else:
				return bestAction[1]
			
			return bestAction[1]

	def minValue(self, state, alpha, beta, depth):
		global maxDepth
		if (depth > maxDepth):
			maxDepth = depth
		global nonTerminal

		stateString = ""
		for i in state.board:
			stateString += str(i)

		stateString += str(state.player_row)


		if (depth >= depth_limit):
			
			# Terminal test
			if (state.is_terminal()): 
				
				utility = state.utility(player)
				print "Applying utiltiy for " + stateString + " " + str(utility)
				transposition_table[stateString] = (None, utility, depth)
				return utility
			
			else:
				
				nonTerminal = True
				value = self.evaluate(state, player.row)
				print "Applying evaluation for " + stateString + " " + str(value)
				transposition_table[stateString] = (None, value, depth)
				return value
			


		bestAction = transposition_table.get(stateString, None)
		#if bestAction is None:
		#	changed = True


		# Terminal test
		if (state.is_terminal()):
			
			utility = state.utility(player)
			"Applying utility not at depth limit for " + stateString + " " + str(utility)
			transposition_table[stateString] = (None, utility, depth)
			return utility
		# Past lowest possible utility, effectively negative infinite
		utility = 2

		# Get the actions from this state
		actions = state.actions()

		# No available actions, repeat state but switch players
		if not(actions):
			nextState = State(state.board, state.opponent_row, state.player)
			utility = self.maxValue(nextState, alpha, beta, depth + 1)
			transposition_table[stateString] = (None, utility, depth)

			if (utility <= alpha):
				return utility

			if (beta > utility):
				beta = utility

		if (bestAction is None):
			# Actions available
			while (actions):
				currentAction = actions.pop(0)
				nextState = state.result(currentAction)

				utilityTmp = self.maxValue(nextState, alpha, beta, depth + 1)
				if (utility > utilityTmp):
					utility = utilityTmp
					bestAction = currentAction
					transposition_table[stateString] = (bestAction, utility, depth)

				# tie break
				'''
				if (utility == utilityTmp):
					bestAction = transposition_table.get(stateString, None)
					index = bestAction[0].index
					if (currentAction.index < index):
						print "tiebreaking"
						bestAction = currentAction
						transposition_table[stateString] = (bestAction, utility)'''


				if (utility <= alpha):
					return utility

				if (utility < beta):
					beta = utility

			return utility
		else:

			# If we're at a higher depth than the depth we last saw this state, we will explore 
			
			if (depth < bestAction[2]):

				#explore
				#print "REEXPLORING at " + stateString
				while (actions):
					currentAction = actions.pop(0)
					nextState = state.result(currentAction)

					utilityTmp = self.maxValue(nextState, alpha, beta, depth + 1)
					if (utility > utilityTmp):
						utility = utilityTmp
						bestAction = currentAction
						#if (nonTerminal == True):
						#	print "UPDATING"
						#print "Updating at " + stateString
						transposition_table[stateString] = (bestAction, utility, depth)

					# tie break
					
		
					if (utility == utilityTmp):
						bestAction = transposition_table.get(stateString, None)
						index = bestAction[0].index
						if (currentAction.index < index):
							print "tiebreaking"
							bestAction = currentAction
							transposition_table[stateString] = (bestAction, utility, depth)

			
					if (utility <= alpha):
						return utility

					if (utility < beta):
						beta = utility

				#print "utility " + str(utility) + "bestaction 1: " + str(bestAction[1])
				return utility
			else:
				return bestAction[1]
			
			return bestAction[1]

	def move(self, state):
		"""Calculates the best move from the given board using the minimax
		algorithm with alpha-beta pruning and transposition table.
		:param state: State, the current state of the board.
		:return: Action, the next move
		"""
		###### Start searching ######



		global changed
		changed = False
		global depth_limit
		depth_limit = 1

		global transposition_table
		transposition_table = {}
		
		global player
		player = state.player


	

		#### ALPHA BETA COMPARISON ###

		return self.alphabetaIterative(state)



	def evaluate(self, state, my_row):
		"""
		Evaluates the state for the player with the given row
		"""


		m = state.M 
		n = state.N 


		''' initialize variables '''
		yourGoalIndex = 0
		opponnentGoalIndex = 0

		stonesInYourGoal = 0
		stonesInOpponentGoal = 0

		stonesOnYourSide = 0
		stonesOnOpponentSide = 0

		emptySpotsOnYourSide = 0
		emptySpotsOnOpponentSide = 0
		''' end  initialize variables '''

		''' evaluate for TOP plyaer '''
		if (my_row == 1):
			yourGoalIndex = 2 * m + 1
			opponnentGoalIndex = m

			stonesInYourGoal = state.board[yourGoalIndex]
			stonesInOpponentGoal = state.board[opponnentGoalIndex]

			for i in range (opponnentGoalIndex + 1, yourGoalIndex):
				if (state.board[i] == 0):
					emptySpotsOnYourSide += 1
				else:
					stonesOnYourSide += state.board[i]

			for i in range (0, opponnentGoalIndex):

				if (state.board[i] == 0):
					emptySpotsOnOpponentSide += 1
				else:
					stonesOnOpponentSide += state.board[i]

		''' END - evaluate for TOP player '''

		''' Evaluate for BOTTOM player '''
		if (my_row == 0):
			#print "MY ROW IS 0"
			yourGoalIndex = m
			opponnentGoalIndex = 2 * m + 1

			for i in range (0, yourGoalIndex):
				stonesOnYourSide += state.board[i]

			for i in range (yourGoalIndex + 1, opponnentGoalIndex):
				stonesOnOpponentSide += state.board[i]
		
		''' End - evaluate for BOTTOM player '''
		#print "stonesInYourGoal: " + str(stonesInYourGoal)
		#print "stonesInOpponentGoal: " + str(stonesInOpponentGoal)
		#print "stonesOnYourSide: " + str(stonesOnYourSide)
		#print "stonesOnOpponentSide: " + str(stonesOnOpponentSide)

		value = (stonesInYourGoal - stonesInOpponentGoal 
			+ stonesOnYourSide - stonesOnOpponentSide)
		value = float(value) / (2 * m * n)
		#print "m: " + str(m)  + " n: " + str(n)
		#print "value: " + str(value)
		



		#raise NotImplementedError("Need to implement this method")

		return value
