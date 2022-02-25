# Topsis_project
This is the package for python to implement topsis method for mcda
Functions Provided:
1. __init__(dataframe->dataframe, weights->list, impacts->list): Constructor for the topsis class.
2. Step1(): Calcuates the root of sum of square of the features.
3. Step2(): Finds Normalized Decision matrix by dividing the feature's values by the value calculated in step1() and then multiplying that value with weights list.
4. Step3(): Calculate V_plus and V_minus array according to the impacts. Impacts value must be boolean (True/False).
5. Step4(): Calculating Eucledian distance for the items and the performance score.
6. Step5(): Calculating Rank of the items on the base of the performance score.
