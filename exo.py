#1
var=1
print(var)

#2
age=25
prenom="Vincent"
concat="je suis {} et j'ai {}".format(prenom,age)
print(concat)

#3
age,prenom=25,"Vincent"

#4
age=10
print(age*4)

#5
var=2
var+=1
print(var)
var=var+1
print(var)

#6
var=2
var-=1
print(var)
var=var-1
print(var)

#7
var=2
var*=2
print(var)
var=var*2
print(var)

#8
var=2
var/=2
print(var)
var=var/2
print(var)

#9
a=1
b=2
c=b
b=a
a=c

#10
a=b=10
a,b=10,10
a=10
b=10

#11
a=10
print(a)
print(a/2)
print(a//2)
print(a%2)
print(a**2)

#12
def get_price_TTC(ht, nbr):
	return (int(ht)*int(nbr)*1.2)
#nbre=input("Nbre d'article \n") 
#price=input("Prix HT \n")
#print(get_price_TTC(price, nbre)) 


#13
liste=[3,4]
print(liste)

#14
liste=[3,4,"oui", "non"]
print(liste)
print(liste[0])
print(liste[2])

#15
x=[1,2]
y=[3,4]
z=x+y
print(z)

#16
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(x[3])
#print([nb for nb in [nb for nb in x if nb >=3] if nb < 5 ])
print(x[3:5])
#print([nb for nb in [nb for nb in [nb for nb in x if nb%2==0] if nb >=2] if nb < 8 ])
print(x[3:5:2])
print(len(x))
print(min(x))
print(max(x))
print(sum(x))
del x[2:4]


#17
x = ["ok", 4, 2, 78, "bonjour"]
print(x[3])
x[1]="toto"
print(x)

#18
liste=[0,1,2,3,4,5]
liste=range(0,6)

#19
x={"key": 'valeur', "key2": "valeur2"}
print(x)
print(x["key"])
x["titi"]="toto"
x["titi"]="tata"
del x["titi"]
x.pop("key")
print(x)
y=x
print(y)


#20
x=(["a","b"],["c","d"],["e","f"],["g","h"])
print(x)



###########################TEST###################################

#1
def main():
	nbre=input("Quel est votre chiffre ? \n")
	if(int(nbre)==0):
		print("nul")
	
	elif(int(nbre)>0):
		print("positif")
	
	else:
		print("negatif")
#main()

#2
def main():
	nbre=input("Quel est votre age ? \n")
	if(int(nbre)>=18):
		print("Majeur")
	
	else:
		print("mineur")
#main()

#3
def main():
	nbre=input("Quel est votre nombre ? \n")
	if(int(nbre)>5 and int(nbre)>10 ):
		print("vrai")
	
	else:
		print("faux")
#main()

#4
def main():
	nbre=input("Quel est votre nombre ? \n")
	if( int(nbre)==6 or int(nbre)==7 or int(nbre)==8 or int(nbre)==9  ):
		print("vrai")
	
	else:
		print("faux")
#main()


#############BOUCLE############################
 #1

liste="012345";
for l in liste:
	print(l)

#2
liste=["Php", "C++", "Ruby"]
for l in liste:
	print(len(l))

#3
x = "anticonstitutionnellement"
for y in x:
	print(y)

#4
x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for y in x:
	for z in y:
		print(z)

#5
x = [1,10,20,30,40,50]
z=0
for y in x:
	z+=y
print(z)
print(sum(x))

#6
for i in range(6):
	print(i)

#7
for i in range(1,10):
	if(i<4):
		print(i)

#8
for i in range(1,10):
	if(i==1):
		un=i
	elif(i==2):
		deux=i
	elif(i==3):
		trois=i
		
#9
for i in range(1,10):
	if(i!=3):
		print(i)

#10
ordi = ["apple", "asus", "dell", "samsung"]
i=0
while (i<4):
	print(ordi[i])
	i+=1

#11
#inputs=input("Quel est votre mot ? \n")
#while (inputs!="exit"):
#	inputs=input("Quel est votre mot ? \n")

#12

i=0
while (i<101):
	if(i%5==0):
		print(i)
	
	i+=1


############FONCTION###################
#1
#nbre=input("Nombre a multiplier \n")
def main(nbr):
	return int(nbr)*5
#print(main(nbre))

#2
nbre=[1,2,3,4,5,6,7,8,9,10]

def main(nbres):
	pair=[]
	for nbr in nbres:
		if(nbr%2==0):
			print(nbr)
	
main(nbre)

#3
#nbre=input("Nombre \n")
def main(nbre):
	y=[1]
	index=len(y)-1
	while ( y[index]+y[index-1]<int(nbre)) :
		if(len(y)<3):
			y=y+[1]
		else:
			index=len(y)-1
			print(y[index]+y[index-1])
			y=y+[y[index]+y[index-1]]
			index=len(y)-1
			
#main(nbre)

#4
string="Python 4 ever"
def main(string):
	i=0
	voyelle=["a", 'e', "y", "o", "u", "i"]
	for char in string:
		if char in voyelle:
			i+=1
	return i
print(main(string))

string="azertyuiop^zyapoeoi"
def main(string):
	i=0
	y=0
	voyelle=["a", 'e', "y", "o", "u", "i"]
	length=len(string)
	while(i<length):
		if string[i] in voyelle:
			y+=1
		i+=1
	return (y)
print(main(string))

#pas compris

#5
nbre=input("Nombre factorielle \n")
def main(nbre):
	y=1
	for x in range(1, int(nbre)+1):
		y*=x
	return y
print(main(nbre))


#6
nbre=input("Nombre factorielle \n")
y=1
x=1
def main(nbre,y,x):
	if(y<=int(nbre)):	
		x=x*y
		y=y+1
		main(nbre,y,x)
	else:
		print(x)
		#return x   Pourquoi ça ne marche pas ???,
main(nbre,y,x)

