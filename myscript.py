from rocket_board import RocketBoard


board = RocketBoard()
board.add_many_rockets(5)
board.add_rocket(RocketBoard.TURBO_TYPE, 2)

board.start_race()
board.print_rockets_status()
board.print_best_rockets()
