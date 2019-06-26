import yaml
file=open("familyinfo.yaml",'r')
data=yaml.load(file)
print(data)
print(data["name"])
print(data["spouse"]["name"])
print(data["children"][0]["name"])
##修改名字--不会更新到yaml文件，只修改当前data变量
data["name"]="David Smith"
print(data["name"])