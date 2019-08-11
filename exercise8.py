#1021.删除最外层括号
class Solution:
    def removeOuterParentheses(self, S: str) -> str:
# 思路：记录每个外层括号的下标值，之后在重构括号字符串的时候去掉外层括号
        l = 0
        res =''
        for i in S:
            if i == '(':
                #记录左括号
                l = l+1
                if l > 1:
                    res =res+i
            else:
                if l > 1:
                    res = res+i
                l = l-1#记录右括号
        return res