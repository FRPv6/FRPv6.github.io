import pandas as pd
import json


def generate_pie_chart(prefix_type, pic_name, csv_file_name, column_name, select_num):
    # Read CSV file into DataFrame
    df = pd.read_csv(csv_file_name)

    # Sort DataFrame based on the specified column in descending order
    df = df.sort_values(by=column_name, ascending=False, inplace=False)

    # Calculate the ratio of selected rows and the ratio of the remaining rows
    other_ratio = 1 - df[column_name][:select_num].sum()

    # Create a list of dictionaries containing information for each selected row and the "Others" category
    data = []
    for index, df_iterrow in df[:select_num].iterrows():
        if pic_name == "Sub_category-Num":
            prefix_str=f"{df_iterrow['sub_category']}-{df_iterrow['number of aliased prefix']}"
        if pic_name == "Org-AS-Num":
            prefix_str=f"{df_iterrow['org_name']}-{df_iterrow['as']}-{df_iterrow['number of aliased prefix']}"
        if pic_name == "Country-Num":
            prefix_str=f"{df_iterrow['country']}-{df_iterrow['number of aliased prefix']}"
        if pic_name == "Category-Num":
            prefix_str=f"{df_iterrow['category']}-{df_iterrow['number of aliased prefix']}"
        if pic_name == "AS-Num-Org":
            prefix_str=f"{df_iterrow['as']}-{df_iterrow['number of aliased prefix']}-{df_iterrow['org_name']}"
        data_dict = {
            "name": f"{prefix_str}",
            "y": df_iterrow[column_name]
        }
        data.append(data_dict)

    data_dict = {
        "name": "Others",
        "y": other_ratio
    }
    data.append(data_dict)

    # Create JSON data
    json_data = {
        "chart": {
            "plotBackgroundColor": "white",
            "plotBorderWidth": "0",
            "plotShadow": "false",
            "type": "pie"
        },
        "title": {
            "text": pic_name,
            "align": "left"
        },
        "tooltip": {
            "pointFormat": "{series.name}: <b>{point.percentage:.1f}%</b>"
        },
        "accessibility": {
            "point": {
                "valueSuffix": "%"
            }
        },
        "plotOptions": {
            "pie": {
                "allowPointSelect": "true",
                "cursor": "pointer",
                "dataLabels": {
                    "enabled": "false"
                },
                "showInLegend": "true"
            }
        },
        "series": [
            {
                "name": column_name,
                "colorByPoint": "true",
                "data": data
            }
        ]
    }

    # Save JSON data to a file
    with open(f"{csv_file_name.split('.csv')[0]}.json", 'w') as json_file:
        json.dump(json_data, json_file, indent=2)


# Specify the variables for each iteration
prefix_types = ["seed"]  # Add more prefix types if needed
pic_names = ["Sub_category-Num", "Org-AS-Num", "Country-Num", "Category-Num",
             "AS-Num-Org"]  # Add more pic names if needed

# Iterate through different combinations
for prefix_type in prefix_types:
    for pic_name in pic_names:
        csv_file_name = f"{prefix_type}_prefix_day_5_{pic_name.split('-')[0].lower()}_sat.csv"  # Modify this as needed
        column_name = 'ratio of aliased prefix'
        select_num = 9

        generate_pie_chart(prefix_type, pic_name, csv_file_name, column_name, select_num)
