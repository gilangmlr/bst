from bst import BinarySearchTree
from aatree import AATree
import time

if __name__ == '__main__':
  upper_exponent = 4

  print('------aatree------')
  start_power = 2
  for j in range(start_power, start_power + upper_exponent):
    start_time = time.time()

    n = 10**j
    aatree = AATree(0)

    for i in range(1, n):
      # print('inserting %d' % (i))
      aatree.insert(i)

    print("n = %d, running time = %.4f seconds " % (n, time.time() - start_time))
    # aatree.traverse()

  print('---bst---')
  start_power = 2
  for j in range(start_power, start_power + upper_exponent):
    start_time = time.time()

    n = 10**j
    bst = BinarySearchTree(0)

    for i in range(1, n):
      bst.insert(i)

    print("n = %d, running time = %.4f seconds " % (n, time.time() - start_time))
