#Q.40 program to sort(ascending and descending) a dictionary by value
dic_1={'D':40,'F':60,'C':30,'E':50,'G':70,'A':10,'B':20}
new_list=list(dic_1.items())
print(new_list)
out_dic=dict(sorted(dic_1.items(),key=lambda item:item[1]))
print(out_dic)
# print(out_dic)
# print(new_list[0][1])