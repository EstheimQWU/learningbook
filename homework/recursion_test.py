import random
import os

# print(random.randint(1, 100))
# os.remove(r'C:/github/learningbook/homework/recursion_test.py')

def recursion_test(x):
    if x > -1:
        x = x + 1
        print(x)
        recursion_test(x)
    pass

def seek_res():
    print(1 or 3)
    print(1 and 3)
    print(0 and 2 and 1)
    print(0 and 2 or 1)
    print(0 and 2 or 1 or 4)
    print(0 or False and 1)


if __name__ == '__main__':
    # x = 0
    # recursion_test(0)
    # seek_res()
    print("\n".join("\t".join(["%s*%s=%s"%(y, x, x*y) for y in range(1, x+1)]) for x in range(1, 10)))
    print('\n'.join('\t'.join(["%s*%s=%s"%(y, x, x*y) for y in range(1, x+1)]) for x in range(1, 10)))
    pass

