import random
import csv
import el




class cooler:
    def __init__ (self):

        print("check")

        self.TKOMP = -5
        self.TRUM = 20
        self.deltatid = 300
        self.T = []
        TMÅL = 5



    def coolerupdate(self, time):
        if time == 0:
            self.T.append(5)
            
        else:
            self.T.append(self.T[time-1] + (self.C1() * (self.TRUM - self.T[time-1]) + self.C2(self.T[time-1]) * (self.TKOMP - self.T[time-1])) * self.deltatid)



    def C1(self):
        #is the door open or closed
        doorChance = random.randrange(0,9)
        if doorChance == 1:
            return(3 * 10**-5)
        else:
            return(5 * 10**-7)
            
       
    def C2(self, Temp):
        if Temp > 5:
            print(Temp)
            #this turns the compressor on
            return(8 * 10**-6)
        else:
            #this turn the compresso off
            return(0 * 300** -1)
      
        


'


'
if __name__ == "__main__":
    el

    my_cooler = cooler()
    for i in range(8640):
        my_cooler.coolerupdate(i)




