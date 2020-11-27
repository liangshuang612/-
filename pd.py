#导入pandas库
import pandas as pd
# 读取数据
data = pd.read_csv("/Users/liangshuang/Downloads/HIN-Datasets-for-Recommendation-and-Network-Embedding-master/Yelp/user_business.dat", header= None)
u = []
m = []
r = []
for i in range(len(data)):
    u.append(data[0][i].split('\t')[0])
    m.append(data[0][i].split('\t')[1]) #['111 111 1']
    r.append(data[0][i].split('\t')[2])
# range()是一个函数， for i in range () 就是给i赋值;len() 方法返回对象（字符、列表、元组等）长度或项目个数。
# append() 方法用于在列表末尾添加新的对象。
#  split() 通过指定分隔符对字符串进行切片。
list = {"user":u , "movie":m , "ratings":r}
df = pd.DataFrame(list) 
# pandas中的数据结构主要包括两种,一种是Series,一种是dataframe。
# DataFrame是一种表格型数据结构，它含有一组有序的列，每列可以是不同的值。DataFrame既有行索引，也有列索引，
def find_repeat_data(name_list):
    """
    查找列表中重复的数据
    :return: 一个重复数据的列表，列表中字典的key 是重复的数据，value 是重复的次数
    """
    repeat_list = []
    for i in set(name_list):  
        ret=name_list.count(i) # 查找该数据在原列表中的个数
        if ret > 1:
            item=dict()
            item[i] = ret
            repeat_list.append(item)
    return repeat_list         
rep = find_repeat_data(u)
for u in rep:
    for i in u.keys():
        if u[i]>10:
            df = df.drop(index=(df.loc[(df['user']==i)].index))
# df.drop()删除含有指定元素的行或列，或删除指定行，列
# df.loc()对行进行选取
df[3]=df['user']+'\t'+df['movie']+'\t'+df['ratings']
df[3].to_csv('/Users/liangshuang/Downloads/yelp_10.txt',header = None,index = None)