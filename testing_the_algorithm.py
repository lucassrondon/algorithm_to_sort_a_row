from row_and_stack_classes import *

row = Row(20)

row.insert(1)
row.insert(4)
row.insert(3)
row.insert(0)
row.insert(7)
row.insert(6)
row.insert(-10)
row.insert(10)
row.insert(9)
row.insert(8)
row.insert(5)
row.insert(2)


print("ROW BEFORE THE SORTING METHOD:", row)

row.sort_row()

print("ROW AFTER THE SORTING METHOD: ", row)
