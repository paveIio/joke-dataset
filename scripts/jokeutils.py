
# http://www.racketracer.com/2016/07/06/pandas-in-parallel/

def parallel_dataframe(dataframe, func):
    from multiprocessing import Pool
    import numpy as np
    #redundant
    import pandas as pd
    #4 CPUs with 10 partitions
    dframe_split = np.array_split(dataframe, 10)
    pool = Pool(4)
    dframe = pd.concat(pool.map(func, dframe_split))
    pool.close()
    pool.join()
    return dframe

def parse_args():
    import sys
    if len(sys.argv) > 1:
        infile = sys.argv[1]
    else:
        print("Usage:   python " + sys.argv[0] +" infile.csv")
        sys.exit()
    return infile

def outfile_name(title):
    from time import strftime
    outfile = title + "_at_" + strftime("%Y-%m-%d_%H:%M") + ".csv"
    return outfile
