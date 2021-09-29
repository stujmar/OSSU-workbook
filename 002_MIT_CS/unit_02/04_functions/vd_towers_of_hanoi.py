# Classic problem of the Towers of Hanoi.
# Can use a recurisive solution, but a more elegant solution is to use a stack.
# The stack is a LIFO (Last In First Out) data structure.

stack_one = []
stack_two = []
stack_three = []

disc_one = 1
disc_two = 2
disc_three = 3
disc_four = 4

stack_one.append(disc_four)
stack_one.append(disc_three)
stack_one.append(disc_two)
stack_one.append(disc_one)

print(stack_one)

def print_stack(stack):
    for i in range(len(stack)):
        print(stack[i])

# i doughnut understand.
def Towers(n, from_stack, to_stack, aux_stack):
    if n == 1:
        print("Move disc %d from %s to %s" % (n, from_stack, to_stack))
        return
    Towers(n-1, from_stack, aux_stack, to_stack)
    print("Move disc %d from %s to %s" % (n, from_stack, to_stack))
    Towers(n-1, aux_stack, to_stack, from_stack)