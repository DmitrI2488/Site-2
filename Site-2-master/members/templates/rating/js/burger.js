// $('body').hide()
document.addEventListener('DOMContentLoaded', function(){
    function toggleMenu1(){
        $('.star-5').toggleClass('.star')
        $('.ratings1').toggleName('rating')
    }


$('.star-5').click(function(){ toggleMenu1() })


function closeMenu() {
    $('.menu-toggle').removeClass('menu-toggle_active')
    $('.top-menu').removeClass('top-menu_active')
}
    $(document).click(function(e) {
        if ($(e.target).closest('.menu-container').length) return
        closeMenu()
})

})


