import sys
import pingsweep

print('.....Welcome to Python Network Scanner.....')
print("1.Ping Sweep")

choice=int(input("Enter your choice:"))

match(choice):
    case 1:
        pingsweep.pingsweep(sys.argv[1])
