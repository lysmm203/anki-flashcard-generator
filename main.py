import csv

if __name__ == '__main__':

    with open('GRE_vocabs.csv') as f:
        csv_reader = csv.reader(f)
        columns = {}

        for row in csv_reader:
            print(row)