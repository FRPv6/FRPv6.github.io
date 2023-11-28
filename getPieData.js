this.dataSeries=[]
this.dataName=[]
this.dataTitle=[]
// select value change function
let pie_id= document.getElementById("pie-router-as-day1")
let select_id=document.getElementById("select-router-as-day1")

select_id.addEventListener('change', event => {
    // 获取当前选中的选项的值
    const selectedValue = event.target.value;
    // 根据选项的值执行不同的操作
    if (selectedValue === '1') {
        pie_id.value="1"

    } else if (selectedValue === '2') {
        pie_id.value="2"
    } else {
        output.textContent = 'Unknown option';
    }
    console.log(pie_id.value)

})
class_list=["router","seed"]
json_file_list=["as", "category", "sub_category", "org"]
id_type_list=["as", "category", "sub-category", "org"]
let table_list=[{},{},{},{}]
$.ajaxSetup({async:false}); // 改异步为同步
for(let i=0;i<4;i++){
    let file_name=`data/get_data_result/pie_result_all_${json_file_list[i]}.json`
    // router or seed
    $.getJSON(file_name, function (chart) {
        table_list[i]=chart
    })
    for(let j=0;j<2;j++){
        for(let day=1;day<8;day++){
        }
    }
}

// 饼状图-四种type-初始化
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
                let dataTableArray=table_list[i]["result"][index]
                let dataTableSeries=dataTableArray["data"]
                let dataTableColumns=dataTableArray["columns"]
                let dataTableDataLength=dataTableArray["dataLength"]
                lineChart.setOption({
                    title: {
                        text: that.dataTitle,
                        left: 'center'
                    },
                    color:['#5470c6', '#91cc75', '#fac858', '#46e0cf','#ee6666', '#73c0de', '#3ba272', '#fc8452', '#9a60b4', '#ea7ccc'],
                    tooltip: {
                        trigger: 'item'
                    },
                    legend: {
                        orient: 'vertical',
                        left: 'left',
                        top:'10%'
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
                                    console.log(dataTableSeries.length)
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
                lineChart.addEventListener('change', event => {
                    // 获取当前的值
                    const selectedValue = event.value;

                })
            })
        }
    }
}

// 饼状图-四种type-change事件监听
select_id.addEventListener('change', event => {

})
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
