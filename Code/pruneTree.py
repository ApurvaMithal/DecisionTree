# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 20:06:04 2018

@author: Apurva Mithal
         axm174531
"""

from DecisionTree import DecisionTree
from validator import Validator
import random
import copy
from collections import deque

class PruneTree:
    
    def pruneTree(self, decisionTree, L, K, validation_set):
        """Post prune the decision tree using two parameters L, K
        
		Function Arguments:
		    L              : The number of iterations of post pruning.
		    K              : The seed to generate a random number of nodes to be pruned.
		Returns:
		        Dbest : The post pruned tree.
		"""
        
        Dbest = decisionTree.root
        
        # Create a validator object against the validation set to decide if the pruned tree has higher accuracy 
        # than the original tree
        validatorObj = Validator(validation_set)
        
        for i in range(0, L):
            Dcurr = copy.deepcopy(Dbest)
            
            # A random number generator between 1 and K.
            M = random.randint(1, K)
            
            for j in range(0, M):
                
                nonLeafNodes = self.bfsOrderedNodes(Dcurr)
                N = len(nonLeafNodes) - 1
                
                if N <= 0:
                    return Dbest
                
                # Let P be a random number generated between 1 and N.
                P = random.randint(1, N)
                            
                nonLeafNodes[P].val = -1
                nonLeafNodes[P].left = None
                nonLeafNodes[P].right = None
            
            accurracyDold = validatorObj.calculateAccuracy(Dbest)
            accurracyDnew = validatorObj.calculateAccuracy(Dcurr)
        
            # If pruned tree accuracy is more than the previous tree, 
            if accurracyDnew >= accurracyDold:
                Dbest = Dcurr
                
        
        decisionTree.root = Dbest
        return Dbest
    
    def bfsOrderedNodes(decisionTree, root):
        """ returns arr[] --- a list of bfsOrderedNodesed non-leaf nodes .
		
		"""
        
        arr = []
        
        if root == None or int(root.val) == -1:
            return arr
        
        # bfsOrderedNodes using BFS 
        queue = deque([root])
        while len(queue) > 0:
            curr  = queue.popleft()
            arr.append(curr)
            if curr.left != None and curr.left.val != -1:
                queue.append(curr.left)
            if curr.right != None and curr.right.val != -1:
                queue.append(curr.right)
                
        # Return the bfsOrderedNodesed non-leaf nodes        
        return arr
    