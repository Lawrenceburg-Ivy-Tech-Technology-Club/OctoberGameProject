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
        return self.callback(data)