import pandas as pd
import json

file_path_week1 = "../data/sat_result_20231103_20231109/com_sat_result/"
file_path_week2 = "../data/sat_result_20231110_20231116/com_sat_result/"
file_name_router = "router_prefix_sat_change.csv"
file_name_seed = "seed_prefix_sat_change.csv"

pathArray = [file_path_week1, file_path_week2]
fileArray = [file_name_router, file_name_seed]

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


def generate_line_data():
    dataArray = []
    # 获取时间，横坐标
    xAxis = []
    for i in range(1, 15):
        day = "Day"+str(i)
        xAxis.append(day)

    # 获取数据，series
    for file_index in range(2):
        for type_index in range(2):
            data_1 = []
            data_2 = []

            for path_index in range(2):
                file_name = pathArray[path_index] + fileArray[file_index]
                df = pd.read_csv(file_name)
                # 获取列标签
                column_headers = list(df.columns.values)
                data_header_1 = column_headers[type_index]  # 第1或 3列
                data_header_2 = column_headers[type_index + 1]  # 第2或 4列
                data_1 = data_1 + df[data_header_1].tolist()
                data_2 = data_2 + df[data_header_2].tolist()
            series_temp_1 = {"name": data_header_1, "data": data_1}
            series_temp_2 = {"name": data_header_2, "data": data_2}
            # data = csv_to_json(file_name)
            data_temp = {
                "xAxis": xAxis,
                "legend": [data_header_1, data_header_2],
                "series": [series_temp_1, series_temp_2]
            }
            dataArray.append(data_temp)

    result = {"result": dataArray, "code": 1001, "msg": "success"}

    # Save JSON data to a file
    with open(f"../data/get_data_result/line_result.json", 'w') as json_file:
        json.dump(result, json_file, indent=2)


if __name__ == "__main__":
    generate_line_data()
