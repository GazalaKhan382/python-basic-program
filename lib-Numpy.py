#Numpy
# Numpy is like list
# Locality of reference

# import numpy as np

# ls=np.array(4) #OD array
# lst=np.array([[7,9,7,5],[1,6,8,7]]) #2D Array
# lst1=np.array([[7,9,7,5],[1,6,8,7]]) #2D Array



# print(ls.ndim)
# print(lst.ndim)
# print(lst1.ndim)

# stk=[4,9,6,7]
# print(stk)


# import numpy as np
# lst=np.array([[7,9,7,5],[4,5,8,7]],ndmin=2) 
# print(lst)
# print(lst.shape)

import numpy as np
lst=np.array([5,6,4,7,1,2,3,8])

newLst=lst.reshape(4,2)
print(newLst)

# print(lst.shape)