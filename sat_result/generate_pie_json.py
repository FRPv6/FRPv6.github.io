import pandas as pd
import json


def generate_pie_chart(path, type_name, csv_file_name):
    # series标签名称
    column_name = 'ratio of aliased prefix'
    # 饼状图top10
    select_num = 9
    json_file_names=[]
    type_name.split('-')[0].lower()
    # Read CSV file into DataFrame
    df = pd.read_csv(path + csv_file_name)

    # Sort DataFrame based on the specified column in descending order
    df = df.sort_values(by=column_name, ascending=False, inplace=False)

    # Calculate the ratio of selected rows and the ratio of the remaining rows
    other_ratio = 1 - df.loc[:int(select_num), column_name].sum()   # .loc[]左右均闭合，包含端点

    # Create a list of dictionaries containing information for each selected row and the "Others" category
    data_array = []
    for idx, row in df[:select_num].iterrows():
        prefix_str = ""
        if type_name == "AS-Num-Org":
            prefix_str = f"{row['as']}-{row['number of aliased prefix']}-{row['org_name']}"
        if type_name == "Category-Num":
            prefix_str = f"{row['category']}-{row['number of aliased prefix']}"
        if type_name == "Sub_category-Num":
            prefix_str = f"{row['sub_category']}-{row['number of aliased prefix']}"
        if type_name == "Org-AS-Num":
            prefix_str = f"{row['org_name']}-{row['as']}-{row['number of aliased prefix']}"
        # if type_name == "Country-Num":
        #     prefix_str = f"{row['country']}-{row['number of aliased prefix']}"

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
    return result_dict


if __name__ == "__main__":

    # Specify the variables for each iteration
    file_path = "../data/sat_result_20231117_20231123/"
    # type_list = ["as", "category", "sub_category", "org"]
    prefix_types = ["router", "seed"]
    type_names = ["AS-Num-Org", "Category-Num", "Sub_category-Num", "Org-AS-Num",
                 # "Country-Num",
                 ]

    # Iterate through different combinations
    for type_name in type_names:
        resultArray = []
        for prefix_type in prefix_types:
            for day in range(1, 8):
                csv_file_name = f"{prefix_type}_prefix_day_{day}_{type_name.split('-')[0].lower()}_sat.csv"

                result_temp = generate_pie_chart(file_path, type_name, csv_file_name)
                resultArray.append(result_temp)

        result = {"result": resultArray, "code": 1001, "msg": "success"}
        # 写入json文件中
        json_path = f"../data/get_data_result/pie_result_{type_name.split('-')[0].lower()}.json"
        # Save JSON data to a file
        with open(json_path, 'w') as json_file:
            json.dump(result, json_file, indent=2)