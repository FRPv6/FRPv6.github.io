import pandas as pd
import json
from datetime import datetime, timedelta
from config import DefaultConfig
config = DefaultConfig()


def generate_time_list():
    day_num = 7
    start_date_string = config.start_date
    start_date = datetime.strptime(start_date_string, "%Y-%m-%d")
    # 获取时间，横坐标
    time_list = [start_date_string]
    for i in range(1, day_num):
        # 计算之后的日期和时间
        day_later = start_date + timedelta(days=i)
        time_list.append(day_later.strftime("%Y-%m-%d"))
    data={
        "data": time_list
    }
    with open(f"../data/get_data_result/line_time_list.json", 'w') as json_file:
        json.dump(data, json_file, indent=2)


def generate_result_temp(path, type_name,file_type, csv_file_name):
    # 下拉框class，type1 or type2
    class_ratio_names = ["","_64"]
    class_num_names = ["", "sta_"]
    # 饼状图top10
    select_num = 9
    # Read CSV file into DataFrame
    df = pd.read_csv(path + csv_file_name)
    data_class_array = []
    for class_index in range(2):
        # series标签名称
        # if type_name == "Sub_category-Num":
        #     column_name = f"{class_ratio_names[class_index]}category_ratio"
        # else:
        #     column_name = f"{class_ratio_names[class_index]}{type_name.split('-')[0].lower()}_ratio"
        # Sort DataFrame based on the specified column in descending order
        column_name = f"alias_prefix{class_ratio_names[class_index]}_ratio"
        df = df.sort_values(by=column_name, ascending=False, inplace=False)

        # Calculate the ratio of selected rows and the ratio of the remaining rows
        other_ratio = 1 - df.loc[:int(select_num), column_name].sum()   # .loc[]左右均闭合，包含端点

        # Create a list of dictionaries containing information for each selected row and the "Others" category
        data_array = []

        for idx, row in df[:select_num].iterrows():
            prefix_str = ""
            column_name_num=f"alias_prefix{class_ratio_names[class_index]}_num"
            if type_name == "AS-Num-ORG":
                prefix_str = f"{row['as']}-{row[column_name_num]}-{row['org_name']}"
            if type_name == "CGBC-Num":
                prefix_str = f"{row['category']}-{row[column_name_num]}"
            if type_name == "FGBC-Num":
                prefix_str = f"{row['sub_category']}-{row[column_name_num]}"
            if type_name == "ORG-AS-Num":
                prefix_str = f"{row['org_name']}-{row['as_y']}-{row[column_name_num]}"
            # if type_name == "Country-Num":
            #     number_head_name=f"{row['country']}_{type_name}_alias_num"
            #     prefix_str = f"{row['country']}-{row[number_head_name]}"

            data_dict = {
                "name": f"{prefix_str}",
                "value": row[column_name]
            }
            data_array.append(data_dict)
        # 加入others计算结果
        data_dict = {
            "name": "Others",
            "value": other_ratio
        }

        data_array.append(data_dict)

        result_dict = {
            "title": type_name,
            "data": data_array,
            "name": column_name
        }
        data_class_array.append(result_dict)
    return data_class_array


def generate_pie_chart(path_name):
    generate_time_list()
    # Specify the variables for each iteration
    type_list = ["as", "category", "sub_category", "org_name", "country"]
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
            result_temp = generate_result_temp(path_name, type_name,file_type, csv_file_name)
            resultArray.append(result_temp)
        result = {"result": resultArray, "code": 1001, "msg": "success"}
        # 写入json文件中
        json_path = config.result_path+f"pie_result_{file_type}.json"
        # Save JSON data to a file
        with open(json_path, 'w') as json_file:
            json.dump(result, json_file, indent=2)