document.getElementById('searchButton').onclick = function() { 
  document.getElementById('searchForm').submit();
};

document.getElementById('searchButtonMobile').onclick = function() {
  document.getElementById('searchFormMobile').submit();
};

function openNav() {
  document.getElementById('searchMobile').style.height = '100%';
}

function closeNav() {
  document.getElementById('searchMobile').style.height = '0%';
}
