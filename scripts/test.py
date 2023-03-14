import os

ValueA = os.environ['INPUT_STORE']
ValueB = os.environ['INPUT_STORE']
int(ValueA)
int(ValueB)


multiply = ValueA*ValueB


print("Values of A and B:", ValueA,ValueB)
print("Multiply of A and B", multiply)