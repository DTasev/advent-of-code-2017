import numpy as np
# 147  142  133  122   59
# 304    5    4    2   57
# 330   10    1    1   54
# 351   11   23   25   26
# 362  747  806  880  931


class MyTup:
    def __init__(self, data):
        self.data = data

    def __sub__(self, rhs):
        self.data[0] -= rhs[0]
        self.data[1] -= rhs[1]

    def __add__(self, rhs):
        self.data[0] += rhs[0]
        self.data[1] += rhs[1]

    def __mul__(self, rhs):
        self.data[0] *= rhs[0]
        self.data[1] *= rhs[1]

    def __getitem__(self, i):
        return self.data[i]

    def rot90anticw(self):
        if self.data[1]:  # going left
            # go up
            self.data[0], self.data[1] = 1, 0
        elif self.data[0]:  # going up
            # go right
            self.data[0], self.data[1] = 0, -1
        elif self.data[0]:  # going up
            # go right
            self.data[0], self.data[1] = 0, -1
        elif self.data[0]:  # going up
            # go right
            self.data[0], self.data[1] = 0, -1


y = [1, 1, 2, 4, 5, 10, 11, 23, 25, 26, 54, 57, 59, 122, 133, 142, 147, 304, 330, 351, 362, 747, 806, 880, 931]

n = 3
x = np.arange(n**2)
x = x.reshape(n, n)
x[:] = 0
print(x)

wraps = 1

# start in the middle
start = MyTup(n - 1 // 2, n - 1 // 2)
# move left
velocity = MyTup(0, 1)
for i in range(wraps):
