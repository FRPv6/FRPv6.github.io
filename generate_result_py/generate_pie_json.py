import pandas as pd
import json
from datetime import datetime, timedelta
from config import DefaultConfig
config = DefaultConfig()
type_name_dict = {
    "AS-Num-Org": "AS-Num-Org",
    "Category-Num": "CGBC-Num",
    "Sub_category-Num": "FGBC-Num",
    "Org-AS-Num": "AS-Num-Org"
}


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


def generate_result_temp(path, type_name, csv_file_name):
    # 下拉框class，type1 or type2
    class_ratio_names = ["","sat_"]
    class_num_names = ["", "sta_"]
    # 饼状图top10
    select_num = 9
    # Read CSV file into DataFrame
    df = pd.read_csv(path + csv_file_name)
    data_class_array = []
    for class_index in range(2):
        # series标签名称
        if type_name == "Sub_category-Num":
            column_name = f"{class_ratio_names[class_index]}category_ratio"
        else:
            column_name = f"{class_ratio_names[class_index]}{type_name.split('-')[0].lower()}_ratio"
        # Sort DataFrame based on the specified column in descending order
        df = df.sort_values(by=column_name, ascending=False, inplace=False)

        # Calculate the ratio of selected rows and the ratio of the remaining rows
        other_ratio = 1 - df.loc[:int(select_num), column_name].sum()   # .loc[]左右均闭合，包含端点

        # Create a list of dictionaries containing information for each selected row and the "Others" category
        data_array = []

        for idx, row in df[:select_num].iterrows():
            prefix_str = ""
            number_head_name=f"{class_num_names[class_index]}{type_name.split('-')[0].lower()}_alias_num"
            if type_name == "AS-Num-Org":
                prefix_str = f"{row['as']}-{row[number_head_name]}-{row['org_name']}"
            if type_name == "Category-Num":
                prefix_str = f"{row['category']}-{row[number_head_name]}"
            if type_name == "Sub_category-Num":
                number_head_name = f"{class_num_names[class_index]}category_alias_num"
                prefix_str = f"{row['sub_category']}-{row[number_head_name]}"
            if type_name == "Org-AS-Num":
                prefix_str = f"{row['org_name']}-{row['as']}-{row[number_head_name]}"
            # if type_name == "Country-Num":
            # number_head_name=f"{class_name}_{type_name}_alias_num"
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
            "title": type_name_dict[type_name],
            "data": data_array,
            "name": column_name
        }
        data_class_array.append(result_dict)
    return data_class_array


def generate_pie_chart():
    generate_time_list()
    # Specify the variables for each iteration
    # type_list = ["as", "category", "sub_category", "org"]
    prefix_types = ["sum", "router", "seed"]
    type_names = ["AS-Num-Org", "Category-Num", "Sub_category-Num", "Org-AS-Num"]
    file_path = config.file_path_last_week

    # Iterate through different combinations
    for type_name in type_names:
        resultArray = []
        for prefix_type in prefix_types:
            for day in range(1, 8):
                csv_file_name = f"{prefix_type}_prefix_day_{day}_{type_name.split('-')[0].lower()}_sat.csv"

                result_temp = generate_result_temp(file_path, type_name, csv_file_name)
                resultArray.append(result_temp)

        result = {"result": resultArray, "code": 1001, "msg": "success"}
        # 写入json文件中
        json_path = f"../data/get_data_result/pie_result_{type_name.split('-')[0].lower()}.json"
        # Save JSON data to a file
        with open(json_path, 'w') as json_file:
            json.dump(result, json_file, indent=2)