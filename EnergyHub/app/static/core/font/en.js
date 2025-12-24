var hamburger = document.querySelector('.navbar__hamburger');
var menuitem = document.querySelectorAll('.navbar__menuitem');
var icontop = document.querySelector('.navbar__hamburger-top');
var iconmiddle = document.querySelector('.navbar__hamburger-middle');
var iconbottom = document.querySelector('.navbar__hamburger-bottom');

hamburger.addEventListener('click', function() {
    for (var i = 0; i < menuitem.length; i++) {
        menuitem[i].classList.toggle('navbar__menuitem--toggled');
    }
    hamburger.classList.toggle('navbar__hamburger--toggled');
    icontop.classList.toggle('navbar__hamburger-top--toggled');
    iconmiddle.classList.toggle('navbar__hamburger-middle--toggled');
    iconbottom.classList.toggle('navbar__hamburger-bottom--toggled');
});