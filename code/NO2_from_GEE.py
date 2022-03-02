import os
import ee
import geemap
import datetime
import pandas as pd
import math
import glob

# Import the SEA points where NO2 values will be pulled from GEE
in_csv = 'https://raw.githubusercontent.com/liyangyang515/NO2-in-South-East-Asia-_GE5219/main/data/Points_locations/SEA_pts.csv'
pts = geemap.csv_to_pandas(in_csv)
pts

#convert to ee 
ee = geemap.pandas_to_ee(pts, latitude="lat", longitude="lon")

#get daily mean (can modify the date for other period)
Date= datetime.datetime(2020,1,1)
# NO2_daily= pd.DataFrame(columns=['first','lon','lat'])
for i in range(60,780,1): #(can modify the range for other period)
    StartDate = (Date + datetime.timedelta(days=i)).strftime('%Y-%m-%d')
    EndDate = (Date + datetime.timedelta(days=(i+1))).strftime('%Y-%m-%d')
    collection = ee.ImageCollection('COPERNICUS/S5P/NRTI/L3_NO2') \
    .select('tropospheric_NO2_column_number_density') \
    .filterDate(StartDate, EndDate) 
    # Reduce the collection with a mean reducer.
    mean = collection.reduce(ee.Reducer.mean())
    out_csv = r'D:\GitHub\NO2-in-South-East-Asia-_GE5219\data\NO2_SEA_Land\NO2_raw_daily\NO2_' + StartDate + '.csv'
    geemap.extract_values_to_points(ee,mean,out_csv, scale = 27750)
#     df = pd.read_csv(out_csv)
#     df['date'] = StartDate
#     NO2_daily= pd.concat([NO2_daily,df],ignore_index=True)
# NO2_daily

# In case the NO2_daily was not saved or the process was interuppted, here is another way to import all files in the folder and concat them.
# This is not needed if NO2_daily is saved
# concat daily mean 
path = r'D:\GitHub\NO2-in-South-East-Asia-_GE5219\data\NO2_SEA_Land\NO2_raw_daily'      
all_files = glob.glob(os.path.join(path, "*.csv"))     
concatenated_daily_mean = pd.DataFrame(columns = [])
for f in all_files:
    df_from_each_file = pd.read_csv(f)
    # create a new column to store year and month (extracted from file name)
    df_from_each_file['date'] = f[-16:-6]
    concatenated_daily_mean   = pd.concat([concatenated_daily_mean, df_from_each_file], ignore_index=True)
concatenated_daily_mean
# save to csv
concatenated_daily_mean.to_csv(r'D:\GitHub\NO2-in-South-East-Asia-_GE5219\data\NO2_SEA_Land\NO2_raw_daily\2020_2021_daily_NO2.csv', index = False)
