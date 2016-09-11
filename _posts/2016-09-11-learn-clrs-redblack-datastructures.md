---
layout: post
title: 算法设计-红黑树
keywords:
  - 数据结构
  - 红黑树

description: 学习红黑树算法的设计
category: 算法设计
tags:
  - CLRS
published: true
---
{% include JB/setup %}



<!--more-->
### 1.原理:
属于***平衡树*** 中的一种，一棵红黑树在任意时刻都满足以下性质:

* 每个结点要么是红色，要么是黑色
* 根结点一定是黑色的
* 每个叶子结点(NIL)是黑色的
* 如果结点是红色的，则它的子结点是黑色的
* 每个结点，从该结点到其后代叶子结点的路径上，都会包含个数相同的黑色结点

### 2.图示:
![cmd-markdown-logo]({{ IMAGE_PATH }}/20160901_RedBlackTreeDataStructures01.PNG)
![cmd-markdown-logo]({{ IMAGE_PATH }}/20160901_RedBlackTreeDataStructures02.PNG)
![cmd-markdown-logo]({{ IMAGE_PATH }}/20160901_RedBlackTreeDataStructures03.PNG)
![cmd-markdown-logo]({{ IMAGE_PATH }}/20160901_RedBlackTreeDataStructures04.PNG)
![cmd-markdown-logo]({{ IMAGE_PATH }}/20160901_RedBlackTreeDataStructures05.PNG)
![cmd-markdown-logo]({{ IMAGE_PATH }}/20160901_RedBlackTreeDataStructures06.PNG)
![cmd-markdown-logo]({{ IMAGE_PATH }}/20160901_RedBlackTreeDataStructures07.PNG)
### 3.伪代码:
```
LEFT-ROTATE(T,x)
y = x.right // set y
x.right = y.left // turn y’s left subtree into x’s right subtree
if y.left != T.nil
	y.left.p = x
y.p = x.p // link x’s parent to y
if x.p == T.nil
	T.root = y
elseif x == x.p. left
	x.p. left = y
else x.p.right = y
y.left = x // put x on y’s left
x.p = y

RB-INSERT(T,z)
y = T.nil
x = T.root
while x != T.nil
	y = x
	if z.key < x.key
		x = x.left
	else x = x.right
z.p = y
if y == T.nil
	T.root = z
elseif z.key < y.key
	y.left = z
else y.right = z
z.left = T.nil
z.right = T.nil
z.color = RED
RB-INSERT-FIXUP(T, z)

RB-INSERT-FIXUP(T, z)
while z.p.color == RED
	if z.p == z.p.p.left
		y = z.p.p.right
		if y.color == RED
			z.p.color = BLACK // case 1
			y.color = BLACK // case 1
			z.p.p.color = RED // case 1
			z = z.p.p // case 1
		else if z == z.p.right
				z = z.p // case 2
				LEFT-ROTATE.T; z/ // case 2
			z.p.color = BLACK // case 3
			z.p.p.color = RED // case 3
			RIGHT-ROTATE.T; z.p.p/ // case 3
	else (same as then clause with "right" and "left" exchanged)

T.root.color = BLACK


RB-TRANSPLANT(T, u, v)
if u.p == T.nil
	T.root = v
elseif u == u.p.left
	u.p.left = v
else u.p.right = v
v.p = u.p


RB-DELETE(T, z)
y = z
y-original-color = y.color
if z.left == T.nil
	x = z.right
	RB-TRANSPLANT(T, z, z.right)
elseif z.right == T.nil
	x = z.left
	RB-TRANSPLANT(T, z, z.left)
else y = TREE-MINIMUM(z.right)
	y-original-color = y.color
	x = y.right
	if y.p == z
		x.p = y
	else RB-TRANSPLANT(T, y, y.right)
		y.right = z.right
		y.right.p = y
	RB-TRANSPLANT.T; z; y/
	y.left = z.left
	y.left.p = y
	y.color = z.color
if y-original-color == BLACK
	RB-DELETE-FIXUP(T, x)


RB-DELETE-FIXUP(T, x)
while x != T.root and x.color == BLACK
	if x == x.p. left
		w = x.p.right
		if w.color == RED
			w.color = BLACK // case 1
			x.p.color = RED // case 1
			LEFT-ROTATE(T, x.p) // case 1
			w = x.p.right // case 1
		if w.left.color == BLACK and w.right.color == BLACK
			w.color = RED // case 2
			x = x.p // case 2
		else if w.right.color == BLACK
				w.left.color = BLACK // case 3
				w.color = RED // case 3
				RIGHT-ROTATE(T,w) // case 3
				w = x.p.right // case 3
			w.color = x.p.color // case 4
			x.p.color = BLACK // case 4
			w.right.color = BLACK // case 4
			LEFT-ROTATE(T, x.p) // case 4
			x = T.root // case 4
	else (same as then clause with “right” and “left” exchanged)
x.color = BLACK


``` 

### 4.代码片段:
```
RED = "RED"
BLACK = "BLACK"

class NilNode(object):
    def __init__(self):
        self.color = BLACK

# we define nil to be the leaf sentinel of our tree.
NIL = NilNode()

class Node(object):
    def __init__(self, key, color= RED, left = NIL, right = NIL, p = NIL):
        assert  color in (RED, BLACK)
        self.color, self.key, self.left, self.right, self.p = (color, key, left, right, p)

class Tree(object):
    def __init__(self, root=NIL):
        self.root = root

def left_rotate(T, x):
    """
    left-rotate node x on tree T.
    """
    assert (x.right != NIL)
    y = x.right
    x.right = y.left
    if y.left != NIL:
        y.left.p = x
    y.p = x.p
    if x.p == NIL:
        T.root = y
    elif x == x.p.left:
        x.p.left = y
    else:
        x.p.right = y
    y.left = x
    x.p = y

def right_rotate(T, x):
    assert(x.left != NIL)
    y = x.left
    x.left = y.right
    if y.right != NIL:
        y.right.p = x
    y.p = x.p
    if x.p == NIL:
        T.root = y
    elif x == x.p.right:
        x.p.right = y
    else:
        x.p.left = y
    y.right = x
    x.p = y

def tree_minimum(x):
     while x.left != NIL:
         x = x.left
     return x


def rb_insert(T, z):
    y = NIL
    x = T.root
    while(x != NIL):
        y = x
        if z.key < x.key:
            x = x.left
        else:
            x = x.right
    z.p = y
    if y == NIL:
        T.root = z
    elif z.key < y.key:
        y.left = z
    else:
        y.right = z
    rb_insert_fixup(T,z)

def rb_insert_fixup(T, z):
    while z.p.color == RED:
        if z.p == z.p.p.left:
            y = z.p.p.right
            if y.color == RED:
                z.p.color = BLACK
                y.color = BLACK
                z.p.p.color = RED
                z = z.p.p
            else:
                if z == z.p.right:
                    z = z.p
                left_rotate(T, z)
                z.p.color = BLACK
                z.p.p.color = RED
                right_rotate(T, z.p.p)
        else:
            y = z.p.p.left
            if y.color == RED:
                z.p.color == BLACK
                y.color = BLACK
                z.p.p.color = RED
                z = z.p.p
            else:
                if z == z.p.left:
                    z = z.p
                    right_rotate(T, z)
                z.p.color = BLACK
                z.p.p.color = RED
                left_rotate(T, z.p.p)


    T.root.color = BLACK

def rb_transplant(T, u, v):
    if u.p == NIL:
        T.root = v
    elif u == u.p.left:
        u.p.left = v
    else:
        u.p.right = v
    v.p = u.p

def rb_delete(T, z):
    y = z
    y_original_color = y.color
    if z.left == NIL:
        x = z.right
        rb_transplant(T, z, z.right)
    elif z.right == NIL:
        x = z.left
        rb_transplant(T, z, z.left)
    else:
        y = tree_minimum(z.right)
        y_original_color = y.color
        x = y.right
        if y.p == z:
            x.p = z
        else:
            rb_transplant(T, y, y.right)
            y.right = z.right
            y.right.p = y
        rb_transplant(T, z, y)
        y.left = z.left
        y.left.p = y
        y.color = z.color
    if y_original_color == BLACK:
        rb_delete_fixup(T, x)

def rb_delete_fixup(T, x):
    while x != T.root and x.color == BLACK:
        if x == x.p.left:
            w = x.p.right
            if w.color == RED:
                w.color = BLACK
                x.p.color = RED
                left_rotate(T, x.p)
                w = x.p.right
            if w.left.color == BLACK and w.right.color == BLACK:
                w.color = RED
                x = x.p
            else:
                if w.right.color == BLACK:
                    w.left.color = BLACK
                    w.color = RED
                    right_rotate(T, w)
                    w = x.p.right
                w.color = x.p.color
                x.p.color = BLACK
                w.right.color = BLACK
                left_rotate(T, x.p)
                x = T.root
        else:
            w = x.p.left
            if w.color == RED:
                w.color = BLACK
                x.p.color = RED
                left_rotate(T, x.p)
                w = x.p.left
            if w.left.color == BLACK and w.right.color == BLACK:
                w.color = RED
                x = x.p
            else:
                if w.left.color == BLACK:
                    w.right.color = BLACK
                    w.color = RED
                    right_rotate(T, w)
                    w = x.p.left
                w.color = x.p.color
                x.p.color = BLACK
                w.left.color = BLACK
                left_rotate(T, x.p)
                x = T.root
        x.color = BLACK








import  unittest
class RedBlackTest(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass

    def testTreeInsertion(self):
        """Checks that we get
             5
            / \
           3   7
          /   /
         1   6
        """


        one, three, five, six, seven = map(lambda x: Node(x), [1, 3, 5, 6, 7])
        tree = Tree()

        rb_insert(tree, five)
        rb_insert(tree, three)
        rb_insert(tree, seven)
        rb_insert(tree, one)
        rb_insert(tree, six)


        self.assertEquals(tree.root, five)
        self.assertEquals(tree.root.left, three)
        self.assertEquals(tree.root.right, seven)
        self.assertEquals(tree.root.left.left, one)
        self.assertEquals(tree.root.right.left, six)

    def testTreeInsertion(self):
        """Checks that we get
                 5                  5
                / \                / \
               3   7      ==>     3   6
              /   /              /
             1   6              1
        """

        one, three, five, six, seven = map(lambda x: Node(x), [1, 3, 5, 6, 7])
        tree = Tree()

        rb_insert(tree, five)
        rb_insert(tree, three)
        rb_insert(tree, seven)
        rb_insert(tree, one)
        rb_insert(tree, six)

        rb_delete(tree, seven)

        self.assertEquals(tree.root.right, six)




if __name__ == '__main__':
    unittest.main()

```
