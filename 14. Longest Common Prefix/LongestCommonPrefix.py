class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs==[]:
            return ""
        prefix = strs[0] #the prefix is now the first string 

        for string in strs[1:]:
            while string[:len(prefix)] != prefix:
                prefix=prefix[:-1]
            if not prefix: 
                return ""
        return prefix 

        
        

        """
        Start with the first string in the array as the initial prefix.
        Compare this prefix with the next string in the array, updating the prefix to the longest common prefix between the two.
        Continue this process with each string in the array. Whenever the prefix becomes an empty string, you can break out of the loop since it won't get any longer.
        Return the prefix that survives after comparing with all strings.
        """