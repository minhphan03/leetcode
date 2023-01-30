class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits[len(digits)-1] += 1
        i = len(digits)-1
        while i > 0 and digits[i] >= 10:
            digits[i] -=10
            digits[i-1] +=1
            i -=1
       
        if i == 0 and digits[i] >=10:
            digits[0] -= 10
            digits.insert(0, 1)

        return digits
