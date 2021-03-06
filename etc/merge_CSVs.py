import pandas as pd
import sys

dataframes = []

if len(sys.argv) > 1:
    outfile = sys.argv[1]
    print "Merging into " + outfile
    for num in range(1, len(sys.argv)):
        if (".csv" in sys.argv[num]) is False:
            print "Not a .csv: " + sys.argv[num]
        else :
            dataframes.append(pd.read_csv(sys.argv[num]))

else:
    print "Usage:   python merge_CSVs.py file1.csv file2.csv ..."

merged = pd.concat(dataframes)

merged.to_csv(outfile, index=False)
