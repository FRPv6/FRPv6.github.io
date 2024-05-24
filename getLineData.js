this.dataSeries=[]
this.dataLegend=[]
this.dataxAxis=[]
this.yAxisName=''
$.getJSON('data/get_data_result/line_result.json', function (chart) {
    let element_id_list = ["line-sum-type1", "line-sum-type2", "line-router-type1", "line-router-type2", "line-seed-type1", "line-seed-type2"]
    for(let i=0;i<6;i++){
        let dataArray=chart["result"][i]
        let that=this
        let element_id=element_id_list[i]
        that.dataSeries=dataArray["series"]
        that.dataLegend=dataArray["legend"]
        that.dataxAxis=dataArray["xAxis"]
        that.yAxisName=dataArray["yAxisName"]
        for (let i = 0; i < that.dataSeries.length; i++) {
            that.dataSeries[i]["type"] = "line";
            if(i==0){
                that.dataSeries[i]["yAxisIndex"]=0
            }else{
                that.dataSeries[i]["yAxisIndex"]=1
            }
        }
        let lineChart = echarts.init(document.getElementById(element_id));
        lineChart.setOption({
            tooltip: {
                trigger: 'axis',
                axisPointer: {
                    type: 'cross',
                },
            },
            legend: {
                data: that.dataLegend,
            },
            xAxis: [
                {
                    type: 'category',
                    boundaryGap: false,
                    // name: "时间",
                    data: that.dataxAxis,
                    axisTick: {
                        alignWithLabel: true,
                    },
                    axisLabel: {
                        textStyle: {
                            color: echarts.textColor,
                        },
                    },
                },
            ],
            yAxis: [
                {
                    name: that.yAxisName,
                    type:"value",
                    scale:true,
                    position: 'left',
                },
                // {
                //     // name: "Right Y-Axis",
                //     name: "#",
                //     type:"value",
                //     scale: true,
                //     position: 'right',
                // },
            ],
            series: that.dataSeries,
            dataZoom: [
                {
                    id: 'dataZoomX',
                    type: 'slider',
                    xAxisIndex: [0],
                    filterMode: 'filter',
                    top: 'bottom'
                }
            ],
        })
    }

});
