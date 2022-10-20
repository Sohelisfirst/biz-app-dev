'''python program to calculate the time required
to meet both the cockroaches'''
# speed of 1st cackroach for 1 sec
a=1
#speed of 2nd cackroach for 1 sec
b=2 
#speed of two cackroachs
c=3
#total distance to be covered
d=100
#time required to travel 100 m
f=100/3
#now deduction for the cackroach backward
g=int(f/10)*2
#distance travelled by the 1st coackroach  in f sec
h=f-g
#distance covered by  2nd coackroach in f secs
i=(f*2)-(g*2+1)
#actual distance coverd by  both coackroaches
j=h+i
#remaining distance to be covered by the coackroaches
k=(d-j)+1
#how much time required to cover remaining distance
l=k/3
#total time
print("total time required to meet both the cockroaches is:",f+l,"seconds")



