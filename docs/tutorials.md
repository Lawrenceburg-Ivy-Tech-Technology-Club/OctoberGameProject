# Tutorials
## Basic program
To create a bare bones program, we need, at minimum, the following:
- 1 choice
- 1 prompt
- An instance of `Game`
- A main function that creates the `Game` instance and runs the game

In this example, we will create a simple program that has a "Hello World" prompt with a single choice that terminates the program.

The following steps need to be taken:
- Create the "Exit" choice.
- Create the "Hello World" prompt that uses the "Exit" choice.
- Set the initial prompt to the "Hello World" prompt
- Run the game.

### Creating the "Exit" choice
Every choice must contain a reference to a callback function. The callback function is called when the choice is selected by the player.

The callback function is where the game logic is implemented. In order for the game logic to be implemented, we must be able to modify the game's runtime data from the callback function. This is accomplished by taking a `GameData` argument that we can access the game's runtime data using.

First, we need to import the `GameData` class from the `game` module.
```python
from game import GameData
```
Next, we need to define our callback function.
```python
def exit_callback(data: GameData):
    data.set_running(False) # Set running state to False
```
In the above code, the game is terminated by setting the running state to `False`. The running state is tracked in the `data: GameData` argument passed to our callback function `exit_callback`.

Next, we need to create the actual choice object by creating an instance of `Choice` with an alias "Exit" that uses our callback function `exit_callback`.

We need to import the `Choice` class from the `choice` module.
```python
from choice import Choice
```

Then, we need to create our `Choice` object and store it in a variable named `exit_choice`.
```python
exit_choice = Choice("Exit", exit_callback)
```
The above choice will be displayed as "Exit". When it is selected by the player, `exit_callback` will be called.

The resulting code should look something like this:
```python
from game import GameData
from choice import Choice

def exit_callback(data: GameData):
    data.set_running(False) # Set running state to False

exit_choice = Choice("Exit", exit_callback) # Create the choice object
```

### Creating the "Hello World" prompt
Now that we have created our "Exit" choice, we must create a prompt containing our "Exit" choice. To keep things simple, this prompt will simply have a "Hello World" title with "Hello, world!" as its content.

First, we need to import the `Prompt` class from the `prompt` module.
```python
from prompt import Prompt
```
Then, we need to create a `Prompt` object with the title "Hello World", the content "Hello, world!", and our choice `exit_choice`.
```python
hello_world_prompt = Prompt("Hello World", "Hello, world!", [exit_choice])
```
The first argument in `Prompt`'s constructor is the prompt's title, which we set to "Hello World". This is displayed above the prompt's content.

The second argument is the prompt's content, which we set to "Hello, world!". This is displayed below the title and above the list of choices.

The third argument is a list of choices for our prompt. The list contains all choices the player can select from for the prompt and is displayed below the content. In this case, we only have our "Exit" choice.

The resulting code should be:
```python
from choice import Choice
from prompt import Prompt

def exit_callback(data: GameData):
    data.set_running(False) # Set running state to False

exit_choice = Choice("Exit", exit_callback) # Create the choice object

hello_world_prompt = Prompt("Hello World", "Hello, world!", [exit_choice])
```

### Running the game
Now that we have a "Hello World" prompt that contains our "Exit" choice, we can run the game using our prompt.

First, we must create our `main` function that is called when the game is executed.
```python
def main():
    # Game code here

if __name__ == "__main__":
    main()
```
Inside `main`, we need to create an instance of `Game` with the initial prompt set to our "Hello World" prompt `hello_world_prompt`.

First, we need to import the `Game` class from the `game` module.
```python
from game import Game
```
Since we already imported `GameData` from the same module, we can shorten this import.
```python
from game import GameData, Game
```
Next, we need to create our `Game` object and set the initial prompt to `hello_world_prompt`.
```python
game = Game(hello_world_prompt)
```
Finally, we can run the game by calling `Game`'s `run` member method.
```python
game.run()
```
This will display our "Hello World" prompt along with our "Exit" choice and handle user input.

The final program should look like:
```python
from choice import Choice
from prompt import Prompt
from game import GameData, Game

def exit_callback(data: GameData):
    data.set_running(False) # Set running state to False

exit_choice = Choice("Exit", exit_callback) # Create the choice object

hello_world_prompt = Prompt("Hello World", "Hello, world!", [exit_choice])

def main():
    game = Game(hello_world_prompt)
    game.run()

if __name__ == "__main__":
    main()
```

When the game is executed from the command line, the output should look like this:
```
Score: 0

Hello World

Hello, world!

[1] Exit


Selection: 
```

## Navigating prompts
Prompts can be navigated by setting the game's current prompt to the prompt that is to be displayed. This is accomplished by passing the prompt to be displayed to `GameData`'s `set_current_prompt` method.

In this example, we will create a game that has three pages of text that the player can navigate between. Each page is implemented as a prompt with navigation options implemented as choices. The player can also exit the game from any of the pages.

The first prompt will contain a choice to navigate to the second prompt and a choice to exit the game.

The second prompt will contain choices for navigating to the third prompt, navigating to the first prompt, and exiting the game.

The third prompt will contain choices for navigating to the second prompt and exiting the game.

### Creating the first page
The first page is the page that is displayed first when the game is executed. This page is titled "[1/3]" and has the content "This is page 1." From this page, we can navigate to the second page or exit the game.

First, we must create the choice for exiting the game. This choice can be re-used in multiple prompts.
```python
def exit_callback(data: GameData):
    data.set_running(False)

exit_choice = Choice("Exit", exit_callback)
```

Next, we need to create the choice for navigating to the second page.
```python
def page1_next_callback(data: GameData):
    data.set_current_prompt(page2_prompt)

page1_next_choice = Choice("Next", page1_next_callback)
```
Notice how `page1_next_callback` sets the current prompt to `page2_prompt` (defined later). This is how we are able to navigate between prompts.

Finally, we can create the prompt for our first page.
```python
page1_prompt = Prompt("[1/3]", "This is page 1.", [page1_next_choice, exit_choice])
```

### Creating the second page
Creating the second page is very similar to how we created the first page except the second page needs options for navigating to the first and third pages.

First, we need to create the choice for navigating to the third (next) page.
```python
def page2_next_callback(data: GameData):
    data.set_current_prompt(page3_prompt)

page2_next_choice = Choice("Next", page2_next_callback)
```

Next, we need to create the choice for navigating to the first (previous) page.
```python
def page2_previous_callback(data: GameData):
    data.set_current_prompt(page1_prompt)

page2_previous_choice = Choice("Previous", page2_previous_callback)
```

Finally, we need to create the prompt for the second page.
```python
page2_prompt = Prompt("[2/3]", "This is page 2.", [page2_next_choice, page2_previous_choice, exit_choice])
```
Notice how we re-used `exit_choice`. A single choice can be used by multiple prompts.

### Creating the third page
The third page needs a choice to navigate to the second (previous) page.

First, we need to create the choice for navigating to the second (previous) page.
```python
def page3_previous_callback(data: GameData):
    data.set_current_prompt(page2_prompt)

page3_previous_choice = Choice("Previous", page3_previous_callback)
```

Then, we need to create the prompt for the third page.
```python
page3_prompt = Prompt("[3/3]", "This is page 3.", [page3_previous_choice, exit_choice])
```

### Running the game
Now that we have all of our prompts and choices set, we can set the initial prompt to our first page and then run the game.
```python
def main():
    game = Game(page1_prompt) # Create a Game object and set the initial prompt
    game.run() # Run the game

if __name__ == "__main__":
    main()
```

The final program should look like:
```python
from game import GameData, Game
from choice import Choice
from prompt import Prompt

def exit_callback(data: GameData):
    data.set_running(False)

exit_choice = Choice("Exit", exit_callback)

def page1_next_callback(data: GameData):
    data.set_current_prompt(page2_prompt)

page1_next_choice = Choice("Next", page1_next_callback)
page1_prompt = Prompt("[1/3]", "This is page 1.", [page1_next_choice, exit_choice])

def page2_next_callback(data: GameData):
    data.set_current_prompt(page3_prompt)

page2_next_choice = Choice("Next", page2_next_callback)

def page2_previous_callback(data: GameData):
    data.set_current_prompt(page1_prompt)

page2_previous_choice = Choice("Previous", page2_previous_callback)

page2_prompt = Prompt("[2/3]", "This is page 2.", [page2_next_choice, page2_previous_choice, exit_choice])

def page3_previous_callback(data: GameData):
    data.set_current_prompt(page2_prompt)

page3_previous_choice = Choice("Previous", page3_previous_callback)

page3_prompt = Prompt("[3/3]", "This is page 3.", [page3_previous_choice, exit_choice])

def main():
    game = Game(page1_prompt)
    game.run()

if __name__ == "__main__":
    main()
```