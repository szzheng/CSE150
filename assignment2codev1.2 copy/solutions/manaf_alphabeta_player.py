# -*- coding: utf-8 -*-
__author__ = 'Manaf Alajami Steven Zheng'
__email__ = 'malajmi@ucsd.edu szzheng@ucsd'

from assignment2 import Player, State, Action

class ManafAlphaBetaPlayer(Player):


        def move(self, state):
		"""Calculates the best move from the given board using the minimax
		algorithm with a-b pruning and transposition table.
		:param state: State, the current state of the board.
		:return: Action, the next move
		"""
		
		
		table = {}

		#global variable that stores the current player
		global currPly
		currPly = state.player;

		#global variable that stores the best move
		global best

                

                        
               

                if state in table:
                    best = table[state];
                    return best[0];
                else:
                      
                    util = self.max(state, -999, 999,table)

		best = table[state.ser]
		
		return best[0]


	def min(self, state, a, b,table):

                best=None;
                util = 999;
                possActs = state.actions()

                if (state.is_terminal()): 
                   return state.utility(currPly)
                
                #if state in table:
                 #   return best;
                #else:
               
                
                

                if not(possActs):
		    nextState = State(state.board, state.opponent_row, state.player)
		    util = self.max(nextState, a, b,table)

		    if (util <= a):
			return util;

                    if (b > util):
			b = util;

		
		if best is None:

			while (possActs):
				curr = possActs.pop(0)
				nextState = state.result(curr)

				nextUtil = self.max(nextState, a, b,table)
				if (util > nextUtil):
					util = nextUtil;
					best = curr;
					table[state.ser] = (best, util)

                                
				if (util <= a):
					return util;

				if (util < b):
					b = util;

			

		return util;



	def max(self, state, a, b,table):

                util = -999;
                possActs = state.actions()
                best = None;
            
                
                     #if state in table:
                 #      return best;
                     #else:
                
                  
                #checks if the current state is terminal
    		if (state.is_terminal()):
                          
                    return state.utility(currPly)


                #if there are no possible actions with this board
                if not(possActs):
                                #set the next state to be the same board,
                                #but with the opponents row
				nextState = State(state.board, state.opponent_row, state.player)
				#and run it
				util = self.min(nextState, a, b,table)

				if (util >= b):
					return util;

				if (util > a):
					a = util;
					
                #if theres no already best set action
		if best is None:

                        #if there are possible actions
			while (possActs):
                                #get the next possible action
				curr = possActs.pop(0);

				#get the state that results from the current action
				nextState = state.result(curr)
                                #get the utility
				nextUtil = self.min(nextState, a, b,table)

				#if the utility is greater reassign the current utility
				#and add the move a the current best move into the table
				if (nextUtil > util):
					util = nextUtil;
					best = curr;
					table[state.ser] = (best, util)

                                #compare the utility with alpha and beta
				if (util >= b):
					return util;
				elif (util > a):
					a = util;

                #return the utility
		return util
		

			