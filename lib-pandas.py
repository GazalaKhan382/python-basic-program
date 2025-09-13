# import pandas as pd

# a=[1,2,3,4]

# name=["Gazala","Tashkil","Sana","Sagar"]

# pt=pd.Series(name, index=["a", "b", "c", "d"])
# print(pt["a"])  


# import pandas as pd

# data={
#      "Name":["Gazala","Tashkil","Sana","Sagar"],
#      "Age":[20,21,19,22],
# }

# print(pd.DataFrame(data).loc[0])


import pandas as pd

df = pd.read_csv("C:/Users/kgaza/OneDrive/Desktop/Python or Data/data.csv")

print(df.to_string())

