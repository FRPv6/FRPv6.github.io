import pandas as pd
import json
country_iso_dict = {}


def get_country_iso_dict():
    path = "../data/countryISO.txt"
    with open(path, "r", encoding='utf-8') as f:
        title = f.readline()
        datas = f.readlines()
    for data in datas:
        data = data.strip()
        dataArray = data.split(" ")
        # print(dataArray)
        country = dataArray[0]
        iso3 = dataArray[2]  # 3位编码
        ChineseName = dataArray[-1]  # 中文名
        EnglishNameList = dataArray[3:-1]
        # print(EnglishNameList)
        EnglishName = str(" ".join(EnglishNameList))
        EnglishName = EnglishName.strip()  # 英文名

        country_iso_dict[country] = EnglishName



def locate_country_iso(country):

    return country_iso_dict[country]


def generate_map_chart(path, type_name, csv_file_name):
    # 下拉框class，type1 or type2
    class_ratio_names = ["","sat_"]
    class_num_names = ["", "sta_"]

    # Read CSV file into DataFrame
    df = pd.read_csv(path + csv_file_name)
    data_class_array = []
    for class_index in range(2):
        # series标签名称
        column_name = f"{class_num_names[class_index]}country_alias_num"
        # Create a list of dictionaries containing information for each selected row
        data_array = []
        for idx, row in df.iterrows():
            # prefix_str = f"{row['country']}-{row['ratio of aliased prefix']}"
            prefix_str = f"{row['country']}"
            if prefix_str == "None":
                english_name = "None"
            else:
                english_name = locate_country_iso(prefix_str)
            data_dict = {
                "name": english_name,
                "value": row[column_name]
            }
            data_array.append(data_dict)

        data_array.append(data_dict)

        result_dict = {
            "title": type_name,
            "data": data_array,
            "name": column_name
        }
        data_class_array.append(result_dict)
    return data_class_array


if __name__== '__main__':
    # Specify the variables for each iteration
    file_path = "../data/sat_result_20231117_20231123/"
    prefix_types = ["sum", "router", "seed"]
    type_name = "Country-Num"
    # Iterate through different combinations
    resultArray = []
    get_country_iso_dict()
    for prefix_type in prefix_types:
        for day in range(1, 8):
            csv_file_name = f"{prefix_type}_prefix_day_{day}_country_sat.csv"

            result_temp = generate_map_chart(file_path, type_name, csv_file_name)
            resultArray.append(result_temp)

        result = {"result": resultArray, "code": 1001, "msg": "success"}
        # 写入json文件中
        json_path = f"../data/get_data_result/map_result_country.json"
        # Save JSON data to a file
        with open(json_path, 'w') as json_file:
            json.dump(result, json_file, indent=2)