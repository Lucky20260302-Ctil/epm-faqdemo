// FAQ Site Authentication Gate
(function() {
  // Skip auth on the login page itself and 404 page
  var path = window.location.pathname;
  if (path.indexOf('/login') !== -1 || path.indexOf('/404') !== -1) return;

  // Check if already authenticated
  if (sessionStorage.getItem('faq_auth') === '1') return;

  // Redirect to login page, preserving the original target
  var target = encodeURIComponent(window.location.pathname + window.location.search);
  var loginUrl = path.replace(/\/[^/]*$/, '/login');
  if (loginUrl.indexOf('/login') === -1) {
    // If we're at root or can't resolve login, use base path
    var base = path.substring(0, path.indexOf('/', 1)) || '/epm-faqdemo';
    loginUrl = base + '/login';
  }
  window.location.href = loginUrl + '?r=' + target;
})();
