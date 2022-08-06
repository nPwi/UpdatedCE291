from game import Game
gameframe = Game()

while gameframe.running:
    gameframe.curr_menu.display_menu()
    gameframe.game_loop()