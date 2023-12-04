import pandas as pd
import json
from datetime import datetime, timedelta
from config import DefaultConfig
config=DefaultConfig()

file_name_sum = "sum_prefix_sat_change.csv"
file_name_router = "router_prefix_sat_change.csv"
file_name_seed = "seed_prefix_sat_change.csv"

pathArray = config.pathArray
week_num = config.week_num
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




def generate_line_chart():
    dataArray = []
    day_num = week_num * 7
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
        for type_index in range(0, 3, 2):
            data_1 = []
            data_2 = []
            header_prefix_list = ["", "", "Standardized "]
            for path_name in pathArray:
                file = path_name + file_name
                df = pd.read_csv(file)
                # 获取列标签
                column_headers = list(df.columns.values)
                # Fully Responsive Prefixes    All Prefixes
# Standardized Fully Responsive Prefixes      Standardized All Prefixes

                data_header_1 = column_headers[type_index]  # 第1或 3列
                data_header_2 = column_headers[type_index + 1]  # 第2或 4列
                name_header_1 = header_prefix_list[type_index] + "Fully Responsive Prefixes"
                name_header_2 = header_prefix_list[type_index] + "All Prefixes"
                data_1 = data_1 + df[data_header_1].tolist()
                data_2 = data_2 + df[data_header_2].tolist()
            series_temp_1 = {"name": name_header_1, "data": data_1}
            series_temp_2 = {"name": name_header_2, "data": data_2}
            # data = csv_to_json(file_name)
            data_temp = {
                "xAxis": xAxis,
                "legend": [name_header_1, name_header_2],
                "series": [series_temp_1, series_temp_2]
            }
            dataArray.append(data_temp)

    result = {"result": dataArray, "code": 1001, "msg": "success"}

    # Save JSON data to a file
    with open(f"../data/get_data_result/line_result.json", 'w') as json_file:
        json.dump(result, json_file, indent=2)

