# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 20:03:18 2018

@author: Apurva Mithal
         axm174531
"""

class TreeNode:
    
    
    """Each node of the decision tree is of TreeNode type.
	Class Variables:
       left  : left subtree.
       right : right subtree.
	    val   : Column index of the selected attribute in the current node. 
                Leaf Nodes have value of -1
	    majorityTargetValue : The majority of target value. Leaf Nodes have majorityTargetValue of -1
	    
     """
     
    def __init__(self, val, left = None, right = None):
        
        self.majorityTargetValue = -1
        self.val = val
        self.left = left
        self.right = right
        