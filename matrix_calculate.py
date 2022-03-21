import numpy as np

class Solution:
    def __init__(self,matrix):
        self.data=matrix

    def calculate_det(self,matrix):
        det = np.linalg.det(np.array(eval(self.data)))
        print(det)
    
    def calculate_trace(self,matrix):
        trace = np.trace(np.array(eval(self.data)))
        print(trace)

    def calculate_rank(self,matrix):
        rank = np.linalg.matrix_rank(np.array(eval(self.data)))
        print(rank)

while 1:
    print("For example:[[a,b],[c,d]]")
    a = input("input a matrix:")

    mx_result = Solution(a)
    i = input("det,trace or rank?:") 
    if i == "det":
        mx_result.calculate_det(a)
    elif i == "trace": mx_result.calculate_trace(a)
    elif i == "rank": mx_result.calculate_rank(a)