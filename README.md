# Hemonaluto
**A text-based adventure game**

Hemonaluto is a text based adventure game where you wake up in a curious magical world with a dark and powerful secret.

The story isn't developed yet, so far there are only three rooms to discover.

## How it works

### Players

1. [Install Python](https://www.python.org/downloads/) and [install pip](https://monovm.com/blog/how-to-install-pip-on-windows-linux/)
2. Open terminal as administrator.
3. Run ```pip install hemonaluto```
4. Run ```hemonaluto```

You are welcomed and prompted to type in a command. This command should be written from the perspective of the player, similar to how you would play in the game Zork. Useful player commands are listed further down on this page.

### Developers

#### Set up
1. [Install Python](https://www.python.org/downloads/) and [install pip](https://monovm.com/blog/how-to-install-pip-on-windows-linux/)
2. Open terminal as administrator.
3. Navigate to the folder you want to clone the project to.
4. Run ```git clone https://github.com/hemonaluto/Hemonaluto.git```
5. Install the required dependencies:
   - Linux: run ```make setup``` to easily install them OR
   - Any OS: run ```pip install -r requirements.txt``` OR
   - use pipenv or anaconda

#### How you can help
If you want to improve this game, fix bugs, write tests or add documentation, please feel free to do so, any kind of contribution is welcome. Simply open an issue and submit a pull request so we can discuss and close it.

#### Makefile
- ```make generate_world```:
Generate the world json used in the game. To create your custom world or change the existing one you can edit ```scripts/world_generation.py``` before running ```make generate_world```.
- ```make generate_test_world```:
Generate the test world json, which some of the unit tests require.
- ```make run_tests```:
Run all the unit tests.
- ```make setup```:
Installs the required libraries for the project.
- ```make run```:
Run the game.
- ```make documentation```:
Generates the project code documentation.

## Player Commands
### quit/q/exit
This command quits the game entirely.
### examine/look/l
Examine any kind of in-game element. Type the thing you want to examine after the command, e.g. examine door, or don't and get a general description of your environment.
### north/northeast/n/up/u/...
Move in desired direction.
### open/unlock
Unlock a door or chest.
### get/take/pick
Take an item.
### inventory/i
List all the items in your inventory.
### save/load
Save or load your game state.
### restart
Restart the game.
### score
View your score.
### diagnostic/health
View your current health.
### throw at
Throw any item at whatever target you choose.
### close
Close a door or chest.
### read
Read an items engraved or written on text.
### drop
Drop an item.
### put
Put an item in or on another item.
### press/turn
Use a button or valve.
### move/push/pull
Move an object to reveal what is underneath it.
### attack with/kill with
Attack an entity with your specified weapon.
### eat/drink
Eat or drink something to replenish health.
### tie/attach
Tie or attach a rope to something.
### destroy/break
Break a breakable item.
### listen
Listen to your surroundings.
### smell
Smell your environment.
### hide in/under
Hide in or under something
### leave/appear
Leave your hiding spot.
