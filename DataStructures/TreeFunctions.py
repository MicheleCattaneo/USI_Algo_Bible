import math
import random
'''
    Implementation of a basic BST data structure
    with many functions related to BSTs
    Author:  Michele Cattaneo
    Version: 09.04.2020
    Sources: Lecture material of prof. A. Carzaniga, USI
'''

class Node:
    def __init__(self, value):
        self.key = value
        self.left = None
        self.right = None
        self.parent = None

def insert(T, xs):
    if isinstance(xs, (list, tuple)):
        for x in xs:
            T = insert_(T, x)
    else:
        T = insert_(T, xs)
    return T

def insert_(T, k):
    if T is None:
        return Node(k)
    if k > T.key:
        T.right = insert_(T.right, k)
        T.right.parent = T
    else:
        T.left = insert_(T.left, k)
        T.left.parent = T
    return T

def isLeaf(N):
    if N is None:
        return False
    return N.left == None and N.right == None

def hasSingleLeftBranch(N):
    return N.left is not None and N.right is None

def hasSingleRightBranch(N):
    return N.left is None and N.right is not None

#____________________________________________________
# Deletation

#TODO
# probably buggy when trying to delete the root
def delete(T, node):
    if node.parent is None and isLeaf(node):
        return None

    if isLeaf(node):
        deleteLeaf(node)

    elif hasSingleLeftBranch(node):
        deleteSingleBranchNode(node, "left")

    elif hasSingleRightBranch(node):
        deleteSingleBranchNode(node, "right")

    else: #double branch
        deleteDoubleBranchNode(T, node)
    return T

def deleteDoubleBranchNode(T, node):
    sobstitute = successor(node)
    sobstitute_value = sobstitute.key
    node.key = sobstitute_value

    delete(T, sobstitute)

def deleteSingleBranchNode(node, branch):
    parent = node.parent
    if parent.left == node:
        if branch == "left":
            parent.left = node.left
            node.left.parent = parent
        else:
            parent.left = node.right
            node.right.parent = parent
    else:
        if branch == "left":
            parent.right = node.left
            node.left.parent = parent
        else:
            parent.right = node.right
            node.right.parent = parent


def deleteLeaf(N):
    parent = N.parent
    if parent.left == N:
        parent.left = None
    else:
        parent.right = None

#____________________________________________________
# Rotations

def rightRotate(A):
    parent = A.parent
    B = A.left

    #set A's left branch
    A.left = B.right
    if B.right is not None:
        B.right.parent = A
    #set B's right branch
    B.right = A
    A.parent = B
    B.parent = parent

    #set parent down link
    if parent is not None:
        if parent.left == A:
            parent.left = B
        else:
            parent.right = B
    return B

def leftRotate(A):
    parent = A.parent
    B = A.right
    A.right = B.left
    if B.left is not None:
        B.left.parent = A
    B.left = A
    A.parent = B
    B.parent = parent

    if parent is not None:
        if parent.left == A:
            parent.left = B
        else:
            parent.right = B
    return B
#____________________________________________________
# Returns the node with the given k, None if not existing
def find(T, k):
    if T is None or T.key == k:
        return T
    if k > T.key:
        return find(T.right, k)
    else:
        return find(T.left, k)

#____________________________________________________
#TODO need to set the parent pointer

# Given two BST, merge them together in a single BALANCED one ( without creating new nodes )
# Get the in-order traversal of T1
# Get in-order traversal of T2
# merge them together
# from that single sorted array of nodes, build a balanced tree
def merge_bst(T1, T2):
    in_order1 = inOrderNode(T1, [])# O(n)
    in_order2 = inOrderNode(T2, [])# O(n)
    res = merge_array_of_nodes(in_order1, in_order2)# O(n)
    return merge_bst_(res, 0, len(res)-1) # O(n)

# Given a SORTED array of NODES, create a balanced tree out of it
def merge_bst_(A, l, r):
    if l <= r:
        m = math.floor((l+r)/2)
        node = A[m]

        node.left = merge_bst_(A, l, m-1)
        node.right = merge_bst_(A, m+1, r)
        return node

# Given two SORTED arrays of NODES, merge them into a single SORTED one
def merge_array_of_nodes(A, B):
    res = []
    j=i=0
    while i < len(A) and j < len(B):
        if A[i].key < B[j].key:
            res.append(A[i])
            i+=1
        else:
            res.append(B[j])
            j+=1
    while i < len(A):
        res.append(A[i])
        i+=1
    while j < len(B):
        res.append(B[j])
        j+=1
    return res
#____________________________________________________

# Given a SORTED array, build a balanced BST
def array_to_bst(A, l, r):
    if l <= r:
        m = math.floor((l+r)/2)
        v = A[m]
        node = Node(v)
        node.left = array_to_bst(A, l, m-1)
        node.right = array_to_bst(A, m+1, r)
        return node
    # return None

# Given an UNSTORTED array of numbers, builds a balanced BST
# Note: the given array A gets sorted, create a copy if you want to keep A like that
def insert_array_balanced_tree(A):
    A.sort()
    return array_to_bst(A, 0, len(A)-1)

# Given a an array, return the order of the values so that if inserted in
# a BST, the result would be a balanced bst
def print_order_to_have_balanced_tree(A):
    A.sort()
    print_order_to_have_balanced_tree_(A, 0, len(A)-1)

# Given a SORTED array and a range ( left, right ), prints the values of that array
# so that if inserted in that order they would result in a BALANCED tree
# The idea is basically to print the middle element, and call recursively the function on the
# left side, which will result in the order for the left branch, and do the same for the right branch
# Basically the order in which the keys will be returned is the same that we would obtain by a PRE-ORDER
# made onto the tree that we will obtain
def print_order_to_have_balanced_tree_(A, l, r):
    if l <= r:
        m = math.floor((l + r) / 2)
        v = A[m]
        print(v,"- ", end='')
        print_order_to_have_balanced_tree_(A, l, m-1)
        print_order_to_have_balanced_tree_(A, m+1, r)

#____________________________________________________

def height(T):
    if T is None:
        return 0
    return 1 + max(height(T.left), height(T.right))

# Given a BST and two numbers a, b a <= b, returns the number of node keys that
# are between a and b ( inclusive )
def keyBetween(T, a, b):
    if T is None:
        return 0
    if T.key < a:
        return 0 + keyBetween(T.right, a, b)
    elif T.key > b:
        return 0 + keyBetween(T.left, a, b)
    else:
        return 1 + keyBetween(T.left, a, b) + keyBetween(T.right, a, b)

# Given a tree, validate it ( check BST condition )
# pass to each call a range, meaning a minimal value and a maximal value,
# between which the node must be
def validate(node):
    return validate_(node, float("-inf"), float("inf"))

def validate_(node, min_bound, max_bound):
    if node is None:
        return True

    if node.key < min_bound or node.key > max_bound:
        return False

    return validate_(node.left, min_bound, node.key) and validate_(node.right, node.key, max_bound)

def numberOfNodesInBranch(node):
    if node is None:
        return 0
    else:
        return 1 + numberOfNodesInBranch(node.left) + numberOfNodesInBranch(node.right)

# Returns true if the tree having T as a root node is balanced
# Balanced is defined like that: the maximal difference of height in ALL nodes must be at most 1
def isBalanced(T):
    if T is None:
        return True
    h_left = height(T.left)
    h_right = height(T.right)
    diff = abs(h_left - h_right)
    return diff <= 1 and isBalanced(T.left) and isBalanced(T.right)

# Returns the node which key is the successive to the given one ( next greater key )
def successor(T):
    if T is None:
        return None
    if T.right is not None:
        return minBST(T.right)
    # if there's no right branch, go up the ancestors line, until you find the first ancestor,
    # for which the Node is not in his right subtree
    ancestor = T.parent
    while ancestor is not None and ancestor.right == T :
        T = ancestor
        ancestor = ancestor.parent
    return ancestor

# Returns the node which key is the previous to the given one ( closest smaller key to the given one)
def predecessor(T):
    if T is None:
        return None
    if T.left is not None:
        return maxBST(T.left)
    # if there's not left branch, go up the ancestors line, until you find the first ancestor,
    # for which the None is not in his left subtree
    ancestor = T.parent
    while ancestor is not None and ancestor.left == T:
        T = ancestor
        ancestor = ancestor.parent
    return ancestor

# Returns the minimal value in the Tree
def minBST(T):
    if T is None:
        return None
    while T.left is not None:
        T = T.left
    return T

# Returns the maximal value in the Tree
def maxBST(T):
    if T is None:
        return None
    while T.right is not None:
        T = T.right
    return T

# Returns True if A is a Subtree of B
def isSubTreeOf(A, B):
    minSub = minBST(A)
    minTree = minBST(B)

    while minSub is not None and minTree is not None:
        if minSub.key < minTree.key:
            #print(minSub.key," < ", minTree.key)
            return False
        if minTree.key < minSub.key:
            minTree = successor(minTree)
        else: #if equal
            minSub = successor(minSub)

    if minSub is None:
        return True
    return False
#______________________________________________________________________
# Return the number of full nodes
# Full nodes are nodes with both left and right different from None
def countFullNodes(T):
    if T is None:
        return 0
    if T.left is not None and T.right is not None:
        return 1 + countFullNodes(T.left) + countFullNodes(T.right)
    else:
        return countFullNodes(T.left) + countFullNodes(T.right)

#TODO might be buggy with the ancestorship ( parents ) ?

# Given a tree, eliminates all double branched nodes, which basically transforms the BST into a LinkedList
# This is done by rotating a node until on of its children is None.
def makeIntoAList(T):
    if T is None: #Base case
        return T
    if T.left is None: #it's already a non-full Node, therefore just continue to the next Node
        T.right = makeIntoAList(T.right)
        return T
    if T.right is None: #it's already a non-full Node, therefore just continue to the next Node
        T.left = makeIntoAList(T.left)
        return T

    #if it's a full node
    # while the left branch is not None, keep executing a right rotation, that is bring the left branch "up of one"
    # when we exit the loop, the left branch will be None, therefore we have a non-full Node, hence we just need to fix
    # its right branch, calling recursively the function
    while T.left is not None:
        T = rightRotate(T)
    T.right = makeIntoAList(T.right)
    return T

#______________________________________________________________________
#BST-Equals(t1, t2) that takes the roots t1 and t2 of two binary
#search trees and returns true if and only if the tree rooted t1 is exactly the same as the tree rooted
#at t2, meaning that the two trees have nodes with the same keys connected in exactly the same
#way.
def bst_equals(T1, T2):
    if T1 is None and T2 is None:
        return True
    if T1.key != T2.key:
        return False
    return T1.key == T2.key and bst_equals(T1.left, T2.left) and bst_equals(T1.right, T2.right)

#an algorithm BST-Equal-Keys(t1, t2) that takes the roots t1 and t2 of two binary
#search trees and returns true if and only if the tree rooted t1 contains exactly the same keys as
#the tree rooted at t2.
def bst_equal_keys(T1, T2):
    curr_node_1 = minBST(T1)
    curr_node_2 = minBST(T2)

    while (curr_node_1 is not None and curr_node_2 is not None) and curr_node_1.key == curr_node_2.key:
        curr_node_1 = successor(curr_node_1)
        curr_node_2 = successor(curr_node_2)

    if curr_node_2 is None and curr_node_1 is None:
        return True
    return False

#______________________________________________________________________

# Tree walks and printing
def inOrderPrint(T):
    if T is not None:
        inOrderPrint(T.left)
        print(T.key, end=' ')
        inOrderPrint(T.right)

def backwardOrderPrint(T):
    if T is not None:
        backwardOrderPrint(T.right)
        print(T.key, end=' ')
        backwardOrderPrint(T.left)

def inOrderNode(T, acc):
    if T is not None:
        inOrderNode(T.left, acc)
        acc.append(T)
        inOrderNode(T.right, acc)
    return acc

def preOrder(T):
    if T is not None:
        print(T.key, end='')
        preOrder(T.left)
        preOrder(T.right)

def postOrder(T):
    if T is not None:
        postOrder(T.left)
        postOrder(T.right)
        print(T.key, end='')


def printAllPathToTheLeaves(T):
    printAllPathToTheLeaves_(T, "")

def printAllPathToTheLeaves_(T, acc):
    # if the nodes is the last node ( left and right are leaves ), print the accumulator + that node
    if T.left is None and T.right is None:
        print(acc +"->"+ str(T.key))
    else:
        # otherwise go left and right when you can
        if T.left is not None:
            printAllPathToTheLeaves_(T.left, acc +"->"+ str(T.key))
        if T.right is not None:
            printAllPathToTheLeaves_(T.right, acc +"->"+ str(T.key))


def allSubtreeSameNumberOfEven(T):
    '''
    :param T: The tree to check
    :return: True if all subtrees have the same number of even numbers
    '''
    if T is None:
        return 0
    if T.left is None and T.right is None:
        return 1 if T.key % 2 == 0 else 0
    left = allSubtreeSameNumberOfEven(T.left)
    right = allSubtreeSameNumberOfEven(T.right)
    #print(T.key, left, right)
    if left != right:
        return False

    return left + right + 1 if T.key % 2 == 0 else left + right

#TODO buggy?
def allPathToLeafSameNumberOfEven(T):
    '''
    :param T: The tree to check
    :return: True is all path from each node to the leaves have the
    same number of even nodes
    '''
    if T is None:
        return 0
    if T.left is None and T.right is None: # if leaf
        return 1 if T.key % 2 == 0 else 0

    left = allPathToLeafSameNumberOfEven(T.left)
    right = allPathToLeafSameNumberOfEven(T.right)
    if left != right:
        return False

    return left + 1 if T.key % 2 == 0 else left

evenTree = Node(9)
evenTree = insert(evenTree, [4,14,1,7,11,17,0,2,6,8,10,12,16,18])


# ------------------------------------------------------------------------------------
# Monte Carlo computation of the average height of a random BST
def generateRandomArrayOfValue(size):
    lower = -99
    upper = 99
    return  [random.randint(lower, upper) for iter in range(size)]

def monte_carlo_height_of_random_bst(n):
    total_height = 0
    tries = 100
    for i in range(tries):
        arr = generateRandomArrayOfValue(n)
        node = Node(arr[0])#first number is root
        node = insert(node, arr[1:])# insert the xs of x:xs ( rest of the list )
        h = height(node)
        total_height += h
    res = total_height / tries
    print("for a (random) tree of", n,"nodes, the average height is:",res)
    return res
# ------------------------------------------------------------------------------------
# Write an algorithm Upper-Bound-BST(T, x) that returns the upper bound of x in a
# binary search tree T. Analyze the complexity of Upper-Bound-BST.
# upperbound u_i in T, s.t u_i < u_k for all u_k >= x
def upperBound(T, x):
    if isLeaf(T):
        if T.key >= x:
            return T
        else:
            return successor(T)
    if T.key == x:
        return T
    if T.key > x:
        return upperBound(T.left, x)
    else:
        return upperBound(T.right, x)

# Return the right most node which value a is a <= x
# in other words the node with the highest value which is not bigger than x
def lowerBound2(T, x):
    if isLeaf(T):
        if T.key <= x:
            return T
        else:
            return predecessor(T)
    if T.key == x:
        return T
    if T.key > x:
        return lowerBound2(T.left, x)
    else:
        return lowerBound2(T.right, x)

# ------------------------------------------------------------------------------------
# Check wether there are two nodes which sum is "sum"
def bst_find_sum(T, sum):
    minimum = minBST(T)
    maximum = maxBST(T)

    while minimum.key < maximum.key:
        if minimum.key + maximum.key > sum:
            maximum = predecessor(maximum)
        elif maximum.key + minimum.key < sum:
            minimum = successor(minimum)
        else:
            #print(minimum.key, "+", maximum.key)
            return True
    return False

#TODO BUGGY ! do not use
def lowerBound(T, x):
    # rightmost element whose key is ≤ v, or null
    while T is not None:
        if x < T.key:
            T = T.left
        elif T.right is not None and T.right.key < x:
            T = T.right
        else:
            return T
    return None

#   10
#     \
#      15
#        \
#        18
#        /
#       16

# ------------------------------------------------------------------------------------
# Given a bst, prints the longest path in that tree
def bst_print_longest_path(T):
    if T is not None:
        print(T.key)
        h1 = height(T.left)
        h2 = height(T.right)
        if h1 > h2:
            bst_print_longest_path(T.left)
        else:
            bst_print_longest_path(T.right)


# ------------------------------------------------------------------------------------
# Returns the median, meaning the element in T
# such that there are as much nodes that are bigger, as nodes that are smaller
def bst_find_median(T):
    tot_nodes = numberOfNodesInBranch(T)
    return bst_select_k_smallest(T, math.floor(tot_nodes/2)+1)

# Returns the k-th smallest element in T
def bst_select_k_smallest(T, k):

    left_weight = numberOfNodesInBranch(T.left)
    if k <= left_weight:
        # if k is less or equal than the number of nodes in the left branch of
        # T, keep searching for the k-th smallest element in the left branch
        return bst_select_k_smallest(T.left, k)
    elif k > left_weight + 1:
        # if k is greater than the number of elements in the left branch + this nodes
        # search for the (k - left_weight - 1)-th element in the right branch
        return bst_select_k_smallest(T.right, k - left_weight - 1)
    else:
        # Otherwise the elements is found and can be returned
        return T

#___________________________________________________________
# Move the given node to the root, using rotations
# if no key with that value is in the tree, leave the tree like that

def moveToRoot(T, k):
    # stack containing the path to arrive to the node
    nodeStack = []
    # stack containing the directions taken in the path
    dirStack = []
    # find the node and fill the stacks
    current = T
    while current is not None:
        if current.key == k:
            break
        elif current.key > k:
            nodeStack.append(current)
            dirStack.append("left")
            current = current.left
        else:
            nodeStack.append(current)
            dirStack.append("right")
            current = current.right


    # if not found:
    if current is None:
        return T
    else:
        # while one of the stacks is empty, rotate the node of the path in the opposite side
        while len(nodeStack) > 0:
            toRotate = nodeStack[-1]
            dir = dirStack[-1]

            if dir == "left":
                #print("rotate", toRotate.key, "right")
                newRoot = rightRotate(toRotate)

            else:
                #print("rotate", toRotate.key, "left")
                newRoot = leftRotate(toRotate)

            # pop one item from each stack
            del nodeStack[-1]
            del dirStack[-1]
    # return the new root
    return newRoot

#______________________________
# Find the Lowest Common Ancestor of two key in a Tree.

# Return the lowest common ancestor of the two nodes
def lowestCommonAncestor(T, k1, k2):
    path1 = find_path(T, k1, [])
    path2 = find_path(T, k2, [])
    return findCommon(path1, path2)

# Given a key, return a sequence of visited nodes that takes you to that node
def find_path(T, k, acc):

    if T is None or T.key == k:
        acc.append(T)
        return acc
    elif k > T.key:
        acc.append(T)
        return find_path(T.right, k, acc)
    else:
        acc.append(T)
        return find_path(T.left, k, acc)

# Given two sequences of nodes, return the last node that they have in common
def findCommon(list1, list2):
    common = None
    i = 0
    while i < len(list1) and i < len(list2) and list1[i].key == list2[i].key:
        common = list1[i]
        i += 1
    return common

#__________________________________
# Print Level by Level

def printLevelByLevel(T):
    Q = [T]
    # Basically execute a BFS
    while len(Q) > 0:
        # remove head of Q
        current = Q[0]
        del Q[0]

        if current is not None:
            print(current.key)
            # Add left and right to the end of Q
            Q.append(current.left)
            Q.append(current.right)

#levelTree = Node(10)
#levelTree = insert(levelTree, [5,15,3,6,20,30,40])

#printLevelByLevel(levelTree)


#__________________________________
# Without building the BST, check whether the two arrays represents the same BST

def areSameBST(arr1, arr2):
    # make sure that the given array have the same length, that's an invariant
    # that must be true for every array passed
    if arr1[0] != arr2[0] or len(arr1) != len(arr2):
        return False
    return areSameBSTHelper(arr1, arr2)

def areSameBSTHelper(arr1, arr2):
    if len(arr1) == 0 and len(arr2) == 0:
        return True
    if arr1[0] != arr2[0]:
        return False
    head = arr1[0]

    leftA1 = [] #everything that would be on the left of the root of arr1
    rightA1 = [] #everything that would be on the right of the root of arr1
    leftA2 = [] # same for arr2
    rightA2 = [] # same for arr2

    for i in range(1, len(arr1)):
        #for a1
        if arr1[i] > head:
            rightA1.append(arr1[i])
        else:
            leftA1.append(arr1[i])
        #for a2
        if arr2[i] > head:
            rightA2.append(arr2[i])
        else:
            leftA2.append(arr2[i])

    # check that the subtrees have the same number of elements
    if len(leftA1) != len(leftA2):
        return False
    if len(rightA2) != len(rightA1):
        return False

    #invariant here, the arrays have the same length
    #for each subtree we are sure that the first element in that array will be the root, because
    #for example for the left subtree it will be the first smaller element encountered.
    # For that reason the subtrees ( subproblems ) obey the same rules and we can recursively
    # call the function for the left subtrees and right subtrees
    return areSameBSTHelper(leftA1, leftA2) and areSameBSTHelper(rightA1, rightA2)

#-------------------------------------------------------------------------------------------------------------------------------------
# _______________Testing _____________
# ____________________________________

''' tree1
                10
              /    \ 
            5       15
             \      / \ 
              8    12  25
              
'''
tree1 = insert(None, [10,15,25,12,5,8])

assert keyBetween(tree1, 8, 12) == 3
assert countFullNodes(tree1) == 2
assert tree1.parent == None
assert tree1.right.parent.key == 10
assert tree1.left.parent.key == 10
assert tree1.left.right.parent.key == 5
assert tree1.right.right.parent.key == 15
assert height(tree1) == 3
assert minBST(tree1).key == 5
assert maxBST(tree1).key == 25
assert successor(find(tree1, 25)) == None
assert successor(find(tree1, 8)).key == 10
assert successor(find(tree1, 10)).key == 12
assert predecessor(find(tree1, 12)).key == 10
assert predecessor(find(tree1, 5)) == None
assert predecessor(find(tree1, 10)).key == 8
assert predecessor(find(tree1, 25)).key == 15

#do a right rotation on 10
'''
        5
         \ 
          10
         /   \ 
        8     15
             /  \ 
            12   25
'''
nodeTen = find(tree1, 10)
tree1 = rightRotate(nodeTen)
assert height(tree1) == 4
assert minBST(tree1).key == 5
assert maxBST(tree1).key == 25

assert find(tree1, 5).parent == None
assert find(tree1, 5).left == None
assert find(tree1, 5).right.key == 10
assert find(tree1, 10).parent.key == 5
assert find(tree1, 5).right.left.key == 8
assert find(tree1, 8).parent.key == 10
assert find(tree1, 5).right.right.key == 15
assert find(tree1, 15).parent.key == 10
assert find(tree1, 5).right.right.left.key == 12
assert find(tree1, 5).right.right.right.key == 25
assert keyBetween(tree1, 11, 26) == 3
assert keyBetween(tree1, 12, 25) == 3

#inOrderPrint(tree1)
#print("")
#ackwardOrderPrint(tree1)
#print("")


tree_for_left_rotate = insert(None, [10,5,15,8,12,25])
tree_for_left_rotate = leftRotate(tree_for_left_rotate)
assert tree_for_left_rotate.key == 15
assert tree_for_left_rotate.left.key == 10
assert tree_for_left_rotate.right.key == 25

# testing delete
treeDeleteLeafTest = insert(None, [10,5,15,8])

#inOrderPrint(treeDeleteLeafTest)
treeDeleteLeafTest = delete(treeDeleteLeafTest, find(treeDeleteLeafTest, 8))
assert find(treeDeleteLeafTest, 8) == None
assert find(treeDeleteLeafTest, 5).right == None
assert find(treeDeleteLeafTest, 15).parent.key == 10
assert find(treeDeleteLeafTest, 5).parent.key == 10

leafTree = Node(10)
leafTree = delete(leafTree, find(leafTree, 10))
assert leafTree == None

# testing subtree of
bigTree = insert(None, [10,5,15,8,20,12,11,13])
smallTree = Node(12)
smallTree = insert(smallTree, [11, 13])
assert isSubTreeOf(smallTree, bigTree)
assert isSubTreeOf(bigTree, smallTree) == False

# testing deleting of node with one branch ---------------------------------------
#       (10)   |          (10)    |        (10)     |       (10)
# A)   /       B)        /       C)          \      D)        \
#     (5)      |         (5)      |           (15)  |          (15)
#    /         |           \      |          /      |            \
#   (2)        |            (7)   |         (12)    |             (20)


treeA = insert(None, [10,5,2])

treeB = insert(None,[10,5,7])

treeC = insert(None, [10,15,12])

treeD = insert(None, [10, 15, 20])
print("")

treeA = delete(treeA, find(treeA, 5))
assert find(treeA, 5) == None
assert find(treeA, 2).parent.key == 10
assert find(treeA, 10).left.key == 2

treeB = delete(treeB, find(treeB, 5))
assert find(treeB, 5) == None
assert find(treeB, 7).parent.key == 10
assert find(treeB, 10).left.key == 7

treeC = delete(treeC, find(treeC, 15))
assert find(treeC, 15) == None
assert find(treeC, 12).parent.key == 10
assert find(treeC, 10).right.key == 12

treeD = delete(treeD, find(treeD, 15))
assert find(treeD, 15) == None
assert find(treeD, 20).parent.key == 10
assert find(treeD, 10).right.key == 20


# ------------------------------------------------------------------------------------
# Testing deleting of a double branch node
#   (10)
#      \
#      (15)
#      /   \
#    (13)  (20)
#          /   \
#        (16)  (25)


doubleBranchTree = insert(None, [10,15,13,20,16,25])
doubleBranchTree = delete(doubleBranchTree, find(doubleBranchTree, 15))

nodeSixteen = find(doubleBranchTree, 16)
assert nodeSixteen.parent.key == 10
assert nodeSixteen.left.key == 13
assert nodeSixteen.right.key == 20
assert find(doubleBranchTree, 15) == None

# ------------------------------------------------------------------------------------
# Testing number of nodes under

tree_test_number_of_nodes = insert(None, [10,2,1,3,4,6,5])
assert numberOfNodesInBranch(tree_test_number_of_nodes) == 7

tree_test_number_of_nodes_2 = Node(10)
assert numberOfNodesInBranch(tree_test_number_of_nodes_2) == 1

# ------------------------------------------------------------------------------------
# Test balanced

balanced_tree_1 = insert(None, [10,5,15,3])
assert isBalanced(balanced_tree_1)

unbalanced_tree_1 = insert(None, [10,15,20])
assert isBalanced(unbalanced_tree_1) == False

unbalanced_tree_2 = insert(None, [10,5,15,3,8,20,25])
assert isBalanced(unbalanced_tree_2) == False
# ------------------------------------------------------------------------------------
# Testing build balanced tree form an array
arr1 = [5,2,4,1,3,6]
tree_from_array = insert_array_balanced_tree(arr1)
assert validate(tree_from_array)
assert tree_from_array.key == 3


#assert find(tree_from_array, 3).left.key == 2

#inOrderPrint(tree_from_array)
test = array_to_bst([1,2,3,4,5], 0, 4)

#inOrderPrint(test)

arr2 = [5,3,6,8,7,9,1,4,2]
#print_order_to_have_balanced_tree(arr2) -> correct output sequence

# ------------------------------------------------------------------------------------
# Test inOrder


tree_to_merge_1 = insert(None, [10,5,15])


tree_to_merge_2 = insert(None, [7,8,6,25])

#print(tree_to_in_order.key)
#arr = inOrderNode(tree_to_in_order, [])
#arr2 = inOrderNode(tree_to_in_order_2, [])
#res = merge_array_of_nodes(arr, arr2)


new_tree = merge_bst(tree_to_merge_1, tree_to_merge_2)
assert isBalanced(new_tree)
assert isSubTreeOf(tree_to_merge_1, new_tree)
in_order_1 = inOrderNode(tree_to_merge_1, [])
in_order_2 = inOrderNode(tree_to_merge_2, [])
for n in in_order_1:
    assert find(new_tree, n.key)
for n in in_order_2:
    assert find(new_tree, n.key)

# ------------------------------------------------------------------------------------
# Testing montecarlo algorithm to get average height of random tree
res = monte_carlo_height_of_random_bst(256)

#______________________________________________________________________
# Test no Full Node ( make the tree be a linked list basically )

full_tree = insert(None, [10,5,15,3,8,13,18,1,4,6,9,11,14,16,20])
assert countFullNodes(full_tree) == 7
assert numberOfNodesInBranch(full_tree) == 15
full_tree = makeIntoAList(full_tree)
assert countFullNodes(full_tree) == 0 # assert that is is indeed a linkedList
assert numberOfNodesInBranch(full_tree) == 15
# ------------------------------------------------------------------------------------
# Testing upper bound: U is upperbound of X if U is the smalles value in T, st U >= X


upper_bound_tree = insert(None, [7, 20, 1, 3, 4, 3, 31, 50, 9, 11])


assert upperBound(upper_bound_tree, 15).key == 20
assert upperBound(upper_bound_tree, 9).key == 9


upper_bound_tree2 = insert(None, [10,5,15,3,7,12,18])
assert upperBound(upper_bound_tree2, 6).key == 7



upper_bound_tree3 = insert(None, [10,5,15,3,8,13,18,1,4,6,9,11,14,16,20])
assert upperBound(upper_bound_tree3, 7).key == 8
assert bst_find_sum(upper_bound_tree3, 21)
assert bst_find_sum(upper_bound_tree3, 17)
assert bst_find_sum(upper_bound_tree3, 28)

assert lowerBound2(upper_bound_tree3, 16).key == 16
#print(lowerBound2(upper_bound_tree3, 16).key, "ciaooo")


lower_bound_tree = insert(None, [10,15,18,16])
assert lowerBound2(lower_bound_tree, 15.5).key == 15
#print(lowerBound2(lower_bound_tree, 15.5).key)

# ------------------------------------------------------------------------------------
# Test bst_equals


tree_equal = insert(None, [10,5,15,8,12])

tree_similar = insert(None, [10,8,12,5,15])

tree_same_shape = insert(None, [10,4,16,8,12])

assert bst_equals(tree_equal, tree_equal)
assert bst_equals(tree_similar, tree_equal) == False
assert bst_equals(tree_equal, tree_same_shape) == False
assert bst_equal_keys(tree_equal, tree_similar)
assert bst_equal_keys(tree_equal, tree_same_shape) == False


#__________________________________________
# Test print longest path


long_tree = insert(None, [50,25,75,20,30,27,29])
#bst_print_longest_path(long_tree) -> should be 50-25-30-27-29

# Test median

assert bst_find_median(long_tree).key == 29
assert bst_find_median(upper_bound_tree3).key == 10
assert bst_find_median(tree_equal).key == 10

#__________________________________________

# Test move to root


tree_to_rotate = insert(None, [15,15,2,35,28,42,19,31])

newRoot = moveToRoot(tree_to_rotate, 19)
assert newRoot.key == 19
assert newRoot.left.key ==15
assert newRoot.right.key == 35
assert newRoot.right.left.key == 28

#__________________________________________

# Test Lowest Common Ancestor


lca = insert(None, [10,5,15,3,7,6,9,8])

assert lowestCommonAncestor(lca, 3,15).key == 10
assert lowestCommonAncestor(lca, 3,8).key == 5
assert lowestCommonAncestor(lca, 5,9).key == 5
assert lowestCommonAncestor(lca, 10, 15).key == 10


#__________________________________________

# Testing same subtree ( without building the tree )

assert areSameBST([5,3,2,10,6], [5,10,6,3,2]) == True
assert areSameBST([5,3,2,10,6], [5,2,3,10,6]) == False
assert areSameBST([15,25,20,22,30,18,10,8,9,12,6], [15,10,12,8,25,30,6,20,18,9,22]) == True
assert areSameBST([15,23,20,22,30,18,10,8,9,12,6], [15,10,12,8,25,30,6,20,18,9,22]) == False