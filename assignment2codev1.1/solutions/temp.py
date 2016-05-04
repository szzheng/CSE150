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

class TEMPTEMPAlphaBetaWithMoveOrderingAndEvaluationPlayer(Player):
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

	def move(self, state):
		"""
		You're free to implement the move(self, state) however you want. Be
		run time efficient and innovative.
		:param state: State, the current state of the board.
		:return: Action, the next move
		"""
		global changed
		changed = False
		global depth_limit
		depth_limit = 1

		global transposition_table
		transposition_table = {}
		
		global player
		player = state.player


	

		#### ALPHA BETA COMPARISON ###

		return self.iterativeDeepeningAlphabeta(state)

		#raise NotImplementedError("Need to implement this method")


	def iterativeDeepeningAlphabeta(self, state):

		global action
		global depth_limit
		global changed 
		changed = False

		stateString = ""
		for i in state.board:
			stateString += str(i)
		stateString += str(state.player_row)

		limit = state.M * state.N + 1

		
		while not(self.is_time_up == True):
			#print str(depth_limit)
			changed = False
			value = self.maxValue(state, limit * -1, limit, 0)
			depth_limit += 1

			# after we search and nothing has changed, we break out
			if (changed == False):
				#print "HI"
				break
		
		print "TIME's UP"
		#value = self.maxValue(state, limit * -1, limit, 0)
		#depth_limit += 1

		bestAction = transposition_table.get(stateString, None)
		if (bestAction is None):
			return None
		else:
			return bestAction[0]

	def maxValue(self, state, alpha, beta, depth):
		#print "maxValue executes at depth " + str(depth)
		stateString = ""
		for i in state.board:
			stateString += str(i)
		stateString += str(state.player_row)

		#print stateString

		global changed

		#print("MAX VALUE CALLED")
		global depth_limit

		# Check the time, start exiting
		if (self.is_time_up == True):
			print("TIME IS UP")

			return self.evaluate(state, state.player_row)

		#print("TIME IS NOT UP")

		# Check the depth:
		if (depth >= depth_limit):
			#print ("REACHED THE LIMIT")
			return self.evaluate(state, state.player_row)

		#print ("PAST THE CHECK")
		# Check if best action exists

		bestAction = transposition_table.get(stateString, None)


		value = (state.M * state.N + 1) * -1
		if (stateString == "020700180"):
			print str(value) + " BWAEfORE"


		# Best Action Exists
		# Expand best node first
		if not(bestAction is None):

			# Terminal test, exit
			if (state.is_terminal()):
				return bestAction[1]

			nextState = state.result(bestAction[0])
			valueTmp = self.minValue(nextState, alpha, beta, depth + 1)

			# Update value
			if (value > valueTmp):
				value = valueTmp

			# Prune if able to
			if (value >= beta):
				return value

			# Update alpha
			if (value > alpha):
				alpha = value

				'''
				# Terminal test
				if (state.is_terminal()): 
					return state.utility(player)

				# Past lowest possible utility, effectively negative infinite
				utility = 2
				'''

		else:
			### Change best action ###
			print "MAX" + stateString
			changed = True


		# Terminal test, exit
		if (state.is_terminal()):
			#print ("TERMINAL STATE")
			value = self.evaluate(state, state.player_row)
			transposition_table[stateString] = (None, value)
			return self.evaluate(state, state.player_row) 

		# Then expand OTHER nodes
		# Get the actions from this state
		actions = state.actions()

		# No available actions, repeat state but switch players
		if not(actions):
			#print "NO ACTIONS FOR MAX"
			nextState = State(state.board, state.opponent_row, state.player)
			value = self.minValue(nextState, alpha, beta, depth + 1)
			transposition_table[stateString] = (None, value)

			if (value >= beta):
				return value

			if (value > alpha):
				alpha = value

		# Actions available
		if (stateString == "020700180"):
			print str(value) + " BEfORE"
		while (actions):
			currentAction = actions.pop(0)

			# Check only nodes that aren't the previous best action
			if not(bestAction == None):
				if not(currentAction == bestAction[0]):

					nextState = state.result(currentAction)

					valueTmp = self.minValue(nextState, alpha, beta, depth + 1)
					if (valueTmp > value):
						value = valueTmp
						newBestAction = currentAction

						#if (stateString == "1011101"):
						#	print "WHAT?"
						transposition_table[stateString] = (newBestAction, value)

						# tie break
						'''
						if (utility == utilityTmp):
							bestAction = alphabetatranspositionTable.get(stateString, None)
							index = bestAction[0].index
							if (currentAction.index < index):
								print "tiebreaking"
								bestAction = currentAction
								alphabetatranspositionTable[stateString] = (bestAction, utility)'''


					# Prune if able
					if (value >= beta):
						return value

					# Update alpha
					if (value > alpha):
						alpha = value

			else:
				

				#print "NO BEST ACTION CHECKING ALL from " + stateString + " with intial value: " + str(value)
				nextState = state.result(currentAction)

				valueTmp = self.minValue(nextState, alpha, beta, depth + 1)
				print str(value)
				if (valueTmp > value):
					if (stateString == "020700180"):
						print "ACTION available"
					value = valueTmp
					newBestAction = currentAction
		
					transposition_table[stateString] = (newBestAction, value)

					# tie break
					'''
					if (utility == utilityTmp):
						bestAction = alphabetatranspositionTable.get(stateString, None)
						index = bestAction[0].index
						if (currentAction.index < index):
							print "tiebreaking"
							bestAction = currentAction
							alphabetatranspositionTable[stateString] = (bestAction, utility)'''


				# Prune if able
				if (value >= beta):
					return value

				# Update alpha
				if (value > alpha):
					alpha = value


		return value

	def minValue(self, state, alpha, beta, depth):

		#print "minValue executes at depth " + str(depth)
		stateString = ""
		for i in state.board:
			stateString += str(i)
		stateString += str(state.player_row)

		#print stateString


		global changed

		global depth_limit
		#print "MIN VALUE VALLED"
		# Check the time, start exiting
		if (self.is_time_up == True):
			print "TIME US UP"
			return self.evaluate(state, state.player_row) 

		#print "TIME US NOT UP"

		'''
		# Terminal test, exit
		if (state.is_terminal()):

			#print "TERMINAL"
			return self.evaluate(state, state.player_row) * -1

		'''

		# Check the depth:
		if (depth >= depth_limit):
			#print self.evaluate(state, state.player_row) * -1
			return self.evaluate(state, state.player_row) 

		# Check if best action exists
		bestAction = transposition_table.get(stateString, None)


		value = state.M * state.N + 1

		# Best Action Exists
		# Expand best node first
		if not(bestAction is None):

			#print "best action exists"

			# Terminal test, exit
			if (state.is_terminal()):
				return bestAction[1]

			nextState = state.result(bestAction[0])
			valueTmp = self.maxValue(nextState, alpha, beta, depth + 1)

			# Update value
			if (value > valueTmp):
				value = valueTmp

			# Prune if able to
			if (value <= alpha):
				return value

			# Update beta
			if (value < beta):
				beta = value

				'''
				# Terminal test
				if (state.is_terminal()): 
					return state.utility(player)

				# Past lowest possible utility, effectively negative infinite
				utility = 2
				'''

		else:
			#print "best action does not exist"
			### Change best action ### 
			print stateString
			changed = True
		#print "must print"

		# Terminal test, exit
		if (state.is_terminal()):
			#print (stateString + "TERMINAL STATE")
			value = self.evaluate(state, state.player_row)
			transposition_table[stateString] = (None, value)
			return self.evaluate(state, state.player_row) 

		# Then expand OTHER nodes
		# Get the actions from this state
		actions = state.actions()

		# No available actions, repeat state but switch players
		if not(actions):
			#print "NO ACTIONS FOR MIN"
			nextState = State(state.board, state.opponent_row, state.player)
			value = self.maxValue(nextState, alpha, beta, depth + 1)
			transposition_table[stateString] = (None, value)

			if (value <= alpha):
				return value

			if (value < beta):
				beta = value

		# Actions available
		while (actions):
			currentAction = actions.pop(0)

			if not(bestAction == None):

				# Check only nodes that aren't the previous best action
				if not(currentAction == bestAction[0]):

					nextState = state.result(currentAction)

					valueTmp = self.maxValue(nextState, alpha, beta, depth + 1)
					if (value > valueTmp):
						value = valueTmp
						newBestAction = currentAction
						transposition_table[stateString] = (newBestAction, value)

						# tie break
						'''
						if (utility == utilityTmp):
							bestAction = alphabetatranspositionTable.get(stateString, None)
							index = bestAction[0].index
							if (currentAction.index < index):
								print "tiebreaking"
								bestAction = currentAction
								alphabetatranspositionTable[stateString] = (bestAction, utility)'''


					# Prune if able
					if (value <= alpha):
						return value

					# Update beta
					if (value < beta):
						beta = value
			else:
	

				nextState = state.result(currentAction)

				valueTmp = self.maxValue(nextState, alpha, beta, depth + 1)
				if (value > valueTmp):
					value = valueTmp
					newBestAction = currentAction

					transposition_table[stateString] = (newBestAction, value)

					# tie break
					'''
					if (utility == utilityTmp):
						bestAction = alphabetatranspositionTable.get(stateString, None)
						index = bestAction[0].index
						if (currentAction.index < index):
							print "tiebreaking"
							bestAction = currentAction
							alphabetatranspositionTable[stateString] = (bestAction, utility)'''


				# Prune if able
				if (value <= alpha):
					return value

				# Update beta
				if (value < beta):
					beta = value

		return value

			
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
		#value = float(value) / (2 * m * n)
		#print "m: " + str(m)  + " n: " + str(n)
		#print "value: " + str(value)
		



		#raise NotImplementedError("Need to implement this method")

		return value
