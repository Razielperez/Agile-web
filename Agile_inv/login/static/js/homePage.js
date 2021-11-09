$(document).ready(function(){


    $(".counterVal").each(function() {
        let element = $(this);
        let endVal = parseInt(element.text());
        element.countup(endVal);
    });

    $('.chart').easyPieChart({
        easing: 'easeInOut',
        barColor:'crimson',
        trackColor: false,
        scaleColor: false,
        lineWidth: 4,
        size: 152,
        onStep: function(from , to ,percent){
            $(this.el).find('.percent').text(Math.round(percent))
        }
    });

    let typed = new Typed(".typing", {
        strings: ["Messages" , "Projects" , "Sprint" , "User Stories" , "Teams"],
        typeSpeed: 100,
        backSpeed: 60,
        startDelay: 2000,
        showCursor: false,
        loop: true
    });


});



