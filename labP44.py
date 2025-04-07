#Q.44 set operations
set_1={10,20,30,40,50}
set_2={30,40,50,60,70}
# for i in set_1:
#     print(i)
# set_1.add(100)
# print(set_1)
# set_1.remove(100)
# print(set_1)
# print(set_1.intersection(set_2))
# print(set_1.union(set_2))
# print(set_1-set_2)
#symmetric_difference ->returns elements which are in set 1 or set2 but not in both
# print(set_1.symmetric_difference(set_2))
# print(set_1^set_2)
print(set_1.issuperset(set_2))