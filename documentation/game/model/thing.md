Module game.model.thing
=======================
data structure to store information about in-game things

Classes
-------

`Thing(name, description, **kwargs)`
:   Class to initialize any kind of object, e.g. a bottle, with its own name and description

    ### Ancestors (in MRO)

    * game.model.element.Element

    ### Descendants

    * game.model.chest.Chest
    * game.model.food.Food
    * game.model.rope.Rope
    * game.model.tool.Tool

    ### Instance variables

    `when_broken_do`
    :   Value must be a method name existing in activator_handler