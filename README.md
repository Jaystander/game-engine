# game-engine

The main module cycles between scenes, each of which are populated by some amount of objects thats are able to be interacted with. 

When drawing strings to a box using the typing(string, box) method, the function recognizes the word 'rtrn' in the string as the call for a newline for the function.

Every object created needs to    import base, main, Draw     and inherit from one of the classes in base(NPC, Item, Transition, Object). The inheritance is not strictly necessary but helps with organization and cuts down on typing out unnecessary information.

Every scene needs to     import scene, Objects      and should inherit the Scene class from scene.py. There may be more specific base scene types added. Use the inheritance unless you want to type out all of the necessary functions for handling objects in every scene.
All Scenes need a reference name that is used to check and see what the current scene is when an object is accessed that is referenced by
```
 Scene.reference
 ```
Stats and flags should be handled in the scenes and objects in which they are relevant. The Player is an object.


To receive a description or some dialogue call Draw.file.DefString(txtfile, keyword) to search for the keyword and append lines until it reads Finished, it will return a string.
i.e.
```
npc_talk = Draw.file.DefString(filed, 'Robot Leader Not Met Office')
response = Draw.file.DefString(filed, 'Robot Leader Not Met Office Response')
```

Format for response text:
```
Name of response text block #Could use more than one block for conditional responses
'reff' 'One word reference to call response' Response display text 'rtrn'
'reff' 'One word reference to call response' Response display text 'rtrn'
Finished
```
TODO

Gotta change the responses to be passed one at a time. Gotta create a system for the response to a dialogue option in the object.
Gotta make the cleanup dialogue function clear the boxes and set it up for a new set of dialogue choices. Have to eventually learn how to do a scroll box. Might just replace some code with other code for that one.
