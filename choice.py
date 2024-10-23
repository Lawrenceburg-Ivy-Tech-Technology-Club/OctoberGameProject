#from game import GameData

class Choice:
    def __init__(self, alias: str, callback: callable):
        """
        Args:
            alias (str): The text to be displayed for the choice.
            callback (callable): The function to execute when the choice is selected.
        """
        self.alias = alias
        self.callback = callback
        self.score = 0
        self.next_prompt = None

    # def __init__(self, alias: str, score: int, next_prompt: str):
    #     self.alias = alias
    #     self.callback = None
    #     self.score = score
    #     self.next_prompt = next_prompt

    def get_alias(self):
        return self.alias
    def get_callback(self):
        return self.callback

    def select(self, data):
        """Executes the choice's callback function.
        
        Args:
            data (GameData): The game's data.
        """
        data.set_message("")
        data.score += self.score

        if self.next_prompt:
            data.set_current_prompt(self.next_prompt)

        if self.callback:
            self.callback(data)