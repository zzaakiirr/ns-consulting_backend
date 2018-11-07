document.getElementById('searchButton').onclick = () => 
  document.getElementById('searchForm').submit();

document.getElementById('searchButtonMobile').onclick = () => 
  document.getElementById('searchFormMobile').submit();

function openNav() {
  document.getElementById('searchMobile').style.height = '100%';
}

function closeNav() {
  document.getElementById('searchMobile').style.height = '0%';
}
