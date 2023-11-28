import pandas as pd
import json


def generate_pie_chart(path, type_name, csv_file_name):
    # series标签名称
    column_name = 'ratio of aliased prefix'
    # 饼状图所有值
    # select_num = 9
    json_file_names=[]
    type_name.split('-')[0].lower()
    # Read CSV file into DataFrame
    df = pd.read_csv(path + csv_file_name)

    # Sort DataFrame based on the specified column in descending order
    df = df.sort_values(by=column_name, ascending=False, inplace=False)

    series_array = []
    # if type_name == "Country-Num":
    #     prefix_str = f"{row['country']}-{row['number of aliased prefix']}"
    num = 0
    for idx, row in df.iterrows():
        num += 1

        if type_name == "AS-Num-Org":
            data_temp = [num, row['as'], row['org_name'], row['number of aliased prefix'], row['ratio of aliased prefix']]
            columns = [
                {"title": "num"},
                {"title": "as"},
                {"title": "org_name"},
                {"title": "number of aliased prefix"},
                {"title": "ratio of aliased prefix", "class": "center"},
            ]

        if type_name == "Category-Num":
            data_temp = [num, row['category'], row['number of aliased prefix'], row['ratio of aliased prefix']]
            columns = [
                {"title": "num"},
                {"title": "category"},
                {"title": "number of aliased prefix"},
                {"title": "ratio of aliased prefix", "class": "center"},
            ]
        if type_name == "Sub_category-Num":
            data_temp = [num, row['sub_category'], row['number of aliased prefix'], row['ratio of aliased prefix']]
            columns = [
                {"title": "num"},
                {"title": "sub_category"},
                {"title": "number of aliased prefix"},
                {"title": "ratio of aliased prefix", "class": "center"},
            ]
        if type_name == "Org-AS-Num":
            data_temp = [num, row['org_name'], row['as'], row['number of aliased prefix'], row['ratio of aliased prefix']]
            columns = [
                {"title": "num"},
                {"title": "org_name"},
                {"title": "as"},
                {"title": "number of aliased prefix"},
                {"title": "ratio of aliased prefix", "class": "center"},
            ]
        series_array.append(data_temp)

    result_dict = {
        "title": type_name,
        "data": series_array,
        "columns": columns,
        "name": column_name,
        "dataLength": len(df)
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
        json_path = f"../data/get_data_result/pie_result_all_{type_name.split('-')[0].lower()}.json"
        # Save JSON data to a file
        with open(json_path, 'w') as json_file:
            json.dump(result, json_file, indent=2)