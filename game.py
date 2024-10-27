from prompt import Prompt
import console

class GameData:
    def __init__(self, init_prompt: Prompt):
        self.running = True
        self.score = 0
        self.current_prompt = init_prompt
        self.message = ""
        self.counter = 0

    def is_running(self):
        return self.running
    def get_score(self):
        return self.score
    def get_current_prompt(self):
        return self.current_prompt
    def get_message(self):
        return self.message
    def get_counter(self):
        return self.counter
    
    def set_running(self, running: bool):
        self.running = running
    def set_score(self, score: int):
        self.score = score
    def set_current_prompt(self, current_prompt: Prompt):
        self.current_prompt = current_prompt
    def set_message(self, message: str):
        self.message = message
    def set_counter(self, counter):
        self.counter = counter

class Game:
    def __init__(self, init_prompt: Prompt):
        self.data = GameData(init_prompt)

    def handle_prompt(self):
        """Displays the score, current prompt, choices, and any error messages to the user, then handles the user's input."""
        console.clear() # Clear console text
        print(f"Score: {self.data.get_score()}\n") # Display score
        console.print_prompt(self.data.get_current_prompt()) # Display prompt and choices
        print(f"{self.data.get_message()}") # Display message

        try:
            selection = int(input("Selection: ")) # Get user selection
        except ValueError:
            self.data.set_message("Invalid selection.")
            return

        # Validate selection
        if selection < 1 or selection > len(self.data.get_current_prompt().get_choices()):
            self.data.set_message("Invalid selection.")
            return
        
        choice = self.data.get_current_prompt().get_choices()[selection - 1] # Get choice from selection
        choice.select(self.data) # Execute choice

    def run(self):
        """Runs the game's main loop."""
        while self.data.is_running():
            self.handle_prompt()