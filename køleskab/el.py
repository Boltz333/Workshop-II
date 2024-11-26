  

class el:

    def elpris():
        # Open csv file
            with open('elpris.csv', newline='', encoding='utf-8') as csvfile:
                csvreader = csv.DictReader(csvfile)
                
                # Reading the header
                header = next(csvreader)  # Skipping to next header

                # Reading and processing each row
                for row in csvreader:
                    Tid = row['Tid']  # Time is in the first column
                    Pris = row['Pris']  # Price is in the second column
                    #print(f"Time: {Tid}, Price: {Pris}")