import pandas as pd
import json
from datetime import datetime, timedelta
from config import DefaultConfig
config=DefaultConfig()

file_name_sum = "sum_frp"
file_name_router = "router_frp"
file_name_seed = "seed_frp"
fileArray = [file_name_sum, file_name_router, file_name_seed]


def read_csv_column(file, delimiter):
    data = []
    df = pd.read_csv(file)
    # 填充缺失值
    df.fillna("missing", inplace=True)
    # 获取列标签
    column_headers = list(df.columns.values)
    for index, row in df.iterrows():
        data.append(row.tolist())
    return data, column_headers


def csv_to_json(file):
    data, column_headers = read_csv_column(file, ',')
    res = []
    for item in data:
        temp = {}
        for i in range(len(column_headers)):
            temp[column_headers[i]] = item[i]
        res.append(temp)
    return res


def generate_line_chart(path_name):
    dataArray = []
    day_num = 180
    start_date_string = "2023-11-03"
    start_date = datetime.strptime(start_date_string, "%Y-%m-%d")
    # 获取时间，横坐标
    xAxis = [start_date_string]
    for i in range(1, day_num):
        # 计算之后的日期和时间
        day_later = start_date + timedelta(days=i)
        xAxis.append(day_later.strftime("%Y-%m-%d"))

    # 获取数据，series
    for file_name in fileArray:
        for type_index in range(2):
            if type_index == 0:
                yAxisName = '#'
                file = path_name + file_name +'.csv'
            else:
                yAxisName = "10^9"
                file = path_name + file_name +'_64.csv'
            df = pd.read_csv(file)
            series_temp = {"name": "Fully Responsive Prefixes", "data": df['frp'].tolist()}
            data_temp = {
                "xAxis": xAxis,
                "legend": ["Fully Responsive Prefixes"],
                "series": [series_temp],
                "yAxisName":yAxisName
            }
            dataArray.append(data_temp)

    result = {"result": dataArray, "code": 1001, "msg": "success"}

    # Save JSON data to a file
    with open(config.result_path+f"line_result.json", 'w') as json_file:
        json.dump(result, json_file, indent=2)

