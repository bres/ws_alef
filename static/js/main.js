
//toggle mega menu
     $('.mega-menu').hide();
     $(window).ready(function() {
       $("nav.inline-menu ul li").click(function() {
         $(this).siblings().find(".mega-menu").hide();
         $(this).find(".mega-menu").toggle();
       });
       // hide grid mega menu after click anywhere on the page
       $("html").click(function(event) {
         if ($(event.target).closest('nav.inline-menu ul li').length == 0) {
           $('.mega-menu').hide();
         }
       });
     });

 //restore default image on grid mega menu after click event anywhere on the page
     $("html").click(function(event) {
       if ($(event.target).closest('nav.inline-menu ul li').length > 0) {
         $("#srcImage1").show();
         $("div.mydiv").hide();
       }
     });

 //change image on hover inside on grid mega menu
     $(document).ready(function() {
       $(".mymultiplediv").mouseover(function() {
         $("#srcImage1").hide();
         myvar = this.id;
         $("div.mydiv").hide();
         $("#div"+myvar).show();
       });
     });

 // grab everything we need
     const btn = document.querySelector(".mobile-menu-button");
     const menu = document.querySelector(".sidebar");
     var para = document.getElementById("scroll");

 // add event listeners
     //Toggle Nav //
     btn.addEventListener("click", () => {
       menu.classList.toggle("-translate-x-full");
       para.classList.toggle("noscrollClass");
     });

     $(window).resize(function() {
       var winWidth = $(window).width();
       if(winWidth >= 640) {
         menu.classList.add("-translate-x-full");
         para.classList.remove("noscrollClass");}
 });
