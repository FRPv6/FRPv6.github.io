
import json

# 自定义地区的名称映射

if __name__ == "__main__":
    resultArray = []
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
        country_iso = {
            EnglishName: country
        }

        resultArray.append(country_iso)
    # 写入json文件中
    json_path = f"../data/get_data_result/country_iso_map.json"
    # Save JSON data to a file
    with open(json_path, 'w') as json_file:
        json.dump(resultArray, json_file, indent=2)

