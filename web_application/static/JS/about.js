console.log('hie')
document.addEventListener("DOMContentLoaded", function () {
    const aboutContent = document.getElementById("about-content");
    console.log(aboutContent)
    alert.message('hie')
    if (aboutContent) {
        alert.message('Done hie')
        $(aboutContent).toggleClass("d-block");

        
        setTimeout(function () {
            $(aboutContent).css("opacity", 1);
        }, 0);
    }
});
document.addEventListener("DOMContentLoaded", function () {
    const aboutContent2 = document.getElementById("about-content2");
    console.log(aboutContent2)
    if (aboutContent2) {
        
        $(aboutContent2).toggleClass("hidden");

        
        setTimeout(function () {
            $(aboutContent2).css("opacity", 1);
        }, 0);
    }
});
