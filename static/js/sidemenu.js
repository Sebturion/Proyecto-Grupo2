const btn = document.querySelector('#header');
const menu = document.querySelector('#sidemenu');
btn.addEventListener('click', e =>{
    menu.classList.toggle("menu-exanded");
    menu.classList.toggle("menu-collapsed");
    
    document.querySelector('body').classList.toggle('body-expanded');
});