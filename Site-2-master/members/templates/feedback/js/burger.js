// $('body').hide()
document.addEventListener('DOMContentLoaded', function(){
    function toggleMenu(){
        $('.menuu').toggleClass('menuu_active')
        $('.popup').toggleClass('popup_active')
    }

$('.menuu').click(function(){ toggleMenu() })

function closeMenu() {
    $('.menu-toggle').removeClass('menu-toggle_active')
    $('.top-menu').removeClass('top-menu_active')
}
    $(document).click(function(e) {
        if ($(e.target).closest('.menu-container').length) return
        closeMenu()
})

})


