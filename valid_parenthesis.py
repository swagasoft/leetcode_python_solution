

def validParenthesis(st: str):

   
 
    stack, pchar = [], {"(": ")", "{": "}", "[": "]"}

    for parenthesis in st:
        if parenthesis in pchar:
            stack.append(parenthesis)
        elif  pchar[stack.pop()] !=  parenthesis:
            return False

    return len(stack) == 0



my_str = '[()]'
# print(validParenthesis(my_str))
print(validParenthesis('()[{)}'))


    