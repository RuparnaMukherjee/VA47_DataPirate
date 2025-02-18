import data
import pickle


avg=0
t=0
low=high=0
count=0
pkl_file = open('patient.pkl', 'rb')
mydict = pickle.load(pkl_file)
pkl_file.close()


def digitize(line,tname,id):
	value=0
	global stat
	print("digitize",id)
	for i in line.split():
		#print(i)
		if(data.param[tname]["data"]):
			if(data.param[tname]["range"]):
				low=high=0
				count=0
				a=[]
				if(i=='-'):
					for x in line.split():
						if(x.replace('.','').isdigit()):
							if(count==0):
								low=float(x)
							if(count==1):
								high=float(x)
							count=count+1
					if(data.param[tname]["gender"]):
						a=data.param[tname][mydict[id]["gender"]] 
							#if result depends on age	
					elif(data.param[tname]["age"]):
						for k in data.param[tname]:
							if(k.isdigit()):
								if(k>=mydict[id]["age"]):
									a=data.param[tname][k]
					else:
						a=data.param[tname]["value"]
					
					a=a.split('-')
					low1,high1= float(a[0]),float(a[1])
					stat="Result "+str(low)+"-"+str(high)+" || Normal Range "+str(low1)+"-"+str(high1)+" || "
					if(low>=low1 and high<=high1):
						value=1
					elif((low1-low)>1 or (high-high1)>1):
						value=2
					elif((low1-low)>3 or (high-high1)>3):
						value=3
					elif((low1-low)>6 or (high-high1)>6):
						value=4
				

					print(value)
					break
				
				elif('-' in i):
						if((i.replace('-','')).replace('.','').isdigit()):
								b=i.split('-')
								count+=1
								if(count<2):
										low,high= float(b[0]),float(b[1])
								if(data.param[tname]["gender"]):
										a=data.param[tname][mydict[id]["gender"]] 
							#if result depends on age	
								elif(data.param[tname]["age"]):
									for k in data.param[tname]:
										if(k.isdigit()):
											if(k>=mydict[id]["age"]):
												a=data.param[tname][k]
								else:
									a=data.param[tname]["value"]
					
								a=a.split('-')
								low1,high1= float(a[0]),float(a[1])
								stat="Result "+str(low)+"-"+str(high)+" || Normal Range "+str(low1)+"-"+str(high1)+" || "
								if(low>=low1 and high<=high1):
										value=1
								elif((low1-low)>1 or (high-high1)>1):
										value=2
								elif((low1-low)>3 or (high-high1)>3):
										value=3
								elif((low1-low)>6 or (high-high1)>6):
										value=4

						print(value)
						break

			else:
				if(i.replace('.','').isdigit()):
					  #gender dependent
						if(data.param[tname]["gender"]):
							a=data.param[tname][mydict[id]["gender"]]
						#age dependent 
						elif(data.param[tname]["age"]):
							for k in data.param[tname]:
								if(type(k)==int):
									if(k>=mydict[id]["age"]):
										a=data.param[tname][k]
						#otherwise
						else:
							a=data.param[tname]["value"]
						a = a.split('-')
						print(a)
						low,high= float(a[0]),float(a[1])
						print(low,",",high)
						i=float(i)
						print(i)
						stat="Result "+str(i)+" || Normal Range "+str(low)+"-"+str(high)+" || "
						if(i<=high and i>=low):
								value=1
						elif(i<=(low+(0.4*low)) or i>=(high +(0.4*high))):
						 		value=4		
						elif(i<=(low+(0.2*low)) or i>=(high +(0.2*high))):
						 		value=3
						elif(i<=(low+(0.1*low)) or i>=(high +(0.1*high))):
						 		value=2
						# elif(i<=(low+(0.1*low)) or i>=(high +(0.1*high))):
						# 		value=2
						# elif(i<=(low+(0.2*low)) or i>=(high +(0.2*high))):
						# 		value=3
						# elif(i<=(low+(0.4*low)) or i>=(high +(0.4*high))):
						# 		value=4

						print(value)
						break

		else:
			if(i=='absent' or i=='not'):
			
					if(data.param[tname]["value"]=='negative'):
						value=1
					elif(data.param[tname]["value"]=='positive'):
						value=4
					print(value)
					break
		

			elif(i=='present' or i=='found' or i=='none'):
			
					if(data.param[tname]["value"]=='negative'):
						value=4
					elif(data.param[tname]["value"]=='positive'):
						value=1
					print(value)
					break
		
	
	return value			

					



def mapping(id):
	print("map id",id)
	avg=0
	t=0
	# with open("outpu1.txt") as openfile:
	# 	for line in openfile:  
	# 		for part in line.split():
	# 			#for i in data.param:
	# 				f= open("static/outpu1.txt","a+")
	# 				if "creatinine" in part:
	# 					print(part)
	# 					val=digitize(line,"creatinine",id)
	# 					if(val>0):
	# 						f.write("creatinine"+" %d\r\n" % val)
	# 						f.close()
	# 						print(val)
	# 						# if(val!=0):
	# 						# 	avg=avg+val
	# 						# 	t=t+1
	# 						# 	print(avg)
	# 						mydict[id]["digit_creatinine"].append(val)
	# 						output = open('patient.pkl', 'wb')
	# 						pickle.dump(mydict, output)
	# 						output.close()

	# with open("outpu1.txt") as openfile:
	# 	for line in openfile:  
	# 		for part in line.split():

	# 			if "glucose" in part:
	# 				f= open("static/outpu1.txt","a+")
	# 				print(part)
	# 				val=digitize(line,"glucose",id)
	# 				if(val>0):
	# 					f.write("glucose "+" %d\r\n" % val)
	# 					f.close()
	# 					print(val)
	# 					# if(val!=0):
	# 					# 	avg=avg+val
	# 					# 	t=t+1
	# 					# 	print(avg)
	# 					mydict[id]["digit_glucose"].append(val)
	# 					output = open('patient.pkl', 'wb')
	# 					pickle.dump(mydict, output)
	# 					output.close()

	with open("outpu1.txt") as openfile:
		f= open("static/outpu1.txt","a+")
		for line in openfile:  
			for part in line.split():
				for i in data.param:
					if(i in part):
						#if(("creatinine" not in part) or ("glucose" not in part)):
							print(part)
							val=digitize(line,i,id)
							if(val>0):
								#f= open("guru99.txt","w+")
								f.write("Parameter :"+i+" || Digitized Value %d || " % val + " "+stat+"\n")
								print(val)
								if(val!=0):
									avg=avg+val
									t=t+1
									print(avg)
								# mydict[id]["digit"].append(val)
								# output = open('patient.pkl', 'wb')
								# pickle.dump(mydict, output)
								# output.close()

		f.close()
	avg1=avg/t
	print(avg1)
	mydict[id]["digit"].append(avg1)

	output = open('patient.pkl', 'wb')
	pickle.dump(mydict, output)
	output.close()

	print(mydict)	