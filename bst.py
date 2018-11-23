class Node(object):
  def __init__(self, _key, _value = None):
    self.key = _key
    self.value = _value
    self.parent == None
    self.left = None
    self.right = None
  
  def __str__(self):
    return 'key: {}, left_key: {}, right_key: {}'.format(self.key,
      self.left.key if self.left != None else None,
      self.right.key if self.right != None else None)

class BinarySearchTree(object):
  def __init__(self, root_key, root_value = None):
    self.root = Node(root_key, root_value)
  
  def search(self, key):
    curr_node = self.root
    while curr_node != None and curr_node.key != key:
      if key < curr_node.key:
        curr_node = curr_node.left
      else:
        curr_node = curr_node.right

    return curr_node
  
  def insert(self, key, value=None):
    prev_node = None
    curr_node = self.root

    while curr_node != None and curr_node.key != key:
      prev_node = curr_node
      if key < curr_node.key:
        curr_node = curr_node.left
      else:
        curr_node = curr_node.right

    if curr_node != None: # key already exists, overwrite value
      curr_node.value = value
    else:
      new_node = Node(key, value)
      new_node.parent = prev_node

      if key < prev_node.key:
        prev_node.left = new_node
      else:
        prev_node.right = new_node
  
  def tree_minimum(self, root):
    if root == None:
      return None

    curr_node = root
    while curr_node.left != None:
      curr_node = curr_node.left

    return curr_node

  def transplant(self, u, v):
    if u.parent == None:
      self.root = u
    elif u == u.parent.left:
      u.parent.left = v
    else:
      u.parent.right = v
    
    if v != None:
      v.parent = u.parent

  def delete(self, key):
    curr_node = self.root

    while curr_node != None and curr_node.key != key:
      if key < curr_node.key:
        curr_node = curr_node.left
      else:
        curr_node = curr_node.right
    
    if curr_node != None:
      if curr_node.left == None:
        self.transplant(curr_node, curr_node.right)
      elif curr_node.right == None:
        self.transplant(curr_node, curr_node.right)
      else:
        successor_node = self.tree_minimum(curr_node.right)

        if successor_node.parent != curr_node:
          self.transplant(successor_node, successor_node.right)
          successor_node.right = curr_node.right
          successor_node.right.parent = successor_node

        successor_node.left = curr_node.left
        successor_node.left.parent = successor_node
