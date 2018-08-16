import sys

print "\n" + "Starting Analog Multipurpose Operation System"

# Output pins returns data in binary decimal format. This function convert it back to normal binary.
# Assuming output is one byte representing 2 digit number.
def ToInt(value):
	return ((value >> 4) & 0xF) * 10 + (value & 0xF)

# Perform full cycle of clock from 0 to 1 and back to 0
def Tick(test):
	test.SetInput("Clock", 0)
	test.Evaluate();
	test.SetInput("Clock", 1)
	test.Evaluate();
	
def Tick2(test):
	test.SetInput("clock", 0)
	test.Evaluate();
	test.SetInput("clock", 1)
	test.Evaluate();
	
def ExitApp():
	from System.Diagnostics import Process
	p = Process()
	p.StartInfo.UseShellExecute = False
	p.StartInfo.RedirectStandardOutput = True
	p.StartInfo.FileName = 'TASKKILL'
	p.StartInfo.Arguments = '/IM logiccircuit.exe'
	p.Start()
	p.WaitForExit()
	
	
	
def Test(n,path,name):
	s="2"
	x=0
	saad="Fail - "
	print n
	n=n+1
	if n==1:
		s,x=Test01(s,x)
	elif n == 2:
		s,x=Test02(s,x)
	elif n == 3:
		s,x=Test03(s,x)
	elif n == 4:
		s,x=Test04(s,x)
	elif n == 6:
		s,x=Test05(s,x)
	print x
	print s
	if (x==1):
		saad="Pass - "
	file = open(path+saad+name+".txt", 'w')

	file.write(s)
	file.close()
	ExitApp()
	

	
def Test01(s,testres):
	s=""
	test=0;
	total=0;
	######################################################
	try:  
		tester = App.CreateTester("01 Not Gate")
		for x in xrange(0, 2):
			tester.SetInput("in", x)
			tester.Evaluate()
			output=tester.GetOutput("out")
			if (x==output):
				test=1
		if (test==0):
			s+= "\n" + "Not Gate test ... Ok"
			total=total+1
		else:
			s+= "\n" + "Not Gate test ... Fail"
	except:
		s+= "\n" + "Not Gate test ..." + str(sys.exc_info()[1])	
	######################################################
	test=0;
	try:  
		tester = App.CreateTester("02 And Gate")	
		for x in xrange(0, 2):
			for y in xrange(0, 2):
				tester.SetInput("a", x)
				tester.SetInput("b", y)
				tester.Evaluate()
				output=tester.GetOutput("q")
				temp=x&y
				if (temp!=output):
					test=1
		if (test==0):
			s+= "\n" + "And Gate test ... Ok"
			total=total+1
		else:
			s+= "\n" + "And Gate test ... Fail"
	except:
		s+= "\n" + "And Gate test ..." + str(sys.exc_info()[1])	
	######################################################	
	test=0;	
	try:  
		tester = App.CreateTester("03 Or Gate")	
		for x in xrange(0, 2):
			for y in xrange(0, 2):
				tester.SetInput("a", x)
				tester.SetInput("b", y)
				tester.Evaluate()
				output=tester.GetOutput("q")
				temp=x|y
				if (temp!=output):
					test=1
		if (test==0):
			s+= "\n" + "Or Gate test ... Ok"
			total=total+1
		else:
			s+= "\n" + "Or Gate test ... Fail"
	except:
		s+= "\n" + "Or Gate test ..." + str(sys.exc_info()[1])	
	######################################################		
	test=0;	
	try:  
		tester = App.CreateTester("04 Xor Gate")	
		for x in xrange(0, 2):
			for y in xrange(0, 2):
				tester.SetInput("a", x)
				tester.SetInput("b", y)
				tester.Evaluate()
				output=tester.GetOutput("q")
				temp=x^y
				if (temp!=output):
					test=1
		if (test==0):
			s+= "\n" + "Xor Gate test ... Ok"
			total=total+1
		else:
			s+= "\n" + "Xor Gate test ... Fail"
	except:
		s+= "\n" + "Xor Gate test ..." + str(sys.exc_info()[1])	
		
	######################################################	
	test=0;
	try: 
		tester = App.CreateTester("05 Multiplexer")	
		for x in xrange(0, 2):
			for y in xrange(0, 2):
				for z in xrange(0, 2):
					tester.SetInput("a", x)
					tester.SetInput("b", y)
					tester.SetInput("Sel", z)
					tester.Evaluate()
					output=tester.GetOutput("q")
					if (z==0):
						temp=x
					else:
						temp=y
					if (temp!=output):
						test=1
		if (test==0):
			s+= "\n" + "Multiplexer Gate test ... Ok"
			total=total+1
		else:
			s+= "\n" + "Multiplexer Gate test ... Fail"
	except:
		s+= "\n" + "Multiplexer Gate test ..." + str(sys.exc_info()[1])	
	

	######################################################		
	test=0;	
	try:  
		tester = App.CreateTester("06 Demultiplexer")	
		for x in xrange(0, 2):
			for y in xrange(0, 2):
				tester.SetInput("in", x)
				tester.SetInput("Sel", y)
				tester.Evaluate()
				output1=tester.GetOutput("a")
				output2=tester.GetOutput("b")
				temp=x^y
				if (y==0):
					temp=output1
				else:
					temp=output2
				if (temp!=x):
					test=1
		if (test==0):
			s+= "\n" + "Demultiplexer Gate test ... Ok"
			total=total+1
		else:
			s+= "\n" + "Demultiplexer Gate test ... Fail"
	except:
		s+= "\n" + "Demultiplexer Gate test ..." + str(sys.exc_info()[1])	
			
		
	######################################################	

	
		
	if (total==6):
		testres=1
		s+= "\n" + "Primitives test ... pass"
	return s,testres
		
def Test02(s,testres):
	s=""
	total=0;
	
	
	######################################################
	test=0;
	tester = App.CreateTester("01 And04")	
	x=1
	y=2
	tester.SetInput("x",x )
	tester.SetInput("x1",y )
	tester.Evaluate()
	output=tester.GetOutput("q")
	temp=x&y
	if (temp!=output):
		test=1
	x=4
	y=5
	tester.SetInput("x",x )
	tester.SetInput("x1",y )
	tester.Evaluate()
	output=tester.GetOutput("q")
	temp=x&y
	if (temp!=output):
		test=1
	x=0
	y=14
	tester.SetInput("x",x )
	tester.SetInput("x1",y )
	tester.Evaluate()
	output=tester.GetOutput("q")
	temp=x&y
	if (temp!=output):
		test=1
		
	
	if (test==0):
		s+= "\n" + "And04 Gate test ... Ok"
		total=total+1
	else:
		s+= "\n" + "And04 Gate test ... Fail"
		
	#######################################################
	test=0;
	try:  
		tester = App.CreateTester("01 And16")	
		x=50
		y=87
		tester.SetInput("x",x )
		tester.SetInput("x1",y )
		tester.Evaluate()
		output=tester.GetOutput("q")
		temp=x&y
		if (temp!=output):
			test=1
		x=1000
		y=5098
		tester.SetInput("x",x )
		tester.SetInput("x1",y )
		tester.Evaluate()
		output=tester.GetOutput("q")
		temp=x&y
		if (temp!=output):
			test=1
		x=3258
		y=2547
		tester.SetInput("x",x )
		tester.SetInput("x1",y )
		tester.Evaluate()
		output=tester.GetOutput("q")
		temp=x&y
		if (temp!=output):
			test=1
			
		
		if (test==0):
			s+= "\n" + "And16 Gate test ... Ok"
			total=total+1
		else:
			s+= "\n" + "And16 Gate test ... Fail"
	except:
		s+= "\n" + "And16 Gate test ..." + str(sys.exc_info()[1])	
		
	#######################################################
	test=0;
	try:  
		tester = App.CreateTester("02 Half Adder")	
		for x in xrange(0, 2):
			for y in xrange(0, 2):
				tester.SetInput("a", x)
				tester.SetInput("b", y)
				tester.Evaluate()
				output2=tester.GetOutput("s")
				output1=tester.GetOutput("c")
				temp1=x&y
				temp2=x^y
				if (temp1!=output1 or temp2!=output2):
					test=1
		if (test==0):
			s+= "\n" + "Half Adder Gate test ... Ok"
			total=total+1
		else:
			s+= "\n" + "Half Adder Gate test ... Fail"	
	except:
		s+= "\n" + "Half Adder Gate test ..." + str(sys.exc_info()[1])	
	#######################################################
	test=0;
	try:  
		tester = App.CreateTester("03 Full Adder")	
		for x in xrange(0, 2):
			for y in xrange(0, 2):
				for z in xrange(0, 2):
					tester.SetInput("a", x)
					tester.SetInput("b", y)
					tester.SetInput("inC", z)
					tester.Evaluate()
					output1=tester.GetOutput("s")
					output2=tester.GetOutput("c")
					temp1=(x^y)^z
					temp2=0
					if (x+y+z>1):
						temp2=1
					if (temp1!=output1 or temp2!=output2):
						test=1
		if (test==0):
			s+= "\n" + "Full Adder Gate test ... Ok"
			total=total+1
		else:
			s+= "\n" + "Full Adder Gate test ... Fail"
	except:
		s+= "\n" + "Full Adder Gate test ..." + str(sys.exc_info()[1])	
#######################################################
	test=0;
	try:  
		tester = App.CreateTester("04 Adder 4 bit")	
		x=10
		y=2
		tester.SetInput("a",x )
		tester.SetInput("b",y )
		tester.Evaluate()
		output=tester.GetOutput("s")
		temp=x+y
		if (temp!=output):
			test=1
		x=5
		y=4
		tester.SetInput("a",x )
		tester.SetInput("b",y )
		tester.Evaluate()
		output=tester.GetOutput("s")
		temp=x+y
		if (temp!=output):
			test=1
		x=7
		y=1
		tester.SetInput("a",x )
		tester.SetInput("b",y )
		tester.Evaluate()
		output=tester.GetOutput("s")
		temp=x+y
		if (temp!=output):
			test=1
			
		if (test==0):
			s+= "\n" + "Add4 Gate test ... Ok"
			total=total+1
		else:
			s+= "\n" + "Add4 Gate test ... Fail"
	except:
		s+= "\n" + "Add4 Gate test ..." + str(sys.exc_info()[1])	
		
	#######################################################
	test=0;
	try:  
		tester = App.CreateTester("04 Adder 16 bit")	
		x=50
		y=87
		tester.SetInput("a",x )
		tester.SetInput("b",y )
		tester.Evaluate()
		output=tester.GetOutput("s")
		temp=x+y
		if (temp!=output):
			test=1
		x=1000
		y=5098
		tester.SetInput("a",x )
		tester.SetInput("b",y )
		tester.Evaluate()
		output=tester.GetOutput("s")
		temp=x+y
		if (temp!=output):
			test=1
		x=3258
		y=2547
		tester.SetInput("a",x )
		tester.SetInput("b",y )
		tester.Evaluate()
		output=tester.GetOutput("s")
		temp=x+y
		if (temp!=output):
			test=1
			
		
		if (test==0):
			s+= "\n" + "Add16 Gate test ... Ok"
			total=total+1
		else:
			s+= "\n" + "Add16 Gate test ... Fail"
	except:
		s+= "\n" + "Add16 Gate test ..." + str(sys.exc_info()[1])	
		
	
		
	#######################################################
	test=0;
	try:  
		tester = App.CreateTester("05 Inc 16")	
		for x in xrange(5000, 5100):
			tester.SetInput("in", x)
			tester.Evaluate()
			output=tester.GetOutput("out")
			temp=x+1
			if (temp!=output):
				test=1
		if (test==0):
			s+= "\n" + "inc16 Gate test ... Ok"
			total=total+1
		else:
			s+= "\n" + "inc16 Gate test ... Fail"
	except:
		s+= "\n" + "inc16 Gate test ..." + str(sys.exc_info()[1])	
	#######################################################
	test=0;
	tester = App.CreateTester("06 Mux04")
	for x in xrange(1, 4):
		for y in xrange(10, 14):
			for z in xrange(0, 1):
				tester.SetInput("a", x)
				tester.SetInput("b", y)
				tester.SetInput("Sel", z)
				tester.Evaluate()
				output=tester.GetOutput("q")
				if (z==0):
					temp=x
				else:
					temp=y
				if (temp!=output):
					test=1
	if (test==0):
		s+= "\n" + "Mux04 Gate test ... Ok"
		total=total+1
	else:
		s+= "\n" + "Mux04 Gate test ... Fail"
	
	#######################################################
	test=0;
	try:  
		tester = App.CreateTester("06 Mux16")
		for x in xrange(100, 200):
			for y in xrange(5000, 5100):
				for z in xrange(0, 2):
					tester.SetInput("a", x)
					tester.SetInput("b", y)
					tester.SetInput("Sel", z)
					tester.Evaluate()
					output=tester.GetOutput("q")
					if (z==0):
						temp=x
					else:
						temp=y
					if (temp!=output):
						test=1
		if (test==0):
			s+= "\n" + "Mux16 Gate test ... Ok"
			total=total+1
		else:
			s+= "\n" + "Mux16 Gate test ... Fail"
	except:
		s+= "\n" + "Mux16 Gate test ..." + str(sys.exc_info()[1])	
	
	#######################################################
	test=0;
	try:  
		tester = App.CreateTester("07 Mux4Way16")
		for x in xrange(100, 200):
			for y in xrange(5000, 5100):
				for z in xrange(0, 3):
					tester.SetInput("a", x)
					tester.SetInput("b", y)
					tester.SetInput("c", x+300)
					tester.SetInput("d", y+300)
					tester.SetInput("sel", z)
					tester.Evaluate()
					output=tester.GetOutput("out")
					if (z==0):
						temp=x
					if (z==1):
						temp=y
					if (z==2):
						temp=x+300
					if (z==3):
						temp=y+300
					if (temp!=output):
						test=1
		if (test==0):
			s+= "\n" + "Mux4way16 Gate test ... Ok"
			total=total+1
		else:
			s+= "\n" + "Mux4way16 Gate test ... Fail"
	except:
		s+= "\n" + "Mux4way16 Gate test ..." + str(sys.exc_info()[1])	
	
	#######################################################
	test=0;
	try:  
		tester = App.CreateTester("08 Mux8Way16")
		for x in xrange(1100, 1200):
			for y in xrange(5000, 5100):
				for z in xrange(0, 8):
					tester.SetInput("x", x)
					tester.SetInput("x1", y)
					tester.SetInput("x2", x+300)
					tester.SetInput("x3", y+300)
					tester.SetInput("x4", x-300)
					tester.SetInput("x5", y-300)
					tester.SetInput("x6", x+600)
					tester.SetInput("x7", y+600)
					tester.SetInput("sel", z)
					tester.Evaluate()
					output=tester.GetOutput("out")
					if (z==0):
						temp=x
					if (z==1):
						temp=y
					if (z==2):
						temp=x+300
					if (z==3):
						temp=y+300
					if (z==4):
						temp=x-300
					if (z==5):
						temp=y-300
					if (z==6):
						temp=x+600
					if (z==7):
						temp=y+600
					if (temp!=output):
						test=1
		if (test==0):
			s+= "\n" + "Mux8way16 Gate test ... Ok"
			total=total+1
		else:
			s+= "\n" + "Mux8way16 Gate test ... Fail"
	except:
		s+= "\n" + "Mux8way16 Gate test ..." + str(sys.exc_info()[1])	
	#######################################################
	test=0;	
	try:  
		tester = App.CreateTester("09 DMux4Way")	
		output = []
		for x in xrange(0, 2):
			for y in xrange(0, 4):
				tester.SetInput("in", x)
				tester.SetInput("Sel", y)
				tester.Evaluate()
				output0=tester.GetOutput("q")
				output1=tester.GetOutput("q1")
				output2=tester.GetOutput("q2")
				output3=tester.GetOutput("q3")
				if (y==0):
					temp=output0
				if (y==1):
					temp=output1
				if (y==2):
					temp=output2
				if (y==3):
					temp=output3
				if (x!=temp):
					test=1
		if (test==0):
			s+= "\n" + "DMux4Way Gate test ... Ok"
			total=total+1
		else:
			s+= "\n" + "DMux4Way Gate test ... Fail"
	except:
		s+= "\n" + "DMux4Way Gate test ..." + str(sys.exc_info()[1])	
	
	#######################################################

	test=0;	
	try:  
		tester = App.CreateTester("10 DMux8Way")	
		output = []
		for x in xrange(0, 2):
			for y in xrange(0, 4):
				tester.SetInput("in", x)
				tester.SetInput("Sel", y)
				tester.Evaluate()
				output0=tester.GetOutput("q")
				output1=tester.GetOutput("q1")
				output2=tester.GetOutput("q2")
				output3=tester.GetOutput("q3")
				output4=tester.GetOutput("q4")
				output5=tester.GetOutput("q5")
				output6=tester.GetOutput("q6")
				output7=tester.GetOutput("q7")
				if (y==0):
					temp=output0
				if (y==1):
					temp=output1
				if (y==2):
					temp=output2
				if (y==3):
					temp=output3
				if (y==4):
					temp=output4
				if (y==5):
					temp=output5
				if (y==6):
					temp=output6
				if (y==7):
					temp=output7
				if (x!=temp):
					test=1
		if (test==0):
			s+= "\n" + "DMux4Way Gate test ... Ok"
			total=total+1
		else:
			s+= "\n" + "DMux4Way Gate test ... Fail"
	except:
		s+= "\n" + "DMux4Way Gate test ..." + str(sys.exc_info()[1])	
	

		
	#######################################################
	if (total==13):
		testres=1
		s+= "\n" + "Advanced calculations test ... pass"
	return s,testres
	
	
def Test03(s,testres):
	total=0;
	s=""
		#######################################################
	
	test=0;
	try:  
		tester = App.CreateTester("01 MiniALU")
		for x in xrange(100, 200):
			for y in xrange(5000, 5100):
				for f in xrange(0, 2):
					for zx in xrange(0, 2):
						for zy in xrange(0, 2):
							tester.SetInput("x", x)
							tester.SetInput("y", y)
							tester.SetInput("f", f)
							tester.SetInput("zx", zx)
							tester.SetInput("zy", zy)
							tester.Evaluate()
							output=tester.GetOutput("out")
							if (f==0):
								temp=((x*(1-zx))&((y*(1-zy))))
							else:
								temp=((x*(1-zx))+((y*(1-zy))))
							if (temp!=output):
								test=1
		if (test==0):
			s+= "\n" + "MiniALU Gate test ... Ok"
			total=total+1
		else:
			s+= "\n" + "MiniALU Gate test ... Fail"
	except:
		s+= "\n" + "MiniALU Gate test ..." + str(sys.exc_info()[1])	
	######################################################
	test=0;
	try:  
		tester = App.CreateTester("02 Not 04")	
		for x in xrange(1, 14):
			tester.SetInput("in", x)
			tester.Evaluate()
			output=tester.GetOutput("out")
			temp=~x+16
			if (temp!=output):
				test=1
		if (test==0):
			s+= "\n" + "Not16 Gate test ... Ok"
			total=total+1
		else:
			s+= "\n" + "Not16 Gate test ... Fail"
	except:
		s+= "\n" + "Not16 Gate test ..." + str(sys.exc_info()[1])	
		
	#######################################################	
	test=0;
	try:  
		tester = App.CreateTester("02 Not 16")	
		for x in xrange(5000, 5100):
			tester.SetInput("in", x)
			tester.Evaluate()
			output=tester.GetOutput("out")
			temp=~x+65536
			if (temp!=output):
				test=1
		if (test==0):
			s+= "\n" + "Not16 Gate test ... Ok"
			total=total+1
		else:
			s+= "\n" + "Not16 Gate test ... Fail"
	except:
		s+= "\n" + "Not16 Gate test ..." + str(sys.exc_info()[1])	
		
	#######################################################	
	test=0;
	try:  
		tester = App.CreateTester("03 Or8Way")
		for x in xrange(0, 2):
			for y in xrange(0, 2):
				for z in xrange(0, 2):
					tester.SetInput("x", x)
					tester.SetInput("x1", y)
					tester.SetInput("x2", z)
					tester.SetInput("x3", x)
					tester.SetInput("x4", y)
					tester.SetInput("x5", z)
					tester.SetInput("x6", x)
					tester.SetInput("x7", y)
					tester.Evaluate()
					output=tester.GetOutput("q")
					temp=x+y+z
					if (output==0 and temp >0):
						test=1
		if (test==0):
			s+= "\n" + "Or8Way Gate test ... Ok"
			total=total+1
		else:
			s+= "\n" + "Or8Way Gate test ... Fail"
	except:
		s+= "\n" + "Or8Way Gate test ..." + str(sys.exc_info()[1])	
	

	#######################################################
	
	test=0;
	try:  
		tester = App.CreateTester("04 ALU")
		for x in xrange(10100, 10102):
			for y in xrange(10100, 5002):
				for f in xrange(0, 2):
					for zx in xrange(0, 2):
						for zy in xrange(0, 2):
							for nx in xrange(0, 2):
								for ny in xrange(0, 2):
									for no in xrange(0, 2):
										tester.SetInput("x", x)
										tester.SetInput("y", y)
										tester.SetInput("f", f)
										tester.SetInput("zx", zx)
										tester.SetInput("zy", zy)
										tester.SetInput("nx", nx)
										tester.SetInput("ny", ny)
										tester.SetInput("zx", zx)
										tester.Evaluate()
										output=tester.GetOutput("out")
										tx=x
										ty=y
										if (nx==1):
											tx=65536-x
										if (ny==1):
											ty=65536-y
										if (f==0):
											temp=((tx*(1-zx))&((ty*(1-zy))))
										else:
											temp=((tx*(1-zx))+((ty*(1-zy))))
										if (no==1):
											temp=65536-temp
										s+= "\n" + temp," ",output," nx ",nx,"ny ",ny," no ",no," x",x," tx ",tx," ",y," ty",ty
										if (temp!=output):
											test=1
		if (test==0):
			s+= "\n" + "ALU Gate test ... Ok"
			total=total+1
		else:
			s+= "\n" + "ALU Gate test ... Fail"
	except:
		s+= "\n" + "ALU Gate test ..." + str(sys.exc_info()[1])	
		
	#######################################################
	if (total==5):
		testres=1
		s+= "\n" + "Arithmetic Logic Unit... fully operational"	
	return s,testres

def Test04(s,testres):
	total=0;
	
	s=""
	
	######################################################
	test=0;
	try:  
		tester = App.CreateTester("01 D flip-flop")	
		for x in xrange(0, 2):
			tester.SetInput("Data", x)
			Tick(tester)
			Tick(tester)
			output=tester.GetOutput("q")
			if (x!=output):
				test=1
		if (test==0):
			s+= "\n" + "DFF Gate test ... Ok"
			total=total+1
		else:
			s+= "\n" + "DFF Gate test ... Fail"
	except:
		s+= "\n" + "DFF Gate test ..." + str(sys.exc_info()[1])	
		
	######################################################
	test=0;
	try:  
		tester = App.CreateTester("02 Bit")	
		tester.SetInput("Load", 1)
		tester.SetInput("Data", 1)
		Tick(tester)
		tester.SetInput("Load", 0)
		Tick(tester)
		tester.SetInput("Data", 1)
		output=tester.GetOutput("q")
		if (output!=1):
			test=1
		Tick(tester)
		output=tester.GetOutput("q")
		if (output!=1):
			test=1
		Tick(tester)
		output=tester.GetOutput("q")
		if (output!=1):
			test=1
		tester.SetInput("Load", 1)
		tester.SetInput("Data", 0)
		Tick(tester)
		tester.SetInput("Load", 1)
		Tick(tester)
		output=tester.GetOutput("q")
		if (output!=0):
			test=1
		
		if (test==0):
			s+= "\n" + "Bit Gate test ... Ok"
			total=total+1
		else:
			s+= "\n" + "Bit Gate test ... Fail"
	except:
		s+= "\n" + "Bit Gate test ..." + str(sys.exc_info()[1])	
			
	######################################################
	test=0;
	try:  
		tester = App.CreateTester("03 Register 16 bit")	
		tester.SetInput("Load", 1)
		tester.SetInput("Data", 1000)
		Tick(tester)
		tester.SetInput("Load", 0)
		Tick(tester)
		tester.SetInput("Data", 2000)
		output=tester.GetOutput("q")
		if (output!=1000):
			test=1
		Tick(tester)
		output=tester.GetOutput("q")
		if (output!=1000):
			test=1
		Tick(tester)
		output=tester.GetOutput("q")
		if (output!=1000):
			test=1
		tester.SetInput("Load", 1)
		tester.SetInput("Data", 3000)
		Tick(tester)
		tester.SetInput("Load", 0)
		Tick(tester)
		output=tester.GetOutput("q")
		if (output!=3000):
			test=1

		if (test==0):
			s+= "\n" + "Register Gate test ... Ok"
			total=total+1
		else:
			s+= "\n" + "Register Gate test ... Fail"
	except:
		s+= "\n" + "Register Gate test ..." + str(sys.exc_info()[1])	
		
	######################################################
	print 1
	test=0;
	try:  
		tester = App.CreateTester("04 Program counter")	
		tester.SetInput("Load", 1)
		tester.SetInput("Data", 1000)
		Tick(tester)
		tester.SetInput("Load", 0)
		tester.SetInput("Inc", 1)
		Tick(tester)
		for x in xrange(1001, 1010):
			output=tester.GetOutput("out")
			if (output!=x):
				test=1
			Tick(tester)
		tester.SetInput("Reset", 1)
		tester.SetInput("Inc", 0)
		tester.SetInput("Data", 3000)
		Tick(tester)
		#Tick(tester)
		output=tester.GetOutput("out")
		if (output!=0):
			test=1
		Tick(tester)
		Tick(tester)
		
		
		if (test==0):
			s+= "\n" + "PC Gate test ... Ok"
			total=total+1
		else:
			s+= "\n" + "PC Gate test ... Fail"
	except:
		s+= "\n" + "PC Gate test ..." + str(sys.exc_info()[1])	
		
	######################################################
	print 1
	test=0;
	try:  
		tester = App.CreateTester("05 RAM8")
		tester.SetInput("load", 1)
		for x in xrange(0, 7):		
			tester.SetInput("in", x+10)
			tester.SetInput("address", x)
			Tick2(tester)
		tester.SetInput("load", 0)
		for x in xrange(0, 7):		
			tester.SetInput("address", x)
			Tick2(tester)
			output=tester.GetOutput("out")
			print (x+10)
			if (output!=(x+10)):
				test=1
		

		if (test==0):
			s+= "\n" + "RAM8 Gate test ... Ok"
			total=total+1
		else:
			s+= "\n" + "RAM8 Gate test ... Fail"
	except:
		s+= "\n" + "RAM8 Gate test ..." + str(sys.exc_info()[1])	
		
	######################################################
	
	if (total==5):
		testres=1
		s+= "\n" + "Memory Unit... fully operational"		
	return s,testres
	
def Test05(s,testres):
	total=0;
	s=""
	
	######################################################
	test=0;
	try:  
		tester = App.CreateTester("02 CPU")	
			
		##cycle##
		test+=CPUtest(tester,0,0,1,-1,-1,-1)
		test+=CPUtest(tester,12345,0,0,12345,-1,-1)
		test+=CPUtest(tester,60432,0,0,-1,-1,-1)
		test+=CPUtest(tester,23456,0,0,23456,-1,-1)
		test+=CPUtest(tester,57808,0,0,-1,-1,-1)
		test+=CPUtest(tester,1000,0,0,1000,-1,-1)
		test+=CPUtest(tester,58120,0,0,-1,-1,-1)
		test+=CPUtest(tester,1001,0,0,1001,-1,-1)
		test+=CPUtest(tester,58264,0,0,-1,-1,-1)
		test+=CPUtest(tester,1000,0,0,1000,-1,-1)
		test2=test-10
		s+="\n"+str(test2)+" of 10"
		if (test==0):
			s+= "\n" + "CPU test ... Ok"
			total=total+1
		else:
			s+= "\n" + "CPU test ... Fail check conections"
	except:
		s+= "\n" + "CPU Gate test ..." + str(sys.exc_info()[1])	
		
	if (total==1):
		testres=1
		s+= "\n" + "Memory Unit... fully operational"	
	return s,testres	
		
def CPUtest(tester,ins,inm,reset,adrs,pc,outm):
	test=0
	try:  
		tester = App.CreateTester("02 CPU")	
		tester.SetInput("instruction", ins)
		tester.SetInput("InM", inm)
		tester.SetInput("reset", reset)
		Tick(tester)
		output1=tester.GetOutput("addressM")
		output2=tester.GetOutput("pc")
		output3=tester.GetOutput("outM")
		output4=tester.GetOutput("Areg")
		output5=tester.GetOutput("Dreg")
		print output1 
		print adrs
		print "--"	
		print output3
		print outm		
		print "***************"		
		if (output1!=adrs and adrs!=-1):
			test=1	
		if (output3!=outm and outm!=-1):
			test=1	
	except:
		test=1
	print test
	return test
	
def cpusim():
	tester = App.CreateTester("02 CPU")	
	str="Reset"
	while (str!="exit"):
		try:
			ins=int(str)
		except ValueError:
			if (str=="reset" or str=="Reset"):
				ins=0
				inm=0
				reset=1
			else:
				s+= "\n" + "Unknown command"
		tester.SetInput("instruction", ins)
		tester.SetInput("InM", inm)
		tester.SetInput("reset", reset)
		Tick(tester)
		output1=tester.GetOutput("addressM")
		output2=tester.GetOutput("pc")
		output3=tester.GetOutput("outM")
		output4=tester.GetOutput("Areg")
		output5=tester.GetOutput("Dreg")
		s+= "\n" + "|---------------------------------"
		s+= "\n" + "|PC        : ",output2
		s+= "\n" + "|---------------------------------"		
		s+= "\n" + "|addressM  : ",output1
		s+= "\n" + "|---------------------------------"
		s+= "\n" + "|outM      : ",output3
		s+= "\n" + "|---------------------------------"
		s+= "\n" + "|A register: ",output4
		s+= "\n" + "|---------------------------------"
		s+= "\n" + "|D register: ",output5
		s+= "\n" + "|---------------------------------"
		s+= "\n" + "|PC        : ",output2
		s+= "\n" + "|---------------------------------"
		s+= "\n" + ""
		s+= "\n" + ""
		str = raw_input('CPU:\\\\')
	s+= "\n" + "AMOS logging out"
