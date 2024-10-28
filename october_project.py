from game import Game
import prompt_data as pdata

def main():
    game = Game(pdata.main_menu_prompt)
    game.run()
    

if __name__ == "__main__":
    main()