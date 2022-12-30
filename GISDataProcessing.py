import pandas as pd
import numpy as np
import geopandas

data = geopandas.read_file('./datasets/Population_Ward_Level.shp')

# largest_area_ward = data.loc[data['Shape_Area'].idxmax()]

# print('Phường có diện tích lớn nhất là phường', largest_area_ward[0] + ', quận ' + largest_area_ward[1]) 

# largest_pop_2019_ward = data.loc[data['Pop_2019'].idxmax()]

# print('Phường có dân số 2019 cao nhất là phường', largest_pop_2019_ward[0] + ', quận ' + largest_pop_2019_ward[1])

# smallest_area_ward = data.loc[data['Shape_Area'].idxmin()]

# print('Phường có diện tích nhỏ nhất là phường', smallest_area_ward[0] + ', ' + smallest_area_ward[1])

# smallest_pop_2019_ward = data.loc[data['Pop_2019'].idxmin()]

# print('Phường có dân số 2019 thấp nhất là phường', smallest_pop_2019_ward[0] + ', ' + smallest_pop_2019_ward[1])

# fastest_increase = 0;
# for i in range(0, len(data), 1):
#   if ((data['Pop_2019'][fastest_increase] / data['Pop_2009'][fastest_increase]) < (data['Pop_2019'][i] / data['Pop_2009'][i])):
#     fastest_increase = i;
# print('Phường có tốc độ tăng trưởng dân số nhanh nhất là: ' + data['Com_Name'][fastest_increase] + ', ' + data['Dist_Name'][fastest_increase]);

# slowest_increase = 0;
# for i in range(0, len(data), 1):
#   if ((data['Pop_2019'][slowest_increase] / data['Pop_2009'][slowest_increase]) > (data['Pop_2019'][i] / data['Pop_2009'][i])):
#     slowest_increase = i;
# print('Phường có tốc độ tăng trưởng dân số chậm nhất là: ' + data['Com_Name'][slowest_increase] + ', ' + data['Dist_Name'][slowest_increase]);

# fluctuate_most = 0;
# for i in range(0, len(data), 1):
#   if ((data['Pop_2019'][fluctuate_most] - data['Pop_2009'][fluctuate_most]) < (data['Pop_2019'][i] - data['Pop_2009'][i])):
#     fluctuate_most = i;
# print('Phường có biến động dân số nhanh nhất là: ' + data['Com_Name'][fluctuate_most] + ', ' + data['Dist_Name'][fluctuate_most]);

# fluctuate_least = 0;
# for i in range(0, len(data), 1):
#   if ((data['Pop_2019'][fluctuate_least] - data['Pop_2009'][fluctuate_least]) > (data['Pop_2019'][i] - data['Pop_2009'][i])):
#     fluctuate_least = i;
# print('Phường có biến động dân số chậm nhất là: ' + data['Com_Name'][fluctuate_least] + ', ' + data['Dist_Name'][fluctuate_least]);

# highest_density_ward = data.loc[data['Den_2019'].idxmax()]

# print('Phường có diện tích lớn nhất là phường', highest_density_ward[0] + ', quận ' + highest_density_ward[1]) 

# lowest_density_ward = data.loc[data['Den_2019'].idxmin()]

# print('Phường có diện tích lớn nhất là phường', lowest_density_ward[0] + ', quận ' + lowest_density_ward[1]) 

temp = data.nlargest(5, 'Den_2019');
print(temp);