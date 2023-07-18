from pyperclip import copy

from ChessGPT.chess import *

driver = create_browser()
open_chess(driver)
select_opponent_and_play(driver)

while 1:
    board = get_board(driver)
    copy(generate_prompt(board))
    input(">>> ")
