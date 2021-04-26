$(document).ready(function(){
	$("#control_card_div").load("/static/solutions/control_cards.html");
	$("#select_type_div").load("/static/solutions/select_motor_type.html");
	//$("#motor_card_div").load("/static/solutions/motor_cards.html");
	$('body').on('click', '#filter_url', function() {
		//$("#select_type_div").slideToggle("fast");
		if ($("#select_type_div").css("visibility") == "hidden") {
			$("#select_type_div").css("visibility","visible");
		}else{
			$("#select_type_div").css("visibility","hidden");
		}
	});

	$('body').on('change', '#input_voltage_sel, #tube_sel, #function_sel', function() {
		getMotorListXML();
	});

	$("#pager").zPager({
		totalData: 8,
		htmlBox: $('#wraper'),
		btnShow: true,
		ajaxSetData: false
	});
});

	function currentPage(currentPage){
	/*触发页码数位置： Page/js/jquery.z-pager.js 64行*/
		//console.log("当前页码数：" + currentPage);
		currMotorCardPageIndex = currentPage;
		updateDisplayMotorCards();
	}

//var xmlHttp = null;

//当前电机卡片的分页索引
var currMotorCardPageIndex = 1;

window.onload = function() {
	setTimeout(addLineToCurrentPageLink('#solutionsLink'),2000);
}

function updateDisplayMotorCards(){
	$('.motor_card').each(function(i,n){
		if($(n).attr("_pageIndex") !== currMotorCardPageIndex.toString()){
			$(n).css("display","none");
		}else{
			$(n).css("display","inline-block");
		}
		//console.log(currMotorCardPageIndex.toString());
	});
}

// $("#motor_card_div").children().remove();

function getMotorListXML(){
	$.ajax({
			  url: "/solutions.html/",
			  type: "POST",
			  data: {
				"voltage": $("#input_voltage_sel option:selected").val(),
				"csrfmiddlewaretoken": $("[name = 'csrfmiddlewaretoken']").val()  // 使用jQuery取出csrfmiddlewaretoken的值，拼接到data中
			  },
			  success: function (data) {
			  	if (data.status)
			  	{
			  		$(".helloTest").children().remove();
			  		$(".helloTest").html()
					console.log("服务器获取数据成功")
			  		console.log(data.data)
					var data_list = data.data;
			  		$.each(data_list, function (index, v) {
			  			var a = document.createElement('a')
						a.text = v.voltage__voltage;
			  			$("#motorCard").append(a);
			  			console.log("获取到的电压")
			  			console.log(v.voltage__voltage)
					})
				}
			  	else
				{
					console.log("服务器没有反馈数据")
					var a = document.createElement('a')
					a.text = "没有获取到符合条件的电机";
				}
			  }
	})
}
