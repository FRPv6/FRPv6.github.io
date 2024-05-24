from config import DefaultConfig
from generate_line_64_csv import generate_line_seed_64_csv,generate_line_router_64_csv
from generate_line_json import generate_line_chart
from generate_line_sum_csv import generate_line_sum_csv
from generate_pie_json import generate_pie_chart
from generate_pie_table_json import generate_table_chart
from generate_pie_64_csv import generate_pie_64_csv
from generate_pie_attributes_csv import generate_pie_attributes_csv
from generate_map_json import generate_map_chart
config = DefaultConfig()
if __name__ == '__main__':

    #生成折线图/64.csv
    # generate_line_router_64_csv(config.router_prefix,config.path_name)
    # generate_line_seed_64_csv(config.seed_prefix,config.path_name)


    # 生成折线图sum.csv
    # generate_line_sum_csv(config.path_name)
    # 生成折线图.json
    # generate_line_chart(config.path_name)
    # 生成饼状图-地图 64.csv
    # generate_pie_64_csv(config.path_name)
    # 生成饼状图-地图 attributes+ratio.csv
    # generate_pie_attributes_csv(config.path_name)
    # 生成饼状图.json
    # generate_pie_chart(config.path_name)
    # # # 生成地图.json
    # generate_map_chart(config.path_name)
    # # # 生成饼状图和地图的 dataTable
    generate_table_chart(config.path_name)

