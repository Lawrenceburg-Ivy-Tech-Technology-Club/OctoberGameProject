# choice
## Classes
### Choice
The `Choice` class represents a single choice that can be added to one or many prompts. Each choice is selectable by the player and contains a callback function that implements game logic that is executed when the choice is selected.
#### Methods
`select(data)` is called when the choice is selected by the player. This method contains a `data` parameter which takes an instance of `GameData` which is then passed to the callback function. This allows for the callback function to edit the game's runtime data to implement behavior such as changing the prompt or editing the score.

**NOTE:** Due to a circular import issue with the `game` module, `data`'s type is not set in the method's signature nor is it enforced in the method's body. **Attempting to pass any type other than `GameData` will crash the game!**
#### Variables
`alias: str` is the text that is displayed for the choice.

`callback: callable` is a reference to the callback function that is called when the choice is selected.

# console
The `console` module contains functions related to command-line input/output.
## Functions
### clear()
Clears all text from the console.
### print_prompt(prompt: Prompt)
Prints a `Prompt` object to the console.
#### Params
`prompt: Prompt` The prompt to print.

# game
The `game` module contains runtime classes for the game.
## Classes
### GameData
The `GameData` class stores the game's runtime data including the running state, score, current prompt, and any error messages to be displayed to the player.
#### Methods
`__init__(init_prompt: Prompt)` is the constructor. `init_prompt` is the initial prompt to be displayed when the game is executed.
#### Variables
`running: bool` is the running state of the game. This acts as the sentinel value for the game's main loop. When `running` is set to false, the game will terminate.

`score: int` tracks the player's score.

`current_prompt: Prompt` tracks the prompt that is displayed on each iteration of the main loop. Changes made to this variable will be reflected on the next iteration.

`message: str` stores any error messages from the previous iteration of the main loop that are to be displayed to the player, such as "Invalid input".
### Game
The `Game` class handles running the game. It is responsible for displaying prompts, handling input, and stores a `GameData` instance.
#### Methods
`__init__(init_prompt: Prompt)` is the class's constructor. `init_prompt` is the initial prompt that is to be displayed when the game is executed.

`handle_prompt()` is called on each iteration of the main loop. This method displays the score, the prompt, the prompt's choices, and handles user input.

`run()` is called when the game is to be run. This method contain's the game's main loop and returns when the game is no longer in a running state.
#### Variables
`data: GameData` The game's runtime data.

# prompt
## Classes
### Prompt
The `Prompt` class stores data for a prompt including the title, content, and choices.
#### Variables
`title: str` is the title of the prompt that is displayed at the top of the screen. This is essentially a brief description of what the prompt is.

`content: str` is the prompt's scenario that the player must respond to.

`choices: list[Choice]` is a list of all possible choices that the player can select from for a given prompt.