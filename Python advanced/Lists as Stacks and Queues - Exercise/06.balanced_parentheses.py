def is_balanced(expression):

    stack = []
    
    brackets_map = {')': '(', '}': '{', ']': '['}
    

    for char in expression:
        if char in '({[':
            stack.append(char)
        elif char in ')}]':

            if not stack:
                return "NO"
            
            top = stack.pop()
            
            if top != brackets_map[char]:
                return "NO"
    
    if not stack:
        return "YES"
    else:
        return "NO"

expression = input().strip()
print(is_balanced(expression))