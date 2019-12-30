# -*- coding: utf-8 -*-
"""
This file read all data points and combine the data into minutes,
and store the data into pandas object for LSTM - RNN to model and make a prediction
@author: Kai
"""
from datetime import datetime, timedelta

import pandas as pd
import numpy as np

import sys
import subprocess

from influxdb import DataFrameClient


# import matplotlib as plt


class StockDataToFromfluxDB:
    def __init__(self, s_host="127.0.0.1", i_port=8086, s_username='', s_password='', s_trans_db='stocktrans',
                 s_stock_daily_db='stockdaily'):
        self.host = s_host
        self.port = i_port
        self.username = s_username
        self.password = s_password

        self.stock_trans_db = s_trans_db
        self.stock_daily_db = s_stock_daily_db

        self.stock_daily_db_client = DataFrameClient(host=self.host, port=self.port,
                                                     username=self.username, password=self.password,
                                                     database=self.stock_daily_db)

    def read_one_stock_data_in_a_range(self, s_stock_id, s_from_day, s_to_day):

        str_full_from_time_am = s_from_day + 'T09:25:00Z'
        str_full_to_time_am = s_from_day + 'T11:30:03Z'

        str_full_from_time_pm = s_to_day + 'T13:00:00Z'
        str_full_to_time_pm = s_to_day + 'T15:00:04Z'

        # 2018-02-01T09:25:00.000011Z

        str_stock_id = self.normalize_market_stock_id(s_stock_id)

        #        str_from_day = self.get_next_day_str(s_from_day)
        #        str_to_day = self.get_next_day_str(s_to_day)

        #        influxql = 'SELECT time, Price, Vol, Type, BuyOrdVol, BuyOrdID, SellOrdVol, SellOrdID FROM "' + self.stock_trans_db + '"."autogen"."'  + str_stock_id + '" WHERE time >= \'' + s_from_day + '\' AND time <= \'' + s_to_day + '\''

        influxql = 'SELECT SUM("Vol") as "sum_vol", SUM("Amount") / SUM("Vol") as "wm_price", SUM("BuyVol") as "buy_vol" FROM "' + self.stock_trans_db + '"."autogen"."' + str_stock_id + '" WHERE time >= \'' + str_full_from_time_am + '\' AND time <= \'' + str_full_to_time_am + '\' GROUP BY time(5m)'

        #        influxql ='SELECT SUM("Vol") as "sum_vol", SUM("Amount") / SUM("Vol") as "wm_price", SUM("BuyOrdVol") as "buy_ord_vol", SUM("SellOrdVol") as "sell_ord_vol"  FROM "' + self.stock_trans_db + '"."autogen"."'  + str_stock_id + '" WHERE time BETWEEN \'' + str_full_from_time_am + '\' AND time <= \'' + str_full_to_time_am + '\' AND Type = \'' + str_order_type + '\' GROUP BY time(1s)'

        #        influxql = 'SELECT SUM("Vol") as "sum_vol", SUM("Amount") / SUM("Vol") as "wm_price", SUM("BuyOrdVol") as "buy_ord_vol", SUM("SellOrdVol") as "sell_ord_vol"  FROM "' + self.stock_trans_db + '"."autogen"."'  + str_stock_id + '" WHERE (time >= \'' + str_full_from_time_am + '\' AND time <= \'' + str_full_to_time_am +  '\') AND (time >= \'' + str_full_from_time_pm + '\' AND time <= \'' + str_full_to_time_pm +  '\') AND Type = \'' + str_order_type + '\' GROUP BY time(1s)'

        cmd = ['E:\\Program Files\\InfluxData\\Influxdb\\influx.exe', '-format', 'csv', '-precision', 'rfc3339',
               '-database', self.stock_trans_db, '-execute', influxql]

        proc = subprocess.Popen(cmd, stdout=subprocess.PIPE)

        is_data_empty = False
        if sys.version_info[0] < 3:
            from StringIO import StringIO
        else:
            from io import StringIO

        str_output = StringIO(proc.communicate()[0].decode('utf-8'))

        df_db_data = None

        try:
            df_db_data = pd.read_csv(str_output, sep=',', low_memory=False)

        except pd.errors.EmptyDataError:
            is_data_empty = True
            print('It seems stock of ' + s_stock_id + ' was not trading on ' + s_from_day + '. Skipped reading data.')
            return is_data_empty, df_db_data

        try:
            df_db_data['wm_price'].fillna(method='ffill', inplace=True)
            df_db_data['wm_price'].fillna(method='bfill', inplace=True)
            df_db_data.fillna(0, inplace=True)
        except TypeError:
            print('no wm_price available, skipped.')
            return df_db_data

        try:
            df_db_data.drop(df_db_data.tail(1).index, inplace=True)
        except AttributeError:
            print('no data on the last row, skipped')

        influxql = 'SELECT SUM("Vol") as "sum_vol", SUM("Amount") / SUM("Vol") as "wm_price", SUM("BuyVol") as "buy_vol" FROM "' + self.stock_trans_db + '"."autogen"."' + str_stock_id + '" WHERE time >= \'' + str_full_from_time_pm + '\' AND time <= \'' + str_full_to_time_pm + '\' GROUP BY time(5m)'

        #        influxql = 'SELECT SUM("Vol") as "sum_vol", SUM("Amount") / SUM("Vol") as "wm_price", SUM("BuyOrdVol") as "buy_ord_vol", SUM("SellOrdVol") as "sell_ord_vol"  FROM "' + self.stock_trans_db + '"."autogen"."'  + str_stock_id + '" WHERE (time >= \'' + str_full_from_time_am + '\' AND time <= \'' + str_full_to_time_am +  '\') AND (time >= \'' + str_full_from_time_pm + '\' AND time <= \'' + str_full_to_time_pm +  '\') AND Type = \'' + str_order_type + '\' GROUP BY time(1s)'

        cmd2 = ['E:\\Program Files\\InfluxData\\Influxdb\\influx.exe', '-format', 'csv', '-precision', 'rfc3339',
                '-database', self.stock_trans_db, '-execute', influxql]

        proc2 = subprocess.Popen(cmd2, stdout=subprocess.PIPE)

        is_data_empty = False
        if sys.version_info[0] < 3:
            from StringIO import StringIO
        else:
            from io import StringIO

        str_output2 = StringIO(proc2.communicate()[0].decode('utf-8'))

        df_db_data2 = None

        try:
            df_db_data2 = pd.read_csv(str_output2, sep=',', low_memory=False)

        except pd.errors.EmptyDataError:
            is_data_empty = True
            print('no data')

        try:
            df_db_data2['wm_price'].fillna(method='ffill', inplace=True)
            df_db_data2['wm_price'].fillna(method='bfill', inplace=True)
            df_db_data2.fillna(0, inplace=True)
        except TypeError:
            print('skipped')

        dfs = [df_db_data, df_db_data2]

        try:

            df_am_pm_data = pd.concat(dfs)
        except ValueError:
            df_am_pm_data = dfs

        print('Finished reading database of stock of ' + s_stock_id + ' of ' + s_from_day + ', at: ' + str(
            datetime.now()))

        return is_data_empty, df_am_pm_data

    def read_daily_data_by_stock_id_and_date_range(self, s_stock_id, s_from_day, s_to_day):

        str_stock_id = self.normalize_market_stock_id(s_stock_id)

        dict_query = self.stock_daily_db_client.query(
            'SELECT adj_factor, close, open, high, low, vol from ' + str_stock_id + ' WHERE time >= \'' + s_from_day + '\' AND time <= \'' + self.get_next_day_str(
                s_to_day) + '\'')

        return dict_query[str_stock_id]

    def read_daily_index_data_by_id_and_date_range(self, s_index_key, s_from_day, s_to_day):

        indices = {'SH': 'SH000001', 'HS300': 'SZ399300', 'SZ50': 'SH000016', 'SZ': 'SZ399001', 'ZZ500': 'SH000905',
                   'CYB': 'SZ399006'}

        str_index_id = indices[s_index_key]

        dict_query = self.stock_daily_db_client.query(
            'SELECT close, open, high, low, vol from ' + str_index_id + ' WHERE time >= \'' + s_from_day + '\' AND time <= \'' + self.get_next_day_str(
                s_to_day) + '\'')

        return dict_query[str_index_id]

    def get_next_day_str(self, s_day):

        dt_next_day = datetime.strptime(s_day, '%Y-%m-%d')
        dt_next_day = dt_next_day + timedelta(days=1)

        str_next_day = str(dt_next_day.year).zfill(4) + '-' + str(dt_next_day.month).zfill(2) + '-' + str(
            dt_next_day.day).zfill(2)
        return str_next_day

    def normalize_market_stock_id(self, s_stock_id):

        #  normalize prefix of all stocks for writing data to influxdb: if the source csv file starts with 'S', then use the first 8 letters,
        #  if start with '6', it's stock from Shanghai (SH) market, if start with '3' or '0', it's from Shenzhen market (SZ).

        stock_first_name = s_stock_id[0]
        stk_id = ''
        if stock_first_name == 'S':
            stk_id = s_stock_id[0:8]
        elif stock_first_name == '6':
            stk_id = 'SH' + s_stock_id[0:6]
        elif stock_first_name == '3' or stock_first_name == '0':
            stk_id = 'SZ' + s_stock_id[0:6]

        return stk_id

    def get_all_days_str_to_list_in_between(self, s_from_day, s_to_day):

        from_datetime_obj = datetime.strptime(s_from_day, '%Y-%m-%d')

        to_datetime_obj = datetime.strptime(s_to_day, '%Y-%m-%d')

        delta = to_datetime_obj - from_datetime_obj

        lst_days = []

        for i in range(delta.days + 1):
            a_day = from_datetime_obj + timedelta(i)
            lst_days.append(str(a_day.year).zfill(4) + '-' + str(a_day.month).zfill(2) + '-' + str(a_day.day).zfill(2))

        return lst_days

    def get_daily_trans_dataframe_from_influxdb(self, s_stock_id, s_day):

        str_from_day = s_day

        next_day_obj = datetime.strptime(str_from_day, '%Y-%m-%d')
        # next_day_obj = next_day_obj + timedelta(days = 1)

        str_to_day = str(next_day_obj.year).zfill(4) + '-' + str(next_day_obj.month).zfill(2) + '-' + str(
            next_day_obj.day).zfill(2)

        # initialize list of lists
        is_empty, df_daily_stock_trans_data = self.read_one_stock_data_in_a_range(s_stock_id, str_from_day, str_to_day)

        return is_empty, df_daily_stock_trans_data

    def format_tushare(self, s_day, s_stock_id):
        str_tushare_date = ''
        str_tushare_stock_id = ''
        list_date = s_day.split('-')

        for item in list_date:
            str_tushare_date += item
        str_tushare_stock_id = s_stock_id[2:] + '.' + s_stock_id[0:2]

        return str_tushare_date, str_tushare_stock_id

    def store_stock_trans_data_in_dict(self, s_stock_id, df_adj_factor):

        lst_day_str_range = df_adj_factor.index.values.tolist()

        # creating two dictionaries for storing adj_factors and close data
        dict_adj_factors = {}
        dict_close = {}
        dict_open = {}
        dict_high = {}
        dict_low = {}
        dict_vol = {}

        for int_timestamp in lst_day_str_range:
            flt_adj_factor = df_adj_factor.loc[int(int_timestamp), 'adj_factor']
            flt_close = df_adj_factor.loc[int(int_timestamp), 'close']
            flt_open = df_adj_factor.loc[int(int_timestamp), 'open']
            flt_high = df_adj_factor.loc[int(int_timestamp), 'high']
            flt_low = df_adj_factor.loc[int(int_timestamp), 'low']
            flt_vol = df_adj_factor.loc[int(int_timestamp), 'vol']

            # Convert timestamp to datetime object
            dt_one_day = datetime.fromtimestamp(int_timestamp / 1e9)
            str_day = str(dt_one_day.year).zfill(4) + '-' + str(dt_one_day.month).zfill(2) + '-' + str(
                dt_one_day.day).zfill(2)

            # storing adjfactor and close data to the two temporary dictionaries
            dict_adj_factors[str_day] = flt_adj_factor
            dict_close[str_day] = flt_close
            dict_open[str_day] = flt_open
            dict_high[str_day] = flt_high
            dict_low[str_day] = flt_low
            dict_vol[str_day] = flt_vol.astype(int)

        dict_stock_data = {}

        for int_timestamp in lst_day_str_range:

            dt_one_day = datetime.fromtimestamp(int_timestamp / 1e9)
            str_day = str(dt_one_day.year).zfill(4) + '-' + str(dt_one_day.month).zfill(2) + '-' + str(
                dt_one_day.day).zfill(2)
            lst_stock_data = []

            if_empty, df_stk_data = self.get_daily_trans_dataframe_from_influxdb(s_stock_id, str_day)
            flt_adj_factor = dict_adj_factors[str_day]
            flt_close

            if not if_empty:
                lst_stock_data.append(df_stk_data)

            else:
                lst_stock_data.append(None)
            lst_stock_data.append(dict_adj_factors[str_day])
            lst_stock_data.append(dict_close[str_day])
            lst_stock_data.append(dict_open[str_day])
            lst_stock_data.append(dict_high[str_day])
            lst_stock_data.append(dict_low[str_day])
            lst_stock_data.append(dict_vol[str_day])

            dict_stock_data[str_day] = lst_stock_data
        return dict_stock_data

    def get_trans_day_moment_day_number(self, d_final_order, str_current_day_str, i_trans_days_compare_return):

        lst_trans_days = list(list(d_final_order.keys()))

        i_day_index = lst_trans_days.index(str_current_day_str)

        i_pre_day_count = 1

        i_actual_trans_days = i_trans_days_compare_return

        found_trans_day_num = 0
        while found_trans_day_num < i_trans_days_compare_return:
            str_day_before = lst_trans_days[i_day_index - i_pre_day_count]
            if d_final_order[str_day_before][0] is not None:
                found_trans_day_num += 1
            else:
                i_actual_trans_days += 1
            i_pre_day_count += 1

        return i_actual_trans_days

    def create_dataset(self, d_final_order, i_trans_days_compare_return, i_trans_days_to_calculate_moment_long,
                       i_trans_days_to_calculate_moment_short):
        df_final_combined = pd.DataFrame()
        lst_trans_days = list(list(d_final_order.keys()))
        segments_in_a_day = len(list(d_final_order.values())[0][0])
        for key, value in d_final_order.items():
            try:
                #                final_order_data[key]
                final_order_data[key][0]['adj_wm_price'] = d_final_order[key][0]['wm_price'] * d_final_order[key][1]
                #                final_buy_order_data[key][0]['adj_wm_price'] = d_final_buy_order[key][0]['wm_price'] * d_final_buy_order[key][1]
                #                final_order_data[key][0]['trans_ype'] = '0'
                #                final_buy_order_data[key][0]['trans_ype'] = '1'

                combined_df = final_order_data[key][0]





            except TypeError:
                print('Data on:' + key + ' has no transaction data.')
                continue
            except IndexError:
                print('The date is on the begining of the available data, moment no available.')
                return df_final_combined

            try:
                str_day_after_compare_days = lst_trans_days[lst_trans_days.index(key) + i_trans_days_compare_return]
                combined_df['future_close'] = d_final_order[str_day_after_compare_days][1] * \
                                              d_final_order[str_day_after_compare_days][2]
            #                float_adj_price_after_compare_days = d_final_order[str_day_after_compare_days][1] * d_final_order[str_day_after_compare_days][2]
            #                combined_df['return'] = (combined_df['adj_wm_price'] - float_adj_price_after_compare_days) / float_adj_price_after_compare_days

            except TypeError:
                print('Data on:' + key + ' has no transaction data.')
                continue
            except IndexError:
                print('No future close data is available for: ' + key)
                combined_df['future_close'] = np.NaN

                # combined_df['revnue'] = np.where(combined_df['return'] > 0, 1, 0)

            #                combined_df['revnue'] = pd.cut(combined_df['return'], [-np.inf, -0.02,  0.02, np.inf], labels=[0,1,2])

            combined_df.sort_values(by='time', ascending=True, inplace=True)
            #                combined_df.drop(combined_df.tail(1).index,inplace=True)
            combined_df.drop(columns=['name'], inplace=True)

            combined_df.drop(columns=['wm_price'], inplace=True)
            #
            #            combined_df.drop(columns=['buy_vol'], inplace=True)
            #
            #            combined_df.drop(columns=['sell_vol'], inplace=True)

            #                combined_df.drop(columns=['return'], inplace=True)

            combined_df.reset_index(inplace=True, drop=True)
            combined_df['time'] = pd.to_datetime(combined_df['time'])
            combined_df = combined_df.set_index('time')
            # df_final_combined = pd.concat(df_final_combined, combined_df, ignore_index=True)
            df_final_combined = df_final_combined.append(combined_df, sort=False)

            df_final_combined['price_moment_long'] = df_final_combined['adj_wm_price'].pct_change(
                periods=i_trans_days_to_calculate_moment_long * segments_in_a_day)

            #            df_final_combined['price_moment_short'] = df_final_combined['adj_wm_price'].pct_change(periods=i_trans_days_to_calculate_moment_short*segments_in_a_day)

            df_final_combined['sum_vol_roll'] = df_final_combined['sum_vol'].rolling(min_periods=1,
                                                                                     window=segments_in_a_day).sum()

            df_final_combined['vol_moment_long'] = df_final_combined['sum_vol_roll'].pct_change(
                periods=i_trans_days_to_calculate_moment_long * segments_in_a_day)

            #            df_final_combined['vol_moment_short'] = df_final_combined['sum_vol_roll'].pct_change(periods=i_trans_days_to_calculate_moment_short*segments_in_a_day)

            df_final_combined['buy_vol_roll'] = df_final_combined['buy_vol'].rolling(min_periods=1,
                                                                                     window=segments_in_a_day).sum()

            df_final_combined['buy_ratio_roll'] = df_final_combined['buy_vol_roll'] / df_final_combined['sum_vol_roll']

            df_final_combined['buy_ratio_long'] = df_final_combined['buy_ratio_roll'].pct_change(
                periods=i_trans_days_to_calculate_moment_long * segments_in_a_day)

            #            df_final_combined['buy_ratio_short'] = df_final_combined['buy_ratio_roll'].pct_change(periods=i_trans_days_to_calculate_moment_short*segments_in_a_day)

            #            df_final_combined.drop(columns=['sum_roll_vol'], inplace=True)

            print('Data on:' + key + ' has been included.')

        return self.further_process(df_final_combined)

    # We put some further processing operations down here in this function
    def further_process(self, d_final_order):

        # we should decrease the scale in volume features to make data less sparse

        final_data = d_final_order

        final_data.drop(columns=['sum_vol'], inplace=True)
        final_data.drop(columns=['buy_vol'], inplace=True)

        final_data['sum_vol_roll'] = final_data['sum_vol_roll'] / 100

        #        new_column_order = ['adj_wm_price', 'price_moment_long', 'price_moment_short', 'sum_vol_roll', 'vol_moment_long', 'vol_moment_short', 'buy_ratio_roll', 'buy_ratio_long', 'buy_ratio_short', 'future_close']

        new_column_order = ['adj_wm_price', 'price_moment_long', 'sum_vol_roll', 'vol_moment_long', 'buy_ratio_roll',
                            'buy_ratio_long', 'future_close']

        #        new_column_order = ['adj_wm_price', 'price_moment_long', 'sum_vol_roll', 'buy_ratio_roll', 'future_close']

        final_data = final_data.reindex(new_column_order, axis=1)

        return final_data


str_db_name = 'stocktrans'
str_daily_db_name = 'stockdaily'

str_stock_id = 'SH601628'

str_index_key = 'SH'

str_from_day = '2018-01-02'
str_to_day = '2019-07-15'

# str_from_day = '2018-01-01'
# str_to_day = '2018-01-31'

read_data_proc = StockDataToFromfluxDB()

raw_daily_data = read_data_proc.read_daily_data_by_stock_id_and_date_range(str_stock_id, str_from_day, str_to_day)

final_order_data = read_data_proc.store_stock_trans_data_in_dict(str_stock_id, raw_daily_data)

# final_combined_data = read_data_proc.create_dataset(final_order_data, 5, 5)

i_predict_day_head = 1

i_long_moment_days = 3

i_short_moment_days = 1

final_combined_data = read_data_proc.create_dataset(final_order_data, i_predict_day_head, i_long_moment_days,
                                                    i_short_moment_days)

index_data = read_data_proc.read_daily_index_data_by_id_and_date_range(str_index_key, str_from_day, str_to_day)

# ********************** run following lines only for avoding loading data from database.

# Hi, please comment the below clodes if you want to try with your code, as I am working on some LSTM experiments


import tensorflow as tf
import keras.backend.tensorflow_backend as KTF
from radam import RAdam

gpu_options = tf.GPUOptions(per_process_gpu_memory_fraction=0.8)
sess = tf.Session(config=tf.ConfigProto(gpu_options=gpu_options))

config = tf.ConfigProto()
config.gpu_options.allow_growth = False
session = tf.Session(config=config)

KTF.set_session(sess)

#
# we approx. 12 months, each month is 21 transaction days) as the timestep value
# given each day we have total of 50 samples (values aggregated in 5 minutes)
# however, given we are using 3 months' data as recurrent network iteration body, so we totally use 15 months' data


# We set the starting and ending date as the test dates for predicting return in the future

str_test_start_date = '2019-05-24'
str_test_end_date = '2019-06-14'

feature_number = 6

# we use 63 days (approx. 3 months, each month is 21 transaction days) as the timestep value,
# given each day we have total of 50 samples (values aggregated in 5 minutes)
# so we have 60*50 = 3000 timestpes
# we use 5 features for now 2019-06-02
i_training_month_number = 12

i_timestep_month = 3

i_days_in_a_month = 21

i_times_in_a_day = 50

lst_date_index = final_combined_data.index.values.astype(str).tolist()

for item in lst_date_index:
    if item.find(str_test_start_date) != -1:
        start_index = lst_date_index.index(item)
        start_date_index = item
        break

for item in lst_date_index:
    if item.find(str_test_end_date) != -1:
        end_index = lst_date_index.index(item)
        end_date_index = item

# print(start_date_index, end_date_index)
#
# print(start_index)


i_training_data_len = (i_training_month_number + i_timestep_month) * i_days_in_a_month * i_times_in_a_day

df_test_set = final_combined_data.loc[start_date_index: end_date_index]

df_train_set = final_combined_data.iloc[start_index - i_training_data_len:start_index]

df_total_set = final_combined_data.iloc[start_index - i_training_data_len:end_index + 1]

# training_set = df_train_set.iloc[:, 0:6].values

set_total_X = df_total_set.iloc[:, 0:feature_number].values
set_train = df_train_set.iloc[:, 0:feature_number + 1].values
set_total_y = df_total_set.iloc[:, feature_number].values
set_total_y = np.reshape(set_total_y, (-1, 1))

from sklearn.preprocessing import MinMaxScaler

sc = MinMaxScaler(feature_range=(0, 1))

training_set_x_and_y_scaled = sc.fit_transform(set_train)

# we should not set set_total_y to zero as it stretches the scaling
# we instead set it to the previous close data to keep the normalization in correct form
# set_total_y = np.nan_to_num(set_total_y)
to_predict_close_val = final_order_data[str_to_day][1] * final_order_data[str_to_day][2]
set_total_y = np.where(np.isnan(set_total_y), to_predict_close_val, set_total_y)

total_set_x_scaled = sc.fit_transform(set_total_X)
set_total_y_scaled = sc.fit_transform(set_total_y)

# training_set_x_scaled = sc.fit_transform(set_X)


X_train = []
y_train = []

X_test = []

i_timestpes = i_timestep_month * i_days_in_a_month * i_times_in_a_day

# We use one week's data as training
for i in range(i_timestpes, i_training_data_len):
    X_train.append(training_set_x_and_y_scaled[i - i_timestpes:i, 0:feature_number])
    y_train.append(training_set_x_and_y_scaled[i - 1, feature_number])

# We use one week's data as training
for j in range(len(training_set_x_and_y_scaled), len(total_set_x_scaled)):
    X_test.append(total_set_x_scaled[j - i_timestpes:j, 0:feature_number])
#    y_train.append(training_set_x_and_y_scaled[i-1, 5])


real_future_price = df_total_set.iloc[len(training_set_x_and_y_scaled):len(total_set_x_scaled), feature_number]

# real_future_price = sc.fit_transform(real_future_price)

#
# for j in range(len(df_train_set), len(total_set_x_scaled)):
#    X_test.append(total_set_x_scaled[j, 0:5])


X_test = np.array(X_test)
X_train, y_train = np.array(X_train), np.array(y_train)

y_real = np.array(real_future_price)

X_train = np.reshape(X_train, (X_train.shape[0], X_train.shape[1], feature_number))

X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], feature_number))

# y_real = np.reshape(y_real, (y_real.shape[0], y_real.shape[1], 0))


# X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 5))


from keras.models import Sequential
from keras.layers import Dense
from keras.layers import CuDNNLSTM
from keras.layers import Dropout
from keras.callbacks import ReduceLROnPlateau

# from keras.callbacks import ModelCheckpoint


regressor = Sequential()

regressor.add(CuDNNLSTM(units=50, return_sequences=True, input_shape=(X_train.shape[1], feature_number)))

regressor.add(Dropout(0))

regressor.add(CuDNNLSTM(units=50, return_sequences=True))

regressor.add(Dropout(0))

regressor.add(CuDNNLSTM(units=50, return_sequences=True))

regressor.add(Dropout(0))

regressor.add(CuDNNLSTM(units=50, return_sequences=False))

regressor.add(Dropout(0))

regressor.add(Dense(units=1))

# regressor.compile(optimizer = 'Adam', loss = 'mean_squared_error', metrics=['accuracy'])
regressor.compile(RAdam(), loss='mean_squared_error', metrics=['accuracy'])

# filepath = '/tmp/weights.hdf5'
#
# val_checkpoint = ModelCheckpoint(filepath,'loss', 1, True)

reduce_lr = ReduceLROnPlateau(monitor='loss', factor=0.2, patience=3, min_lr=0.00000001, cooldown=1)

print(datetime.now())

# regressor.fit(X_train, y_train, epochs = 100, batch_size = 32, callbacks=[reduce_lr])

# test for a small number of epochs
history = regressor.fit(X_train, y_train, epochs=100, batch_size=32, callbacks=[reduce_lr])

now = datetime.now()

print(now)

mode_time = now.strftime("%Y-%m-%d-%H-%M")

str_model_file_name = str_test_start_date + '_' + str_stock_id + '_v88_longdays_' + str(
    i_long_moment_days) + '_' + mode_time + '.h5'

regressor.save('models/' + str_model_file_name)

# Load the model when needed
#
# from keras.models import load_model
#
# regressor = load_model('models/ ' + str_model_file_name)

predicted_future_price = regressor.predict(X_test)

predicted_future_price = sc.inverse_transform(predicted_future_price)

predicted_future_price = predicted_future_price / final_order_data[str_test_end_date][1]

i_future_days = int(len(predicted_future_price) / i_times_in_a_day)

dict_predicted_future_price = {}

for l in range(i_future_days):
    str_day_indicator = 'day_' + str(l + 1).zfill(2)
    dict_predicted_future_price[str_day_indicator] = predicted_future_price[
                                                     l * i_times_in_a_day:(l + 1) * i_times_in_a_day]

# array_test_vol = df_test_set['sum_vol_roll'].values
# array_test_price = df_test_set['adj_wm_price'].values
#
# lst_vol_in_days = []
# lst_price_in_days =[]
# lst_predicted_price_in_days = []
#
# for l_num in range (0, int(len(predicted_future_price)/i_times_in_a_day)):
#    lst_vol_in_days.append(array_test_vol[l_num*i_times_in_a_day:(l_num+1)*i_times_in_a_day])
#    lst_price_in_days.append(array_test_price[l_num*i_times_in_a_day:(l_num+1)*i_times_in_a_day])
#    lst_predicted_price_in_days.append(predicted_future_price[l_num*i_times_in_a_day:(l_num+1)*i_times_in_a_day])
#
# final_predicted_price = []
#
# for n_num in range (0, int(len(predicted_future_price)/i_times_in_a_day)):
#    sum_price_in_a_day = np.sum(lst_price_in_days[n_num])
#    lst_price_in_days[n_num] = lst_price_in_days[n_num] / sum_price_in_a_day
#    lst_vol_in_days[n_num] = lst_vol_in_days[n_num] * lst_price_in_days[n_num]
#
#    sum_vol_in_a_day = np.sum(lst_vol_in_days[n_num])
#    lst_vol_in_days[n_num] = lst_vol_in_days[n_num] / sum_vol_in_a_day
#    final_predicted_price.append(np.dot(lst_vol_in_days[n_num], lst_predicted_price_in_days[n_num]))