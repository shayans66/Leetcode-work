class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open = ['(','[','{']
        close = [')',']','}']
        for ch in s:
            if ch in open:
                stack.append(ch)
            elif ch in close:
                if stack and open.index(stack.pop()) == close.index(ch):
                    print('ffffhi')
                    pass
                else:
                    print('hfi')
                    return False
            else: 
                print('hi')
                return False
        return not stack