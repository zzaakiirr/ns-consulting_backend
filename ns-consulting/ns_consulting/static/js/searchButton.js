document.getElementById('searchButton').onclick = function() { 
  document.getElementById('searchForm').submit();
};

document.getElementById('searchButtonMobile').onclick = function() {
  document.getElementById('searchFormMobile').submit();
};

function openSearchMobile() {
  document.getElementById('searchMobile').style.height = '100%';
};

function closeSearchMobile() {
  document.getElementById('searchMobile').style.height = '0%';
};
