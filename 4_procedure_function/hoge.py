import numpy as np

arr = np.array([0,1,2,3,4])
if ((arr == 0).any()):
    print("arr is included 0")
else:
    print("arr is not included 0")
if ((arr == 0).all()):
    print("arr all index is 0")
else:
    print("arr not all index is 0")

arr2 = np.array([1,2,3,4])
if ((arr2 == 0).any()):
    print("arr2 is included 0")
else:
    print("arr2 is not included 0")
