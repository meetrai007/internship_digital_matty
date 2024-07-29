emp_detail={"emp1":{"name":"akash","rank":1,"age":33},"emp2":{"name":"meet","rank":1,"age":33},"emp3":{"name":"amit","rank":1,"age":33}}
# print(emp_detail["emp2"])

# print(dir(emp_detail))

# print(help(emp_detail.fromkeys))

# dict2=emp_detail.copy()
# print(dict2)

# print(help(emp_detail.get))
# print(emp_detail.get("emp1"))

# print(help(emp_detail.items))
# print(emp_detail.items())
# c=emp_detail.items()
# print(type(c))
# print(c)

# print(help(emp_detail.setdefault))
# print(emp_detail.setdefault("akash",10))

# print(help(emp_detail.pop))
# print(emp_detail.pop("emp1"))
# emp_detail.pop("emp1")
# print(emp_detail)

# # print(help(emp_detail.values))
# a=emp_detail.values()
# print(type(a))
# print(a)

# emp_detail["maan"]={"name":"ajay","roll":10}
# print(emp_detail)
# for i in emp_detail:
#     for k,v in emp_detail[i].items():
#         print(k,v)

emp_detail.pop("emp1")
print(emp_detail)