this.dataSeries=[]
this.dataLegend=[]
this.dataxAxis=[]
// let lineChart = echarts.init(document.getElementById('line-router-1'));
// lineChart.setOption({
//     tooltip: {
//         trigger: 'axis',
//         axisPointer: {
//             type: 'cross',
//         },
//     },
//     legend: {
//         data: [
//             "aliased prefix",
//             "all prefix"
//         ],
//     },
//     xAxis: [
//         {
//             type: 'category',
//             boundaryGap: false,
//             name: "时间",
//             data: [
//                 "Day1",
//                 "Day2",
//                 "Day3",
//                 "Day4",
//                 "Day5",
//                 "Day6",
//                 "Day7"
//             ],
//             axisTick: {
//                 alignWithLabel: true,
//             },
//             axisLabel: {
//                 textStyle: {
//                     color: echarts.textColor,
//                 },
//             },
//         },
//     ],
//     yAxis: [
//         {
//             name: "左侧Y轴",
//             type:"value",
//             position: 'left',
//
//         },
//         {
//             name: "右侧Y轴",
//             type:"value",
//             position: 'right',
//
//         },
//     ],
//     series: [
//          {
//             "name": "aliased prefix",
//             "data": [
//                 4359.0,
//                 4335.0,
//                 4336.0,
//                 4868.0,
//                 4384.0,
//                 4357.0,
//                 4384.0
//             ],
//              yAxisIndex: 0,
//              type:"line"
//          },
//          {
//              "name": "all prefix",
//                 "data": [
//                     201974.0,
//                     201689.0,
//                     201902.0,
//                     202254.0,
//                     202569.0,
//                     203482.0,
//                     204301.0
//                 ],
//              yAxisIndex: 1,
//              type:"line"
//          }
//     ],
//     dataZoom: [
//         {
//             id: 'dataZoomX',
//             type: 'slider',
//             xAxisIndex: [0],
//             filterMode: 'filter',
//             top: 'bottom'
//         }
//     ],
// })
$.getJSON('data/get_data_result/line_result.json', function (chart) {
    let element_id_list = ["line-sum-type1", "line-sum-type2", "line-router-type1", "line-router-type2", "line-seed-type1", "line-seed-type2"]
    for(let i=0;i<6;i++){
        let dataArray=chart["result"][i]
        let that=this
        let element_id=element_id_list[i]
        that.dataSeries=dataArray["series"]
        that.dataLegend=dataArray["legend"]
        that.dataxAxis=dataArray["xAxis"]
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
                    name: "Left Y-Axis",
                    type:"value",
                    scale:true,
                    position: 'left',
                },
                {
                    name: "Right Y-Axis",
                    type:"value",
                    scale: true,
                    position: 'right',
                },
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
