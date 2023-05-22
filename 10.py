# 字典根据键从小到大排序
dic = {"name": "zhangmingzhe", "age": 21, "city": "昆明", "tel": "18317829770"}
list1 = sorted(dic.items(), key=lambda i: i[0], reverse=False)
print(list1)
print(dict(list1))