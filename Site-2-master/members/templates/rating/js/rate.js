let star = document.querySelectorAll('input')
let showValue = document.querySelector('#rating-value')

for (let i = 0; i < star.length; i++){
    star[i].addEventListener('click', function(){
        i = this.value;
        document.getElementById('rating-value').value = i;
        showValue.innerHTML = i;
    });
}