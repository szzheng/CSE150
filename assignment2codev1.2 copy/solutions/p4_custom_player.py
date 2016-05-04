# -*- coding: utf-8 -*-

__author__ = 'Dan'
__email__ = 'daz040@eng.ucsd.edu'

from assignment2 import Player, State, Action


class CustomPlayer(Player):
	"""The custom player implementation.
	"""

	def __init__(self):
		"""Called when the Player object is initialized. You can use this to
		store any persistent data you want to store for the  game.

		For technical people: make sure the objects are picklable. Otherwise
		it won't work under time limit.
		"""

		global transpositionTableForMax
		transpositionTableForMax = {}

		global transpositionTableForMin
		transpositionTableForMin = {}

		pass

	def move(self, state):
		"""Calculates the best move from the given board using the minimax
		algorithm with alpha-beta pruning and transposition table.
		:param state: State, the current state of the board.
		:return: Action, the next move
		"""

		global player
		player = state.player

		global transpositionTableForMax
		#transpositionTableForMax = {}

		global transpositionTableForMin
		#transpositionTableForMin = {}

		global depth_limit
		depth_limit = 1

		return self.iterativeDeepeningAlphaBeta(state)


	def iterativeDeepeningAlphaBeta(self, state):

		''' state key '''
		'''
		stateString = ""
		for i in state.board:
			stateString += str(i)
			stateString += ","
		'''
		stateString = state.ser()

		global transpositionTableForMax
		transpositionTableForMax = {}

		global transpositionTableForMin
		transpositionTableForMin = {}

		global depth_limit
		depth_limit = 1

		global search_is_complete
		search_is_complete = True

		global max_depth_reached
		max_depth_reached = 0

		while not(self.is_time_up()):
			#print "ITERATE at " + str(depth_limit)
			#transpositionTableForMax = {}
			#transpositionTableForMin = {}

			currentDepth = max_depth_reached

			search_is_complete = True

			self.maxValue(state, -2, 2, 0)

			#if (currentDepth == max_depth_reached):
				#break
			if (search_is_complete):
				break

			#print str(depth_limit)
			depth_limit = depth_limit + 1



		action = transpositionTableForMax.get(stateString, None)
		if (action is None):
			return None
		else:
			return action[0]

	def maxValue(self, state, alpha, beta, depth):

		global depth_limit
		global transpositionTableForMax
		global search_is_complete
		global max_depth_reached


		if (depth >= max_depth_reached):
			max_depth_reached = depth
			
		''' state key '''
		'''
		stateString = ""
		for i in state.board:
			stateString += str(i)
			stateString += ","
		'''
		stateString = state.ser()

		''' Check the time '''
		
		if (self.is_time_up()):
			if (state.is_terminal()): 
				value = state.utility(player)

			else:
				value = self.evaluate(state, player.row, depth)
				search_is_complete = False

			#transpositionTableForMax[stateString] = (None, value, depth)
			return value
		

		''' Check the depth '''

		if (depth >= depth_limit):
			if (state.is_terminal()): 
				value = state.utility(player)

			else:
				value = self.evaluate(state, player.row, depth)
				search_is_complete = False

			#transpositionTableForMax[stateString] = (None, value, depth)
			return value
		

		''' PROCEED NORMALLY FROM HERE '''

		''' 1. Terminal test '''
		if (state.is_terminal()): 
			value = state.utility(player)
			#transpositionTableForMax[stateString] = (None, value, depth)
			return value

		''' 2. Initialize value to negative infinite (effectively) '''
		value = -2 


		''' Process actions '''
		actions = state.actions()

		# No actions available
		if not(actions): 
			nextState = State(state.board, state.opponent_row, state.player)
			value = self.minValue(nextState, alpha, beta, depth + 1)
			#transpositionTableForMax[stateString] = (None, value, depth)

			# Prune if possible
			'''
			if (value >= beta):
				print "PRUNING WHEN THERE's NO ACTION"
				return value
			'''
			'''
			if (value > alpha):
				alpha = value
			'''
			return value

		else:
			bestAction = transpositionTableForMax.get(stateString, None)
			if not(bestAction is None):
				currentAction = bestAction[0]
				#print "BEST ACTION AT MAX" + stateString + " " + str(currentAction.index)
				#print str(state.board)
				nextState = state.result(currentAction)

				valueTmp = self.minValue(nextState, alpha, beta, depth + 1)


				# Get the max value
				if (value < valueTmp):
					value = valueTmp
					#print "Storing for max, at " + stateString + " " + str(currentAction.index)
					transpositionTableForMax[stateString] = (currentAction, value, depth)


				# Prune if possible
				if (value >= beta):
					return value
				if (value > alpha):
					alpha = value

				while (actions):

					currentAction = actions.pop(0)
					if not(currentAction == bestAction[0]):
						nextState = state.result(currentAction)

						valueTmp = self.minValue(nextState, alpha, beta, depth + 1)

						#if (depth == 0):
						#	print str(nextState.board) + " " + str(valueTmp)

						# Get the max value
						if (value < valueTmp):
							value = valueTmp
							#print "Storing for max, at " + stateString + " " + str(currentAction.index)
							transpositionTableForMax[stateString] = (currentAction, value, depth)

						# TIEBREAKER
						if (value == valueTmp):
							if (currentAction.index < (bestAction[0]).index):
								transpositionTableForMax[stateString] = (currentAction, value, depth)


						# Prune if possible
						if (value > beta):
							return value
						if (value > alpha):
							alpha = value
			else :
				while (actions):

					currentAction = actions.pop(0)
					nextState = state.result(currentAction)

					valueTmp = self.minValue(nextState, alpha, beta, depth + 1)

					#if (depth == 0):
					#	print str(nextState.board) + " " + str(valueTmp)

					# Get the max value
					if (value < valueTmp):
						value = valueTmp
						#print "Storing for max, at " + stateString + " " + str(currentAction.index)
						transpositionTableForMax[stateString] = (currentAction, value, depth)


					# Prune if possible
					if (value >= beta):
						return value
					if (value > alpha):
						alpha = value

			return value

	def minValue(self, state, alpha, beta, depth):

		global depth_limit
		global transpositionTableForMin
		global search_is_complete
		global max_depth_reached

		if (depth >= max_depth_reached):
			max_depth_reached = depth

		''' state key '''
		'''
		stateString = ""
		for i in state.board:
			stateString += str(i)
			stateString += ","
		'''
		stateString = state.ser()

		
		''' Check the time '''
		
		if (self.is_time_up()):
			if (state.is_terminal()): 
				value = state.utility(player)

			else:
				value = self.evaluate(state, player.row, depth)
				search_is_complete = False

			#transpositionTableForMax[stateString] = (None, value, depth)
			return value
		
		

		''' Check the depth '''
		
		if (depth >= depth_limit):
			if (state.is_terminal()): 
				value = state.utility(player)

			else:
				value = self.evaluate(state, player.row, depth)
				search_is_complete = False

			#transpositionTableForMax[stateString] = (None, value, depth)
			return value

		''' PROCEED NORMALLY FROM HERE '''

		''' 1. Terminal test '''
		if (state.is_terminal()): 
			value = state.utility(player)
			#transpositionTableForMin[stateString] = (None, value, depth)
			return value

		''' 2. Initialize value to positive infinite (effectively) '''
		value = 2

		''' Process actions '''
		actions = state.actions()

		# No actions available
		if not(actions): 
			nextState = State(state.board, state.opponent_row, state.player)
			value = self.maxValue(nextState, alpha, beta, depth + 1)
			#transpositionTableForMin[stateString] = (None, value, depth)

			'''
			if (value <= alpha):
				print "PRUNING WHEN THERE's NO ACTION"
				return value
			'''
			'''
			if (value > beta):
				beta = value
			'''

			return value

		else:

			bestAction = transpositionTableForMin.get(stateString, None)
			if not(bestAction is None):

				currentAction = bestAction[0]
				#print "BEST ACTION AT MIN" + stateString + " " + str(currentAction.index)

				nextState = state.result(currentAction)

				valueTmp = self.maxValue(nextState, alpha, beta, depth + 1)

				# Get the max value
				if (value > valueTmp):
					value = valueTmp
					#print "Storing for min, at " + stateString + " " + str(currentAction.index)
					transpositionTableForMin[stateString] = (currentAction, value, depth)

				if (value <= alpha):
					return value

				if (value > beta):
					beta = value

				while (actions):

					currentAction = actions.pop(0)
					if not(currentAction == bestAction[0]):
						nextState = state.result(currentAction)

						valueTmp = self.maxValue(nextState, alpha, beta, depth + 1)

						# Get the max value
						if (value > valueTmp):
							value = valueTmp
							#print "Storing for min, at " + stateString + " " + str(currentAction.index)
							transpositionTableForMin[stateString] = (currentAction, value, depth)

						# TIEBREAKER
						if (value == valueTmp):
							if (currentAction.index < (bestAction[0]).index):
								transpositionTableForMax[stateString] = (currentAction, value, depth)

						if (value < alpha):
							return value

						if (value > beta):
							beta = value

			else:
				while (actions):

					currentAction = actions.pop(0)
					nextState = state.result(currentAction)

					valueTmp = self.maxValue(nextState, alpha, beta, depth + 1)

					#if (depth == 0):
					#	print str(nextState.board) + " " + str(valueTmp)

					# Get the max value
					if (value > valueTmp):
						value = valueTmp
						#print "Storing for min, at " + stateString + " " + str(currentAction.index)
						transpositionTableForMin[stateString] = (currentAction, value, depth)

					if (value <= alpha):
						return value

					if (value > beta):
						beta = value

			return value


	


	def evaluate(self, state, my_row, depth):
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

			if (stonesInYourGoal > (m * n)):
				return 1

			if (stonesInOpponentGoal > (m * n)):
				return -1

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

			stonesInYourGoal = state.board[yourGoalIndex]
			stonesInOpponentGoal = state.board[opponnentGoalIndex]

			if (stonesInYourGoal > (m * n)):
				return 1
			if (stonesInOpponentGoal > (m * n)):
				return -1

			for i in range (0, yourGoalIndex):
				if (state.board[i] == 0):
					emptySpotsOnYourSide += 1
				else:
					stonesOnYourSide += state.board[i]

			for i in range (yourGoalIndex + 1, opponnentGoalIndex):
				if (state.board[i] == 0):
					emptySpotsOnOpponentSide += 1
				else:
					stonesOnOpponentSide += state.board[i]
		
		''' End - evaluate for BOTTOM player '''
		#print "stonesInYourGoal: " + str(stonesInYourGoal)
		#print "stonesInOpponentGoal: " + str(stonesInOpponentGoal)
		#print "stonesOnYourSide: " + str(stonesOnYourSide)
		#print "stonesOnOpponentSide: " + str(stonesOnOpponentSide)

		value = 2*(stonesInYourGoal - stonesInOpponentGoal) + (stonesOnYourSide - stonesOnOpponentSide)
		value = float(value) / (3 * m * n)
		#print "m: " + str(m)  + " n: " + str(n)
		#print "value: " + str(value)
		



		#raise NotImplementedError("Need to implement this method")

		return value
