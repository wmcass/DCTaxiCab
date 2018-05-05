'''
@author:     Will

description: clean and reformat DC taxi cab data
'''

## Packages & Directories
import pandas as pd
import numpy as np
import re

root = r'/project/rcc/deep_learning_hack/dc-taxi/DCTaxiCab/'

## Data
feb = pd.read_csv(root + 'data/2017/taxi_2017_02.txt', sep='|', nrows=10000)

feb.columns = \
    ['object_id', 'trip_type', 'provider', 'meterfare', 'tip', 'surcharge', 
     'extras', 'tolls', 'total_amount', 'payment_type',
     'payment_card_provider', 'pickup_city', 'pickup_state', 'pickup_zip', 
     'dropoff_city', 'dropoff_state', 'dropoff_zip', 'trip_mileage', 
     'trip_time', 'pickup_block_latitude', 'pickup_block_longitude', 
     'pickup_blockname', 'dropoff_block_latitude', 'dropoff_block_longitude',
     'dropoff_blockname', 'airport', 'pickupdatetime_tr', 'dropoffdatetime_tr']

for col in feb.columns.tolist():
    feb[col] = feb[col].astype(str).apply(lambda x: re.sub('^(\s)*', '', x))

del feb['trip_time']

feb.pickupdatetime_tr = pd.to_datetime(feb.pickupdatetime_tr)
feb.dropoffdatetime_tr = pd.to_datetime(feb.dropoffdatetime_tr)

feb.to_csv(root + 'data/intermediate/taxi_2017_02.txt')

