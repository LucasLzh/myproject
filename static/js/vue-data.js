var navbarTop = new Vue({
  el: '#navbar_top',
  data: {
    dataContent: '\
		<nav class="navbar navbar-expand-md flex-top navbar-light" style="font-size: 10px;\
		color: #303030;position: relative">\
		  <a class="navbar-brand" href="/" target=_self>\
		    <img src="/static/img/01 logo-01@2x.png" alt="Logo" style="width:100px">\
		  </a>\
		  <button class="navbar-toggler" type="button" data-toggle="collapse" \
		  data-target="#collapsibleNavbar" style="outline:none">\
		    <span class="navbar-toggler-icon"></span>\
		  </button>\
		  <div class="collapse navbar-collapse" id="collapsibleNavbar">\
		    <ul class="navbar-nav m-auto">\
		      <li class="nav-item">\
		        <a class="nav-link nav_link_top" id="autoSysLink" href="/auto_sys.html" \
		        target=_self>Automation System</a>\
		      </li>\
		      <li class="nav-item">\
		        <a class="nav-link nav_link_top" id="solutionsLink" href="/solutions.html" target=_self>Solutions</a>\
		      </li>\
		      <li class="nav-item">\
		        <a class="nav-link nav_link_top" id="productsLink" href="/product.html" target=_self>Products</a>\
		      </li>\
		      <li class="nav-item">\
		        <a class="nav-link nav_link_top" href="###" target=_self>Support</a>\
		      </li>\
		      <li class="nav-item">\
		        <a class="nav-link nav_link_top" href="###" target=_self>Contact</a>\
		      </li>\
		    </ul>\
		  </div>\
		  <div class="navbar_menu">\
		    <ul> \
		      <li>\
		        <a href="###" target=_self>\
		          <img src="/static/img/03 user.png" alt="user" style="width:16px">\
		        </a>\
		      </li>\
		      <li>\
		        <a href="###" target=_self>\
		          <img src="/static/img/02 Search gray.png" alt="search" style="width:16px">\
		        </a>\
		      </li>\
		    </ul>\
		  </div>\
		</nav>'
  	}
})