import random
import el
import doctest


class cooler:
    """
    this module is for caculating when the compressor is on and when the door is open
     
    """
    def __init__ (self):

        print("check")

        #the general variables
        self.TKOMP = -5
        self.TRUM = 20
        self.deltatid = 300
        self.T = []
        self.compressor_on = []
        self.price = 0

        #updates the big fridge -_-
    def coolerupdate(self, time):
        """
        >>> test.coolerupdate(0)
        >>> len(test.T)  # Ensures that a temperature is added
        1
        >>> test.coolerupdate(1)
        >>> len(test.T)  # Ensures that another temperature is added
        2
        """
        if time == 0:
            self.T.append(5)
            
        else:
            self.T.append(self.T[time-1] + (self.C1() * (self.TRUM - self.T[time-1]) + self.C2(self.T[time-1]) * (self.TKOMP - self.T[time-1])) * self.deltatid)


        #Door
    def C1(self):
        """
        
        >>> test.C1()  # Fixed value for predictable testing
        3e-05
        
        """
        #is the door open or closed
        self.doorChance = random.randint(0,9)
        if self.doorChance == 1:
            return(3 * 10**-5)
        else:
            return(5 * 10**-7)
            
        #Compressor
    def C2(self, Temp):
        """
        >>> [test.C2(val) for val in [6, 4]]
        [8e-06, 0.0]

        """
        if Temp > 5.949: #dette er det den "smarte" loesning, da den fjernede flere kroner fra prisen end hvis man bare havde den "normale" loessning som var en starttal på 6.
            self.compressor_on.append(True)
            #this turns the compressor on
            return(8 * 10**-6)
            
        else:
            #this turn the compresso off
            self.compressor_on.append(False)
            return(0 * 300** -1)
      
        


if __name__ == "__main__":
    #does so the douments communicates
    doctest.testmod(extraglobs={"test" : cooler()})
    el
    my_cooler = cooler()
    for n in range(8640):
        my_cooler.coolerupdate(n)




