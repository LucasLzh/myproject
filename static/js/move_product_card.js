 $(document).ready(function(){

	$('body').on('mouseenter', "#in_card_pro_screen", function() {
		clearInterval(proCardSlideTimer);
	});

	$('body').on('mouseleave', "#in_card_pro_screen", function() {
		proCardSlideTimer = setInterval("productCardSlide()",timeInterval);
	});

	$('body').on('mouseenter', "#in_card_sys_screen", function() {
		clearInterval(controlSysSlideTimer);
	});

	$('body').on('mouseleave', "#in_card_sys_screen", function() {
		controlSysSlideTimer = setInterval("controlSysCardSlide()",timeInterval);
	});

	//鼠标移动滚动区域
	$('body').on('mousedown', '#in_card_pro_screen , #in_card_sys_screen', function() {
		isMouseDown = true;
		startX = event.clientX;
	});

	$('body').on('mousemove', '#in_card_pro_screen , #in_card_sys_screen', function() {
		if (isMouseDown === true) {
			var moveX = event.clientX-startX;
			if (moveX > 20) {
				if ($(this).attr('id')=='in_card_pro_screen'){
					proCardLeftMova = false;
					productCardSlide();
				}else if ($(this).attr('id')=='in_card_sys_screen') {
					controlSysCardLeftMove = false;
					controlSysCardSlide();
				}
				isMouseDown = false;
			}else if (moveX < -20){
				if ($(this).attr('id')=='in_card_pro_screen'){
					proCardLeftMova = true;
					productCardSlide();
				}else if ($(this).attr('id')=='in_card_sys_screen') {
					controlSysCardLeftMove = true;
					controlSysCardSlide();
				}
				isMouseDown = false;
			}
		}
	});

	$("body").on("touchstart", "#in_card_pro_screen , #in_card_sys_screen", function(e) {
		// 判断默认行为是否可以被禁用
		if (e.cancelable) {
		// 判断默认行为是否已经被禁用
			if (!e.defaultPrevented) {
				e.preventDefault();
			}
		}
		startX = e.originalEvent.changedTouches[0].pageX;
	});

	$("body").on("touchend", "#in_card_pro_screen , #in_card_sys_screen", function(e) {
		// 判断默认行为是否可以被禁用
		if (e.cancelable) {
		// 判断默认行为是否已经被禁用
			if (!e.defaultPrevented) {
				e.preventDefault();
			}
		}
		var moveEndX = e.originalEvent.changedTouches[0].pageX;
		var X = moveEndX - startX;
		if ( X > 20 ) {
			if ($(this).attr('id')=='in_card_pro_screen'){
				proCardLeftMova = false;
				productCardSlide();
			}else if ($(this).attr('id')=='in_card_sys_screen') {
				controlSysCardLeftMove = false;
				controlSysCardSlide();
			}
		}else if ( X < -20 ) {
			if ($(this).attr('id')=='in_card_pro_screen'){
				proCardLeftMova = true;
				productCardSlide();
			}else if ($(this).attr('id')=='in_card_sys_screen') {
				controlSysCardLeftMove = true;
				controlSysCardSlide();
			}
		}
	});

});

//产品滚动区自动向左滑动
{
	var timeInterval=2000;//间隔周期
	//定时函数：
	var proCardSlideTimer = setInterval("productCardSlide()",timeInterval);
	var controlSysSlideTimer = setInterval("controlSysCardSlide()",timeInterval);

	var isMouseDown=false;
	var startX=0;

	var proCardLeftMova = true;
	var controlSysCardLeftMove = true;
}

function productCardSlide(){
	if ($('#in_card_pro_screen').children().length == 5) {
		$('#in_card_pro_screen').html($('#in_card_pro_screen').html()+$('#in_card_pro_screen').html());
	}
	if (proCardLeftMova == true) {
		if($('#in_card_pro_screen').css('left')=='-1100px'){
			$('#in_card_pro_screen').css('left','0px');
		}else{
			$('#in_card_pro_screen').css('left','-=50px');
		}
	}else{
		if($('#in_card_pro_screen').css('left')=='0px'){
			$('#in_card_pro_screen').css('left','-1100px');
		}
		$('#in_card_pro_screen').css('left','+=50px');
	}
}

function controlSysCardSlide(){
	if ($('#in_card_sys_screen').children().length == 6) {
		$('#in_card_sys_screen').html($('#in_card_sys_screen').html()+$('#in_card_sys_screen').html());
	}

	if (controlSysCardLeftMove == true) {
		if($('#in_card_sys_screen').css('left')=='-1100px'){
			$('#in_card_sys_screen').css('left','0px');
		}else{
			$('#in_card_sys_screen').css('left','-=50px');
		}
	}else{
		if($('#in_card_sys_screen').css('left')=='0px'){
			$('#in_card_sys_screen').css('left','-1100px');
		}
		$('#in_card_sys_screen').css('left','+=50px');
	}
}