window.onscroll = function() {
    scrollFunction();
};

function scrollFunction() {
    var btnScrollToTop = document.getElementById('btnScrollToTop');
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
        btnScrollToTop.style.display = 'block';
    } else {
        btnScrollToTop.style.display = 'none';
    }
}

function scrollToTop() {
    window.scrollTo({
        top: 0,
        behavior: 'smooth'
    });
}