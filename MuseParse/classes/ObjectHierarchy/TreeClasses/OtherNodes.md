Module classes.ObjectHierarchy.TreeClasses.OtherNodes
-----------------------------------------------------

Classes
-------
#### ClefNode 
##### Ancestors (in MRO)
- classes.ObjectHierarchy.TreeClasses.OtherNodes.ClefNode

- classes.ObjectHierarchy.TreeClasses.OtherNodes.KeyNode

- MuseParse.classes.ObjectHierarchy.TreeClasses.BaseTree.Node

- builtins.object

##### Static methods
- **__init__** (self)

- **AddChild** (self, item, index=-1)

    adds the child to the list - index is included as an optional param but doesn't do anything because
this allows us to ducktype between this and IndexedNode

- **AddRule** (self, rule)

- **GetChild** (self, index)

- **GetChildrenIndexes** (self)

- **GetItem** (self)

- **PopAllChildren** (self)

- **PopChild** (self, key)

- **ReplaceChild** (self, key, item)

- **SetItem** (self, new_item)

- **toLily** (self)

#### DirectionNode 
##### Ancestors (in MRO)
- classes.ObjectHierarchy.TreeClasses.OtherNodes.DirectionNode

- classes.ObjectHierarchy.TreeClasses.OtherNodes.SelfNode

- MuseParse.classes.ObjectHierarchy.TreeClasses.BaseTree.Node

- builtins.object

##### Static methods
- **__init__** (self)

- **AddChild** (self, item, index=-1)

    adds the child to the list - index is included as an optional param but doesn't do anything because
this allows us to ducktype between this and IndexedNode

- **AddRule** (self, rule)

- **GetChild** (self, index)

- **GetChildrenIndexes** (self)

- **GetItem** (self)

- **PopAllChildren** (self)

- **PopChild** (self, key)

- **ReplaceChild** (self, key, item)

- **SetItem** (self, new_item)

- **toLily** (self)

    Method which converts the object instance and its attributes to a string of lilypond code

    
* :return: str of lilypond code

#### ExpressionNode 
##### Ancestors (in MRO)
- classes.ObjectHierarchy.TreeClasses.OtherNodes.ExpressionNode

- classes.ObjectHierarchy.TreeClasses.OtherNodes.SelfNode

- MuseParse.classes.ObjectHierarchy.TreeClasses.BaseTree.Node

- builtins.object

##### Static methods
- **__init__** (self)

- **AddChild** (self, item, index=-1)

    adds the child to the list - index is included as an optional param but doesn't do anything because
this allows us to ducktype between this and IndexedNode

- **AddRule** (self, rule)

- **GetChild** (self, index)

- **GetChildrenIndexes** (self)

- **GetItem** (self)

- **PopAllChildren** (self)

- **PopChild** (self, key)

- **ReplaceChild** (self, key, item)

- **SetItem** (self, new_item)

- **toLily** (self)

    Method which converts the object instance and its attributes to a string of lilypond code

    
* :return: str of lilypond code

#### KeyNode 
##### Ancestors (in MRO)
- classes.ObjectHierarchy.TreeClasses.OtherNodes.KeyNode

- MuseParse.classes.ObjectHierarchy.TreeClasses.BaseTree.Node

- builtins.object

##### Descendents
- classes.ObjectHierarchy.TreeClasses.OtherNodes.ClefNode

##### Static methods
- **__init__** (self)

- **AddChild** (self, item, index=-1)

    adds the child to the list - index is included as an optional param but doesn't do anything because
this allows us to ducktype between this and IndexedNode

- **AddRule** (self, rule)

- **GetChild** (self, index)

- **GetChildrenIndexes** (self)

- **GetItem** (self)

- **PopAllChildren** (self)

- **PopChild** (self, key)

- **ReplaceChild** (self, key, item)

- **SetItem** (self, new_item)

- **toLily** (self)

#### SelfNode 
##### Ancestors (in MRO)
- classes.ObjectHierarchy.TreeClasses.OtherNodes.SelfNode

- MuseParse.classes.ObjectHierarchy.TreeClasses.BaseTree.Node

- builtins.object

##### Descendents
- classes.ObjectHierarchy.TreeClasses.OtherNodes.DirectionNode

- classes.ObjectHierarchy.TreeClasses.OtherNodes.ExpressionNode

##### Static methods
- **__init__** (self)

- **AddChild** (self, item, index=-1)

    adds the child to the list - index is included as an optional param but doesn't do anything because
this allows us to ducktype between this and IndexedNode

- **AddRule** (self, rule)

- **GetChild** (self, index)

- **GetChildrenIndexes** (self)

- **GetItem** (self)

- **PopAllChildren** (self)

- **PopChild** (self, key)

- **ReplaceChild** (self, key, item)

- **SetItem** (self, new_item)

- **toLily** (self)

    Method which converts the object instance and its attributes to a string of lilypond code

    
* :return: str of lilypond code
