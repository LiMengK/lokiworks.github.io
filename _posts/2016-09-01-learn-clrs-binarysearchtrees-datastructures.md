---
layout: post
title: 算法设计-二叉搜索树
keywords:
  - 数据结构
  - 二叉搜索树

description: 学习数据结构二叉搜索树算法的设计
category: 算法设计
tags:
  - CLRS
published: true
---
{% include JB/setup %}



<!--more-->
### 1.原理:
二叉树某一结点中的元素总是大于等于其左子树中任一结点中的元素，总是小于等于其右子树中任一结点中的元素。

### 2.图示:
![cmd-markdown-logo]({{ IMAGE_PATH }}/20160901_BinarySearchTreeDataStructures.PNG)
### 3.伪代码:
```
INORDER-TREE-WALK(x)
if x != NIL
	INORDER-TREE-WALK(x.left)
	print x.key
	INORDER-TREE-WALK(x.right)

ITERATIVE-TREE-SEARCH(x,k)
while x != NIL and k != x.key
	if k < x.key
		x = x.left
	else
		x = x.right
return x

TREE-MINIMUM(x)
while x.left != NIL
	x = x.left
return x

TREE-MAXIMUM(x)
while x.right != NIL
	x = x.right
return x

TREE-SUCCESSOR(x)
if x.right != NIL
	return TREE-MINIMUM(x.right)
y = x.p
while y != NIL and x == y.right
	x = y
	y = y.p
return y

TREE-INSERT(T, z)
y = NIL
x = T.root
while x != NIL
	y = x
	if z.key < x.key
		x = x.left
	else
		x = x.right

z.p = y
if y == NIL
	T.root = z // tree T was empty
elseif z.key < y.key
	y.left = z
else
	y.right = z

TRANSPLANT(T, u, v)
if u.p == NIL
	T.root = v
elseif u == u.p.left
	u.p.left = v
else
	u.p.right = v
if v != NIL
	v.p = u.p

TREE-DELETE(T, z)
if z.left == NIL
	TRANSPLANT(T, z, z.right)
elseif z.right == NIL
	TRANSPLANT(T, z, z.left)
else
	y = TREE-MINIMUM(z.right)
	if y.p != z
		TRANSPLANT(T, y, y.right)
		y.right = z.right
		y.right.p = y
	TRANSPLANT(T, z, y)
	y.left = z.left
	y.left.p = y


``` 

### 4.代码片段:
```

class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.p = None

    def InorderTreeWalk(self):
        if self.left:
            self.left.InorderTreeWalk()
        print self.key
        if self.right:
            self.right.InorderTreeWalk()

    def TreeSearch(self, k):
        if k == self.key:
            return self
        if k < self.key:
            if self.left:
                return  self.left.TreeSearch(k)
            else:
                return  None
        else:
            if self.right:
                return self.right.TreeSearch(k)
            else:
                return  None

    def IterativeTreeSearch(self, k):
        x = self
        while x  and k != self.key:
            if k < self.key:
                x = self.left
            else:
                x = self.right
        return  x

    def TreeMinimum(self):
        x = self
        while x.left:
            x = x.left
        return  x

    def TreeMaximum(self):
        x = self
        while x.right:
            x = x.right
        return  x

    def TreeSuccssor(self):
        if self.right:
            return  self.TreeMinimum()
        x = self
        y = x.p
        while y != None and x == y.right:
            x = y
            y = y.p
        return y


    def TreeInsert(self, z):
        x = self
        y = None
        while x:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.p = y

        if z.key < y.key:
            y.left = z
        else:
            y.right = z









class BinarySearchTree:
    def __init__(self):
        self.root = None

    def TreeInsert(self, z):
        if self.root:
            self.root.TreeInsert(z)
        else:
            self.root = z

    def InorderTreeWalk(self):
        if self.root:
            self.root.InorderTreeWalk()

    def Transplant(self, u, v):
        if u.p == None:
            self.root = v
        elif u == u.p.left:
            u.p.left = v
        else:
            u.p.right = v
        if v :
            v.p = u.p

    def TreeDelete(self, z):
        if z.left == None:
            self.Transplant(z, z.right)
        elif z.right == None:
            self.Transplant(z, z.left)
        else:
            y = self.TreeMinimum(z.right)
            if y.p != z:
                self.Transplant(y, y.right)
                y.right = z.right
                y.right.p = y
            self.Transplant(z, y)
            y.left = z.left
            y.left.p = y


    def TreeSearch(self, k):
        if self.root:
          return  self.root.TreeSearch(k)

    def IterativeTreeSearch(self, k):
        if self.root:
            return self.root.IterativeTreeSearch(k)

    def  TreeMinimum(self):
        if self.root:
            return self.root.TreeMinimum()

    def TreeMaximum(self):
        if self.root:
            return  self.root.TreeMaximum()

    def TreeSuccssor(self):
        if self.root:
            return  self.root.TreeSuccssor()




if __name__ == '__main__':
  b =  BinarySearchTree()
  b.TreeInsert(TreeNode(2))
  b.TreeInsert(TreeNode(3))
  b.TreeInsert(TreeNode(1))

  b.InorderTreeWalk()

  n3 = b.TreeSearch(3)
  print  "n3 = %d" % n3.key

  minNode = b.TreeMinimum()
  print  "min node is %d" % minNode.key

  b.TreeDelete( n3)

  b.InorderTreeWalk()


```
