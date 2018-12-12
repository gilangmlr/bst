from bst import BinarySearchTree
from aatree import AATree
import time

if __name__ == '__main__':
  upper_exponent = 5

  print('------aatree - 1 hlink------')
  start_power = 2
  for j in range(start_power, start_power + upper_exponent):
    start_time = time.time()

    n = 10**j
    aatree = AATree(0)

    for i in range(1, n):
      # print('inserting %d' % (i))
      aatree.insert(i)
    
    insertion_time = time.time() - start_time
    
    start_time = time.time()

    for i in range(0, n):
      aatree.search(i)
    
    searching_time = time.time() - start_time

    print("n: %d, insertion: %.4f s, split: %d, skew: %d, searching: %.4f s, compare: %d" % (n, insertion_time, aatree.num_split, aatree.num_skew, searching_time, aatree.search_comparison))
  
  print('------aatree - 2 hlink------')
  start_power = 2
  for j in range(start_power, start_power + upper_exponent):
    start_time = time.time()

    n = 10**j
    aatree = AATree(0, None, 2)

    for i in range(1, n):
      # print('inserting %d' % (i))
      aatree.insert(i)

    insertion_time = time.time() - start_time

    start_time = time.time()

    for i in range(0, n):
      aatree.search(i)
    
    searching_time = time.time() - start_time

    print("n: %d, insertion: %.4f s, split: %d, skew: %d, searching: %.4f s, compare: %d" % (n, insertion_time, aatree.num_split, aatree.num_skew, searching_time, aatree.search_comparison))

  # print('---bst---')
  # start_power = 2
  # for j in range(start_power, start_power + upper_exponent):
  #   start_time = time.time()

  #   n = 10**j
  #   bst = BinarySearchTree(0)

  #   for i in range(1, n):
  #     bst.insert(i)

  #   print("n = %d, running time = %.4f seconds " % (n, time.time() - start_time))
