# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 22:58:08 2018

@author: Apurva Mithal
         axm174531
"""

from CsvParser import CsvParser

class Validator:
    
    def __init__(self, filename):
        parserCsv = CsvParser(filename)
        self.targetAttribute = parserCsv.targetAttribute
        self.data = parserCsv.data
        
    def calculateAccuracy(self, root):
        """
        Returns the accuracy prediction for the trained decision tree.
		"""
        if root == None or len(self.data) == 0:
            return 0
        
        noOfCorrectOutputs = 0
        for i in range(len(self.data)):
            if int(self.getValuePredicted(root, self.data[i])) == int(self.targetAttribute[i]):
                noOfCorrectOutputs = noOfCorrectOutputs + 1        
        self.accuracy = float(1.0 * noOfCorrectOutputs / len(self.data))
        return(self.accuracy)
        
    def getValuePredicted(self, root, datapoint):
        """
        Returns the predicted target value based on the modeled decision tree
		"""
        
        
        if int(root.val) == -1:
            return int(root.majorityTargetValue)
        
        if int(datapoint[root.val]) == 0:
            return self.getValuePredicted(root.left, datapoint)
        else:
            return self.getValuePredicted(root.right, datapoint)
        
    def printAccuracy(self):
        """Display the accuracy of the modeled decision tree.
		"""
        print ("The predicted accuracy is  {0:.2f}%".format((self.accuracy) * 100))
        


        
    
    
    