datas =[1,2,1,3,4,5,6,2,1]
result=[]
for each in datas:
    if datas.count(each) > 1 and each not in result:
        result.append(each)
print(result)
        