import sys

numof_args = len(sys.argv) - 1

if numof_args == 0:
    print("0 arguments.")
elif numof_args == 1:
    print("1 argument:")
else:
    print("{:d} arguments:".format(numof_args))

for i, arg in enumerate(sys.argv[1:], 1):
    print("{:d}: {}".format(i, arg))
if __name__ == "__main__":
    pass