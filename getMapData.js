let dataNameMap=[]
// let class_list=["sum""router","seed"]
let chart_map_list=[]
let table_object={}
let table_file_name=`data/get_data_result/pie_result_table_country.json`
let map_file_name=`data/get_data_result/map_result_country.json`
$.ajaxSetup({async:false}); // 改异步为同步

// sum or router or seed
$.getJSON(table_file_name, function (data) {
    table_object=data
})

// sum or router or seed 地图初始化
for(let i=0;i<3;i++){
    // 一共7天
    for(let day=1;day<8;day++){
        let index=i*7+day-1
        $.getJSON(map_file_name, function (chart) {
            let select_id=document.getElementById(`select-${class_list[i]}-country-day${day}`)
            let select_value=select_id.value
            // that.dataNameMap=this.dataNameMap
            let dataSeries=chart["result"][index][select_value-1]["data"]
            let dataName=chart["result"][index][select_value-1]["name"]
            let dataTitle=chart["result"][index][select_value-1]["title"]
            let dataTableArray=table_object["result"][index][select_value-1]
            let dataTableSeries=dataTableArray["data"]
            let dataTableColumns=dataTableArray["columns"]
            let element_id=`map-${class_list[i]}-country-day${day}`
            let mapChart = echarts.init(document.getElementById(element_id));
            chart_map_list.push(mapChart)
            let option = {
                title: {
                    text: dataTitle,
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
                    feature:{
                        dataView:{
                            show:true,
                            title:"查看全部数据",
                            lang : ['全部数据', 'close', 'refresh'],
                            buttonColor : '#3170c2',
                            optionToContent: function(opt) {
                                let table='<table class="table table-striped"></table>'
                                $(document).ready(function() {
                                    $('.table-striped').dataTable({
                                        searching: false,// 是否允许检索
                                        scrollX: false,// 水平滚动条
                                        scrollY: false,// 垂直滚动条
                                        data: dataTableSeries,
                                        columns: dataTableColumns
                                    });
                                })

                                return table;
                            }
                        }
                    }
                },
                // toolbox: {
                //     show: true,
                //     orient: 'vertical',
                //     x: 'right',
                //     y: 'center',
                //     feature: {
                //         mark: { show: true },
                //         dataView: { show: true, readOnly: false },
                //         restore: { show: true },
                //         saveAsImage: { show: true }
                //     }
                // },
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
                        name: dataName,
                        type: 'map',
                        map: 'world',
                        // type: 'effectScatter',//影响散点
                        coordinateSystem: 'geo',
                        data: dataSeries,
                        nameMap:dataNameMap,
                        label: {
                            show: false //地图上不显示国家名称
                        },
                    }
                ]
            };
            mapChart.setOption(option);
            mapChart.on('click', {seriesIndex: 0},function (params) {
                //点击节点事件的操作
                that.old_node=that.node
                that.node=params.value[2]
                console.log(that.node)
                // this.nodeChange.emit(this.node)
            })
        })
    }
}

// sum or router or seed type-select-change事件监听
for(let i=0;i<3;i++){
    // 一共7天
    for(let day=1;day<8;day++){
        let select_id=document.getElementById(`select-${class_list[i]}-country-day${day}`)
        select_id.addEventListener('change', event => {
            let element_id=document.getElementById(`map-${class_list[i]}-country-day${day}`)
            // 获取当前选中的选项的值
            let selectedValue = event.target.value;
            // 根据选项的值执行不同的操作
            if (selectedValue === '1') {
                element_id.value="1"

            } else if (selectedValue === '2') {
                element_id.value="2"
            } else {
                output.textContent = 'Unknown option';
            }
            $.getJSON(map_file_name, function (chart) {
                let index=i*7+day-1
                // that.dataNameMap=this.dataNameMap
                let dataSeries=chart["result"][index][element_id.value-1]["data"]
                let dataName=chart["result"][index][element_id.value-1]["name"]
                let dataTitle=chart["result"][index][element_id.value-1]["title"]
                let dataTableArray=table_object["result"][index][element_id.value-1]
                let dataTableSeries=dataTableArray["data"]
                let dataTableColumns=dataTableArray["columns"]
                let mapChart = chart_map_list[index]
                let option = {
                    title: {
                        text: dataTitle,
                    },
                    toolbox: {
                        feature:{
                            dataView:{
                                optionToContent: function(opt) {
                                    let table='<table class="table table-striped"></table>'
                                    $(document).ready(function() {
                                        $('.table-striped').dataTable({
                                            data: dataTableSeries,
                                            columns: dataTableColumns
                                        });
                                    })
                                    return table;
                                }
                            }
                        }
                    },
                    series: [
                        {
                            name: dataName,
                            data: dataSeries
                        }
                    ]
                };
                mapChart.setOption(option);
            })

        })


    }
}

