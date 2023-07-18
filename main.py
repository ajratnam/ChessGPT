from ChessGPT.chess import *

driver = create_browser()
open_chess(driver)
print(get_board(driver))
