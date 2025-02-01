class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        arr1 = [*word1]
        arr2 = [*word2]
        finalarr = []
        if len(arr1) > len(arr2):
            for i in range(0,len(arr2)):
                finalarr.append(arr1[i])
                finalarr.append(arr2[i])
            finalarr.extend(arr1[int(len(arr1)-len(arr2)):])
            return "".join(finalarr)
        elif len(arr1) < len(arr2):
            for i in range(0,len(arr1)):
                finalarr.append(arr1[i])
                finalarr.append(arr2[i])
            finalarr.extend(arr2[int(len(arr2)-len(arr1)):])
            return "".join(finalarr)    
        else:
            for i in range(0,len(arr1)):
                finalarr.append(arr1[i])
                finalarr.append(arr2[i])            
            return "".join(finalarr) 
        
print(Solution().mergeAlternately("abcd","pq"))

array = ["a","b","c","d"]