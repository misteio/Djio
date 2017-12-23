/*
 Project Name : Columba
 Author Company : Theme Foundry
 Project Date: 09-07-2017
 Author Website : http://digitsol.co/
 */
/* Table of Content
==================================================
 1. Loader
 2. Screen height
 3. Screen Height
 4. Login And Registration Forms
 5. Progress Bar
 6. Single Product Zoom
 7. Increment Decrement
 8. TEAM Slider
 9. Service slider
 10.Client slider
 11.On load Scroll Top
 12.Add And Remove active
 13.Parallax
 14.Contact Form
 15.Date picker
 16.Aside slider
 17.Count function
 18.Animation
 19.Mobile sub menu

 */

jQuery(document).ready(function($) {

    "use strict";

    var win = $(window);
    //$("#loading").delay(2000).fadeOut(500);
    win.on('load', function() {
        $("#pre_loader").addClass('down');
        animate_elems();
    });
    //============================================
    //Screen height
    //=============================================
    $(".screen-height").css({
        'height': window.innerHeight
    });

    win.resize(function() {
        $(".screen-height").css({
            'height': window.innerHeight
        });
    });
    //============================================
    //Login And Registration Forms
    //=============================================
    $('#top-bar #forms').on('click', function() {
        if ($('#top-bar .forms').hasClass('active')) {
            $('#top-bar .forms').removeClass('active');
        } else {
            $('#top-bar .login-form').addClass('active');
        }
    });

    $('#top-bar .register').on('click', function() {
        $('#top-bar .login-form').removeClass('active');
        $('#top-bar .register-form').addClass('active');
    });
    $('#top-bar .login').on('click', function() {
        $('#top-bar .register-form ').removeClass('active');
        $('#top-bar .login-form').addClass('active');
    });

    //======================================================
    // progress Bar
    //=====================================================
    $('.skill').each(function() {
        $(this).appear(function() {
            $(this).find('.skill-box').animate({
                width: jQuery(this).attr('data-percent')
            }, 1000);
        });
    });
    //================================================
    //Single Product Zoom
    //=================================================
    $('.zoom').elevateZoom({
        zoomType: "inner",
        cursor: "crosshair",
        zoomWindowFadeIn: 500,
        zoomWindowFadeOut: 750
    });

    //================================================
    //Increment Decrement
    //=================================================
    $("input[name='demo_vertical']").TouchSpin({
        verticalbuttons: true
    });
    //===================================================
    // TEAM Slider
    //===================================================
    var owl = $(".team-slider");

    owl.owlCarousel({

        itemsCustom: [
            [0, 1],
            [450, 1],
            [600, 2],
            [700, 2],
            [1000, 3],
            [1200, 3],
            [1400, 3],
            [1600, 3]
        ],
        navigation: true,
        pagination: false,
        autoPlay: true,
        navigationText: ['<i class="fa fa-angle-left" aria-hidden="true"></i>', '<i class="fa fa-angle-right" aria-hidden="true"></i>']
    });
    //============================================
    //Service slider
    //=============================================
    var owl = $(".service-slider");

    owl.owlCarousel({

        itemsCustom: [
            [0, 1],
            [450, 1],
            [600, 2],
            [700, 2],
            [1000, 3],
            [1200, 4],
            [1400, 4],
            [1600, 4]
        ],
        navigation: false,
        pagination: false,
        autoPlay: true,
        navigationText: ['<i class="fa fa-angle-left" aria-hidden="true"></i>', '<i class="fa fa-angle-right" aria-hidden="true"></i>']
    });
    //============================================
    //Client slider
    //=============================================
    var owl = $(".logo-slider");

    owl.owlCarousel({

        itemsCustom: [
            [0, 1],
            [450, 1],
            [600, 2],
            [700, 3],
            [1000, 4],
            [1200, 6],
            [1400, 6],
            [1600, 6]
        ],
        navigation: false,
        pagination: false,
        autoPlay: true,
        navigationText: ['<i class="fa fa-angle-left" aria-hidden="true"></i>', '<i class="fa fa-angle-right" aria-hidden="true"></i>']
    });
    //===============================================
    //On load Scroll Top
    //===============================================
    $('html, body').scrollTop(0);

    win.on('load', function() {
        setTimeout(function() {
            $('html, body').scrollTop(0);
        }, 0);
    });
    //========================================
    // Add And Remove active
    //======================================

    $('.accordion .panel').on('click', function(e) {
        e.preventDefault();
        var $this = $(this);
        $('.accordion .panel').removeClass('active');
        $this.addClass('active');

    });
    /*--------------------------------------------------
     Parallax
     ---------------------------------------------------*/
    $(window).stellar({
        responsive: true,
        horizontalScrolling: false,
        hideDistantElements: false,
        horizontalOffset: 0,
        verticalOffset: 0
    });
    /* ---------------------------------------------------------------------- */
    /*  Contact Form
     /* ---------------------------------------------------------------------- */

    var submitContact = $('#submit_contact'),
        message = $('#msg');

    submitContact.on('click', function(e) {
        e.preventDefault();

        var $this = $(this);

        $.ajax({
            type: "POST",
            url: 'send',
            dataType: 'json',
            cache: false,
            data: $('#contact-form').serialize(),
            success: function(data) {
                alert('Votre message a bien été envoyé')
                if (data.success !== 'error') {
                    $this.parents('form').find('input[type=text],textarea,select').filter(':visible').val('');
                    $this.hide().removeClass('success').removeClass('error').addClass('success').html(data.msg).fadeIn('slow').delay(5000).fadeOut('slow');
                } else {
                    $this.hide().removeClass('success').removeClass('error').addClass('error').html(data.msg).fadeIn('slow').delay(5000).fadeOut('slow');
                }
            },
            error: function (request, error) {
                console.log(arguments);
                alert("Vous devez remplir tous les champs");
            },
        });
    });
    //================================================
    //Date picker
    //===============================================

    var firstDayOfMonth = function() {
        return 5;
    };
    var d = new Date();
    var currMonth = d.getMonth();
    var currYear = d.getFullYear();
    var startDate = new Date(currYear, currMonth, firstDayOfMonth());
    $('form .date').datepicker('setDate', startDate);
    //============================================
    // aside slider
    //============================================


    $(".testi-slider,.feature-post-slider").owlCarousel({

        navigation: false, // Show next and prev buttons
        slideSpeed: 300,
        paginationSpeed: 400,
        singleItem: true,
        pagination: true,
        autoPlay: true,
        navigationText: ['<i class="fa fa-angle-left"></i>', '<i class="fa fa-angle-right"></i>']

    });
    //========================================
    // count function
    //======================================

    $('.counter-block').each(function() {
        $(this).appear(function() {
            var focus = $(this),
                i = focus.find(".odometer");
            window.setTimeout(function() {
                i.html(focus.attr("data-count"))
            }, 500)
        });
    });
    //===============================================
    //animation
    //==============================================
    // Show element on scroll

    var $elems = $('.animate-in');
    var winheight = win.height();
    var fullheight = $(document).height();

    win.scroll(function() {
        animate_elems();
    });

    function animate_elems() {
        var wintop = win.scrollTop(); // calculate distance from top of window
        // loop through each item to check when it animates
        $elems.each(function() {
            var $elm = $(this);

            var topcoords = $elm.offset().top; // element's distance from top of page in pixels

            if (wintop > (topcoords - (winheight * .99999))) {
                // animate when top of the window is 3/4 above the element
                $elm.addClass('animated');

            }else {
                $elm.removeClass('animated');
            }

        });
    } // end animate_elems()
    //============================================
    // Mobile sub menu
    //============================================
    if (win.width() <= 767) {
        $("#slide-nav #menu_nav ul > li.dropdown").append('<div class="more"></div>');

        $("#slide-nav #menu_nav").on("click", ".more", function(e) {
            e.stopPropagation();

            $(this).parent().toggleClass("current")
                .children("#slide-nav #menu_nav ul > li.dropdown > ul").toggleClass("open");

        });

    }

    win.resize(function() {
        if (window.innerWidth > 767) {
            if ($('#slide-nav #menu_nav ul > li.dropdown .more').length !== 0) {
                $('#slide-nav #menu_nav ul > li.dropdown div').remove('.more');
            }
        } else {
            $("#slide-nav #menu_nav ul > li.dropdown").append('<div class="more"></div>');
        }
    });

    var $body = $('body'),
        $wrapper = $('.body-innerwrapper'),
        $toggler = $('.navbar-toggle'),
        $close = $('.closs'),
        $offCanvas = $('.navbar-collapse');

    $toggler.on('click', function(event) {
        event.preventDefault();
        stopBubble(event);
        setTimeout(offCanvasShow, 50);
    });

    $close.on('click', function(event) {
        event.preventDefault();
        offCanvasClose();
    });

    var offCanvasShow = function() {
        $body.addClass('offcanvas');
        $wrapper.on('click', offCanvasClose);
        $close.on('click', offCanvasClose);
        $offCanvas.on('click', stopBubble);

    };

    var offCanvasClose = function() {
        $body.removeClass('offcanvas');
        $wrapper.off('click', offCanvasClose);
        $close.off('click', offCanvasClose);
        $offCanvas.off('click', stopBubble);
    };

    var stopBubble = function(e) {
        e.stopPropagation();
        return true;
    };



});
