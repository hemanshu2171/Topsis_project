import pandas as pd
import math
import numpy as np
import warnings

class Topsis:
    df = 0
    weighs = []
    impacts = []
    headers = 0
    rows = 0
    sqrd_sum = []
    v_plus_dict = {}
    v_min_dict = {}
    perf_dict = {}
    rank = []
    def __init__ (self, dataframe, weighs, criteria):
        self.df = dataframe
        self.weighs = np.copy(weighs)
        self.impacts = (criteria)
        self.headers = (dataframe.columns)
        self.rows = len(dataframe.index)
    '''
        Reducing the decimal points in the dataframe of the features
    '''
    def cleaning(self):
        arr = self.df.iloc[:,1:]
        for i in range(len(self.headers)-1):
            val_arr = arr.iloc[:,i]
            val_arr = [round(x,4) for x in val_arr]
            self.df.iloc[:,i+1] = val_arr
    '''
        Step1: Find Root of sum of squares of every column
    '''
    def step1 (self):
        arr = self.df.iloc[:,1:]
        for i in range(len(self.headers)-1):
            val_arr = arr.iloc[:,i]
            self.sqrd_sum.append(math.sqrt(sum(val_arr*val_arr)))
    '''
        Step2: Find Normalized Decision Matrix and calculating weight * Normalized performance value
    '''
    def step2(self):
        arr = self.df.iloc[:,1:]
        for i in range(len(self.headers)-1):
            val_arr = arr.iloc[:,i]
            val_arr = [x / self.sqrd_sum[i] for x in val_arr]
            val_arr = [x * self.weighs[i] for x in val_arr]
            self.df.iloc[:,i+1] = val_arr
    '''
        Step3: calculate v_plus and v_minus values according to the impacts
    '''
    def step3(self):
        arr = self.df.iloc[:,1:]
        for i in range(len(self.headers)-1):
            val_arr = arr.iloc[:,i]
            if(self.impacts[i]==True):
                self.v_min_dict[i] = min(val_arr)
                self.v_plus_dict[i] = max(val_arr)
            else:                
                self.v_min_dict[i] = max(val_arr)
                self.v_plus_dict[i] = min(val_arr)
    '''
        Step4: calculating eucledian distance
    '''
    def step4(self):
        arr = self.df.iloc[:,1:]
        s_minus_dict = 0
        s_plus_dict = 0
        for i in range(self.rows):
            val_arr = arr.iloc[i,1:]
            val_arr = [(x - self.v_min_dict[ind]) for ind,x in enumerate(val_arr)]
            val_arr = [x *x for x in val_arr]
            s_minus_dict = math.sqrt(sum(val_arr))
            val_arr = self.df.iloc[i,1:]
            val_arr = [(x- self.v_plus_dict[ind])  for ind,x in enumerate(val_arr)]
            val_arr = [x *x for x in val_arr]
            s_plus_dict = math.sqrt(sum(val_arr))
            self.perf_dict[i] = s_minus_dict/(s_minus_dict+s_plus_dict)
    '''
        Step5: calculating rank according to the perf_dict
    '''
    def step5(self):
        self.perf_list = list(self.perf_dict.values())
        for perf in (self.perf_list):
            self.rank.append(sorted(self.perf_list,reverse=True).index(perf)+1)
        self.perf_list = [round(x,4) for x in self.perf_list]
        self.cleaning()
    '''
        Final output result to be sent to the user
    '''
    def calc(self):
        print("------------------------------------------------------------------")
        print("Initiating Step1 of finding root of sum of squares of every column")
        print("-----------------------------------------------------------")
        self.step1()
        print("------------------------------------------------------------------")
        print('Initiating Step2 of finding Normalized Decision Matrix and calculating weight * Normalized performance value')
        print("------------------------------------------------------------------")
        self.step2()
        print("------------------------------------------------------------------")
        print("Initiating step3 of finding V_plus and V_minus values of each column")
        print("------------------------------------------------------------------")
        self.step3()
        print("------------------------------------------------------------------")
        print("Initiating step4 of calculating eucledian distance and performance matrix for each feature")
        print("------------------------------------------------------------------")
        self.step4()
        print("------------------------------------------------------------------")
        print("Initiating step5 of calculating rank for each feature")
        self.step5()
        print("\n--------------------------THE END---------------------------------")
        return self.rank,self.perf_list