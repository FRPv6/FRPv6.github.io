this.dataSeries=[]
this.dataName=[]
this.dataTitle=[]
class_list=["router","seed"]
json_file_list=["as", "category", "sub_category", "org"]
id_type_list=["as", "category", "sub-category", "org"]
// 饼状图-四种type
for(let i=0;i<4;i++){
    let file_name=`data/get_data_result/pie_result_${json_file_list[i]}.json`
    // router or seed
    for(let j=0;j<2;j++){
        for(let day=1;day<8;day++){
            $.getJSON(file_name, function (chart) {
                let index=j*7+day-1
                let element_id=`pie-${class_list[j]}-${id_type_list[i]}-day${day}`
                let that=this
                let lineChart = echarts.init(document.getElementById(element_id));
                let dataArray=chart["result"][index]
                that.dataTitle=dataArray["title"]
                that.dataSeries=dataArray["data"]
                that.dataName=dataArray["name"]
                lineChart.setOption({
                    title: {
                        text: that.dataTitle,
                        left: 'center'
                    },
                    tooltip: {
                        trigger: 'item'
                    },
                    legend: {
                        orient: 'vertical',
                        left: 'left',
                        top:'10%'
                    },
                    series: [
                        {
                            name: that.dataName,
                            type: 'pie',
                            radius: '50%',
                            data: that.dataSeries,
                            emphasis: {
                                itemStyle: {
                                    shadowBlur: 10,
                                    shadowOffsetX: 0,
                                    shadowColor: 'rgba(0, 0, 0, 0.5)'
                                }
                            }
                        }
                    ]
                })
            })
        }
    }

}

