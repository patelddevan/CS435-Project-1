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
        currentNode = self.left_child
      else:
        if currentNode.right_child is None:
          currentNode.right_child = node
          return
        currentNode = self.right_child
    
  def removeIter(self, value):
    currentNode = self
    while currentNode.value != value:
      if value <= currentNode.value:
        currentNode = self.left_child
      else:
        currentNode = self.right_child
    # remove currentNode

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
      print("Provided value does not exist.")
      return -1
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
      print("Provided value does not exist.")
      return -1
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
  root.insertIter(0)
  root.insertIter(4)
  root.insertIter(3)
  root.insertIter(5)
  print(root.findPrevIter(6).value)

if __name__ == "__main__":
  main()
