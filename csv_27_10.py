# x = "sbsir"

# assert x == 'Royal.__balance',"_Royal.__balance"


# CSV ----> Tabular Data using comma

# Index, Name, Address
# 1,"Shr","Gnr"

import csv  # Comma Seprated Values


header = []
data = []

filename = 'heart.csv'

with open(filename, 'r') as fileref:
    csvreader = csv.reader(fileref)

    # header = next(csvreader)
    # header = next(csvreader)
    header = next(csvreader)
    print(header)   # ['Age', 'Sex', 'ChestPainType', 'RestingBP', 'Cholesterol', 'FastingBS', 'RestingECG', 'MaxHR', 'ExerciseAngina', 'Oldpeak', 'ST_Slope', 'HeartDisease']

    for d in csvreader:
        data.append(d)
        # print(d)

    # print(data)



    print("Total Lines %d"%(csvreader.line_num))


for sublist in data[:5]:
    for word in sublist:
        print("%7s"%word,end=' ')
        # print(word,end=' ')
    print()