from bst import BinarySearchTree
from aatree import AATree
import time

if __name__ == '__main__':
  upper_exponent = 5

  print('------aatree - 1 hlink------')
  start_power = 2
  for j in range(start_power, start_power + upper_exponent):
    n = 10**j
    aatree = AATree(n)

    for i in range(n - 1, 0, -1):
      aatree.insert(i)
    
    start_time = time.time()

    for i in range(n - 1, 0, -1):
      aatree.delete(i)
    
    deletion_time = time.time() - start_time

    print("n: %d, deletion: %.4f s, split: %d, skew: %d" % (n, deletion_time, aatree.num_split, aatree.num_skew))
  
  print('------aatree - 2 hlink------')
  start_power = 2
  for j in range(start_power, start_power + upper_exponent):

    n = 10**j
    aatree = AATree(n, None, 2)

    for i in range(n - 1, 0, -1):
      aatree.insert(i)
    
    start_time = time.time()

    for i in range(n - 1, 0, -1):
      aatree.delete(i)
    
    deletion_time = time.time() - start_time

    print("n: %d, deletion: %.4f s, split: %d, skew: %d" % (n, deletion_time, aatree.num_split, aatree.num_skew))
