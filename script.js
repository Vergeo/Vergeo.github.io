window.onbeforeunload = function () {
    window.scrollTo(0, 0);
}

document.addEventListener("DOMContentLoaded", () => {


    document.querySelector(".modeswitch").onclick = function() {
        if (document.querySelector(".circle").classList.contains('dark')) {
            document.querySelector(".circle").classList.add('light');
            document.querySelector(".circle").classList.remove('dark');


        } else {
            document.querySelector(".circle").classList.add('dark');
            document.querySelector(".circle").classList.remove('light');
        } 
    }

    const left = document.querySelector(".home-btn").getBoundingClientRect().left+"px";
    const width = document.querySelector(".home-btn").offsetWidth+"px";
    document.querySelector(".nav-highlight").style.setProperty('--prev-width', width);
    document.querySelector(".nav-highlight").style.setProperty('--prev-left', left);
    document.querySelector(".nav-highlight").style.width = width;
    document.querySelector(".nav-highlight").style.left = left;

    document.querySelector(".home-btn").onclick = function() {
        // window.scrollTo(0, 0);
        document.querySelector(".pages").style.left = "0vw";
        document.querySelector(".pages").style.setProperty('--to', "0vw");
        document.querySelector(".pages").style.animation = "page-slide 1s ease-in-out";

        const left = document.querySelector(".home-btn").getBoundingClientRect().left+"px";
        const width = document.querySelector(".home-btn").offsetWidth+"px"

        document.querySelector(".nav-highlight").style.width = width;
        document.querySelector(".nav-highlight").style.setProperty('--cur-width', width);
        

        document.querySelector(".nav-highlight").style.left = left;
        document.querySelector(".nav-highlight").style.setProperty('--cur-left', left);

        document.querySelector(".nav-highlight").style.animation = "move-highlight 1s ease-in-out";

        setTimeout(function() {
            document.querySelector(".pages").style.setProperty('--from', "0vw");
            document.querySelector(".pages").style.animation = "";

            document.querySelector(".nav-highlight").style.setProperty('--prev-width', width);
            document.querySelector(".nav-highlight").style.setProperty('--prev-left', left);
            document.querySelector(".nav-highlight").style.animation = "";
        }, 1000);
    }

    document.querySelector(".qua-btn").onclick = function() {
        document.querySelector(".pages").style.left = "-100vw";
        document.querySelector(".pages").style.setProperty('--to', "-100vw");
        document.querySelector(".pages").style.animation = "page-slide 1s ease-in-out";

        const left = document.querySelector(".qua-btn").getBoundingClientRect().left+"px";
        const width = document.querySelector(".qua-btn").offsetWidth+"px"

        document.querySelector(".nav-highlight").style.width = width;
        document.querySelector(".nav-highlight").style.setProperty('--cur-width', width);
        

        document.querySelector(".nav-highlight").style.left = left;
        document.querySelector(".nav-highlight").style.setProperty('--cur-left', left);

        document.querySelector(".nav-highlight").style.animation = "move-highlight 1s ease-in-out";

        setTimeout(function() {
            document.querySelector(".pages").style.setProperty('--from', "-100vw");
            document.querySelector(".pages").style.animation = "";

            document.querySelector(".nav-highlight").style.setProperty('--prev-width', width);
            document.querySelector(".nav-highlight").style.setProperty('--prev-left', left);
            document.querySelector(".nav-highlight").style.animation = "";
        }, 1000);
    }

    document.querySelector(".pro-btn").onclick = function() {
        document.querySelector(".pages").style.left = "-200vw";
        document.querySelector(".pages").style.setProperty('--to', "-200vw");
        document.querySelector(".pages").style.animation = "page-slide 1s ease-in-out";

        const left = document.querySelector(".pro-btn").getBoundingClientRect().left+"px";
        const width = document.querySelector(".pro-btn").offsetWidth+"px"

        document.querySelector(".nav-highlight").style.width = width;
        document.querySelector(".nav-highlight").style.setProperty('--cur-width', width);
        

        document.querySelector(".nav-highlight").style.left = left;
        document.querySelector(".nav-highlight").style.setProperty('--cur-left', left);

        document.querySelector(".nav-highlight").style.animation = "move-highlight 1s ease-in-out";

        setTimeout(function() {
            document.querySelector(".pages").style.setProperty('--from', "-200vw");
            document.querySelector(".pages").style.animation = "";

            document.querySelector(".nav-highlight").style.setProperty('--prev-width', width);
            document.querySelector(".nav-highlight").style.setProperty('--prev-left', left);
            document.querySelector(".nav-highlight").style.animation = "";
        }, 1000);
    }

    document.querySelector(".contact-btn").onclick = function() {
        document.querySelector(".pages").style.left = "-300vw";
        document.querySelector(".pages").style.setProperty('--to', "-300vw");
        document.querySelector(".pages").style.animation = "page-slide 1s ease-in-out";

        const left = document.querySelector(".contact-btn").getBoundingClientRect().left+"px";
        const width = document.querySelector(".contact-btn").offsetWidth+"px"

        document.querySelector(".nav-highlight").style.width = width;
        document.querySelector(".nav-highlight").style.setProperty('--cur-width', width);
        

        document.querySelector(".nav-highlight").style.left = left;
        document.querySelector(".nav-highlight").style.setProperty('--cur-left', left);

        document.querySelector(".nav-highlight").style.animation = "move-highlight 1s ease-in-out";
        
        setTimeout(function() {
            document.querySelector(".pages").style.setProperty('--from', "-300vw");
            document.querySelector(".pages").style.animation = "";

            document.querySelector(".nav-highlight").style.setProperty('--prev-width', width);
            document.querySelector(".nav-highlight").style.setProperty('--prev-left', left);
            document.querySelector(".nav-highlight").style.animation = "";
        }, 1000);
    }


    var cards = document.getElementsByClassName("card");

    for (var i = 0, len = cards.length; i < len; i++) {
        const card = cards[i];
        card.addEventListener("mouseenter", () => {

            card.querySelector(".content").style.setProperty('--cur-margin', "-300px");
    
            card.querySelector(".content").style.animation = "card-hover 0.5s ease-out";
    
            card.querySelector(".content").style.margin = "-300px 0 0 0";
    
            setTimeout(function() {
                card.querySelector(".content").style.setProperty('--prev-margin', "-300px");
                card.querySelector(".content").style.animation = "";
            }, 500);
        })

        card.addEventListener("mouseleave", () => {

            card.querySelector(".content").style.setProperty('--cur-margin', "300px");
    
            card.querySelector(".content").style.margin = "300px 0 0 0";
    
            card.querySelector(".content").style.animation = "card-hover 0.5s ease-out";
    
            setTimeout(function() {
                card.querySelector(".content").style.setProperty('--prev-margin', "300px");
                card.querySelector(".content").style.animation = "";
            }, 500);
        })
    }

})