Module game.data.texts
======================
responses to the players inputs, excluding descriptions of the in-game world

Functions
---------

    
`door_leads_to(directions)`
:   describes where a door leads to

    
`door_not_locked(door_name)`
:   Returns the message for when the player tries to unlock a    specific door that already is unlocked.

    
`door_unlocked(door_name)`
:   Returns the message for when the player unlocks a specific door.

    
`eat_food(food_name, taste)`
:   Eating food message

    
`element_in_container(things_as_string, preposition, container)`
:   Returns a description for a thing within a container

    
`element_not_found(element_name)`
:   Returns element not found message

    
`element_not_in_inventory(element_name)`
:   Returns element not in inventory message

    
`entering_thing(thing)`
:   Entering thing message

    
`hit_target(target_name)`
:   Returns hit target message

    
`noises_description(noises)`
:   Describes noises

    
`picked_up_element(element_name)`
:   Returns the information that the player picked up a specific element

    
`reveal_element(moved_item, revealed_item)`
:   Revealing element message

    
`smell_description(smells)`
:   Describes smells

    
`tie_rope_to_target(target)`
:   Tying rope to something message