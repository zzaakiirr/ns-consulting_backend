document.getElementById('searchButton').onclick = function() { 
  document.getElementById('searchForm').submit();
};

function openSearchMobile() {
  document.getElementById('searchMobile').style.height = '100%';
}

function closeSearchMobile() {
  document.getElementById('searchMobile').style.height = '0%';
}
