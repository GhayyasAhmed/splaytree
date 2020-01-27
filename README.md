# Splay Tree

# Introduction:

The splay tree is a type of binary search tree. Unlike other variants like the AVL tree, the red-black tree, or the scapegoat tree, the splay tree is not always balanced Instead, it is optimized so that elements that have been recently accessed are quick to access again. The main difference, though, is that the root node is always the last element that was accessed.

# Basic Operations:

# Splaying:
 
Splaying is what keeps the splay tree roughly balanced. To splay a node, splaying steps are repeatedly performed on it until it becomes the root while maintaining the in-order relationships of the nodes in the tree. To decide what kind of splaying step to perform, the tree looks at three possibilities:

# Zig-Zig:

The x(node) to be splay and y(its parent) are both left children or both right children. We promote x, making y a child of x and z(grandparent) a child of y.

# Zig-Zag:

One of x(node) and y(its parent) is a left child and the other is a right child. In this case, we promote x by making x have y and z(grandparent) as its children.
# Zig:

When x(node) does not have a grandparent. In this case, we perform a single rotation to promote x over y(its parent), making y a child of x.

# Insert:

Insert a node as like in BinarySearchTree and preform splay operation on that node to make it the root of the tree.

# Search:

Search for a node, if found then perform the splay operation on that node. Otherwise, splay the leaf position at which the search terminates unsuccessfully.

# Delete:

The node to be deleted is first splayed, i.e. brought to the root of the tree and then deleted. Leaves the tree with two sub trees. The two sub-trees are then joined by splaying the node with maximum value in left sub tree the node of that tree and then joins the right sub tree on the right of left sub tree.


All the other functions in the code are just to check the above mentioned operations.
