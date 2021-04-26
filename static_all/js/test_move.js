// 定时器的启动与停止
// $('body').on('mouseenter', "#in_card_pro_screen", function() {
// 	clearInterval(proCardSlideTimer);
// });

// $('body').on('mouseleave', "#in_card_pro_screen", function() {
// 	proCardSlideTimer = setInterval("productCardSlide()",timeInterval);
// });

// $('body').on('mouseenter', "#in_card_sys_screen", function() {
// 	clearInterval(controlSysSlideTimer);
// });

// $('body').on('mouseleave', "#in_card_sys_screen", function() {
// 	controlSysSlideTimer = setInterval("controlSysCardSlide()",timeInterval);
// });

var startX = 0;
var startY = 0;
$("body").on("touchstart", "#in_card_pro_screen", function(e) {
	// 判断默认行为是否可以被禁用
	if (e.cancelable) {
	// 判断默认行为是否已经被禁用
		if (!e.defaultPrevented) {
			e.preventDefault();
		}
	}
	startX = e.originalEvent.changedTouches[0].pageX;
	startY = e.originalEvent.changedTouches[0].pageY;
});

$("body").on("touchend", "#in_card_pro_screen", function(e) {
	// 判断默认行为是否可以被禁用
	if (e.cancelable) {
	// 判断默认行为是否已经被禁用
		if (!e.defaultPrevented) {
			e.preventDefault();
		}
	}
	var moveEndX = e.originalEvent.changedTouches[0].pageX;
	var moveEndY = e.originalEvent.changedTouches[0].pageY;
	var X = moveEndX - startX;
	var Y = moveEndY - startY;
	if ( X > 0 ) {
		//alert('右滑');
		productCardSlide(false);
	}
	else if ( X < 0 ) {
		//alert('左滑');
		productCardSlide(true);
	}
});


  var box=$("#small-box");
  var body=$('body');
  var index=0;
  var x1;
  box.mousedown(function(){
    index=1;       //鼠标按下才能触发onmousemove方法
    var x=event.clientX;   //鼠标点击的坐标值，x
    var left= this.style.left;
    left=left.substr(0,left.length-2);  //去掉px
    x1=parseInt(x-left);
  });
  box.mousemove(function(){
    if(index===1){
      this.style.left=event.clientX-x1+'px';
      if(this.style.left.substr(0,this.style.left.length-2)<0){
        this.style.left=0;
      };
      if(this.style.left.substr(0,this.style.left.length-2)>150){
        this.style.left='150px';
      };
    }
  });
  box.mouseup(function(){
    index=0;
  });
  body.mouseup(function(){
    index=0;
  });