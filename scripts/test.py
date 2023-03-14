import os

ValueA = os.environ['INPUT_STORE']
ValueB = os.environ['INPUT_STORE']

attach = ValueA+ValueB


print("Values of A and B:", ValueA,ValueB)
print("Attaching A and B", attach)