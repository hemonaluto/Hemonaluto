Module game.model.location
==========================
data structure to store information about in-game locations

Classes
-------

`Location(name, description, **kwargs)`
:   Class to initialize any kind of place, e.g. a room, with its own name and description

    ### Ancestors (in MRO)

    * game.model.element.Element

    ### Instance variables

    `exits`
    :   Keys must be directions e.g. west, values must be names of locations e.g. cellar