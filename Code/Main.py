# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 16:38:57 2018

@author: Apurva Mithal
         axm174531
"""

import sys
from DecisionTree import DecisionTree
from validator import Validator
from pruneTree import PruneTree
from DecisionTreeVarianceImp import DecisionTreeVarianceImp

def main():
    
    if len(sys.argv) < 7:
        print("There should be 6 arguments -- L K train.csv validate.csv test.csv yes/no")
        sys.exit(1)
    
    L = int(sys.argv[1])
    K = int(sys.argv[2])
    
    
    training_set = sys.argv[3]
    validation_set = sys.argv[4]
    test_set =  sys.argv[5]
    to_print = sys.argv[6]
    
    decisionTree = DecisionTree(training_set)
    if to_print == "yes":
        print("Before Pruning: DecisionTree based on information Gain Heuristics")
        print (decisionTree)
    
    validatorObj = Validator(test_set)
    print("Before Pruning: Accuracy of Decision Tree based on information Gain Heuristics")
    validatorObj.calculateAccuracy(decisionTree.root)
    validatorObj.printAccuracy()
    
    
    decisionTreeVarImp = DecisionTreeVarianceImp(training_set)
    if to_print == "yes":
        print("Before Pruning: DecisionTree based on Variance Impurity Heuristics")
        print (decisionTreeVarImp)
        
    validatorVar = Validator(test_set)
    print("Before Pruning: Accuracy of DecisionTree based on Variance Impurity Heuristics")
    validatorVar.calculateAccuracy(decisionTreeVarImp.root)
    validatorVar.printAccuracy()
    
    # Post pruning starts
    prune = PruneTree()
    
    
    prune.pruneTree(decisionTree,L, K, validation_set)
    if to_print == "yes":
        print("After Pruning: DecisionTree based on information Gain Heuristics")
        print (decisionTree)
        
    validatorObj.calculateAccuracy(decisionTree.root)
    print("After Pruning: Accuracy of DecisionTree based on information Gain Heuristics")
    validatorObj.printAccuracy()
    
    prune = PruneTree()
    
    print("After Pruning: DecisionTree based on Variance Impurity Heuristics")
    prune.pruneTree(decisionTreeVarImp,L, K, validation_set)
    if to_print == "yes":
        print (decisionTreeVarImp)  
        
    validatorObj.calculateAccuracy(decisionTreeVarImp.root)
    print("After Pruning: Accuracy of DecisionTree based on Variance Impurity Heuristics")
    validatorObj.printAccuracy()
    
if __name__ == '__main__':
    main()