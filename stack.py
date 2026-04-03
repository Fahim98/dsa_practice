# 1 ---> STACK
#stack is a linear data structure that follows LIFO principle
#stack can be implemented using list in python

stack=[]

# lets push some elements onto the stack
stack.append('a')
stack.append('b')
stack.append('c')

print('Initial stack: ')
print(stack)

#lets pop the elements now; it will follow LIFO principle meaning the most recently pushed element will be the first to get removed
print('First popped element: ')
print(stack.pop())
#lets pop the remaining elements
print('the elements popped later: ')
print(stack.pop())
print(stack.pop())

print('stack after all elements popped: ')
print(stack)
