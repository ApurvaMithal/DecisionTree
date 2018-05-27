# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 16:42:26 2018

@author: Apurva Mithal
         axm174531
"""

import math

from CsvParser import CsvParser
from treeNode import TreeNode

        
class DecisionTree:
    
    def __init__(self, filename):
        parserCsv = CsvParser(filename)
        
        self.data = parserCsv.data
        self.attributeNames = parserCsv.attributeNames
        self.examples = parserCsv.examples
        self.attributes = parserCsv.attributes
        self.targetAttribute = parserCsv.targetAttribute
        
        # root of the decision tree build by ID3 heuristic
        self.root = self.Id3(self.examples, self.targetAttribute, self.attributes)
        
    def Id3(self, examples, targetAttribute, attributes):
        
        if (len(examples) == 0):
            return None
        
        root = TreeNode(-1)
        
        # The entropy calculation of the datapoints
        entropy = self.getEntropy(examples, targetAttribute)
        
        # majorityTargetValue of the root node stores the majority value of the targetAttribute
        root.majorityTargetValue = self.getMostCommonValue(targetAttribute)
        
        # If entropy is 0, return root node
		 # If no attributes, return root node
        if entropy ==  0 or len(attributes) == 0:
            return root
        
        else:
            selectedAttribute = self.chooseBestAttribute(examples, targetAttribute, attributes, entropy)
            
            if int(selectedAttribute) == -1:
                return root
            root.val = selectedAttribute
            
            
            # Can have one attribute considered only once in the tree path
            remainingAttributes = []
            for attr in attributes:
                if attr != selectedAttribute:
                    remainingAttributes.append(attr)
            
            attributes = remainingAttributes
            
            #splitMatrix[0][0] = indices of the datapoints with value  0
            #splitMatrix[1][0] = indices of the datapoints with value  1
            #splitMatrix[0][1] = target values corresponding to splitMatrix[0][0]
            #splitMatrix[1][1] = target values corresponding to splitMatrix[1][0]
            splitMatrix = self.split(examples, targetAttribute, selectedAttribute)
            root.left = self.Id3(splitMatrix[0][0], splitMatrix[0][1], attributes)
            root.right = self.Id3(splitMatrix[1][0], splitMatrix[1][1], attributes)
            
            return root
            
    def getEntropy(self, examples, targetAttribute):
        
        """
        Return entropy value
        """
        
        noOfRows = len(examples)
        
        noOfPos = 0
        for i in range(len(examples)):
            if int(targetAttribute[i]) == 1:
                noOfPos = noOfPos + 1
        
        ratioOfPos = 1.0 * noOfPos/noOfRows
        ratioOfNeg = 1 - ratioOfPos
        
        # if ratioOfPos == 0 or ratioOfNeg == 0, entropy = 0
        if ratioOfPos == 0 or ratioOfNeg == 0:
            return 0
        
        # returns entropy value
        return -(ratioOfPos * math.log(ratioOfPos,2) + ratioOfNeg * math.log(ratioOfNeg, 2))
    
    
    def getMostCommonValue(self, targetAttribute):
        
        """returns the most common target value.
		   
		  """

        if len(targetAttribute) == 1:
            return targetAttribute[0]
        
        noOfPos = 0
        for i in range(len(targetAttribute)):
            if int(targetAttribute[i]) == 1:
                noOfPos += 1
                 
        if noOfPos >= len(targetAttribute)/2:
            return 1
        else:
            return 0
    
    def chooseBestAttribute(self, examples, targetAttribute, attributes, entropy):
        
        
        """.
		  returns the column index of the best attribute according to information gain heuristic
         """      
        maxInfoGain = -1
        selectedAttribute = -1
        
        for attr in attributes:
            splitDetails = self.getsplitDetails(examples, attr)
            
            if splitDetails > 0:
                infoGain = self.getInfoGain(examples, targetAttribute, entropy, attr)
                if infoGain > maxInfoGain:
                    maxInfoGain = infoGain
                    selectedAttribute = attr
            
        
        return selectedAttribute
    
    
    
    def getsplitDetails(self, examples, attr):
        
        noOfRows = len(examples)
        count0 = 0
        
        for row in examples:
            if int(self.data[row][attr]) == 0:
                count0 = count0 + 1
        
        
        # Calculate the ratio of the number of data points with value 0 to total no of data points
        percentage_count0 = 1.0 * count0/noOfRows
        percentage_count1 = 1 - percentage_count0
        
        if percentage_count0 ==0 or percentage_count1 == 0:
            return 0
        
        return -(percentage_count0 * math.log(percentage_count0, 2) + percentage_count1 * math.log(percentage_count1, 2))
    
        
    def getInfoGain(self, examples, targetAttribute, entropy, attr):
        
        """returns the calculated infomation gain corresponding to given attribute
		 """

        noOfRows = len(examples)
        
        splitMatrix = self.split(examples, targetAttribute, attr)
        entropy0 = self.getEntropy(splitMatrix[0][0], splitMatrix[0][1])
        entropy1 = self.getEntropy(splitMatrix[1][0], splitMatrix[1][1])
        
        percentage0 = 1.0 * len(splitMatrix[0][0]) / noOfRows
        percentage1 = 1 - percentage0
        
        infoGain = entropy - (percentage0 * entropy0) - (percentage1 * entropy1)
        
        return infoGain
    
    def split(self, examples, targetAttribute, attribute):
        
        """ Split the training example by their values for a given attribute.
		Returns:
			example_v0  = indices of the datapoints with value  0
          example_v1  = indices of the datapoints with value  1
          target_v0 = target values corresponding to splitMatrix[0][0]
          target_v1 = target values corresponding to splitMatrix[1][0] 
     """
     
     
        example_v0 = []
        example_v1 = []
        target_v0 = []
        target_v1 = []
        
        for i in range(len(examples)):
            if int(self.data[examples[i]][attribute]) == 0:
                example_v0.append(examples[i])
                target_v0.append(targetAttribute[i])
            else:
                example_v1.append(examples[i])
                target_v1.append(targetAttribute[i])
                
        return [(example_v0, target_v0),(example_v1, target_v1)]
    
    
    def __str__ (self):
        
        """ used in printing the decision tree
		 """
        
        return self.treeToruleFormat(self.root, 0, self.attributeNames)
            
    
    def treeToruleFormat(self, root, level, attributeNames):
        
        """
        converts tree to rule format
		"""
        ruleFormat = ''
        
        if root == None:
            return ""
        
        if root.left == None and root.right == None:
            ruleFormat += str(root.majorityTargetValue) + '\n'
            return ruleFormat
        
        currentNode = attributeNames[root.val]
        
        barLevels = ''
        for i in range(0, level):
            barLevels += '| '
        
        ruleFormat += barLevels
        
        if root.left.left == None and root.left.right == None:
            ruleFormat +=  currentNode + "= 0 :"
        else:
            ruleFormat +=  currentNode + "= 0 :\n"
        
        ruleFormat += self.treeToruleFormat(root.left, level + 1, attributeNames)
        
        ruleFormat += barLevels
        
        if root.right.left == None and root.right.right == None:
            ruleFormat +=  currentNode + "= 1 :"
        else:
            ruleFormat +=  currentNode + "= 1 :\n"
        
        ruleFormat += self.treeToruleFormat(root.right, level + 1, attributeNames)
        
        return ruleFormat
    
        
        
        
    
    
        
       
        