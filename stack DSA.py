stack = []

#push
stack.append ('A')
stack.append ('B')
stack.append ('C')
stack.append ('D')
stack.append ('E')
stack.append ('F')
stack.append ('G')
print("Stack:", stack)

#pop
element = stack.pop()
print("Pop:", element)

#peak
top_element = stack[-1]
print("Peak:", top_element)

#is empty
isempty = not bool (stack)
print("isempty:", isempty)

#size
size = len(stack)
print("Size:", size)
