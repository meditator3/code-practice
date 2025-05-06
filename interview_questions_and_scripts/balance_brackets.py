def scan_string(string):
    length = len(string)
    which_parenthesis = {')':'(', ']':'[', '}':'{'}
    open_parenthesis_kinds = {'(':0, '[':0, '{':0 }
    closed_parenthesis_kinds = {')':0, ']':0, '}':0 }
    mark = 0 # if all praenthesis occurances equated correctly
    first_closing = False
     # use parenthesis_kinds.values() or .keys() to iterate
    for i in range(0,length):
        if string[i] in open_parenthesis_kinds.keys():
            print(f"i={i}, {string[i]}")
            print(f"open with kind {string[i]} , value:{open_parenthesis_kinds[string[i]]}")
            open_parenthesis_kinds[string[i]] += 1
            last_opened = string[i] # handle last bracket not closed properly
            print(f" last bracket opened:{last_opened}")
       # id kind of each parenthesis-    
        if string[i] in which_parenthesis.keys():
            current_opened = which_parenthesis[string[i]]
            print(f"current opened:{current_opened}")
            
          # use value of which_parenthesis to reference open
       # add condition for starting with open paren.   
        if string[i] in closed_parenthesis_kinds.keys():
        # add condition if first closed equal to last opened kind(see example )
        # only for first time
            if first_closing == False and which_parenthesis[string[i]] != last_opened:
                return False
            first_closing = True
            print(string[i])
            print(i)
            print(f"open: {open_parenthesis_kinds[current_opened]}, closed {closed_parenthesis_kinds[string[i]]}")
            print(f"closed paren. ", closed_parenthesis_kinds[string[i]])
            if closed_parenthesis_kinds[string[i]] <= open_parenthesis_kinds[which_parenthesis[string[i]]]:
                print(f"added +1 to closed {string[i]}")
                closed_parenthesis_kinds[string[i]] += 1
    print(f"total open: {open_parenthesis_kinds['(']}, closed {closed_parenthesis_kinds[')']}") 
    print(f"total values:{open_parenthesis_kinds.values()}, {closed_parenthesis_kinds.values()}")  
    # need to compare each value inside dict - respectively   
    for key in which_parenthesis.keys():
        print(key)
        # extracting opposite parenthesis
        current_opened = which_parenthesis[key] # using reverse key value to reference opened
        if  closed_parenthesis_kinds[key] == open_parenthesis_kinds[current_opened]:
            print(f"opened {open_parenthesis_kinds[current_opened]} = closed {closed_parenthesis_kinds[key]}")
            mark +=1
            print(f"mark= {mark}")
    if mark == 3:
           return True    
    else:
        return False    
          



print(scan_string("{{[[(())]]}}"))
print("1-------------------------------------------------------")


print(scan_string("{[(])}"))
print("2-------------------------------------------------------")
print(scan_string("([{]})"))
print("3-------------------------------------------------------")
print(scan_string("([]){}"))
print("4-------------------------------------------------------")




# print(scan_string("([{]})")) example of FALSE, since [] isn't closed properly, and mixed with {}





# condition to return false if closed before the last opened brackets.
#           related to kinds of parenthesis- 
                # if ! same kind & last opened isn't closed with same.
                #   or, if last opened isn;t closed with same.. 
                #   how to know last? if first closing- is same as last opened.
                #   if not same > return false

# much better method:

# def isBalanced(s):
  
#     # Declare a stack to store the opening brackets
#     st = []
#     for i in range(len(s)):
        
#         # Check if the character is an opening bracket
#         if s[i] == '(' or s[i] == '{' or s[i] == '[':
#             st.append(s[i])
        
#         else:
#             # If it's a closing bracket, check if the stack is non-empty
#             # and if the top of the stack is a matching opening bracket
#             if st and ((st[-1] == '(' and s[i] == ')') or 
#                        (st[-1] == '{' and s[i] == '}') or
#                        (st[-1] == '[' and s[i] == ']')):

#                 # Pop the matching opening bracket
#                 st.pop()
#             else:
#                 # Unmatched closing bracket
#                 return False

#     # If stack is empty, return True (balanced), otherwise False
#     return not st


# if __name__ == "__main__":
# 	s = "{([])}"
# 	if isBalanced(s):
# 	    print("true")
# 	else:
# 		print("false")
