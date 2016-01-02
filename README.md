# game-engine

The main module cycles between scenes, each of which are populated by some amount of objects thats are able to be interacted with. 

When drawing strings to a box using the typing(string, box) method, the function recognizes the word 'rtrn' in the string as the call for a newline for the function.

Every object created needs to    import base, main, Draw     and inherit from one of the classes in base(NPC, Item, Transition, Object).

Every scene needs to     import scene, Objects      and should inherit the Scene class from scene.py.
