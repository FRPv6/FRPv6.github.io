import pandas as pd
import json
import math
from config import DefaultConfig
config = DefaultConfig()

def generate_result_temp(path, type_name, file_type,csv_file_name):
    # 下拉框class，type1 or type2
    class_ratio_names = ["","_64"]
    class_num_names = ["", "sta_"]
    # 饼状图所有值
    # Read CSV file into DataFrame
    df = pd.read_csv(path + csv_file_name)
    data_class_array = []
    for class_index in range(2):
        column_name = f"alias_prefix{class_ratio_names[class_index]}_num"
        # Sort DataFrame based on the specified column in descending order
        df = df.sort_values(by=column_name, ascending=False, inplace=False)

        series_array = []

        num = 0
        for idx, row in df.iterrows():
            num += 1
            if type_name == "AS-Num-ORG":
                if isinstance(row['org_name'],float):
                    org_name=""
                else:
                    org_name=row['org_name']

                data_temp = [num, row['as'], org_name, row[column_name]]
                columns = [
                    {"title": "num"},
                    {"title": "as"},
                    {"title": "org_name"},
                    {"title": column_name, "class": "center"},
                ]

            if type_name == "CGBC-Num":
                data_temp = [num, row['category'],  row[column_name]]
                columns = [
                    {"title": "num"},
                    {"title": "category"},
                    {"title": column_name, "class": "center"},
                ]
            if type_name == "FGBC-Num":
                data_temp = [num, row['sub_category'], row[column_name]]
                columns = [
                    {"title": "num"},
                    {"title": "sub_category"},
                    {"title": column_name, "class": "center"},
                ]
            if type_name == "ORG-AS-Num":
                data_temp = [num, row['org_name'], row['as_y'], row[column_name]]
                columns = [
                    {"title": "num"},
                    {"title": "org_name"},
                    {"title": "as"},
                    {"title": column_name, "class": "center"},
                ]
            if type_name == "Country-Num":
                data_temp = [num, row['country'],  row[column_name]]
                columns = [
                    {"title": "num"},
                    {"title": "country"},
                    {"title": column_name, "class": "center"},
                ]
            series_array.append(data_temp)

        result_dict = {
            "title": type_name,
            "data": series_array,
            "columns": columns,
            "name": column_name,
            "dataLength": len(df)
        }
        data_class_array.append(result_dict)
    return data_class_array


def generate_table_chart(path_name):
    type_list = ["as", "category", "sub_category", "org","country"]
    prefix_types = ["all", "router", "seed"]
    type_names = ["AS-Num-ORG", "CGBC-Num", "FGBC-Num", "ORG-AS-Num","Country-Num"]
    type_name_dict = {
        "AS-Num-ORG": "as",
        "CGBC-Num": "category",
        "FGBC-Num": "sub_category",
        "ORG-AS-Num": "org_name",
        "Country-Num": "country"
    }
    # Iterate through different combinations
    for type_name in type_names:
        resultArray = []
        file_type=type_name_dict[type_name]
        for prefix_type in prefix_types:
            csv_file_name = f"{prefix_type}_six_month_{file_type}.csv"
            result_temp = generate_result_temp(path_name, type_name, file_type,csv_file_name)
            resultArray.append(result_temp)

        result = {"result": resultArray, "code": 1001, "msg": "success"}
        # 写入json文件中
        json_path = config.result_path+f"pie_result_table_{file_type}.json"
        # Save JSON data to a file
        with open(json_path, 'w') as json_file:
            json.dump(result, json_file, indent=2)