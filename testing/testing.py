# between list and tuple

# List
import sys

y = ["hello", 123, "chill", 23.08]

x = ("Hello", 222, "what", 23.88)

print(y)
print(x)

# y[1] = "hello again"
# z = x
# z[0] = 123


print("Changing value ....")
print(sys.getsizeof(y))
print(sys.getsizeof(x))
