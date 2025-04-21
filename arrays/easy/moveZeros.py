def move_zeros(inputList: list[int]) -> None:
  # finding the count of zeros first.
  count_of_zeros = inputList.count(0) # count method in list to find the count of Zero
  if len(inputList) == 0 or len(inputList) == 1 or count_of_zeros == 0: # basecase
      print(inputList)
      return
  inputList = [nonZeroList for nonZeroList in inputList if nonZeroList != 0] # removing the Zero from the existing list if any Zeros
  inputList.extend(count_of_zeros * [0])
  print(inputList)

#Calling Function
move_zeros([]) # testcase1 with emptylist
move_zeros([0]) # testcase2 with only 0
move_zeros([0,1]) # testcase3
move_zeros([1,0]) # testcase4
move_zeros([1,0,2]) # testcase5
move_zeros([0,1,2,3,0,4,5,6,0]) # testcase6     
