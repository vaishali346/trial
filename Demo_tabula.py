import tabula
import csv
import pandas as pd 
#import img2pdf
# Read pdf into DataFrame

df = tabula.read_pdf(r"C:\Programs\data.pdf", output_format= "dataframe", encoding = 'utf-8',)

tabula.convert_into(r"C:\Programs\data.pdf", r"C:\Programs\Output\outputOfTabula.csv", output_format="csv")

dataframe = pd.read_csv(r"C:\Programs\Output\outputOfTabula.csv")
print(dataframe)

with open(r"C:\Programs\Output\outputOfTabula.txt", "w") as my_output_file:
    with open(r"C:\Programs\Output\outputOfTabula.csv", "r") as my_input_file:
        [ my_output_file.write(" ".join(row)+'\n') for row in csv.reader(my_input_file)]
    my_output_file.close()
