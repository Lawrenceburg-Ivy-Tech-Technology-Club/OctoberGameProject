from game import GameData, Game
from choice import Choice
from prompt import Prompt
import parser

try:
  prompt_data = parser.load_prompt('1')
except FileNotFoundError:
  raise FileNotFoundError("Prompt file not found.")
except Exception as e:
  raise Exception(f"An error occured while loading the prompt: {e}")



def nav_score_editor_callback(data: GameData):
    data.set_current_prompt(score_editor_prompt)

for c in range(len(prompt_data["choices"])):
    nav_score_editor_choice = Choice(prompt_data["choices"][c]["alias"], nav_score_editor_callback)

def quit_callback(data: GameData):
    data.set_running(False)

quit_choice = Choice("Quit", quit_callback)

main_menu_prompt = Prompt("Main Menu", "", [nav_score_editor_choice, quit_choice])

def increment_score_callback(data: GameData):
    data.score += 1


#increment_score_choice = Choice(questions["questions"][counter]["q"][0], increment_score_callback())
increment_score_choice = Choice("Yes", increment_score_callback)

def decrement_score_callback(data: GameData):
    data.score -= 1


#decrement_score_choice = Choice(questions["questions"][counter]["q"][1], decrement_score_callback())
decrement_score_choice = Choice("No", decrement_score_callback)

def nav_main_menu_callback(data: GameData):
    data.set_current_prompt(main_menu_prompt)

nav_main_menu_choice = Choice("Main Menu", nav_main_menu_callback)

score_editor_prompt = Prompt("Score Editor", "is this a phishing email?", [increment_score_choice, decrement_score_choice, nav_main_menu_choice])

def main():
    global ngame
    ngame = Game(main_menu_prompt)
    ngame.run()


if __name__ == "__main__":
    main()