import os
import ee
import geemap
import datetime
import pandas as pd
import math
import glob

# Import the SEA points where NO2 values will be pulled from GEE
in_csv = 'https://raw.githubusercontent.com/liyangyang515/NO2-in-South-East-Asia-_GE5219/main/data/SEA_pts.csv'
pts = geemap.csv_to_pandas(in_csv)
pts

#split dataset due to capacity limit of GEE
pts_1 = pts.iloc[:25344,1:]
pts_2 = pts.iloc[25344:,1:]

#convert to ee 
ee_1 = geemap.pandas_to_ee(pts_1, latitude="lat", longitude="lon")
ee_2 = geemap.pandas_to_ee(pts_2, latitude="lat", longitude="lon")

#get daily mean (can modify the date for other period)
# This is very similar to pull monthly mean
startDate= datetime.datetime(2020,1,1)
# NO2_daily= pd.DataFrame(columns=['first','lon','lat'])
for i in range(60,700,1): #(can modify the range for other period)
    date1 = (startDate + datetime.timedelta(days=i)).strftime('%Y-%m-%d')
    date2 = (startDate + datetime.timedelta(days=(i+1))).strftime('%Y-%m-%d')
    collection = ee.ImageCollection('COPERNICUS/S5P/NRTI/L3_NO2') \
    .select('tropospheric_NO2_column_number_density') \
    .filterDate(date1, date2) 
    # Reduce the collection with a mean reducer.
    mean = collection.reduce(ee.Reducer.mean())
    out_csv1 = r'D:\GitHub\NO2-in-South-East-Asia-_GE5219\data\NO2_raw_daily\NO2_' + date1 + '_1.csv'
    out_csv2 = r'D:\GitHub\NO2-in-South-East-Asia-_GE5219\data\NO2_raw_daily\NO2_' + date1 + '_2.csv'
    geemap.extract_values_to_points(ee_1,mean,out_csv1, scale = 27750)
    geemap.extract_values_to_points(ee_2,mean,out_csv2, scale = 27750)
#     df_1 = pd.read_csv(out_csv1)
#     df_2 = pd.read_csv(out_csv2)
#     df = pd.concat([df_1, df_2])
#     df['date'] = date1
#     df['week_id'] = int(math.floor(i / 7)+1)
#     NO2_daily= pd.concat([NO2_daily,df],ignore_index=True)
# NO2_daily

# In case the NO2_daily was not saved or the process was interuppted, here is another way to import all files in the folder and concat them.
# This is not needed if NO2_daily is saved
# concat daily mean 
path = r'D:\GitHub\NO2-in-South-East-Asia-_GE5219\data\NO2_raw_daily'      
all_files = glob.glob(os.path.join(path, "*.csv"))     
concatenated_daily_mean = pd.DataFrame(columns = [])
for f in all_files:
    df_from_each_file = pd.read_csv(f)
    # create a new column to store year and month (extracted from file name)
    df_from_each_file['date'] = f[-16:-6]
    concatenated_daily_mean   = pd.concat([concatenated_daily_mean, df_from_each_file], ignore_index=True)
concatenated_daily_mean
# save to csv
concatenated_daily_mean.to_csv(r'D:\GitHub\NO2-in-South-East-Asia-_GE5219\data\NO2_raw_daily\2020_2021_daily_NO2.csv', index = False)
