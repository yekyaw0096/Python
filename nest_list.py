nested_lst = [
              [1,2,3],
              [4,5,6],
              [7,8,9],
              ]
print("Nested_list ",nested_lst)
print("Row 0 ",nested_lst[0])

print("Row [0] Col [1] is ",nested_lst[0][1])
print("Row [2] Col [2] is ",nested_lst[2][2])

for lst in nested_lst: #return individual rows
    for item in lst:    #return each elements
        print("item ",item)

for row,row_item in enumerate(nested_lst):
    print("Row ",row,"value ",row_item)
    for col,col_item in enumerate(row_item):
        print("Col ",col,"col_item ",col_item)
    
