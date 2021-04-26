 $(document).ready(function(){

	$('body').on('mouseenter', "#in_card_pro_screen", function() {
		clearInterval(proCardSlideTimer);
	});

	$('body').on('mouseleave', "#in_card_pro_screen", function() {
		proCardSlideTimer = setInterval("productCardAutoSlide()",timeInterval);
	});

	$('body').on('mouseenter', "#in_card_sys_screen", function() {
		clearInterval(controlSysSlideTimer);
	});

	$('body').on('mouseleave', "#in_card_sys_screen", function() {
		controlSysSlideTimer = setInterval("controlSysCardAutoSlide()",timeInterval);
	});

	$('body').on('mousedown', '#in_card_pro_screen , #in_card_sys_screen', function(e) {
		isMouseDown = true;
		if ($(this).attr('id') == 'in_card_pro_screen'){
			moveProduct = true;
			moveControlSys = false;
		}else if($(this).attr('id') == 'in_card_sys_screen'){
			moveControlSys = true;
			moveProduct = false;
		}
		startX = e.clientX - this.offsetLeft;
		pressX = e.clientX;
		this.setCapture && this.setCapture();
		return false;
	});

	document.onmousemove = function(e) {
		if (isMouseDown) {
			var e = e || window.event;
			var oX = e.clientX - startX;
			var moveX = e.clientX - pressX;
			if (moveProduct) {
				productCardSlide(oX);
				if (moveX > 0) {
					proCardLeftMova = false;
				}else{
					proCardLeftMova = true;
				}
			}else if (moveControlSys) {
				controlSysCardSlide(oX);
				if (moveX > 0) {
					controlSysCardLeftMove = false;
				}else{
					controlSysCardLeftMove = true;
				}
			}
			return false;
		}
	};

	$(document).mouseup(function(e) {
		isMouseDown = false;
		// $("#in_card_pro_screen")[0].releaseCapture();
		// $("#in_card_sys_screen")[0].releaseCapture();
		e.cancelBubble = true;
		moveProduct = false;
		moveControlSys = false;
	});

//手机上的滑动
	$("body").on("touchstart", "#in_card_pro_screen , #in_card_sys_screen", function(e) {
		// 判断默认行为是否可以被禁用
		if (e.cancelable) {
		// 判断默认行为是否已经被禁用
			if (!e.defaultPrevented) {
				e.preventDefault();
			}
		}
		startX = e.originalEvent.changedTouches[0].pageX - this.offsetLeft;
		pressX = e.originalEvent.changedTouches[0].pageX;
	});

	$("body").on("touchmove", "#in_card_pro_screen , #in_card_sys_screen", function(e) {
		// 判断默认行为是否可以被禁用
		if (e.cancelable) {
		// 判断默认行为是否已经被禁用
			if (!e.defaultPrevented) {
				e.preventDefault();
			}
		}
		if ($(this).attr('id') == 'in_card_pro_screen'){
			moveProduct = true;
			moveControlSys = false;
		}else if($(this).attr('id') == 'in_card_sys_screen'){
			moveControlSys = true;
			moveProduct = false;
		}

		var oX = e.originalEvent.changedTouches[0].pageX - startX;
		var moveX = e.originalEvent.changedTouches[0].pageX - pressX;
		if (moveProduct) {
			productCardSlide(oX);
			if (moveX > 0) {
				proCardLeftMova = false;
			}else{
				proCardLeftMova = true;
			}
		}else if (moveControlSys) {
			controlSysCardSlide(oX);
			if (moveX > 0) {
				controlSysCardLeftMove = false;
			}else{
				controlSysCardLeftMove = true;
			}
		}
	});

});

//产品滑动
{
	var isMouseDown = false;
	var startX = 0;
	var pressX = 0;
	var moveProduct = false;
	var moveControlSys = false;

	var proCardLeftMova = true;
	var controlSysCardLeftMove = true;
	var timeInterval=2000;//间隔周期
	//定时函数：
	var proCardSlideTimer = setInterval("productCardAutoSlide()",timeInterval);
	var controlSysSlideTimer = setInterval("controlSysCardAutoSlide()",timeInterval);
}

function productCardSlide(moveX){
	if ($('#in_card_pro_screen').children().length == 5) {
		$('#in_card_pro_screen').html($('#in_card_pro_screen').html()+$('#in_card_pro_screen').html());
	}
	if (moveX >= 0) {
		$('#in_card_pro_screen').css('left',-1100 + moveX + 'px');
	}else if (moveX <= -1100) {
		$('#in_card_pro_screen').css('left', 1100 + moveX + 'px');
	}else{
		$("#in_card_pro_screen").css({"left": moveX + "px"});
	}
}

function controlSysCardSlide(moveX){
	if ($('#in_card_sys_screen').children().length == 6) {
		$('#in_card_sys_screen').html($('#in_card_sys_screen').html()+$('#in_card_sys_screen').html());
	}
	if (moveX >= 0) {
		$('#in_card_sys_screen').css('left',-1100 + moveX + 'px');
	}else if (moveX <= -1100) {
		$('#in_card_sys_screen').css('left', 1100 + moveX + 'px');
	}else{
		$("#in_card_sys_screen").css({"left": moveX + "px"});
	}
}


function productCardAutoSlide(){
	if ($('#in_card_pro_screen').children().length == 5) {
		$('#in_card_pro_screen').html($('#in_card_pro_screen').html()+$('#in_card_pro_screen').html());
	}
	if (proCardLeftMova == true) {
		if(parseInt($('#in_card_pro_screen').css('left')) <=-1100){
			$('#in_card_pro_screen').css('left','0px');
		}else{
			$('#in_card_pro_screen').css('left','-=50px');
		}
	}else{
		if(parseInt($('#in_card_pro_screen').css('left')) >= 0){
			$('#in_card_pro_screen').css('left','-1100px');
		}
		$('#in_card_pro_screen').css('left','+=50px');
	}
}

function controlSysCardAutoSlide(){
	if ($('#in_card_sys_screen').children().length == 6) {
		$('#in_card_sys_screen').html($('#in_card_sys_screen').html()+$('#in_card_sys_screen').html());
	}

	if (controlSysCardLeftMove == true) {
		if(parseInt($('#in_card_sys_screen').css('left')) <= -1100){
			$('#in_card_sys_screen').css('left','0px');
		}else{
			$('#in_card_sys_screen').css('left','-=50px');
		}
	}else{
		if(parseInt($('#in_card_sys_screen').css('left')) >= 0){
			$('#in_card_sys_screen').css('left','-1100px');
		}
		$('#in_card_sys_screen').css('left','+=50px');
	}
}