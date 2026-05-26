// FAQ Site Authentication Gate
(function() {
  var path = window.location.pathname;

  // Skip auth on the login page itself and 404 page
  if (path.indexOf('/login') !== -1 || path.indexOf('/404') !== -1) return;

  // Already authenticated — auth-verified class already set by inline script in <head>
  if (sessionStorage.getItem('faq_auth') === '1') return;

  // Resolve the correct login URL from this script's own src.
  // auth.js lives at {siteRoot}/static/auth.js, so login is at {siteRoot}/login.
  var loginUrl = '/login';
  var scripts = document.getElementsByTagName('script');
  for (var i = scripts.length - 1; i >= 0; i--) {
    var src = scripts[i].src || '';
    var idx = src.indexOf('/static/auth.js');
    if (idx !== -1) {
      var a = document.createElement('a');
      a.href = src;
      loginUrl = a.pathname.substring(0, idx) + '/login';
      break;
    }
  }

  window.location.href = loginUrl + '?r=' + encodeURIComponent(path + window.location.search);
})();
