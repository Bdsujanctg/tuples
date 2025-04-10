fruits=['apple','mango','blueberry','watermelon','orange']
nums=['2300','1234','2090','5600','4800']
result={fruits[0]: nums for fruits,nums in zip(fruits,nums)}
print("\n",result )