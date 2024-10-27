import json


class Parser:

    def __init__(self):
        self.counter = 1

    def load_prompts(self,json_file):
        try:
            with open(json_file, 'r') as file:
                data = json.load(file)
                return data
        except:
            raise IOError("Error reading file")
        


    def load_prompt(self, id: int):
        prompt_data = self.load_prompts("prompts\prompts.json")
        return prompt_data['prompts'][str(id)]