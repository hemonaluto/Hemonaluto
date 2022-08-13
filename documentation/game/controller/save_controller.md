Module game.controller.save_controller
======================================
storing and loading game save files

Classes
-------

`SaveController()`
:   Class to save and load the game state

    ### Class variables

    `ElementEncoder`
    :   json encoder for elements

    ### Methods

    `dictionary_to_elements(self, contents_dictionary_list: Dict)`
    :   Converts dictionary to elements

    `load(self, filename: str)`
    :   Loads the save file

    `save(self, all_name_locations: List[Tuple[str, game.model.location.Location]], filename)`
    :   Saves the game