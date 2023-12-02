from config import DefaultConfig
from generate_pie_json import generate_pie_chart
from generate_pie_table_json import generate_table_chart
from generate_pie_sum_csv import generate_pie_sum_csv
from generate_line_json import generate_line_chart
from generate_line_sum_csv import generate_line_sum_csv
from generate_map_json import generate_map_chart
config = DefaultConfig()
if __name__ == '__main__':

    # 生成折线图sum.csv
    # pathArray = config.pathArray
    # for path in pathArray:
    #     generate_line_sum_csv(path)
    # 生成折线图.json
    # generate_line_chart()

    # 生成饼状图-地图 sum.csv
    generate_pie_sum_csv(config.file_path_last_week)
    # 生成饼状图.json
    generate_pie_chart()
    # 生成地图.json
    generate_map_chart()
    # 生成饼状图和地图的 dataTable
    generate_table_chart()

