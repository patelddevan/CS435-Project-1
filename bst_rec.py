class Node:
  def __init__(self, value):
    self.value = value
    self.left_child = None
    self.right_child = None

  def insertRec(self, value):
    # create node from value
    node = Node(value)
    # node belongs in left subtree
    if value <= self.value: 
      # left child of current node does not exist
      if self.left_child is None:
        # set node as left child of current node
        self.left_child = node
      else:
        # insert somewhere in left subtree
        self.left_child.insertRec(value)
    # node belongs in right subtree
    else:
      # right child of current node does not exist
      if self.right_child is None:
        # set node as right child of current node
        self.right_child = node
      else:
        # insert somewhere in right subtree
        self.right_child.insertRec(value)

  def deleteRec(self, value):
    # node was not found
    if self is None:
      return self
    if value < self.value:
      # search for node in left subtree
      self.left_child = self.left_child.deleteRec(value)
    elif value > self.value:
      # search for node in right subtree
      self.right_Child = self.right_child.deleteRec(value)
    # found node
    else:
      # node has at most one child
      if self.left_child is None: 
        # set right child as node and delete node
        temp = self.right_child
        self = None
        return temp
      elif self.right_child is None:
        # set the left child as node and delete node
        temp = self.left_child
        self = None
        return temp
      # node has two children
      inorder_successor = self.right_child.findMinRec()
      self.value = inorder_successor.value
      self.right.deleteRec(inorder_successor.value)  
    return self
  
  def findMinRec(self):
    min_node = self
    if self.left_child is not None:
      min_node = self.left_child.findMinRec()
    return min_node

  def findMaxRec(self):
    max_node = self
    if self.right_child is not None:
      max_node = self.right_child.findMaxRec()
    return max_node

  def findRec(self, value):
    if self.value == value:
      return self 
    elif self.left_child is not None and value < self.value:
      return self.left_child.findRec(value)
    elif self.right_child is not None and value > self.value:
      return self.right_child.findRec(value)
    else:
      return None

  def findNextRec(self, value):
    node = self.findRec(value)
    if node is None:
      print("Provided value does not exist.")
      return -1
    elif node.right_child is None:
      return self.findNextAncestorRec(value)
    return node.right_child.findNextChildRec()

  def findNextChildRec(self):
    if self.left_child is None:
      return self
    return self.left_child.findNextChildRec()

  def findNextAncestorRec(self, value):
    if ((self.left_child is None or self.left_child.value <= value) and self.value > value):
      return self
    if self.left_child is not None and value < self.value:
      return self.left_child.findNextAncestorRec(value)
    if self.right_child is not None and value > self.value:
      return self.right_child.findNextAncestorRec(value)

  def findPrevRec(self, value):
    node = self.findRec(value)
    if node is None:
      print("Provided value does not exist.")
      return -1
    elif node.left_child is None:
      return self.findPrevAncestorRec(value)
    return node.left_child.findPrevChildRec()
  
  def findPrevChildRec(self):
    if self.right_child is None:
      return self
    return self.right_child.findPrevChildRec()

  def findPrevAncestorRec(self, value):
    if ((self.right_child is None or self.right_child.value >= value) and self.value < value):
      return self
    if self.left_child is not None and value < self.value:
      return self.left_child.findPrevAncestorRec(value)
    if self.right_child is not None and value > self.value:
      return self.right_child.findPrevAncestorRec(value)


  
def sort(root):  
    if root is not None:
        sort(root.left_child) 
        print(root.value), 
        sort(root.right_child)
  
def main():
  #root = Node(21)
  #root.insertRec(15)
  #root.insertRec(25)
  #root.insertRec(17)
  #root.insertRec(19)
  #root.insertRec(11)
  #root.insertRec(13)
  #root.insertRec(22)
  #root.insertRec(20)
  #print(root.findNextRec(21).value)
  #print(root.findPrevRec(21).value)

  root = Node(2)
  root.insertRec(0)
  root.insertRec(4)
  root.insertRec(3)
  root.insertRec(5)
  print(root.findNextRec(3).value)

if __name__ == "__main__":
  main()
