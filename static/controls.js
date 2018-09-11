$(document).ready(function () {
    $(document).on("scroll", onScroll);
    
    //smoothscroll
    $('a[href^="#"]').on('click', function (e) {
        e.preventDefault();
        
        $(document).off("scroll");
        
        $('a').each(function () {
            $(this).removeClass('active');
        })
        $(this).addClass('active');
        var temp0=0;
        var temp=document.getElementById('main-menu').offsetHeight; 
        if ($('.navbar-toggler').attr('aria-expanded') === "true") {
        temp0=document.getElementById('navbarNav').offsetHeight;
         }
         temp=temp-temp0;
         var target = this.hash,
            menu = target;
        $target = $(target);
        $('html, body').stop().animate({
            'scrollTop': $target.offset().top-temp
        }, 500, 'swing', function () {
            window.location.hash = target;
            $(document).on("scroll", onScroll);
        });
    });

    $(window).resize(function (e) { 
        var temp=document.getElementById('main-menu').offsetHeight; 
        $('body').css('padding-top', temp);
    });
});

$(window).on('load',function (e) { 
        var temp=document.getElementById('main-menu').offsetHeight; 
        $('body').css('padding-top', temp);         
        if($(window).width()<990)
            $('#sxz').addClass('mr-5');
}); 



function onScroll(event){
    var scrollPos = $(document).scrollTop();
    $('#navbarNav a').each(function () {
       if (this.id!="res") {
        
        
         var currLink = $(this);
        var refElement = $(currLink.attr("href"));
        var temp0=0;
        var temp=document.getElementById('main-menu').offsetHeight+1; 
        if ($('.navbar-toggler').attr('aria-expanded') === "true") {
        temp0=document.getElementById('navbarNav').offsetHeight;
         }
         temp=temp-temp0;
        if (refElement.position().top <= (scrollPos+temp) && refElement.position().top + refElement.height() > (scrollPos+temp)) {
            $('#navbarNav ul li a').removeClass("active");
            currLink.addClass("active");
        }
        else{
            currLink.removeClass("active");
        } }
    });
}

