import random
import time

class Node:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None
    self.height = 1

def getRandomArray(n):
  random_array = list()
  for i in range(n):
    random_int = getRandomNumber(n)
    while random_int in random_array:
      random_int = getRandomNumber(n)
    random_array.append(random_int)
  return random_array 

def getRandomNumber(n):
  return random.randint(0, n*10)

def getSortedArray(n):
  sorted_array = list()
  for i in range(n, 0, -1):
    sorted_array.append(i)
  return sorted_array

def findMinIter(root):
    while root.left is not None:
      root = root.left
    return root

def findMaxIter(root):
    while root.right is not None:
      root = root.right
    return root

def getHeight(node): 
  if not node: 
      return 0
  return node.height

def getBalance(node): 
  if not node: 
      return 0
  return getHeight(node.left) - getHeight(node.right)

def leftRotate(node):
  temp = node.right
  node.right = temp.left
  temp.left = node
  node.height = max(getHeight(node.left), getHeight(node.right)) + 1
  temp.height = max(getHeight(temp.left), getHeight(temp.right)) + 1
  return temp

def rightRotate(node):
  temp = node.left
  node.left = temp.right
  temp.right = node
  node.height = max(getHeight(node.left), getHeight(node.right)) + 1
  temp.height = max(getHeight(temp.left), getHeight(temp.right)) + 1
  return temp

def leftRightRotate(node):
  node.left = leftRotate(node.left)
  return rightRotate(node)

def rightLeftRotate(node):
  node.right = rightRotate(node.right)
  return leftRotate(node)

def insertIterAVL(root, value):
  count = 0
  currentNode = root
  ancestors = list()
  while True:
    ancestors.append(currentNode)
    if value < currentNode.value:
      if currentNode.left is None:
        currentNode.left = Node(value)      
        # print(value, count) 
        break
      currentNode = currentNode.left
      count += 1
    elif value > currentNode.value:
      if currentNode.right is None:
        currentNode.right = Node(value)
        # print(value, count)
        break
      currentNode = currentNode.right
      count +=1
    else:
      return False
  #print("Start Ancestors")
  #for x in ancestors: print(x.value)
  #print("End Ancestors")
  while len(ancestors) != 0:
    a = ancestors.pop()
    a.height = max(getHeight(a.left), getHeight(a.right)) + 1
    balance = getBalance(a)
    if balance > 1:
      leftBalance = getBalance(a.left)
      if leftBalance == -1:
        #print("--- left-right rotation ---", a.value)
        if len(ancestors) == 0:
          root = leftRightRotate(a)
        else:
          if ancestors[-1].left == a:
            ancestors[-1].left = leftRightRotate(a)
          else:
            ancestors[-1].right = leftRightRotate(a)
      elif leftBalance == 1:
        #print("--- right rotation ---", a.value)
        if len(ancestors) == 0:
          root = rightRotate(a)
        else:
          if ancestors[-1].left == a:
            ancestors[-1].left = rightRotate(a)
          else:
            ancestors[-1].right = rightRotate(a)
    elif balance < -1:
      rightBalance = getBalance(a.right)
      if rightBalance == -1:
        #print("--- left rotation ---", a.value)
        if len(ancestors) == 0:
          root = leftRotate(a)
        else:
          if ancestors[-1].left == a:
            ancestors[-1].left = leftRotate(a)
          else:
            ancestors[-1].right = leftRotate(a)
      elif rightBalance == 1:
        #print("--- right-left rotation ---", a.value)
        if len(ancestors) == 0:
          root = rightLeftRotate(a)
        else:
          if ancestors[-1].left == a:
            ancestors[-1].left = rightLeftRotate(a)
          else:
            ancestors[-1].right = rightLeftRotate(a)
  return root, count

def insertRecAVL(root, value): # recursive insert is broken
  if value < root.value:
    if root.left is None:
      root.left = Node(value)
    else:
      insertRec(root.left, value)
  else:
    if root.right is None:
      root.right = Node(value)
    else:
      insertRec(root.right, value)
  root.height = max(getHeight(root.left), getHeight(root.right)) + 1
  balance = getBalance(root)
  if balance > 1:
      leftBalance = getBalance(root.left)
      if leftBalance == -1:
        #print("--- left-right rotation ---")
        return leftRightRotate(root)
      elif leftBalance == 1:
        #print("--- right rotation ---")
        return rightRotate(root)
  elif balance < -1:
    rightBalance = getBalance(root.right)
    if rightBalance == -1:
      #print("--- left rotation ---")       
      return leftRotate(root)
    elif rightBalance == 1:
      #print("--- right-left rotation ---")
      return rightLeftRotate(root)
  return root

def insertRec(root, value):
    if root == None:
      root = Node(value)
      return
    # node belongs in left subtree
    if value < root.value: 
      # left child of current node does not exist
      if root.left is None:
        # set node as left child of current node
        root.left = Node(value)
      else:
        # insert somewhere in left subtree
        insertRec(root.left, value)
    # node belongs in right subtree
    else:
      # right child of current node does not exist
      if root.right is None:
        # set node as right child of current node
        root.right = Node(value)
      else:
        # insert somewhere in right subtree
        insertRec(root.right, value)

def insertIter(root, value):
  count = 0
  while True:
    if value < root.value:
      if root.left is None:
        root.left = Node(value)       
        #print(value, count)
        break
      root = root.left
      count += 1
    elif value > root.value:
      if root.right is None:
        root.right = Node(value)
        #print(value, count)
        break
      root = root.right
      count +=1
    else:
      return False
  return True, count

def deleteIter(root, value):
  returnValue = None
  currentNode = root
  parentNode = None
  isLeft = None
  while True:
    if currentNode.value == value:
      break
    if value < currentNode.value and currentNode.left is not None:
      parentNode = currentNode
      currentNode = currentNode.left
      isLeft = True
    elif value > currentNode.value and currentNode.right is not None:
      parentNode = currentNode
      currentNode = currentNode.right
      isLeft = False
    else:
      returnValue = root
      break
  while True:
    c = currentNode
    if c.left is None and c.right is None:
      if parentNode is None:
        returnValue = None
        break
      elif isLeft:
        parentNode.left = None
      else:
        parentNode.right = None
      returnValue = root
      break
    elif c.left is None:
      if isLeft is None:
        returnValue = root.right
        break
      elif isLeft:
        parentNode.left = c.right
      elif not isLeft:
        parentNode.right = c.right
      returnValue = root
      break
    elif c.right is None:
      if isLeft is None:
        returnValue = root.left
        break
      elif isLeft:
        parentNode.left = c.left
      elif not isLeft:
        parentNode.right = c.left
      returnValue = root
      break
    else:
      parentNode = c
      inOrderSuccessor = c.right
      isLeft = False
      while inOrderSuccessor.left is not None:
        parentNode = inOrderSuccessor
        inOrderSuccessor = inOrderSuccessor.left
        isLeft = True
      c.value = inOrderSuccessor.value
      currentNode = inOrderSuccessor
  return returnValue

def deleteIterAVL(root, value):
  returnValue = None
  currentNode = root
  parentNode = None
  isLeft = None
  ancestors = list()
  while True:
    ancestors.append(currentNode)
    if currentNode.value == value:
      break
    if value < currentNode.value and currentNode.left is not None:
      parentNode = currentNode
      currentNode = currentNode.left
      isLeft = True
    elif value > currentNode.value and currentNode.right is not None:
      parentNode = currentNode
      currentNode = currentNode.right
      isLeft = False
    else:
      returnValue = root
      break
  while True:
    c = currentNode
    if c.left is None and c.right is None:
      if parentNode is None:
        returnValue = None
        break
      elif isLeft:
        parentNode.left = None
      else:
        parentNode.right = None
      returnValue = root
      break
    elif c.left is None:
      if isLeft is None:
        returnValue = root.right
        break
      elif isLeft:
        parentNode.left = c.right
      elif not isLeft:
        parentNode.right = c.right
      returnValue = root
      break
    elif c.right is None:
      if isLeft is None:
        returnValue = root.left
        break
      elif isLeft:
        parentNode.left = c.left
      elif not isLeft:
        parentNode.right = c.left
      returnValue = root
      break
    else:
      parentNode = c
      inOrderSuccessor = c.right
      ancestors.append(inOrderSuccessor)
      isLeft = False
      while inOrderSuccessor.left is not None:
        parentNode = inOrderSuccessor
        inOrderSuccessor = inOrderSuccessor.left
        isLeft = True
        ancestors.append(inOrderSuccessor)
      c.value = inOrderSuccessor.value
      currentNode = inOrderSuccessor
  while len(ancestors) != 0:
    a = ancestors.pop()
    a.height = max(getHeight(a.left), getHeight(a.right)) + 1
    balance = getBalance(a)
    if balance > 1:
      leftBalance = getBalance(a.left)
      if leftBalance < 0:
        #print("--- left-right rotation ---", a.value)
        if len(ancestors) == 0:
          returnValue = leftRightRotate(a)
        else:
          if ancestors[-1].left == a:
            ancestors[-1].left = leftRightRotate(a)
          else:
            ancestors[-1].right = leftRightRotate(a)
      elif leftBalance >= 0:
        #print("--- right rotation ---", a.value)
        if len(ancestors) == 0:
          returnValue = rightRotate(a)
        else:
          if ancestors[-1].left == a:
            ancestors[-1].left = rightRotate(a)
          else:
            ancestors[-1].right = rightRotate(a)
    elif balance < -1:
      rightBalance = getBalance(a.right)
      if rightBalance <= 0:
        #print("--- left rotation ---", a.value)
        if len(ancestors) == 0:
          returnValue = leftRotate(a)
        else:
          if ancestors[-1].left == a:
            ancestors[-1].left = leftRotate(a)
          else:
            ancestors[-1].right = leftRotate(a)
      elif rightBalance > 0:
        #print("--- right-left rotation ---", a.value)
        if len(ancestors) == 0:
          returnValue = rightLeftRotate(a)
        else:
          if ancestors[-1].left == a:
            ancestors[-1].left = rightLeftRotate(a)
          else:
            ancestors[-1].right = rightLeftRotate(a)
  return returnValue

def deleteRecAVL(root, value):
    if root is None: return root
    if value > root.value and root.right is not None:
      root.right = deleteRecAVL(root.right, value)
    elif value < root.value and root.left is not None:
      root.left = deleteRecAVL(root.left, value)
    else:
      if root.left is None: 
        x = root.right
        root = None
        return x
      elif root.right is None:
        x = root.left
        root = None
        return x
      elif root.right is not None:
        inorder_successor = findMinIter(root.right)
        root.value = inorder_successor.value
        root.right = deleteRecAVL(root.right, inorder_successor.value)  
    root.height = max(getHeight(root.left), getHeight(root.right)) + 1
    balance = getBalance(root)
    if balance > 1:
      leftBalance = getBalance(root.left)
      if leftBalance < 0:
        return leftRightRotate(root)
      else:
        return rightRotate(root)
    elif balance < -1:
      rightBalance = getBalance(root.right)
      if rightBalance > 0:
        return rightLeftRotate(root)
      else:
        return leftRotate(root)
    return root

def findIter(root, value):
    while root is not None:
      if value < root.value:
        root = root.left
      elif value > root.value:
        root = root.right
      else:
        return root
    # node with value equal to the provided was not found
    return None

def findNextChildIter(root):
    while root.left is not None:
      root = root.left
    return root

def findNextAncestorIter(root, value):
    currentNode = root
    while True:
      if ((currentNode.left is None or root.left.value <= value) and currentNode.value > value):
        return currentNode
      if currentNode.left is not None and value < currentNode.value:
        currentNode = currentNode.left
      elif currentNode.right is not None and value > currentNode.value:
        currentNode = currentNode.right
      # an ancestor with value greater than the provided was not found
      else:
        return None

def findNextIter(root, value):
    node = findIter(root, value)
    if node is None:
      return None
    elif node.right is None:
      return findNextAncestorIter(root, value)
    return findNextChildIter(node.right)

def findPrevChildIter(root):
    while root.right is not None:
      root = root.right
    return root

def findPrevAncestorIter(root, value):
    currentNode = root
    while True:
      if ((currentNode.right is None or root.right.value >= value) and currentNode.value < value):
        return currentNode
      if currentNode.left is not None and value < currentNode.value:
        currentNode = currentNode.left
      elif currentNode.right is not None and value > currentNode.value:
        currentNode = currentNode.right
      # an ancestor with value lesser than the provided was not found
      else:
        return None

def findPrevIter(root, value):
    node = findIter(root, value)
    if node is None:
      return None
    elif node.left is None:
      return findPrevAncestorIter(root, value)
    return findPrevChildIter(node.left)

def printInorder(node):  
    if node is not None:
      printInorder(node.left)
      print("value ->", node.value, "height ->", node.height)
      printInorder(node.right)

def main():
  '''
  # 5a
  arr = getRandomArray(10000)
  root = Node(arr[0])
  for i in range(1, len(arr), 1):
    root = insertIterAVL(root, arr[i])[0]

  _root = Node(arr[0])
  for i in range(1, len(arr), 1):
    insertRec(_root, arr[i])
  '''

  '''
  # 5b
  arr = getRandomArray(10)
  root = Node(arr[0])
  for i in range(1, len(arr), 1):
    root = insertIterAVL(root, arr[i])[0]

  _root = Node(arr[0])
  for i in range(1, len(arr), 1):
    insertRec(_root, arr[i])
  '''

  '''
  # 5c
  total = 0
  print("--- Building Balanced Binary Search Tree ---")
  arr = getRandomArray(10000)
  root = Node(arr[0])
  for i in range(1, len(arr), 1):
    x = insertIterAVL(root, arr[i])
    root = x[0]
    total += x[1]
  print(total)

  _total = 0
  print("--- Building Binary Search Tree ---")
  _root = Node(arr[0])
  for i in range(1, len(arr), 1):
    _total += insertIter(_root, arr[i])[1]
  print(_total)
  '''

  '''
  # 5c
  total = 0
  print("--- Building Balanced Binary Search Tree ---")
  arr = getSortedArray(10000)
  root = Node(arr[0])
  for i in range(1, len(arr), 1):
    x = insertIterAVL(root, arr[i])
    root = x[0]
    total += x[1]
  print(total)

  _total = 0
  print("--- Building Binary Search Tree ---")
  _root = Node(arr[0])
  for i in range(1, len(arr), 1):
    _total += insertIter(_root, arr[i])[1]
  print(_total)
  '''

  '''
  # 7a
  start_time = time.time()
  arr = getRandomArray(10000)
  root = Node(arr[0])
  for i in range(1, len(arr), 1):
    root = insertIterAVL(root, arr[i])[0]
  for i in range(1, len(arr), 1):
    root = deleteIterAVL(root, arr[i])
  bbst_time = time.time() - start_time
  print("--- %s seconds elapsed performing operations on balanced binary search tree---" % (bbst_time))
  start_time = time.time()
  _root = Node(arr[0])
  for i in range(1, len(arr), 1):
    insertIter(_root, arr[i])
  for i in range(1, len(arr), 1):
    _root = deleteIter(_root, arr[i])
  bst_time = time.time() - start_time
  print("--- %s seconds elapsed performing operations on binary search tree ---" % (bst_time))
  print("time it took to perform operations on balanced binary search tree - time it took to perform operations on binary search tree =", bbst_time - bst_time)
  '''

  pass

if __name__ == "__main__":
  main()
