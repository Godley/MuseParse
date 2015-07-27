Module classes.ObjectHierarchy.TreeClasses.BaseTree
---------------------------------------------------

Functions
---------
- **BackwardSearch** (cls_type, node, index, depth=0, start_index=0)

    Helper method which backwards-recursively searches for objects

    * :param cls_type: class type of the object we are in search of

    * :param node: object instance to start at

    * :param index: number of the object to look for e.g <cls_type> num 1

    * :param depth: current depth in the tree

    * :param start_index: index to start with in children

    * :return: object <index> of <cls_type>

- **FindByIndex** (node, index)

    Method which finds child according to index. Applies only to nodes whose children are sorted into a dict,
so if the current node's children are in a list it will recursively search - similarly if the index is not found
in the current node's dictionary indexes.

    * :param node: current node to search for

    * :param index: index of child.
:return:

- **FindPosition** (node, addition, index=0)

    Method to search for children according to their position in list. Similar functionality to above method,
except this is for adding items to the tree according to the nodes limits on children or types of children they can have

    * :param node: current node being searched

    * :param addition: the thing being added

    * :param index: index to search
:return:

- **Search** (cls_type, node, index, depth=0, start_index=0)

    recursive method that goes through finding the "index"th object of cls_type. outside of piecetree
so that it can be used by any node

    * :param cls_type: class type of the object we are in search of

    * :param node: object instance to start at

    * :param index: number of the object to look for e.g <cls_type> num 1

    * :param depth: current depth in the tree

    * :param start_index: index to start with in children

    * :return: object <index> of <cls_type>

Classes
-------
#### CannotAddToTreeException 
error in tree addition!

##### Ancestors (in MRO)
- classes.ObjectHierarchy.TreeClasses.BaseTree.CannotAddToTreeException

- builtins.BaseException

- builtins.object

##### Class variables
- **args**

#### CannotFindInTreeException 
error! can't find element

##### Ancestors (in MRO)
- classes.ObjectHierarchy.TreeClasses.BaseTree.CannotFindInTreeException

- builtins.BaseException

- builtins.object

##### Class variables
- **args**

#### EmptyNode 
This is a class used to represent gaps in note representation - i.e where we want to jump forward in the measure and then come back
and fill the gap in later on. Used mostly in voices where we maybe want to fill in an extra voice at a specific moment

##### Ancestors (in MRO)
- classes.ObjectHierarchy.TreeClasses.BaseTree.EmptyNode

- classes.ObjectHierarchy.TreeClasses.BaseTree.Node

- builtins.object

##### Static methods
- **__init__** (self, duration, **kwargs)

- **AddChild** (self, item, index=-1)

    adds the child to the list - index is included as an optional param but doesn't do anything because
this allows us to ducktype between this and IndexedNode

- **AddRule** (self, rule)

- **GetChild** (self, index)

- **GetChildrenIndexes** (self)

    Method to get a list of indexes at which children reside at

    
* :return: list of indexes

- **GetItem** (self)

- **PopAllChildren** (self)

    Method to remove and return all children of current node

    
* :return: list of children

- **PopChild** (self, key)

- **ReplaceChild** (self, key, item)

    Method to remove child at <key> and replace it with <item>, then put the child back onto the end of the list

    
* :param key: index to position <item>

    
* :param item: child object to add

    :return:

- **SetItem** (self, new_item)

##### Instance variables
- **duration**

#### IndexedNode 
same as node, except the children section have their own indexes. to be used in nodes like Piece and Part, as both have
children which have indexes applied to them in xml

##### Ancestors (in MRO)
- classes.ObjectHierarchy.TreeClasses.BaseTree.IndexedNode

- classes.ObjectHierarchy.TreeClasses.BaseTree.Node

- builtins.object

##### Static methods
- **__init__** (self, **kwargs)

- **AddChild** (self, item, index=-1)

- **AddRule** (self, rule)

- **GetChild** (self, index)

- **GetChildrenIndexes** (self)

- **GetItem** (self)

- **PopAllChildren** (self)

    Method to remove and return all children of current node

    
* :return: list of children

- **PopChild** (self, key)

- **ReplaceChild** (self, key, item)

    Method to remove child at <key> and replace it with <item>, then put the child back onto the end of the list

    
* :param key: index to position <item>

    
* :param item: child object to add

    :return:

- **SetItem** (self, new_item)

##### Instance variables
- **children**

    dictionary of children attached to this node

#### Node 
This class is very generic, and has 3 attributes:  

* - children: as with any tree it needs to have children

* - limit: the maximum amount of children before castcading to the next level

* - rules: the class instances allowed to be children of this object

  
Optional inputs:  

* limit: the maximum num of children the node can have. 0 for no limit.

* rules: list of class types this node can have as child objects.

##### Ancestors (in MRO)
- classes.ObjectHierarchy.TreeClasses.BaseTree.Node

- builtins.object

##### Descendents
- classes.ObjectHierarchy.TreeClasses.BaseTree.EmptyNode

- classes.ObjectHierarchy.TreeClasses.BaseTree.IndexedNode

##### Static methods
- **__init__** (self, **kwargs)

- **AddChild** (self, item, index=-1)

    adds the child to the list - index is included as an optional param but doesn't do anything because
this allows us to ducktype between this and IndexedNode

- **AddRule** (self, rule)

- **GetChild** (self, index)

- **GetChildrenIndexes** (self)

    Method to get a list of indexes at which children reside at

    
* :return: list of indexes

- **GetItem** (self)

- **PopAllChildren** (self)

    Method to remove and return all children of current node

    
* :return: list of children

- **PopChild** (self, key)

- **ReplaceChild** (self, key, item)

    Method to remove child at <key> and replace it with <item>, then put the child back onto the end of the list

    
* :param key: index to position <item>

    
* :param item: child object to add

    :return:

- **SetItem** (self, new_item)

##### Instance variables
- **children**

    list of child nodes belonging to this node

- **item**

#### Tree 
Your basic generic tree structure, but with a few improvements to handle automatic ruling.

##### Ancestors (in MRO)
- classes.ObjectHierarchy.TreeClasses.BaseTree.Tree

- builtins.object

##### Static methods
- **__init__** (self)

- **AddNode** (self, node, index=-1)

- **FindNode** (self, cls_type, index, id=None)

- **FindNodeByIndex** (self, index)

##### Instance variables
- **root**

    The root node of the tree
