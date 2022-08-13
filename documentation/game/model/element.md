Module game.model.element
=========================
data structure to store information about in-game elements

Classes
-------

`Element(name, description, **kwargs)`
:   Class to initialize any element with its own name and description

    ### Descendants

    * game.model.activator.Activator
    * game.model.animate.Animate
    * game.model.chest.Chest
    * game.model.door.Door
    * game.model.food.Food
    * game.model.location.Location
    * game.model.player.Player
    * game.model.rope.Rope
    * game.model.thing.Thing
    * game.model.tool.Tool

    ### Instance variables

    `contents`
    :   Values in list must be Element objects