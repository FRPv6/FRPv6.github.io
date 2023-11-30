// 修改饼状图和地图导航栏的innerHTML
// pie or map class
let nav_prefix_list = ["pie", "map"]
let nav_class_list=["sum","router","seed"]
let time_list=[]
$.ajaxSetup({async:false}); // 改异步为同步
$.getJSON("data/get_data_result/line_time_list.json",function (data){
   time_list=data["data"]

});
// pie-sum-as-day2-tab
for(let day=1;day<8;day++){
    for(let i=0;i<3;i++){
        for(let j=0;j<2;j++){
            if(j===0){
                let nav_type_list=["as", "category", "sub-category", "org"]
                for(let type=0;type<4;type++){
                    let tab_id=`${nav_prefix_list[j]}-${nav_class_list[i]}-${nav_type_list[type]}-day${day}-tab`
                    let tab_element = document.getElementById(tab_id)
                    tab_element.innerHTML=time_list[day-1]
                }
            }else{
                let tab_id=`${nav_prefix_list[j]}-${nav_class_list[i]}-country-day${day}-tab`
                let tab_element = document.getElementById(tab_id)
                tab_element.innerHTML=time_list[day-1]
            }
        }
    }
}

