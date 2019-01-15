const forEach=function(t,o,r){if('[object Object]'===Object.prototype.toString.call(t))for(var c in t)Object.prototype.hasOwnProperty.call(t,c)&&o.call(r,t[c],c,t);else for(var e=0,l=t.length;l>e;e++)o.call(r,t[e],e,t)};

var hamburgers = document.querySelectorAll('.hamburger');
if (hamburgers.length > 0) {
  forEach(hamburgers, function(hamburger) {
    hamburger.addEventListener('click', function() {
      this.classList.toggle('is-active');
      var navbarSM = document.getElementById('topNavbarSM');
      if(!navbarSM.classList.contains('is-active')) {
        navbarSM.className += ' is-active';
        navbarSM.style.display = 'block';
      } else {
        navbarSM.className = navbarSM.className.replace(/\b is-active\b/g, '');
        navbarSM.style.display = 'none';
      }
    }, false);
  });
}

window.onresize = function() {
  var navbarSM = document.getElementById('topNavbarSM');
  if(window.outerWidth >= 660) {
    var navbarSM = document.getElementById('topNavbarSM');
    navbarSM.style.display = 'none';
  } else if (window.outerWidth < 660 && navbarSM.className.includes('is-active')) {
    navbarSM.style.display = 'block';
  }
};
