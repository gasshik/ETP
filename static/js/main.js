const themeBtn = document.getElementById('theme-switcher');
const htmlElement = document.documentElement;

themeBtn.addEventListener('click', () => {
  htmlElement.classList.toggle('dark-theme');
  if (htmlElement.classList.contains('dark-theme')) {
    themeBtn.innerText = "☀️";
  }
  else {
    themeBtn.innerText = "🌙";
  }
  


});