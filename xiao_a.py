# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 22:28:35 2019
This file read and parse the CSV stock high frequency data, then store all data points into InfluxDB
@author: Kai
"""

# import numpy as np
import pandas as pd
import os
# from influxdb import client as influxdb
from influxdb import DataFrameClient

from dateutil.relativedelta import relativedelta

from datetime import datetime, timedelta

import tushare as ts

import math


class StockDataToInfluxDB:

    def __init__(self, s_host="127.0.0.1", i_port=8086, s_username='', s_password='',
                 s_rootdir='E:\\Level-2_All_China_A_Stocks', s_trans_db='stocktrans', s_stock_daily_db='stockdaily'):
        self.host = s_host
        self.port = i_port
        self.username = s_username
        self.password = s_password
        self.rootdir = s_rootdir
        self.stock_trans_db = s_trans_db
        self.stock_daily_db = s_stock_daily_db

        self.stock_trans_db_client = DataFrameClient(host=self.host, port=self.port,
                                                     username=self.username, password=self.password,
                                                     database=self.stock_trans_db)

        self.stock_daily_db_client = DataFrameClient(host=self.host, port=self.port,
                                                     username=self.username, password=self.password,
                                                     database=self.stock_daily_db)

        ts.set_token('8d28258b02cf3d02feb667de09c0c584ef549fd60a53c5a08c1477fd')
        self.prodata = ts.pro_api()

    def convert_eng_ver1_dataframe(self, df_stk_data):

        # formatting input csv file (current version 1) of English version

        # global df_stock_data

        df_stk_data.drop(['SaleOrderPrice', 'BuyOrderPrice', 'TranID'], axis=1, inplace=True)

        lst_org_col_names = ['Time', 'BuyOrderID', 'BuyOrderVolume', 'Price',
                             'SaleOrderID', 'SaleOrderVolume', 'Volume', 'Type']

        df_stk_data = df_stk_data[lst_org_col_names]

        df_stk_data.rename(columns={'Time': 'time', 'Price': 'Price', 'Volume': 'Vol',
                                    'Type': 'Type', 'BuyOrderVolume': 'BuyOrdVol',
                                    'BuyOrderID': 'BuyOrdID', 'SaleOrderVolume': 'SellOrdVol',
                                    'SaleOrderID': 'SellOrdID'}, inplace=True)

        df_stk_data['BuyVol'] = df_stk_data.apply(lambda x: float(x['Vol']) if x['Type'] == 'B' else 0, axis=1)

        df_stk_data['SellVol'] = df_stk_data.apply(lambda x: float(x['Vol']) if x['Type'] == 'S' else 0, axis=1)

        df_stk_data['time'] = pd.to_datetime(df_stk_data['time'])

        df_stk_data["time"] = df_stk_data["time"] + timedelta(seconds=3)

        df_stk_data["time"] = df_stk_data["time"].dt.strftime('%H:%M:%S')

        return df_stk_data

    def convert_chn_ver1_dataframe(self, df_stk_data):

        # formatting input csv file (current version 1) of Chinese version

        df_stk_data.drop(['卖单成交状态', '卖委托价格', '买单成交状态', '买委托价格'], axis=1, inplace=True)

        lst_org_col_names = ['成交时间', '买成交序号', '买委托数量', '成交价格',
                             '卖成交序号', '卖委托数量', '成交数量', '主动买卖属性']

        df_stk_data = df_stk_data[lst_org_col_names]

        df_stk_data.rename(columns={'成交时间': 'time', '成交价格': 'Price', '成交数量': 'Vol',
                                    '主动买卖属性': 'Type', '买委托数量': 'BuyOrdVol',
                                    '买成交序号': 'BuyOrdID', '卖委托数量': 'SellOrdVol',
                                    '卖成交序号': 'SellOrdID'}, inplace=True)

        df_stk_data['Vol'] = df_stk_data.apply(lambda x: x['Vol'] * 100, axis=1)

        df_stk_data['BuyVol'] = df_stk_data.apply(lambda x: x['Vol'] if x['Type'] == 'B' else 0, axis=1)

        df_stk_data['SellVol'] = df_stk_data.apply(lambda x: x['Vol'] if x['Type'] == 'S' else 0, axis=1)

        df_stk_data['time'] = df_stk_data['time'].str.split(' ').str[1]

        # In the Chinese csv files, the last seconds is 14:59:59, however this value will not be recognized by our system
        # Therefore, we add one second to make our dataset standardized.

        df_stk_data['time'] = pd.to_datetime(df_stk_data['time'])

        df_stk_data["time"] = df_stk_data["time"] + timedelta(seconds=3)

        df_stk_data["time"] = df_stk_data["time"].dt.strftime('%H:%M:%S')

        return df_stk_data

    def arrange_time_in_microseconds_for_influxdb(self, df_stk_data, str_day_dir):

        # Start ranking to add microsecond to distinguish datapoints within one single second.

        df_stk_data['nindex'] = df_stk_data.index

        df_stk_data['rank'] = 0
        df_stk_data['rank'] = df_stk_data.groupby('time')['nindex'].rank('dense', ascending=True)
        df_stk_data['rank'] = df_stk_data['rank'].map(int).apply(lambda x: '{0:0>5}'.format(x))

        str_day = str_day_dir
        str_day = str_day.replace('全息原始', '')

        df_stk_data['time'] = str_day + 'T' + df_stk_data['time'] + '.' + df_stk_data['rank'].map(str) + '1Z'

        return df_stk_data

    def normalize_market_stock_id(self, str_stk_file_name):

        #  normalize prefix of all stocks for writing data to influxdb: if the source csv file starts with 'S', then use the first 8 letters,
        #  if start with '6', it's stock from Shanghai (SH) market, if start with '3' or '0', it's from Shenzhen market (SZ).

        stock_first_name = str_stk_file_name[0]
        stk_id = ''
        if stock_first_name == 'S':
            stk_id = str_stk_file_name[0:8]
        elif stock_first_name == '6':
            stk_id = 'SH' + str_stk_file_name[0:6]
        elif stock_first_name == '3' or stock_first_name == '0':
            stk_id = 'SZ' + str_stk_file_name[0:6]

        return stk_id

    def normalize_market_index_id(self, str_tushare_index_id):

        #  normalize prefix of all stocks for writing data to influxdb: if the source csv file starts with 'S', then use the first 8 letters,
        #  if start with '6', it's stock from Shanghai (SH) market, if start with '3' or '0', it's from Shenzhen market (SZ).

        index_prefix = str_tushare_index_id[7:9]
        index_number = str_tushare_index_id[0:6]

        return index_prefix + index_number

    def normalize_dataframe_data_type_and_index_for_influxdb_dataframeclient(self, df_stk_data):

        df_stk_data['time'] = pd.to_datetime(df_stk_data['time'])

        df_stk_data['Price'] = df_stk_data['Price'].astype(float)
        df_stk_data['Vol'] = df_stk_data['Vol'].astype(int)
        df_stk_data['BuyOrdVol'] = df_stk_data['BuyOrdVol'].astype(int)
        df_stk_data['SellOrdVol'] = df_stk_data['SellOrdVol'].astype(int)

        df_stk_data['BuyVol'] = df_stk_data['BuyVol'].astype(int)
        df_stk_data['SellVol'] = df_stk_data['SellVol'].astype(int)

        df_stk_data['Amount'] = df_stk_data['Price'].astype(float) * df_stk_data['Vol'].astype(int)

        df_stk_data.set_index(["time"], inplace=True, append=False, drop=True)

        df_stk_data.drop(['nindex', 'rank'], axis=1, inplace=True)

        return df_stk_data

    def write_one_csv_file_data_to_influxdb(self, root_dir, s_mon_folder_name, s_day_folder_name, s_file_name):

        full_stock_csv_file_name = os.path.join(root_dir, s_mon_folder_name, s_day_folder_name, s_file_name)

        print('Reading CSV file:' + full_stock_csv_file_name + ' at ' + str(datetime.now()))

        # We should specifcy engine to avoid conflict between OS and Python's file reading protocol
        # We should try to read file without using engine at first, apply it when UnicodeDecodeError is raised
        try:
            df_stock_data = pd.read_csv(full_stock_csv_file_name)
        except UnicodeDecodeError:
            df_stock_data = pd.read_csv(full_stock_csv_file_name, engine='python')

        colname = df_stock_data.columns.values.tolist()
        if colname[0] == 'TranID':
            df_stock_data = self.convert_eng_ver1_dataframe(df_stock_data)

        elif colname[0] == '成交时间':
            df_stock_data = self.convert_chn_ver1_dataframe(df_stock_data)
        else:
            print('A new csv format is found, modifications on parsing should be applied.')

        print('Arranging time value into microseconds to be written to InfluxDB')

        self.arrange_time_in_microseconds_for_influxdb(df_stock_data, s_day_folder_name)

        print('Preparing data to influxdb at ' + str(datetime.now()))

        stock_id = self.normalize_market_stock_id(s_file_name)

        self.normalize_dataframe_data_type_and_index_for_influxdb_dataframeclient(df_stock_data)

        print('Writing data to influxdb at ' + str(datetime.now()))

        self.stock_trans_db_client.write_points(df_stock_data, stock_id, protocol='json', time_precision='u')

        print('One stock transaction data in one day is written to influxdb at ' + str(datetime.now()))

    def write_one_csv_file_data_to_influxdb_by_stock_id(self, root_dir, s_mon_folder_name, s_day_folder_name,
                                                        s_stock_id):

        stock_csv_folder_name = os.path.join(root_dir, s_mon_folder_name, s_day_folder_name)

        full_stock_csv_file_name = stock_csv_folder_name + '\\' + s_stock_id + '.csv'

        exists = os.path.isfile(full_stock_csv_file_name)
        #
        print(full_stock_csv_file_name)
        #
        #
        if exists:
            print('the file exists')
        else:
            stock_first_name = s_stock_id[0]
            stk_id = ''
            if stock_first_name == 'S':
                print('!!!The stock: ' + s_stock_id + ' does not exist or did not trade in the day!!!')
                full_stock_csv_file_name = ''
            elif stock_first_name == '6':
                stk_id = 'SH' + s_stock_id[0:6]
                full_stock_csv_file_name = stock_csv_folder_name + '\\' + stk_id + '.csv'
                exists = os.path.isfile(full_stock_csv_file_name)
                if not exists:
                    print('!!!The stock: ' + s_stock_id + ' does not exist or did not trade in the day!!!')
                    full_stock_csv_file_name = ''

            elif stock_first_name == '3' or stock_first_name == '0':
                stk_id = 'SZ' + s_stock_id[0:6]
                full_stock_csv_file_name = stock_csv_folder_name + '\\' + stk_id + '.csv'
                exists = os.path.isfile(full_stock_csv_file_name)
                if not exists:
                    print('!!!The stock: ' + s_stock_id + ' does not exist or did not trade in the day!!!')
                    full_stock_csv_file_name = ''
            else:
                print('!!!The stock id: ' + s_stock_id + ' is wrong or not supported!!!')
                full_stock_csv_file_name = ''

        if full_stock_csv_file_name == '':
            return
        else:
            print('Reading CSV file:' + full_stock_csv_file_name + ' at ' + str(datetime.now()))

            # We should specifcy engine to avoid conflict between OS and Python's file reading protocols
            # We should try to read file without using engine at first, apply it when UnicodeDecodeError is raised
            try:
                df_stock_data = pd.read_csv(full_stock_csv_file_name)
            except UnicodeDecodeError:
                df_stock_data = pd.read_csv(full_stock_csv_file_name, engine='python')

            colname = df_stock_data.columns.values.tolist()
            if colname[0] == 'TranID':
                df_stock_data = self.convert_eng_ver1_dataframe(df_stock_data)

            elif colname[0] == '成交时间':
                df_stock_data = self.convert_chn_ver1_dataframe(df_stock_data)
            else:
                print('A new CSV data file format is found, modifications should be applied')
                return

            print('Arranging time value into microseconds to be written to InfluxDB')

            self.arrange_time_in_microseconds_for_influxdb(df_stock_data, s_day_folder_name)

            print('Preparing data to influxdb at ' + str(datetime.now()))

            stock_id = self.normalize_market_stock_id(s_stock_id)

            self.normalize_dataframe_data_type_and_index_for_influxdb_dataframeclient(df_stock_data)

            print('Writing data to influxdb at ' + str(datetime.now()))

            self.stock_trans_db_client.write_points(df_stock_data, stock_id, protocol='json', time_precision='u')

            print('One stock transaction data in one day is written to influxdb at ' + str(datetime.now()))

    def get_months_string_list(self, s_from_date, s_to_date):

        from_datetime_obj = datetime.strptime(s_from_date, '%Y-%m-%d')

        to_datetime_obj = datetime.strptime(s_to_date, '%Y-%m-%d')

        lst_months = []

        lst_months.append(str(from_datetime_obj.year).zfill(4) + str(from_datetime_obj.month).zfill(2))

        while (from_datetime_obj.year != to_datetime_obj.year) or (from_datetime_obj.month != to_datetime_obj.month):
            from_datetime_obj = from_datetime_obj + relativedelta(months=+1)
            lst_months.append(str(from_datetime_obj.year).zfill(4) + str(from_datetime_obj.month).zfill(2))

        return lst_months

    def get_all_days_to_list_in_between(self, s_from_date, s_to_date):

        from_datetime_obj = datetime.strptime(s_from_date, '%Y-%m-%d')

        to_datetime_obj = datetime.strptime(s_to_date, '%Y-%m-%d')

        delta = to_datetime_obj - from_datetime_obj

        lst_days = []

        for i in range(delta.days + 1):
            lst_days.append(from_datetime_obj + timedelta(i))

        return lst_days

    def create_dictionary_month_day(self, s_from_date, s_to_date):
        lst_months = self.get_months_string_list(s_from_date, s_to_date)
        lst_days = self.get_all_days_to_list_in_between(s_from_date, s_to_date)

        dict_month_day = {}
        for one_month in lst_months:
            dict_month_day[one_month] = []

        for one_day in lst_days:
            str_year_month = str(one_day.year).zfill(4) + str(one_day.month).zfill(2)
            dict_month_day[str_year_month].append(
                str(one_day.year).zfill(4) + '-' + str(one_day.month).zfill(2) + '-' + str(one_day.day).zfill(2))

        return dict_month_day

    # for tushare daily data
    def get_raw_daily_data(self, s_stock_id, s_from_day, s_to_day):

        df_adj_factor = self.prodata.adj_factor(ts_code=s_stock_id, start_date=s_from_day, end_date=s_to_day)
        # df4.set_index('trade_date')

        df_daily_k = self.prodata.daily(ts_code=s_stock_id, start_date=s_from_day, end_date=s_to_day)

        df_daily_data = df_adj_factor.set_index('trade_date').join(df_daily_k.set_index('trade_date'),
                                                                   lsuffix='_caller', rsuffix='_other')

        df_daily_data.drop('ts_code_other', axis='columns', inplace=True)

        df_daily_data.rename({'ts_code_caller': 'ts_code'}, axis='columns', inplace=True)

        df_daily_data.drop('pct_chg', axis=1, inplace=True)
        df_daily_data.drop('pre_close', axis=1, inplace=True)

        df_daily_data.sort_index(ascending=True, inplace=True)

        return df_daily_data

    def get_index_daily_data(self, s_stock_id, s_from_day, s_to_day):

        # df4.set_index('trade_date')

        df_daily_index_data = self.prodata.index_daily(ts_code=s_stock_id, start_date=s_from_day, end_date=s_to_day)

        df_daily_index_data = df_daily_index_data.set_index('trade_date')

        df_daily_index_data.drop('ts_code', axis='columns', inplace=True)
        df_daily_index_data.drop('pct_chg', axis=1, inplace=True)
        df_daily_index_data.drop('pre_close', axis=1, inplace=True)

        df_daily_index_data.sort_index(ascending=True, inplace=True)

        return df_daily_index_data

    # for tushare daily data
    def get_one_day_k_data(self, s_stock_id, s_day):
        df_daily_k = self.prodata.daily(ts_code=s_stock_id, start_date=s_day, end_date=s_day)
        return df_daily_k

    def is_first_day_nan(self, df_raw_daily_data):
        if df_raw_daily_data.shape[0] == 0:
            return True
        else:
            if math.isnan(df_raw_daily_data['open'].values[0]):
                return True
            else:
                return False

                # for tushare daily data

    def get_previous_day_ts_str(self, s_day):

        dt_prev_day = datetime.strptime(s_day, '%Y%m%d')
        dt_prev_day = dt_prev_day + timedelta(days=-1)

        str_prev_day = str(dt_prev_day.year).zfill(4) + str(dt_prev_day.month).zfill(2) + str(dt_prev_day.day).zfill(2)
        return str_prev_day

    # for tushare daily data
    def get_first_day_nan_filled_data(self, s_stock_id, s_start_day, s_end_day):
        df_whole_daily_data = self.get_raw_daily_data(s_stock_id, s_start_day, s_end_day)
        b_if_first_day_nan = self.is_first_day_nan(df_whole_daily_data)

        if not b_if_first_day_nan:
            return df_whole_daily_data

        df_one_daily_data = self.get_one_day_k_data(s_stock_id, s_start_day)

        str_prev_day = s_start_day
        while b_if_first_day_nan:
            str_prev_day = self.get_previous_day_ts_str(str_prev_day)
            df_one_daily_data = self.get_one_day_k_data(s_stock_id, str_prev_day)
            b_if_first_day_nan = self.is_first_day_nan(df_one_daily_data)

        df_whole_daily_data.iloc[0, df_whole_daily_data.columns.get_loc('open')] = df_one_daily_data['close'].values[0]
        df_whole_daily_data.iloc[0, df_whole_daily_data.columns.get_loc('high')] = df_one_daily_data['close'].values[0]
        df_whole_daily_data.iloc[0, df_whole_daily_data.columns.get_loc('low')] = df_one_daily_data['close'].values[0]
        df_whole_daily_data.iloc[0, df_whole_daily_data.columns.get_loc('close')] = df_one_daily_data['close'].values[0]

        df_whole_daily_data.iloc[0, df_whole_daily_data.columns.get_loc('change')] = 0.0
        df_whole_daily_data.iloc[0, df_whole_daily_data.columns.get_loc('vol')] = 0.0
        df_whole_daily_data.iloc[0, df_whole_daily_data.columns.get_loc('amount')] = 0.0

        print(str_prev_day + 'is not empty')
        return df_whole_daily_data

    # for tushare daily data
    def get_all_other_day_nan_filled_data(self, df_raw_data):
        last_row = None
        for str_ndx, srs_row in df_raw_data.iterrows():

            if math.isnan(srs_row['open']):
                df_raw_data.at[str_ndx, 'open'] = last_row['close']
                df_raw_data.at[str_ndx, 'high'] = last_row['close']
                df_raw_data.at[str_ndx, 'low'] = last_row['close']
                df_raw_data.at[str_ndx, 'close'] = last_row['close']

                df_raw_data.at[str_ndx, 'change'] = 0.0
                df_raw_data.at[str_ndx, 'vol'] = 0.0
                df_raw_data.at[str_ndx, 'amount'] = 0.0

                print('Set one empty internal day as 0.0')

            else:
                last_row = srs_row
        return df_raw_data

    # for tushare daily data
    def format_date_for_tushare(self, s_day):
        str_tushare_date = ''
        list_date = s_day.split('-')

        for item in list_date:
            str_tushare_date += item

        return str_tushare_date

    # for tushare daily data
    def format_stock_id_for_tushare(self, s_stock_id):

        stock_first_name = s_stock_id[0]

        stk_id = ''
        if stock_first_name == 'S':
            stk_id = s_stock_id[2:8] + '.' + s_stock_id[0:2]
        elif stock_first_name == '6':
            stk_id = s_stock_id[0:6] + '.' + 'SH'
        elif stock_first_name == '3' or stock_first_name == '0':
            stk_id = s_stock_id[0:6] + '.' + 'SZ'

        return stk_id

    # do not use this function unless really necessary, tushare daily data are not included in this function
    def write_all_csv_files_in_root_folder(self):
        lst_root_dir = os.listdir(self.rootdir)
        for str_month_dir in lst_root_dir:
            str_path_month = os.path.join(self.rootdir, str_month_dir)
            lst_day_dir = os.listdir(str_path_month)
            for str_day_dir in lst_day_dir:

                str_full_day_path = os.path.join(str_path_month, str_day_dir)
                lst_stock_full_file_name = os.listdir(str_full_day_path)
                for str_stock_file_name in lst_stock_full_file_name:
                    self.write_one_csv_file_data_to_influxdb(self.rootdir, str_month_dir, str_day_dir,
                                                             str_stock_file_name)

    def write_stock_data_by_id_and_date_range_to_influxdb(self, s_from_date, s_to_date, l_stock_id):
        dictmd = self.create_dictionary_month_day(s_from_date, s_to_date)
        for str_stock_id in l_stock_id:
            for month_str in dictmd:
                for day_str in dictmd[month_str]:
                    self.write_one_csv_file_data_to_influxdb_by_stock_id(self.rootdir, month_str, day_str, str_stock_id)

    def write_stock_daily_data_by_id_and_date_range_to_influxdb(self, s_from_date, s_to_date, l_stock_id):
        for s_stock_id in l_stock_id:
            str_from_date = self.format_date_for_tushare(s_from_date)
            str_to_date = self.format_date_for_tushare(s_to_date)
            str_stock_id = self.format_stock_id_for_tushare(s_stock_id)
            df_all_filled = self.get_all_other_day_nan_filled_data(
                self.get_first_day_nan_filled_data(str_stock_id, str_from_date, str_to_date))

            df_all_filled.index = pd.to_datetime(df_all_filled.index) + pd.DateOffset(hours=15)

            str_influx_stock_id = self.normalize_market_stock_id(s_stock_id)

            df_all_filled['vol'] = df_all_filled['vol'] * 100
            df_all_filled['vol'].astype(int)

            self.stock_daily_db_client.write_points(df_all_filled, str_influx_stock_id, protocol='json',
                                                    time_precision='u')

    def write_index_daily_data_by_id_and_date_range_to_influxdb(self, s_from_date, s_to_date, l_index_id):

        indices = {'SH': '000001.SH', 'HS300': '399300.SZ', 'SZ50': '000016.SH', 'SZ': '399001.SZ',
                   'ZZ500': '000905.SH', 'CYB': '399006.SZ'}
        for s_index_key in l_index_id:
            str_index_id = indices[s_index_key]

            str_from_date = self.format_date_for_tushare(s_from_date)
            str_to_date = self.format_date_for_tushare(s_to_date)
            df_all_filled = self.get_index_daily_data(str_index_id, str_from_date, str_to_date)

            df_all_filled.index = pd.to_datetime(df_all_filled.index) + pd.DateOffset(hours=15)

            str_influx_stock_id = self.normalize_market_index_id(str_index_id)

            df_all_filled['vol'] = df_all_filled['vol'] * 100
            df_all_filled['vol'].astype(int)

            self.stock_daily_db_client.write_points(df_all_filled, str_influx_stock_id, protocol='json',
                                                    time_precision='u')


# can import multiple stocks in a list here
stocks = ['601628']

# indices = {'SH':'000001.SH', 'HS300':'399300.SZ', 'SZ50':'000016.SH', 'SZ':'399001.SZ', 'ZZ500':'000905.SH', 'CYB':'399006.SZ'}
indices = ['SH']

# str_start_day = '20180207'
from_date = '2018-01-02'
to_date = '2019-08-06'

write_to_influx_proc = StockDataToInfluxDB()

write_to_influx_proc.write_stock_data_by_id_and_date_range_to_influxdb(from_date, to_date, stocks)

write_to_influx_proc.write_stock_daily_data_by_id_and_date_range_to_influxdb(from_date, to_date, stocks)

write_to_influx_proc.write_index_daily_data_by_id_and_date_range_to_influxdb(from_date, to_date, indices)

# a= write_to_influx_proc.get_index_daily_data(indices['SH'], write_to_influx_proc.format_date_for_tushare(from_date),  write_to_influx_proc.format_date_for_tushare(to_date))


# df_pre_daily_data = get_raw_daily_data(str_stock_id, str_start_day, str_end_day)
#
# df_one_day_k = get_one_day_k_data(str_stock_id, str_start_day)
#
# x = is_first_day_empty(df_pre_daily_data)
#
# write_to_influx_proc = StockDataToInfluxDB()
# from_date = write_to_influx_proc.format_date_for_tushare(from_date)
# to_date = write_to_influx_proc.format_date_for_tushare(to_date)
# stock_id = write_to_influx_proc.format_stock_id_for_tushare(str_stock_id)
#
# df = write_to_influx_proc.get_first_day_nan_filled_data(stock_id, from_date, to_date)
#
# df_all_filled = write_to_influx_proc.get_all_other_day_nan_filled_data(write_to_influx_proc.get_first_day_nan_filled_data(stock_id, from_date, to_date))
#