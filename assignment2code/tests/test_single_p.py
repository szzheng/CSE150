# -*- coding: utf-8 -*-

__author__ = 'Dan'
__email__ = 'daz040@eng.ucsd.edu'

import os
import sys
import inspect

from assignment2 import Player, State, Action


def run_code_from(python_file, input_text):
    # Load the player class from the specified .py file
    sys.path.append(os.path.abspath(os.path.dirname(python_file)))
    module = __import__(os.path.splitext(os.path.basename(python_file))[0])
    player_class = next(getattr(module, name) for name in dir(module) if
                        inspect.isclass(getattr(module, name)) and issubclass(getattr(module, name), Player) and \
                        getattr(module, name) != Player)
    players = Player.create_players([player_class, Player])  # Second player is a dummy
    init_txt, state_txt = input_text.strip().split("\n")
    eval(init_txt)
    state = eval(state_txt)
    state.player = players[0]
    return repr(players[0].move(state))


if __name__ == '__main__':
    print run_code_from(sys.argv[1], sys.stdin.read().strip())