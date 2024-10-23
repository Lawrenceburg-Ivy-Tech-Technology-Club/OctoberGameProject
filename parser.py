import json
from choice import Choice
from prompt import Prompt

def load_prompts(json_file):
    try:
        with open(json_file, 'r') as file:
            data = json.load(file)
            return data
    except:
        raise IOError("Error reading file")
    
def parse_prompts(json_data):
    prompts = []
    for prompt in json_data["prompts"]:
        choices = []
        for choice in prompt["choices"]:
            choices.append(Choice(choice["alias"], choice["score"], choice["next"]))
        prompts.append(Prompt(prompt["alias"], prompt["message"], choices))

def load_prompt(id: str):
    prompt_data = load_prompts("prompts\prompts.json")
    return prompt_data['prompts'][id]