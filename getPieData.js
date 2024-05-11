let class_list=["sum","router","seed"]
let json_file_list=["as", "category", "sub_category", "org"]
let id_type_list=["as", "category", "sub-category", "org"]
let chart_list=[[],[],[],[]]
let table_list=[{},{},{},{}]
$.ajaxSetup({async:false}); // 改异步为同步
for(let i=0;i<4;i++){
    let file_name=`data/get_data_result/pie_result_table_${json_file_list[i]}.json`
    // router or seed
    $.getJSON(file_name, function (data) {
        table_list[i]=data
    })
}

// 饼状图-四种type-初始化
for(let i=0;i<4;i++){
    let file_name=`data/get_data_result/pie_result_${json_file_list[i]}.json`
    // sum or router or seed
    for(let j=0;j<3;j++){
        for(let day=1;day<8;day++){
            $.getJSON(file_name, function (chart) {
                let index=j*7+day-1
                let element_id=`pie-${class_list[j]}-${id_type_list[i]}-day${day}`
                let lineChart = echarts.init(document.getElementById(element_id))
                chart_list[i].push(lineChart)
                let select_id=document.getElementById(`select-${class_list[j]}-${id_type_list[i]}-day${day}`)
                let select_value=select_id.value
                // console.log(`select-${class_list[j]}-${id_type_list[i]}-day${day}`,select_value)
                let dataArray=chart["result"][index][select_value-1]
                let dataTitle=dataArray["title"]
                let dataSeries=dataArray["data"]
                let dataName=dataArray["name"]
                let dataTableArray=table_list[i]["result"][index][select_value-1]
                let dataTableSeries=dataTableArray["data"]
                let dataTableColumns=dataTableArray["columns"]
                // let dataTableDataLength=dataTableArray["dataLength"]
                lineChart.setOption({
                    title: {
                        text: dataTitle,
                        left: 'center'
                    },
                    color:['#5470c6', '#91cc75', '#fac858', '#46e0cf','#ee6666', '#73c0de', '#3ba272', '#fc8452', '#9a60b4', '#ea7ccc'],
                    tooltip: {
                        trigger: 'item'
                    },
                    legend: {
                        orient: 'vertical',
                        left: 'left',
                        top:'10%',
                        show:false
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
                    series: [
                        {
                            name: dataName,
                            type: 'pie',
                            radius: '65%',//圆的半径
                            data: dataSeries,
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
// 饼状图-四种type-select-change事件监听
for(let i=0;i<4;i++){
    let file_name=`data/get_data_result/pie_result_${json_file_list[i]}.json`
    // sum or router or seed
    for(let j=0;j<3;j++){
        for(let day=1;day<8;day++) {
            let select_id=document.getElementById(`select-${class_list[j]}-${id_type_list[i]}-day${day}`)
            select_id.addEventListener('change', event => {
                let element_id=document.getElementById(`pie-${class_list[j]}-${id_type_list[i]}-day${day}`)
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
                $.getJSON(file_name, function (chart) {
                    let index=j*7+day-1
                    let lineChart = chart_list[i][index]
                    let dataArray=chart["result"][index][element_id.value-1]
                    let dataTitle=dataArray["title"]
                    let dataSeries=dataArray["data"]
                    let dataName=dataArray["name"]
                    let dataTableArray=table_list[i]["result"][index][element_id.value-1]
                    let dataTableSeries=dataTableArray["data"]
                    let dataTableColumns=dataTableArray["columns"]
                    // let dataTableDataLength=dataTableArray["dataLength"]
                    lineChart.setOption({
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
                                data: dataSeries,
                            }
                        ]
                    })
                    console.log(`pie-${class_list[j]}-${id_type_list[i]}-day${day}`)
                    // let line_element=document.getElementById(element_id)
                    // line_element.addEventListener('change', event => {
                    // })
                })
            })

        }
    }
}


// optionToContent: function(opt) {
//     let table='<table class="st-table">'
//     let table_th='<thead><tr><th scope="col">num</th>'
//     for(let k=0;k<dataTableHeadLength;k++){
//         table_th+='<th scope="col">' + dataTableSeries[k]["name"] + '</th>'
//     }
//     table_th+='</tr></thead>'
//     table+=table_th
//     let table_tb='<tbody>'
//     let table_tr=''
//     for(let k=0;k<dataTableDataLength;k++){
//         let table_tr_temp=`<tr><th scope="row">${k+1}</th>`
//         let table_tr_tb=''
//         for(let s=0;s<dataTableHeadLength;s++) {
//             table_tr_tb += '<td>'+dataTableSeries[s]["data"][k] + '</td>'
//         }
//         table_tr_temp=table_tr_temp+table_tr_tb+'</tr>'
//         table_tr+=table_tr_temp
//     }
//     console.log(table_th)
//     table_tb=table_tb+table_tr+'</tbody>'
//     table=table+table_tb+"</table>"
//     //初始化smart-table插件
//     $('.st-table').dataTable({
//         filterOn: true,
//         paginationPerPage: 10
//     });
//     return table
// },
