# Riadulislam 2k15
# 06
#riadnwu@gmail.com
import random
import Queue

class Genetic_Algorithm:
    def __init__(self,n,a,fitness,l):
        self.Initial()
        self.Selection()
        #self.Fitness_Chack()
        self.Cross_Over()
        self.Mutation()

    def Initial (self):
        self.fitnessData = Queue.PriorityQueue()
        self.data = []
        temp1 = ""
        for i in range(n):
            x=random.sample(range(l),l)
            temp=""
            for j in range(l):
                temp+=`a[x[j]]`
            temp1+=temp+", "
            self.fitnessData.put((self.Fitness_Chack(temp)))
        while not self.fitnessData.empty():
            self.data.append(self.fitnessData.get()[2])
        print  "\nInitial Data:" + `temp1`
        print "Fitness Data:"+str (self.data)


    def Fitness_Chack(self,temp):
        sum = 0;
        for j in range(0,l-1):
            sub=temp[j:j+2]
            sum+=int(fitness[sub])
        return -sum,sum,temp


    def Selection(self):

        temp1 = self.Fitness_Chack(self.data[0])
        temp2 = self.Fitness_Chack(self.data[n-1])
        self.max =temp1
        self.min=temp2
        self.select1=temp1[2]
        self.select2=temp2[2]
        print "\nSelection Data1: "+str(self.select1)+" Fitness Value: "+`temp1[1]`
        print "Selection Data2: "+str(self.select2)+" Fitness Value: "+`temp2[1]`

    def Cross_Over(self):
        ln=int(l/2)
        temp1=self.select1[0:ln]+self.select2[ln:l]
        temp2=self.select2[0:ln]+self.select1[ln:l]
        print "\nCross Over Data1: "+`temp1`
        print "Cross Over Data2: " + `temp2`
        loc1= self.Match_Same_Value(temp1)
        loc2= self.Match_Same_Value(temp2)
        for i in range(len(loc1)):
            t1=temp1[loc1[i]]
            t2 = temp2[loc2[i]]
            temp1= temp1.replace(temp1[int(loc1[i])],t2,1)
            temp2 =temp2.replace(temp2[int(loc2[i])],t1,1)
        self.cross1= temp1
        self.cross2 = temp2
        print "\nSwap Same Data1: " + `self.cross1`
        print "Swap Same Data2: " + `self.cross2`

    def Match_Same_Value(self,temp):
        loc=[]
        x=[]
        for i in temp:
            if i not in x:
                 x.append(i)
                 a=[]
                 a=([pos for pos, char in enumerate(temp) if char == i])
                 if len(a)>1:
                     loc.append(a[0])
        return loc
    def Mutation(self):
        x1=random.sample(self.cross1,2)
        temp1 = self.cross1.replace(x1[0],x1[1], 1).replace(x1[1],x1[0], 1)
        x2= random.sample(self.cross2, 2)
        temp2 = self.cross2.replace(x2[0], x2[1], 1).replace(x2[1], x2[0], 1)
        mutation1=self.Fitness_Chack(temp1)
        mutation2 = self.Fitness_Chack(temp2)
        self.Max_Min(mutation1)
        self.Max_Min(mutation2)
        print "\nMutation Data1: "+`mutation1[2]`+" Fitness Value: "+`mutation1[1]`
        print "Mutation Data2: " + `mutation2[2]`+" Fitness Value: "+`mutation2[1]`
        print "\nMaximum Data:"+`self.max[2]`+" Fitness Value: "+`self.max[1]`
        print "Minimum Data:" + `self.min[2]` + " Fitness Value: " + `self.min[1]`

    def Max_Min(self,data):
        if int(data[1]) > int(self.max[1]):
            self.max=data
        elif int(data[1]) < int(self.min[1]):
            self.min=data



def Fitness_Value(a,fitness,l):
    for i in range(l):
        for j in range(l):
            if(i==j):
                fitness[`a[i]`+`a[j]`]=0
                print str(a[i])+" -> "+str (a[j])+" : 0"
            else:
                fitness[`a[i]`+`a[j]`]=input(str(a[i])+" -> "+str (a[j])+" :")
    return fitness

x=input("How many Number:")
a=[]
for i in range(x):
  a.append(input("Enter Your "+str(i+1)+" Value:"))
l=len(a)
n=input("How Mamy Initial Value:")
fitness={}
print ("Enter Fitness Value:")
fitness=Fitness_Value(a,fitness,l)

'''n = 10
a = [1, 2, 3, 4]
l=len(a)
fitness={"11":0,"12":4,"13":5,"14":6,"21":4,"22":0,"23":5,"24":6,
         "31":5,"32":4,"33":0,"34":6,"41":1,"42":4,"43":5,"44":0}'''

print "Number List:"+`a`+"   Initial Length:"+`n`
print "Fitness List:"+`fitness`
oj= Genetic_Algorithm(n,a,fitness,l)