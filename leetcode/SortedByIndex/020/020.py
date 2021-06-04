class Solution:
    def isValid(self, s: str) -> bool:
        # 用栈
        m = list()
        # if len(s) % 2 != 0:
        #     return False
        for item in s:
            if item == '}':
                if m != []:
                    if m[-1] == '{':
                        m.pop()
                        continue
                return False
            elif item == ')':
                if m != []:
                    if m[-1] == '(':
                        m.pop()
                        continue
                return False
            elif item == ']':
                if m != []:
                    if m[-1] == '[':
                        m.pop()
                        continue
                return False
            else:
                # 压栈
                m.append(item)
        if m == []:
            return True
        else:
            return False