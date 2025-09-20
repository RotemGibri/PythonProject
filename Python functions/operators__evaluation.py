def operators_evaluation(a,b,c):
    return a or b or c

print(operators_evaluation(False,False,False))
print(operators_evaluation(1>4,"i"=="u",False))
print(operators_evaluation(False,False,True))
