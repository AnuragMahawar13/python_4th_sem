#Q.41 Program to concatenate multiple dictionaries into one

dic_1={1:10,2:20}
dic_2={3:30,4:40}
dic_3={5:50,6:60}
print(dic_1)
print(dic_2)
print(dic_3)
output_dic={}
# output_dic=dic_1 | dic_2 | dic_3
output_dic.update(dic_1)
output_dic.update(dic_2)
output_dic.update(dic_3)
print(output_dic)