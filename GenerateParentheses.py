class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        answer = []
        
        def backtrack(string, parentheses, n):
            if string.count("(") == n:
                for time in range(n - string.count(")")):
                    string += ")"
                answer.append(string)
                return
            
            for parent in parentheses:
                if string.count(")") == string.count("(") and parent == ")":
                    return
                backtrack(string + parent, parentheses, n)
                
        backtrack("", ["(", ")"], n)
        return answer