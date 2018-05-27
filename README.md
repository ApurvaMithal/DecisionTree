# DecisionTree

Apurva Mithal
axm174531
CS 6375.001
			                                        
-	Implemented the Decision tree based on the following two heuristics for choosing the best attribute:
	-	Information Gain Heuristic
	-	Variance Impurity Heuristic

-	System Details
	-	Operating System: Windows
	-	Python: 3.6

-	File Names:
	-	Main.py – Start point of the code. Run the code using this file.
	-	CsvParser.py – Parses the Csv file
	-	DecisionTree.py – Implements the decision tree using Information Gain heuristics
	-	DecisionTreeVarianceImp.py– Implements the decision tree using Variance    Impurity heuristics.
	-	pruneTree.py – Implements logic for pruning of the tree.
	-	treeNode.py – Defines tree node structure
	-	validator.py – Implements the calculation of accuracy 

-	How to run the code
	-	Install Python 3.6
	-	Add the python.exe file to the environment variables.
	-	Create a folder in the system with the code files in it. (eg. D:\ML\hw1)
	-	Add the training, validation and test files to the same path as above. (D:\ML\hw1)
	-	Open the command prompt in Windows.
	-	Go to the path where the python files are present. (D:\ML\hw1)
	-	Run by giving the following command:
		-	python Main.py <L> <K> <training_filename.csv> < validation_filename.csv > < test_filename.csv >   yes/no
		-	eg. 
			python Main.py 5 5 training_set.csv validation_set.csv test_set.csv yes
