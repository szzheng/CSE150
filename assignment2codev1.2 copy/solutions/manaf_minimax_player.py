__author__ = 'Manaf Alajmi Steven Zheng'
__email__ = 'malajmi@ucsd.edu szzheng@ucsd.edu'

from assignment2 import Player, State, Action


class ManafMinimaxPlayer(Player):
    def __init__(self):
        self.cache ={}

    def move(self, state):
        """
        Calculates the best move from the given board using the minimax
        algorithm.
        :param state: State, the current state of the board.
        :return: Action, the next move
        """
        global currPly

        #sets who the current player is, needed for rows
        currPly = state.player
        
       

        util = self.minmax(state, True)


        return action



    #minmax method, takes the current state of the board
    #and a boolean that checks which recursive call this is
    def minmax(self, state, num):
         
        #starts off by getting all possible actions
        posActs=state.actions()
    

        global action
        
        
        if (state.is_terminal()): 
            return state.utility(currPly)
        #checks if the game reached a terminal state
        #and if it did it return the utility

        #sets the util based on current player
        if(currPly.row == state.player_row):
            util =-1;
        else:
            util =1;
            
            #if there are no possible actions available
        if not(posActs):
            nextState = State(state.board, state.opponent_row, state.player)
            util = self.minmax(nextState, False)
        
               
        while(posActs):
            currentAction =posActs.pop()
            nextState = state.result(currentAction)
 
            nextUtility = self.minmax(nextState, False)
                
            if (currPly.row == state.player_row):
                if (util <= nextUtility):
                    util = nextUtility;
                    if (num):
                        action = currentAction
            else:
                 if (util > nextUtility):
                    util = nextUtility
                    if (num):
                        action = currentAction

                
                    

        return util
