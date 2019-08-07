#LeetCode中第682题
class Solution:
    def calPoints(self,ops) :
        res = []
        sum =0
        res.append(ops[0])
        for i in range(len(ops)):
            if ops[i] == '+':
                res.append(int(res[-1])+int(res[-2]))
                sum = sum+int(res[-1])
            elif ops[i] == 'D':
                res.append(int(res[-1])*2)
                sum = sum+int(res[-1])
            elif ops[i] == 'C':
                sum = sum-int(res[-1])
                res.pop()#移除队尾元素
            else:
                res.append(ops[i])
                sum=sum+int(res[-1])
        return sum