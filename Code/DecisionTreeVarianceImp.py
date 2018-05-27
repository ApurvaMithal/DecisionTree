# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 20:19:56 2018

@author: Apurva Mithal
         axm174531
"""

from CsvParser import CsvParser
from treeNode import TreeNode

        
class DecisionTreeVarianceImp:
    
    def __init__(self, filename):
        parserCsv = CsvParser(filename)
        
        self.data = parserCsv.data
        self.attributeNames = parserCsv.attributeNames
        self.examples = parserCsv.examples
        self.attributes = parserCsv.attributes
        self.targetAttribute = parserCsv.targetAttribute
        
        # Build a decision tree using Variance Impurity Heuristic algorithm.
        self.root = self.VarianceImpurityHeur(self.examples, self.targetAttribute, self.attributes)
        
    def VarianceImpurityHeur(self, examples, targetAttribute, attributes):
        
        if (len(examples) == 0):
            return None
        
        root = TreeNode(-1)
        
        # The variance impurity calculation of the datapoints
        varImp = self.getVarImpurity(examples, targetAttribute)
        
        # majorityTargetValue of the root node stores the majority value of the targetAttribute
        root.majorityTargetValue = self.getMostCommonValue(targetAttribute)
        
        # If variance impurity is 0, return root node
		 # If no attributes, return root node
        if varImp ==  0 or len(attributes) == 0:
            return root
        
        else:
            selectedAttribute = self.chooseSelectedAttribute(examples, targetAttribute, attributes, varImp)
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
            root.left = self.VarianceImpurityHeur(splitMatrix[0][0], splitMatrix[0][1], attributes)
            root.right = self.VarianceImpurityHeur(splitMatrix[1][0], splitMatrix[1][1], attributes)
            
            return root
        
    def getVarImpurity(self, examples, targetAttribute):
        
        """
        returns variance impurity value
        """
        
        noOfRows = len(examples)
        noOfPos = 0
        for i in range(len(examples)):
            if int(targetAttribute[i]) == 1:
                noOfPos = noOfPos + 1
        
        ratioOfpos = 1.0 * noOfPos/noOfRows
        ratioOfneg = 1 - ratioOfpos
        
        if ratioOfpos == 0 or ratioOfneg == 0:
            return 0
        
        # return variance Impurity
        return ratioOfpos * ratioOfneg
    
        
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
            
    def chooseSelectedAttribute(self, examples, targetAttribute, attributes, varImp):
        
        """.
		  returns the column index of the best attribute according to variance impurity heuristic
        """
        
        maxgainVarImp = -1
        selectedAttribute = -1
        
        for attr in attributes:
            splitDetails = self.getsplitDetails(examples, attr)
            
            if splitDetails > 0:
                gainVarImp = self.getVarImpgain(examples, targetAttribute, varImp, attr)
                if gainVarImp > maxgainVarImp:
                    maxgainVarImp = gainVarImp
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
        
        return 1
    
    def getVarImpgain(self, examples, targetAttribute, varImp, attr):
        
        """returns the calculated gain corresponding to given attribute
		 """

        noOfRows = len(examples)
        
       #  Calculate the varImp for each  whose attribute value {0,1}
        splitMatrix = self.split(examples, targetAttribute, attr)
        varImp_v0 = self.getVarImpurity(splitMatrix[0][0], splitMatrix[0][1])
        varImp_v1 = self.getVarImpurity(splitMatrix[1][0], splitMatrix[1][1])
        
        percentage_v0 = 1.0 * len(splitMatrix[0][0]) / noOfRows
        percentage_v1 = 1 - percentage_v0
        
        gainVarImp = varImp - (percentage_v0 * varImp_v0) - (percentage_v1 * varImp_v1)
        
        return gainVarImp
    
    
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
