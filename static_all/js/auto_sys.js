 $(document).ready(function(){
	$("#mid_product_content").load("/static/auto_sys/bridge_menu.html");

	$('body').on('click', '.bdg_card_url', function() {
		var currLink = $(this).attr('_link');

		midProductContentChange(currLink)

		sessionStorage.setItem("goTo",currLink);
	});

});

window.onload = function() {
	setTimeout(goToSelectContent,500);

	setTimeout(addLineToCurrentPageLink('#autoSysLink'),2000);
}

function goToSelectContent(){
	var currLink = sessionStorage.getItem("goTo");
	if (currLink.length > 0) {
		midProductContentChange(currLink)
	}
}

function midProductContentChange(currLink){
	$("#top_image_div").css("display","none");
	$("#mid_product_content").children().remove();
	$("#mid_product_content").load(currLink);
}