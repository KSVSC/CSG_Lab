import subprocess
c='./a.out '
n=10

f=open("CompileTime.csv","w+")

while(n<5000):
	c1=c+str(n)
	subprocess.call(["gcc","-o1", "MatrixMult.c"])
	tmp=subprocess.call(c1,shell=True)
	t1=tmp
	print(t1," ")
	
	subprocess.call(["gcc","-o2", "MatrixMult.c"])
	tmp=subprocess.call(c1,shell=True)
	t2=tmp
	print(t2," ")
	
	subprocess.call(["gcc","-o3", "MatrixMult.c"])
	tmp=subprocess.call(c1,shell=True)
	t3=tmp
	print(t3,"\n")
	
	t=str(t1)+"	"+str(t2)+"	"+str(t3)+"	"+str(n)
	f.write(t)
	f.write("\n")
	
	if(n<100):
		n+=1
	elif(n<1000):
		n+=10
	else:
		n+=500;
		
f.close()	
