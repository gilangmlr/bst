class SentinelNode(object):
  def __init__(self, _parent):
    self.key = None
    self.value = None
    self.level = 0
    self.parent = _parent
    self.left = self
    self.right = self

class Node(object):
  def __init__(self, _key, _value = None):
    self.key = _key
    self.value = _value
    self.level = 1
    self.parent = None
    self.left = SentinelNode(self)
    self.right = SentinelNode(self)
  
  # def __str__(self):
  #   return 'key: {}, left_key: {}, right_key: {}'.format(self.key,
  #     self.left.key if self.left != None else None,
  #     self.right.key if self.right != None else None) 

  def __str__(self):
    return '{}'.format(self.key)

# http://www.eternallyconfuzzled.com/tuts/datastructures/jsw_tut_andersson.aspx
class AATree(object):
  def __init__(self, root_key, root_value = None, num_hlink = 1):
    self.num_hlink = num_hlink
    self.root = Node(root_key, root_value)
    self.num_skew = 0
    self.num_split = 0
    self.search_comparison = 0
  
  def traverse(self, root = None):
    # https://www.geeksforgeeks.org/inorder-tree-traversal-without-recursion/
    # Set current to root of binary tree
    current = self.root if root == None else root
    # print('key: %s, right: %s' % (current.key, current.right.key if current.right != None else None))
    s = [] # initialze stack
    done = 0

    while(not done):
      # Reach the left most Node of the current Node
      if current.level != 0:
        # Place pointer to a tree node on the stack
        # before traversing the node's left subtree
        s.append(current)
        # print('%s, ' % (current.key))

        current = current.left

      # BackTrack from the empty subtree and visit the Node
      # at the top of the stack; however, if the stack is
      # empty you are done
      else:
        if(len(s) >0 ):
          current = s.pop()
          print('%s, ' % (current.key), end="")

          # We have visited the node and its left
          # subtree. Now, it's right subtree's turn
          current = current.right

        else:
          print()
          done = 1

  def skew(self, root):
    if root.level != 0:
      if root.left.level == root.level:
        old = root
        new = root.left
        child = new.right

        if old.parent != None:
          old.parent.left = new
        new.parent = old.parent
        
        new.right = old
        old.parent = new

        old.left = child
        child.parent = old

        # save = root

        # root = root.left
        # save.left = root.right
        # root.right = save

      root.right = self.skew(root.right)

    return root
  
  def __skew(self, root):
    # print('skewing? root.key: %d, root.level: %d' % (root.key, root.level))
    if root != None and root.level != 0 and root.left.level == root.level:
      # print('skewing root.key: %d, root.level: %d' % (root.key, root.level))
      self.num_skew += 1

      old = root
      new = root.left
      child = new.right

      if old.parent != None:
        dir = 'left' if old.parent.left == old else 'right'
        old.parent.__dict__[dir] = new
      new.parent = old.parent
      
      new.right = old
      old.parent = new

      old.left = child
      child.parent = old

      return new
    return root
  
  def split(self, root):
    if root.right.right.level == root.level and root.level != 0:
      old = root
      new = root.right
      child = new.left

      if old.parent != None:
        old.parent.right = new
      new.parent = old.parent

      new.left = old
      old.parent = new

      old.right = child
      child.parent = old

      # save = root

      # root = root.right
      # save.right = root.left
      # root.left = save
      # root.level += 1

      new.right = self.split(root.right)

      return new
  
  def __split(self, root):
    # print('splitting? root.key: %d, root.level: %d' % (root.key, root.level))
    right = root.right
    for _ in range(self.num_hlink):
      right = right.right
    hlinks = right.level == root.level

    if root != None and root.level != 0 and hlinks:
      # print('splitting root.key: %d, root.level: %d' % (root.key, root.level))
      self.num_split += 1
      
      old = root
      new = root.right
      child = new.left

      if old.parent != None:
        dir = 'left' if old.parent.left == old else 'right'
        old.parent.__dict__[dir] = new
      new.parent = old.parent

      new.left = old
      old.parent = new

      old.right = child
      child.parent = old

      new.level += 1

      return new
    return root
  
  def search(self, key):
    current = self.root
    while current.level != 0 and current.key != key:
      dir = 'right' if current.key < key else 'left'
      self.search_comparison += 1

      current = current.__dict__[dir]
    
    return current

  def insert(self, key, value = None):
    self.__insert(self.root, key, value)
  
  def __insert__(self, node, key, value = None):
    if node.level == 0:
      new = Node(key, value)
      new.parent = node

      if key < node.parent.key:
        node.parent.left = new
      else:
        node.parent.right = new
      
      return new
    else:
      if key < node.key:
        node.left = self.__insert__(node.left, key, value)
      else:
        node.right = self.__insert__(node.right, key, value)

      if node.parent != None and node.parent.key != None:
        if key < node.parent.key:
          node.parent.left = self.skew(node)
          node.parent.left = self.split(node)
        else:
          node.parent.right = self.skew(node)
          node.parent.right = self.split(node)

    return node

  def __insert(self, root, key, value = None):
    it = root
    up = []
    top = 0
    dir = 'left'

    while True:
      up.insert(top, it)
      top += 1
      dir = 'right' if it.key < key else 'left'

      if it.__dict__[dir].level == 0:
        break
      
      it = it.__dict__[dir]
    
    new = Node(key, value)
    it.__dict__[dir] = new
    new.parent = it

    top -= 1
    while top >= 0:
      # print('top: %d' % (top))
      
      if top != 0:
        dir = 'right' if up[top - 1].right == up[top] else 'left'
      # print('up[top].key: %d, up[top].level: %d, dir: %s' % (up[top].key, up[top].level, dir))
      
      skewed = self.__skew(up[top])
      # print('skewed.key: %s, skewed.level: %s' % (skewed.key if skewed != None else None , skewed.level if skewed != None else None))
      up[top] = skewed
      
      split = self.__split(up[top])
      up[top] = split

      if top != 0:
        up[top - 1].__dict__[dir] = up[top]
      
      root = up[top]

      if top == 0:
        self.root = up[top]

      top -= 1

    return root
  
  def delete(self, key):
    self.__delete(self.root, key)
  
  def __delete(self, root, key, value = None):
    it = root
    up = []
    top = 0
    dir = 'left'

    while True:
      up.insert(top, it)
      top += 1
      # print('level: %d, it.key: %d, key: %d' %(it.level, it.key, key))

      if it.level == 0:
        return root
      elif it.key == key or top > 10:
        break
      
      dir = 'right' if it.key < key else 'left'
      it = it.__dict__[dir]
    
    if it.left.level == 0 or it.left.level == 1:
      dir2 = 'right' if it.left.level == 0 else 'left'

      top -= 1
      if top != 0:
        up[top - 1].__dict__[dir] = it.__dict__[dir2]
        it.__dict__[dir2].parent = up[top - 1]
      else:
        self.root = it.right # inorder successor
        self.root.parent = None
    else:
      heir = it.right
      prev = it

      while heir.left.level != 0:
        prev = heir
        up.insert(top, heir)
        top += 1
        heir = heir.left
      
      it.key = heir.key
      it.value = heir.value

      prev.__dict__['right' if prev == it else 'left'] = heir.right
      heir.right.parent = prev

    top -= 1
    while top >= 0:
      if top != 0:
        dir = 'right' if up[top - 1].right == up[top] else 'left'

      if up[top].left.level < up[top].level - 1 or up[top].left.level < up[top].level - 1:
        curr_node = up[top]
        for _ in range(self.num_hlink):
          curr_node.level -= 1
          if curr_node.right.level > curr_node.level:
            curr_node.right.level = curr_node.level
          curr_node = curr_node.right

        up[top] = self.__skew(up[top])
        up[top].right = self.__skew(up[top].right)

        curr_node = up[top].right.right
        for _ in range(self.num_hlink):
          curr_node.parent.right = self.__skew(curr_node)
          curr_node = curr_node.right

        up[top] = self.__split(up[top])
        up[top].right = self.__split(up[top].right)

      if top != 0:
        up[top - 1].__dict__[dir] = up[top]
      
      root = up[top]

      if top == 0:
        self.root = up[top]

      top -= 1

    return root
