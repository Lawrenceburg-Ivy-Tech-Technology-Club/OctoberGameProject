from choice import Choice

class Prompt:
    def __init__(self, title: str, content: str, choices: list[Choice]):
        """
        Args:
            title (str): The title of the prompt.
            content (str): The content of the prompt.
            choices (list[Choice]): The choices available to the player.
        """
        self.title = title
        self.content = content
        self.choices = choices

    def get_title(self):
        return self.title
    def get_content(self):
        return self.content
    def get_choices(self):
        return self.choices
    