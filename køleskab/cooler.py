import random
import csv

# Open csv file
with open('elpris.csv', newline='', encoding='utf-8') as csvfile:
    csvreader = csv.DictReader(csvfile)
    
    # Reading the header
    header = next(csvreader)  # Skipping to next header

    # Reading and processing each row
    for row in csvreader:
        Tid = row['Tid']  # Time is in the first column
        Pris = row['Pris']  # Price is in the second column
        print(f"Time: {Tid}, Price: {Pris}")





class cooler:
    def __init__ (self, time, PTime):
        T = []
        TKOMP = -5
        TRUM = 20
        deltatid = 300
        TMÅL = 5
    
        T[time] = PTime + (self.C1() * (TRUM - PTime) + self.C2() * (TKOMP - PTime)) * deltatid
        PTime = T(time)

    def C1():
        if doorclosed:
            return(5 * 10**-7 * 300**-1)
        else:
            return(3 * 10**-5 * 300**-1)
       
    def C2():
        if compressor_off:
            return(0 * 300**-1)
        else:
            return(8 * 10**-6 * 300**-1)
      
        
    def Termostat(TM):
      
        
for n in range(8640):
    if n == 0:
        PTime = 3.65
    cooler(n, PTime)
    doorChance= random.randrange(1,10)

pass






