from prompt import Prompt

def clear():
    """Clears console text."""
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def print_prompt(prompt: Prompt):
    """Prints a prompt to the console.
    
    Args:
        prompt (Prompt): The prompt to print.
    """
    print(f"{prompt.get_title()}\n")
    print(f"{prompt.get_content()}\n")
    i = 1
    for choice in prompt.get_choices():
        print(f"[{i}] {choice.alias}")
        i += 1
    print("")