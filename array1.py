import array as arr
array_num=arr.array("i",[2,3,4,5,6,5,4,3,5])
print('The original array: ', array_num)
print("The number of occurances for the number 5 is: "+str (array_num.count(5)))
array_num.reverse()
print("The reversed order is:", array_num)
