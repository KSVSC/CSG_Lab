import subprocess
c='./a.out '
n=10

f=open("CompileTime.csv","w+")

while(n<5000):
	c1=c+str(n)
	
	subprocess.call(["gcc","-o1", "MatrixMult.c"])
	process = subprocess.Popen(c1, shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
	out, err = process.communicate()
	t1=str(out).replace('b',"")
	t1=t1.replace('\'',"")
	print(t1)
	
	subprocess.call(["gcc","-o2", "MatrixMult.c"])
	process = subprocess.Popen(c1, shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
	out, err = process.communicate()
	t2=str(out).replace('b',"")
	t2=t2.replace('\'',"")
	print(t2)
	
	subprocess.call(["gcc","-o3", "MatrixMult.c"])
	process = subprocess.Popen(c1, shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
	out, err = process.communicate()
	t3=str(out).replace('b',"")
	t3=t3.replace('\'',"")
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
