# Example 1: Breaking out from a deeply nested loop:
from goto import goto, label
for i in range(1, 10):
    for j in range(1, 20):
        for k in range(1, 30):
            print i, j, k
            if k == 3:
                goto .end
label .end
print "Finished\n"