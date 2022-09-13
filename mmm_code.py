# Mean = Average value of all numbers
numblist = [2, 4, 5, 8, 9, 10]
numblen = len(numblist)
numbsum = sum(numblist)
numbmean = numbsum / numblen
print("The mean of all the listed numbers (", numblist, ") is", str(numbmean))

# Median
numblist = [2, 4, 5, 8, 9, 10]
numblen = len(numblist)
numblist.sort()
if numblen % 2 == 0:
  median1 = numblist[numblen // 2]
  median2 = numblist[numblen // 2-1]
  numbmedian = (median1+median2)/2
print("The median of all the listed numbers (", numblist, ") is", str(numbmedian))

# Mode
from collections import Counter
numblist = [2, 4, 4, 5, 8, 9, 10]
numblen = len(numblist)
val = Counter(numblist)
findMode = dict(val)
mode = [i for i, v in findMode.items() if v == max(list(val.values()))]  
if len(mode) == numblen:
    findMode = "The group of number do not have any mode"
else:
    findMode = "The mode of a number is / are: " + ', '.join(map(str, mode))
print(findMode)

