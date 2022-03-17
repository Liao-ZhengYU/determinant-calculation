import numpy as np
while 1:
    class Solution:
        def __init__(self,matrix):
            self.data=matrix
        def calculate(self,matrix):
            det = np.linalg.det(np.array(eval(self.data)))
            print(det)
    print("例:[[1,1],[2,1]]")
    a = input("请输入矩阵：")
    mx_result = Solution(a)
    mx_result.calculate(a)