a={
    	"杭州市":{
        	"上城区":["清波街道", "南山街道"],
        	"西湖区":["灵隐街道", "湖滨街道"]
    	},
    	"温州市":{
        	"鹿城区":["五马街道","滨江街道"],
        	"瓯海区":["茶山街道","高教园区"]
    	}
}
num=0
b=list(a.keys())
for i in b:
    print(i,end=" ")

print("\n请输入城市")
c = input()
while(c not in b):
        num=num+1
        print("输入城市错误，三次输入错误将退出程序，目前错误"+str(num)+"次！")
        if num==3:
            break
        c=input()
if c in b:
        d=list(a[c].keys())
        print("二级城区为：")
        for i in d:
            print(i,end=" ")
f=list(a.values())
print("\n请输入二级城区:")
k=input()
g={}
for i in f:
   g.update(i)

m=list(g[k])
for i in m:
    print(i,end=" ")
print("\n输入q推出程序")
p=input()
while p!='q':
    print("输入q推出程序")
    p=input()

    # for i in g:
    #     print(i,end=" ")






