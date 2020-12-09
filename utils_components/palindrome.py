class Palindrome:
    @staticmethod
    def longest_palindrome(string: str) -> str:
        """Return the longest palindrome in a string
        Args:
            string (str): string
        Return:
            str: The longest palindrome in the string
        """

        def expend(string, left, right):
            """Expend from center"""
            if string[left-1:right+2] == string[left-1:right+2][::-1] and (left > 0 and right < len(string)):
                return expend(string, left - 1, right + 1)
            else:
                return string[left:right+1]
            
        longest = string[0] if len(string) > 0 else ""
        for i in range(len(string)-1):
            #odd palindrome
            odd_palindrome = expend(string, i, i)
            #even palindrome
            even_palindrome = expend(string, i, i+1) if string[i] == string[i+1] else ''
            # Check if the two palindrome found from their center i, i+1 are longer than the current longest one
            if len(odd_palindrome) > len(longest):
                longest = odd_palindrome
            if len(even_palindrome) > len(longest):
                longest = even_palindrome

        return longest