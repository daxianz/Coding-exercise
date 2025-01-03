import pandas as pd

def Is_Reapeted(lst):
    s = pd.Series(lst)
    return s.duplicated().any()

lst1 = [1, 2, 3, 4, 5]
lst2 = [1, 2, 3, 4, 5, 5]

print(Is_Reapeted(lst1))
print(Is_Reapeted(lst2))