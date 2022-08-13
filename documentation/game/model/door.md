Module game.model.door
======================
data structure to store information about in-game doors

Classes
-------

`Door(name, description, **kwargs)`
:   Class to initialize any kind of door, e.g. a trapdoor, with its own name and description

    ### Ancestors (in MRO)

    * game.model.element.Element

    ### Instance variables

    `connects`
    :   Values in list must be names of locations as strings

    `locked`
    :   Value must be the name of the key as a string