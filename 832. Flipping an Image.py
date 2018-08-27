class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        reversedL = []
        for x in A:
            reversedL.append(x[::-1])
        
        print(reversedL)
        for x in reversedL:
            for y in range(len(x)):
                if x[y] == 1:
                    x[y] = 0
                else:
                    x[y] = 1
        
        return (reversedL)
