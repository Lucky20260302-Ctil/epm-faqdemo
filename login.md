---
title: "FAQ 知識庫 — 登入"
---

<style>
.login-container {
  max-width: 400px;
  margin: 80px auto;
  padding: 2rem;
  text-align: center;
}
.login-container input {
  width: 100%;
  padding: 0.75rem;
  margin: 0.5rem 0;
  border: 2px solid var(--lightgray);
  border-radius: 8px;
  font-size: 1rem;
  background: var(--light);
  color: var(--dark);
  box-sizing: border-box;
}
.login-container input:focus {
  border-color: var(--secondary);
  outline: none;
  box-shadow: 0 0 0 3px rgba(199, 81, 46, 0.2);
}
.login-container button {
  width: 100%;
  padding: 0.75rem;
  background: var(--secondary);
  color: white;
  border: none;
  border-radius: 8px;
  font-size: 1rem;
  cursor: pointer;
  margin-top: 1rem;
}
.login-container button:hover {
  opacity: 0.9;
}
.login-error {
  color: #e53e3e;
  font-size: 0.85rem;
  margin-top: 0.5rem;
  display: none;
}
</style>

<div class="login-container">
  <h2>FAQ 知識庫</h2>
  <p>請輸入密碼以繼續訪問</p>
  <input type="password" id="pwd" placeholder="密碼" autofocus>
  <button onclick="doLogin()">登入</button>
  <p class="login-error" id="err">密碼錯誤，請重試</p>
</div>

<script>
// SHA-256 hash of the password
var PASS_HASH = '13f6f86007009ba5d103db1937abde14f4ac65dcd6d4c5a98fd65e3386e2124c';

async function sha256(str) {
  var buf = new TextEncoder().encode(str);
  var hash = await crypto.subtle.digest('SHA-256', buf);
  return Array.from(new Uint8Array(hash)).map(b => b.toString(16).padStart(2, '0')).join('');
}

async function doLogin() {
  var pwd = document.getElementById('pwd').value;
  var hash = await sha256(pwd);
  if (hash === PASS_HASH) {
    sessionStorage.setItem('faq_auth', '1');
    var params = new URLSearchParams(window.location.search);
    var target = params.get('r') || './';
    window.location.href = decodeURIComponent(target);
  } else {
    document.getElementById('err').style.display = 'block';
    document.getElementById('pwd').value = '';
  }
}

document.getElementById('pwd').addEventListener('keydown', function(e) {
  if (e.key === 'Enter') doLogin();
});
</script>
