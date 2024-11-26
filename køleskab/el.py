import cooler as cl
import csv

class el:
        if __name__ == "__main__":
            my_cooler = cl.cooler()
            for n in range(8640):
                  my_cooler.coolerupdate(n)
        
            # Open csv file
            with open('elpris.csv', newline='', encoding='utf-8') as csvfile:
                csvreader = csv.DictReader(csvfile)
                cash = 0
                i = -1

                # Reading the header
                header = next(csvreader)  # Skipping to next header

                # Reading and processing each row
                for row in csvreader:
                    Tid = row['Tid']  # Time is in the first column
                    Pris = row['Pris']  # Price is in the second column
                    #print(f"Time: {Tid}, Price: {Pris}")
                    i+=1
                    if my_cooler.compressor_on[i-1] == True:
                        cash += float(Pris)
                
                print(cash)

                

