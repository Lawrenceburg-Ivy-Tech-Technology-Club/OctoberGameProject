from game import GameData
from choice import Choice
from prompt import Prompt

# Main Menu
def play_callback(data: GameData):
    data.set_current_prompt(pentest_prompt)
play_choice = Choice("Play", play_callback)

def quit_callback(data: GameData):
    data.set_running(False)
quit_choice = Choice("Quit", quit_callback)

main_menu_prompt = Prompt("Main Menu", "", [play_choice, quit_choice])

# Prompt 1: Pentest
def nav_next_callback(data: GameData):
    data.set_current_prompt(netscan_prompt)
nav_next_choice = Choice("Next", nav_next_callback)

pentest_prompt = Prompt("Pentest", "You email back Marina, the IT Manager, that you think the top priority should be to run a penetration test. She responds back and provides you with a Virtual Machine with a simulated version of their network. Taking inspiration from your boss, you roll up your sleeves, take a sip of your coffee, and get to work.", [nav_next_choice])

# Prompt 2: Network Scan
def forward_proxy_callback(data: GameData):
    # TODO: Set score
    data.set_current_prompt(password_prompt)
forward_proxy_choice = Choice("Implement forward proxy", forward_proxy_callback)

def reverse_proxy_callback(data: GameData):
    # TODO: Set score
    data.set_current_prompt(password_prompt)
reverse_proxy_choice = Choice("Implement reverse proxy", reverse_proxy_callback)

def keep_open_callback(data: GameData):
    # TODO: Set score
    data.set_current_prompt(password_prompt)
keep_open_choice = Choice("Keep ports open", keep_open_callback)

netscan_prompt = Prompt("Network Scan", "The first step that you take is to run a network scan, searching for any open ports. The scan is complete and you find open ports. Port 80 (Http) and Port 3389 (RDP, Remote Desktop Protocol) are open. You know that Port 80 is likely open to host a web application and Port 3389 is likely open because the IT department uses RDP to manage and troubleshoot company devices.", [forward_proxy_choice, reverse_proxy_choice, keep_open_choice])

# Prompt 3: Weak Password Search
def bad_password_callback(data: GameData):
    data.score -= 1 # Incorrect answer
    data.set_current_prompt(software_prompt)
bad_password_choice = Choice("Set the password to match the username", bad_password_callback)

def update_password_policy_callback(data: GameData):
    data.score += 1 # Correct answer
    data.set_current_prompt(software_prompt)
update_password_policy_choice = Choice("Set a minimum password character limit and require special characters.", update_password_policy_callback)

password_prompt = Prompt("Weak Password Search", "The second step that you take is to search for any weak passwords. You perform a Brute Force Attack on the network to check for any weak passwords. {\\Success}. You find the password for one of the administrator accounts is qwerty123", [bad_password_choice, update_password_policy_choice])

# Prompt 4: Software Version/Vulnerability Search
def update_ms_office_callback(data: GameData):
    data.score += 1 # Correct answer
    software_prompt.choices.remove(update_ms_office_choice) # Remove choice after selection
    if len(software_prompt.choices) == 0:
        data.set_current_prompt(end_prompt) # Go to end after all choices are selected
    else:
        data.set_current_prompt(software_prompt)
update_ms_office_choice = Choice("Update to the latest version of Microsoft Office", update_ms_office_callback)

def document_solution_callback(data: GameData):
    data.score += 1 # Correct answer
    software_prompt.choices.remove(document_solution_choice) # Remove choice after selection
    if len(software_prompt.choices) == 0:
        data.set_current_prompt(end_prompt) # Go to end after all choices are selected
    else:
        data.set_current_prompt(software_prompt)
document_solution_choice = Choice("Document how you implemented the solution", document_solution_callback)

def notify_sysadmin_callback(data: GameData):
    data.score += 1 # Correct answer
    software_prompt.choices.remove(notify_sysadmin_choice) # Remove choice after selection
    if len(software_prompt.choices) == 0:
        data.set_current_prompt(end_prompt) # Go to end after all choices are selected
    else:
        data.set_current_prompt(software_prompt)
notify_sysadmin_choice = Choice("Notify system administrators", notify_sysadmin_callback)

software_prompt = Prompt("Software Version/Vulnerability Search", "The third step that you take is to search for any devices with outdated software or software vulnerabilities. During your search you find that several of the accounting computers are running an outdated version of Microsoft Office. Because the software is no longer supported, it is vulnerable to many different known exploits. To go one step further you attempt one of the exploits targeting the machines with the outdated Microsoft Office software. The exploit works and you now have root access to the machine.", [update_ms_office_choice, document_solution_choice, notify_sysadmin_choice])

# Prompt 5: End Game
def view_score_callback(data: GameData):
    data.set_message(f"Your final score is: {data.get_score()}")
view_score_choice = Choice("View Score", view_score_callback)

end_prompt = Prompt("End Game", "The final step that you take is to write a report on your findings and the potential next steps to resolve the issues. You complete documentation for the entire process to present to your manager.", [view_score_choice, quit_choice])