document.getElementById('searchButton').onclick = () => 
  document.getElementById('searchForm').submit();

function openSearchMobile() {
  document.getElementById('searchMobile').style.height = '100%';
}

function closeSearchMobile() {
  document.getElementById('searchMobile').style.height = '0%';
}
