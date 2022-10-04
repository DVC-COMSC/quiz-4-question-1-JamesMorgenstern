countLoop = 0
countClusters = 0
check = True

num1 = int(input())
num2 = num1

while (countLoop < 9):
    
    num1 = int(input())
    if (check == True):
        if (num1 % 2 == 0 and num2 % 2 == 0):
            countClusters += 1
            check = False
    if (num1 % 2 == 1):
        check = True
    num2 = num1
    countLoop += 1

print(countClusters)
# ******************************
# Make your Code 
# ******************************


# Requirement
# No need to use list
# All input values are taken one by one separatively.
###
