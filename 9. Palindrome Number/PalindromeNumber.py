class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        if x < 0:
            return False
        if x == 0:
            return True

        rev = 0
        temp = x
        while temp > 0:
            digit = temp % 10
            rev = rev * 10 + digit
            temp //= 10

        return rev == x

        """
        If the number is negative, it's not a palindrome, so return False.
        If the number is zero, it's a palindrome, so return True.
        You create a reversed version of the number by iteratively taking the last digit of temp and adding it to rev while scaling rev up by 10 each time to shift the digits correctly.
        Finally, you compare the reversed number rev with the original number x to check if they are the same.
        """