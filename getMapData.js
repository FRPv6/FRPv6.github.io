let file_name="data/get_data_result/map_result_country.json"
let dataNameMap=[]
class_list=["router","seed"]
$.ajaxSetup({async:false}); // 改异步为同步
// $.getJSON("data/get_data_result/country_iso_map.json",function (data){
//     dataNameMap=data
// })
// router or seed
for(let i=0;i<2;i++){
    // 一共7天
    for(let day=1;day<8;day++){
        let index=i*7+day-1
        $.getJSON(file_name, function (chart) {
            let that=this
            // that.dataNameMap=this.dataNameMap
            that.dataSeries=chart["result"][index]["data"]
            let element_id=`map-${class_list[i]}-country-day${day}`
            let myChart = echarts.init(document.getElementById(element_id));
            let option = {
                title: {
                    text: 'Country-Num',
                    x: 'center'
                },
                tooltip: {
                    trigger: 'item',
                    formatter: '{a}<br/>{b}: {c}',
                    showDelay: 0,
                    transitionDuration: 0.2
                },
                visualMap: {
                    left: 'right',
                    min: 0,
                    max: 150,
                    inRange: {
                        color: [
                            '#e0f3f8',
                            '#abd9e9',
                            '#74add1',
                            '#4575b4',
                            '#313695',
                        ]
                    },
                    text: ['High', 'Low'],
                    calculable: true
                },
                toolbox: {
                    show: true,
                    orient: 'vertical',
                    x: 'right',
                    y: 'center',
                    feature: {
                        mark: { show: true },
                        dataView: { show: true, readOnly: false },
                        restore: { show: true },
                        saveAsImage: { show: true }
                    }
                },
                // roamController: {
                //     show: true,
                //     x: 'right',
                //     mapTypeControl: {
                //         'world': true
                //     }
                // },
                geo: {
                    map: 'world',

                },
                series: [
                    {
                        name: 'number of aliased prefix',
                        type: 'map',
                        map: 'world',
                        // type: 'effectScatter',//影响散点
                        coordinateSystem: 'geo',
                        data: that.dataSeries,
                        nameMap:dataNameMap,
                        label: {
                            show: false //地图上不显示国家名称
                        },
                    }
                ]
            };

            myChart.setOption(option);

            myChart.on('click', {seriesIndex: 0},function (params) {
                //点击节点事件的操作
                that.old_node=that.node
                that.node=params.value[2]
                console.log(that.node)
                // this.nodeChange.emit(this.node)
            })
        })


    }
}

