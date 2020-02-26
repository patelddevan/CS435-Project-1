class Node:
  def __init__(self, value):
    self.value = value
    self.left_child = None
    self.right_child = None

  def insertIter(self, value):
    currentNode = self
    node = Node(value)
    while True:
      if value <= currentNode.value:
        if currentNode.left_child is None:
          currentNode.left_child = node
          return
        currentNode = currentNode.left_child
      else:
        if currentNode.right_child is None:
          currentNode.right_child = node
          return
        currentNode = currentNode.right_child

  def deleteIter(self, value):
      currentNode = self
      parentNode = None
      is_left_child = None
      while True:
        if currentNode.value == value:
          break
        if value < currentNode.value and currentNode.left_child is not None:
          parentNode = currentNode
          currentNode = currentNode.left_child
          is_left_child = True
        elif value > currentNode.value and currentNode.right_child is not None:
          parentNode = currentNode
          currentNode = currentNode.right_child
          is_left_child = False
        else:
          return self
      if currentNode is None:
        return self
      stack = list()
      stack.append(currentNode)
      while len(stack) > 0:
        c = stack.pop()
        if c.left_child is None and c.right_child is None:
          if parentNode is None:
              return None
          elif is_left_child:
            parentNode.left_child = None
          else:
            parentNode.right_child = None
          return self
        elif c.left_child is None:
          if is_left_child is None:
            return self.right_child
          elif is_left_child:
            parentNode.left_child = c.right_child
          elif is_left_child == False:
            parentNode.right_child = c.right_child
          return self
        elif c.right_child is None:
          if is_left_child is None:
            return self.left_child
          elif is_left_child:
            parentNode.left_child = c.left_child
          elif is_left_child == False:
            parentNode.right_child = c.left_child
          return self
        else:
          parentNode = c
          inorder_successor = c.right_child
          is_left_child = False
          while inorder_successor.left_child is not None:
            parentNode = inorder_successor
            inorder_successor = inorder_successor.left_child  
            is_left_child = True
          #print('replacing ' + str(c.value) + ' with ' + str(inorder_successor.value))        
          c.value = inorder_successor.value
          stack.append(inorder_successor)
          
  def findMinIter(self):
    currentNode = self
    while currentNode.left_child is not None:
      currentNode = currentNode.left_child
    return currentNode
  
  def findMaxIter(self):
    currentNode = self
    while currentNode.right_child is not None:
      currentNode = currentNode.right_child
    return currentNode

  def findIter(self, value):
    currentNode = self
    while currentNode is not None:
      if value < currentNode.value:
        currentNode = currentNode.left_child
      elif value > currentNode.value:
        currentNode = currentNode.right_child
      else:
        return currentNode
    # node with value equal to the provided was not found
    return None

  def findNextChildIter(self):
    currentNode = self
    while currentNode.left_child is not None:
      currentNode = currentNode.left_child
    return currentNode

  def findNextAncestorIter(self, value):
    currentNode = self
    while True:
      if ((currentNode.left_child is None or self.left_child.value <= value) and currentNode.value > value):
        return currentNode
      if currentNode.left_child is not None and value < currentNode.value:
        currentNode = currentNode.left_child
      elif currentNode.right_child is not None and value > currentNode.value:
        currentNode = currentNode.right_child
      # an ancestor with value greater than the provided was not found
      else:
        return None 
    
  def findNextIter(self, value):
    node = self.findIter(value)
    if node is None:
      return None
    elif node.right_child is None:
      return self.findNextAncestorIter(value)
    return node.right_child.findNextChildIter()

  def findPrevChildIter(self):
    currentNode = self
    while currentNode.right_child is not None:
      currentNode = currentNode.right_child
    return currentNode

  def findPrevAncestorIter(self, value):
    currentNode = self
    while True:
      if ((currentNode.right_child is None or self.right_child.value >= value) and currentNode.value < value):
        return currentNode
      if currentNode.left_child is not None and value < currentNode.value:
        currentNode = currentNode.left_child
      elif currentNode.right_child is not None and value > currentNode.value:
        currentNode = currentNode.right_child
      # an ancestor with value lesser than the provided was not found
      else:
        return None 

  def findPrevIter(self, value):
    node = self.findIter(value)
    if node is None:
      return None
    elif node.left_child is None:
      return self.findPrevAncestorIter(value)
    return node.left_child.findPrevChildIter()

def printInorder(root):  
    if root is not None:
        printInorder(root.left_child) 
        print(root.value), 
        printInorder(root.right_child)

def main():
  root = Node(2)
  root.insertIter(5)
  root.insertIter(1)
  root.insertIter(4)
  root.insertIter(0)
  root.insertIter(3)
  root = root.deleteIter(2)
  printInorder(root)

if __name__ == "__main__":
  main()
