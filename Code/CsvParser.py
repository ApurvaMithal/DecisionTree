# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 16:03:13 2018

@author: Apurva Mithal
         axm174531
"""

import csv

class CsvParser:
    """
    Parses a csv file. Records all attribute names, the attribute values for each data point,
    column index of each attribute (except target attribute), the row index for each data point,
    the target values corresponding to each data point 
    
     Class Variables:
		attributeNames  : A list of all the attribute names.
       attributes      : A list of column indices of each attribute (except target attribute).
       examples        : A list of the row indices for each data point
		 targetAttribute : A vector of the target values corresponding to each data point.
       data            : A matrix to store the attribute values for each data point.
	  
    """
    
    def __init__(self, filename):
        
        self.data = []
        with open(filename) as csvfile:
            readercsv = csv.reader(csvfile, delimiter = ',')
            counter = 0
            for datapoint in readercsv:
                if counter == 0:
                    self.attributeNames = datapoint[:-1]
                    counter = counter + 1
                else:
                    self.data.append([i for i in datapoint])
                    #print(self.data)
                    
        self.attributes = range(len(self.attributeNames))
        #print(self.attributeNames)
        
        self.examples = range(len(self.data))
        #print(self.examples)
        
        self.targetAttribute = [datapoint[-1] for datapoint in self.data]
        #print(self.targetAttribute)
              
			    