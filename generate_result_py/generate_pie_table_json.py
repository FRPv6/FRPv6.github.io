import pandas as pd
import json


def generate_pie_chart(path, type_name, csv_file_name):
    # 下拉框class，type1 or type2
    class_ratio_names = ["","sat_"]
    class_num_names = ["", "sta_"]
    # 饼状图所有值
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

        series_array = []

        num = 0
        for idx, row in df.iterrows():
            num += 1
            number_head_name=f"{class_num_names[class_index]}{type_name.split('-')[0].lower()}_alias_num"
            if type_name == "AS-Num-Org":
                data_temp = [num, row['as'], row['org_name'], row[number_head_name], row[column_name]]
                columns = [
                    {"title": "num"},
                    {"title": "as"},
                    {"title": "org_name"},
                    {"title": number_head_name},
                    {"title": column_name, "class": "center"},
                ]

            if type_name == "Category-Num":
                data_temp = [num, row['category'], row[number_head_name], row[column_name]]
                columns = [
                    {"title": "num"},
                    {"title": "category"},
                    {"title": number_head_name},
                    {"title": column_name, "class": "center"},
                ]
            if type_name == "Sub_category-Num":
                number_head_name = f"{class_num_names[class_index]}category_alias_num"
                data_temp = [num, row['sub_category'], row[number_head_name], row[column_name]]
                columns = [
                    {"title": "num"},
                    {"title": "sub_category"},
                    {"title": number_head_name},
                    {"title": column_name, "class": "center"},
                ]
            if type_name == "Org-AS-Num":
                data_temp = [num, row['org_name'], row['as'], row[number_head_name], row[column_name]]
                columns = [
                    {"title": "num"},
                    {"title": "org_name"},
                    {"title": "as"},
                    {"title": number_head_name},
                    {"title": column_name, "class": "center"},
                ]
            if type_name == "Country-Num":
                data_temp = [num, row['country'], row[number_head_name], row[column_name]]
                columns = [
                    {"title": "num"},
                    {"title": "country"},
                    {"title": number_head_name},
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


if __name__ == "__main__":

    # Specify the variables for each iteration
    file_path = "../data/sat_result_20231117_20231123/"
    # type_list = ["as", "category", "sub_category", "org"]
    prefix_types = ["sum", "router", "seed"]
    type_names = ["AS-Num-Org", "Category-Num", "Sub_category-Num", "Org-AS-Num", "Country-Num" ]

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
        json_path = f"../data/get_data_result/pie_result_table_{type_name.split('-')[0].lower()}.json"
        # Save JSON data to a file
        with open(json_path, 'w') as json_file:
            json.dump(result, json_file, indent=2)