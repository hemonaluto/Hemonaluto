Module game.view.console_view
=============================
console view that prints out what the player sees

Classes
-------

`ConsoleView(dungeon_master)`
:   Class to initialize a view for the console

    ### Methods

    `parse(self, user_input: str)`
    :   Runtime polymorphic method to map the possible user input to a corresponding method

    `start_view(self)`
    :   Start the process of displaying messages to the cosole

    `toggle_quit(self)`
    :   Quits the game