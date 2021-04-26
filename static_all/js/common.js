 $(document).ready(function(){
	//$("#navbar_top").load("common/navbar_top.html");
	$("#product_menu").load("/static/index/product_menu.html");
	$("#product_slide").load("/static/index/product_slide.html");
	$("#control_system_slide").load("/static/index/control_system_slide.html");
	$("#how_to_buy").load("/static/common/how_to_buy.html");
	$("#footer").load("/static/common/footer.html");
	// $('body').on('mouseenter', "#search img", function() {
	// 	$(this).attr("src", "img/search-hover.png");
	// });

	// $('body').on('mouseleave', "#search img", function() {
	// 	$(this).attr("src", "img/search.png");
	// });

	$('body').on('mouseenter', ".product_bg", function() {
		$(this).children(".product_hide_url").css({ "opacity": "1" });
	});

	$('body').on('mouseleave', ".product_bg", function() {
		$(this).children(".product_hide_url").css({ "opacity": "0"  });
	});

	$('body').on('click', '.nav-link', function() {
		sessionStorage.setItem("goTo","");
		$(this).css('background-size','100% 3px');
		$(this).parent().siblings(".nav-item").children(".nav-link").css('background-size','0 3px');
		//销毁 from 防止页面刷新触发$('#xxx').click()
	});


	// $('body').on('click', '#more_url', function() {
	// 	if($('#in_card_screen').css('left')=='-1000px'){
	// 		$('#in_card_screen').css('left','0px');
	// 	}
	// 	$('#in_card_screen').css('left','-=200px');
	// });

});

function addLineToCurrentPageLink(currLink){
	$(currLink).css('background-size','100% 3px');
}


//横屏与竖屏的检查和刷新
window.addEventListener("onorientationchange" in window ? "orientationchange" : "resize", hengshuping, false);
	$(function(){  //页面加载时检查
		hengshuping();
	});

function hengshuping() {
	if (window.orientation == 0 || window.orientation == 180) {
		var shu=window.localStorage.getItem('name')
		if(shu=='a'){
			window.location.reload();
			window.localStorage.setItem('name','b');
		}
		//alert('竖屏')
		orientation = 'portrait';
		return false;
	}
	else if (window.orientation == 90 || window.orientation == -90) {
		window.localStorage.setItem('name','a');
		//alert('横屏')
		orientation = 'landscape';
		return false;
	}
}