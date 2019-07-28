"""f=open("newfile.txt",'a+')
str=input("Enter text:")
f.write(str)
f.seek(3,0)
a=f.read()
print(a)
f.close()"""




f=open("new2file.txt",'w')
print("Enter the text untile u dont fount str in th end (@in the end):" )
while(str!='@'):
    if(str!='@'):
        str=input("enter string:")
        f.write(str+"\n")
        
f.close()
f=open("new2file.txt","r")
b=f.read().splitlines()
f.seek(0,0)
v=f.readlines()
print(b)
print(v)
f.close()
          
               
