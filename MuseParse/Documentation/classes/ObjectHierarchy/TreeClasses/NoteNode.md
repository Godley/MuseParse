Module classes.ObjectHierarchy.TreeClasses.NoteNode
---------------------------------------------------

Classes
-------
#### NoteNode 
Node which encapsulates the Note class.

  
Optional inputs are minimal on this one as info about the note itself is stored in the Note class.

  
In order to maintain lilypond's output flow, Notes have a specific child order:  

* - left: Expression (dynamic or other expressive thing that has to be attached to a note)

* - middle: Any other notes, if this note is part of a chord

* - right: direction (anything that's not a note or expression)

##### Ancestors (in MRO)
- classes.ObjectHierarchy.TreeClasses.NoteNode.NoteNode

- MuseParse.classes.ObjectHierarchy.TreeClasses.BaseTree.Node

- builtins.object

##### Descendents
- classes.ObjectHierarchy.TreeClasses.NoteNode.Placeholder

##### Static methods
- **__init__** (self, **kwargs)

- **AddChild** (self, item, index=-1)

    adds the child to the list - index is included as an optional param but doesn't do anything because
this allows us to ducktype between this and IndexedNode

- **AddRule** (self, rule)

- **AttachDirection** (self, item)

- **AttachExpression** (self, new_node)

- **AttachNote** (self, new_note)

- **CheckForGraceNotes** (self)

- **Find** (self, node_type, item_type)

    method for finding specific types of notation from nodes.
will currently return the first one it encounters because this method's only really intended
for some types of notation for which the exact value doesn't really
matter.

    

    * :param node_type: the type of node to look under

    
* :param item_type: the type of item (notation) being searched for

    
* :return: first item_type object encountered

- **GetChild** (self, index)

- **GetChildrenIndexes** (self)

- **GetItem** (self)

- **PopAllChildren** (self)

- **PopChild** (self, key)

- **PositionChild** (self, key, node)

- **ReplaceChild** (self, key, item)

- **SetGrace** (self)

- **SetItem** (self, new_item)

- **SetLast** (self)

- **UpdateArpeggiates** (self, type='start')

    method which searches for all arpeggiates and updates the top one of each chord to be a start,
and the bottom one to be a stop ready for lilypond output
:param type:  
:return:

- **toLily** (self)

    Method which converts the object instance, its attributes and children to a string of lilypond code

    
* :return: str of lilypond code

#### Placeholder 
##### Ancestors (in MRO)
- classes.ObjectHierarchy.TreeClasses.NoteNode.Placeholder

- classes.ObjectHierarchy.TreeClasses.NoteNode.NoteNode

- MuseParse.classes.ObjectHierarchy.TreeClasses.BaseTree.Node

- builtins.object

##### Static methods
- **__init__** (self, **kwargs)

- **AddChild** (self, item, index=-1)

    adds the child to the list - index is included as an optional param but doesn't do anything because
this allows us to ducktype between this and IndexedNode

- **AddRule** (self, rule)

- **AttachDirection** (self, item)

- **AttachExpression** (self, new_node)

- **AttachNote** (self, new_note)

- **CheckForGraceNotes** (self)

- **Find** (self, node_type, item_type)

    method for finding specific types of notation from nodes.
will currently return the first one it encounters because this method's only really intended
for some types of notation for which the exact value doesn't really
matter.

    

    * :param node_type: the type of node to look under

    
* :param item_type: the type of item (notation) being searched for

    
* :return: first item_type object encountered

- **GetChild** (self, index)

- **GetChildrenIndexes** (self)

- **GetItem** (self)

- **PopAllChildren** (self)

- **PopChild** (self, key)

- **PositionChild** (self, key, node)

- **ReplaceChild** (self, key, item)

- **SetGrace** (self)

- **SetItem** (self, new_item)

- **SetLast** (self)

- **UpdateArpeggiates** (self, type='start')

    method which searches for all arpeggiates and updates the top one of each chord to be a start,
and the bottom one to be a stop ready for lilypond output
:param type:  
:return:

- **toLily** (self)

    Method which converts the object instance, its attributes and children to a string of lilypond code

    
* :return: str of lilypond code

##### Instance variables
- **item**
