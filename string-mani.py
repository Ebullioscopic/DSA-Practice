# class Solution:
#     def gcdOfStrings(self, str1: str, str2: str) -> str:
#         def goStraight(bigString:str,subString:str):
#             if subString in bigString:
#                 return subString
#             else:
#                 if len(subString) > 1:
#                     subString = subString.removesuffix(subString[-1])
#                     return goStraight(bigString,subString)
#                 else:
#                     return ""
#         def goReverse(bigString:str,subString:str):
#             if subString in bigString:
#                 return subString
#             else:
#                 if len(subString) > 1:
#                     subString = subString.removeprefix(subString[0])
#                     return goReverse(bigString,subString)
#                 else:
#                     return ""
#         if goStraight(str1,str2) != "":
#             return goStraight(str1,str2)
#         if goReverse(str1,str2) != "":
#             return goReverse(str1,str2) 
#         if goStraight(str2,str1) != "":
#             return goStraight(str2,str1)
#         if goReverse(str2,str1) != "":
#             return goReverse(str2,str1) 
#         return ""

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def check(a, b):
            c = ""
            while len(c) < len(b):
                c += a
            return c == b

        for i in range(min(len(str1), len(str2)), 0, -1):
            t = str1[:i]
            if check(t, str1) and check(t, str2):
                return t
        return ''

