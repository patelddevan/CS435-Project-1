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
    if self is None: return self
    if value > self.value and self.right_child is not None:
      # search for node in right subtree
      self.right_Child = self.right_child.deleteRec(value)
    elif value < self.value and self.left_child is not None:
      # search for node in left subtree
      self.left_child = self.left_child.deleteRec(value)
    # found node (self.value == value)
    else:
      # node has at most one child
      if self.left_child is None: 
        # set right child as node and delete node
        x = self.right_child
        self = None
        return x
      elif self.right_child is None:
        # set the left child as node and delete node
        x = self.left_child
        self = None
        return x
      # node has two children
      elif self.right_child is not None:
        inorder_successor = self.right_child.findMinRec()
        self.value = inorder_successor.value
        self.right_child = self.right_child.deleteRec(inorder_successor.value)  
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
      return None
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
      return None
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

def sortHelper(node, arr):
  if node is None:
    return None
  sortHelper(node.left_child, arr)
  arr.append(node.value)
  sortHelper(node.right_child, arr)

def sort(arr):
  if len(arr) == 0: return None
  root = Node(arr[0])
  for element in arr[1:]:
    root.insertRec(element)
  sorted_arr = list()
  sortHelper(root, sorted_arr)
  return sorted_arr

def printInorder(root):  
    if root is not None:
        printInorder(root.left_child) 
        print(root.value), 
        printInorder(root.right_child)

def main():
  root = Node(25)
  root.insertRec(20)
  root.insertRec(36)
  #root.insertRec(10)
  #root.insertRec(22)
  #root.insertRec(30)
  #root.insertRec(40)
  #root.insertRec(5)
  #root.insertRec(12)
  #root.insertRec(28)
  #root.insertRec(38)
  #root.insertRec(48)
  #root.insertRec(1)
  #root.insertRec(8)
  #root.insertRec(15)
  #root.insertRec(45)
  #root.insertRec(50)
  root = root.deleteRec(25)
  printInorder(root)

  #arr = [25, 20, 36, 10, 22, 30, 40, 5, 12, 28, 38, 48, 1, 8, 15, 45, 50]
  #sorted_arr = sort(arr)
  #for e in sorted_arr:
  #  print(e)
  pass
 
if __name__ == "__main__":
  main()    
