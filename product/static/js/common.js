$(function () {
    // Пользовательские функции
    $('.input__icon--filter').click(function () {
        $(this).parents('.input--filter').toggleClass('input--filter-active');
    });


    $('.button-link__button--add-good').click(function (e) {
        e.preventDefault();
        $('.block--add-good').addClass('display-flex');
    });
    $('.table__td-edit').click(function (e) {
        e.preventDefault();
        $('.block--add-good').addClass('display-flex');
    });
    $('#add-good-close').click(function (e) {
        e.preventDefault();
        $('.block--add-good').removeClass('display-flex');
    });
    $('.button-link__button--add-group').click(function (e) {
        e.preventDefault();
        $('.block--add-group').addClass('display-flex');
    });
    $('#add-group-close').click(function (e) {
        e.preventDefault();
        $('.block--add-group').removeClass('display-flex');
    });
    $('.button-link__button--plus-cashbox').click(function (e) {
        e.preventDefault();
        $('.block--add-cashbox').addClass('display-flex');
    });
    $('#add-cashbox-close').click(function (e) {
        e.preventDefault();
        $('.block--add-cashbox').removeClass('display-flex');
    });
    $('.button-link__button--plus-suppliers').click(function (e) {
        e.preventDefault();
        $('.block--add-suppliers').addClass('display-flex');
    });
    $('#add-suppliers-close').click(function (e) {
        e.preventDefault();
        $('.block--add-suppliers').removeClass('display-flex');
    });
    $('.button-link__button--plus-customers').click(function (e) {
        e.preventDefault();
        $('.block--add-customers').addClass('display-flex');
    });
    $('#add-customers-close').click(function (e) {
        e.preventDefault();
        $('.block--add-customers').removeClass('display-flex');
    });
    $('.button-link__button--plus-cashier').click(function (e) {
        e.preventDefault();
        $('.block--add-cashier').addClass('display-flex');
    });

    $('.button-link__button--plus-employees').click(function (e) {
        e.preventDefault();
        $('.block--add-employees').addClass('display-flex');
    });

    $('.edit-dots__item--edit').click(function (e) {
        e.preventDefault();
        $('.block--add-shop').addClass('display-flex');
        $('.block--add-cashier').addClass('display-flex');
    });
    $('#add-cashier-close').click(function (e) {
        e.preventDefault();
        $('.block--add-cashier').removeClass('display-flex');
    });

    $('#add-employees-close').click(function (e) {
        e.preventDefault();
        $('.block--add-employees').removeClass('display-flex');
    });

    $('.button-link__button--plus-shop').click(function (e) {
        e.preventDefault();
        $('.block--add-shop').addClass('display-flex');
    });
    $('#add-shop-close').click(function (e) {
        e.preventDefault();
        $('.block--add-shop').removeClass('display-flex');
    });


    $('#open-change').click(function (e) {
        e.preventDefault();
        $('.open-change__content').addClass('display-flex');
    });
    $('#close-change').click(function (e) {
        e.preventDefault();
        $('.open-change__content').removeClass('display-flex');
    });
    $('#open-change-req').click(function (e) {
        e.preventDefault();
        $('.open-change').removeClass('display-flex');
    });


    $('#search-cus-input').click(function () {
        $('.sidebar--hidden').toggleClass('display-flex');
    });
    $('#search-cus-close').click(function (e) {
        e.preventDefault();
        $('.sidebar--hidden').toggleClass('display-flex');
    });


    $('#add-cus-open').click(function (e) {
        e.preventDefault();
        $('.main-cashier__add-cus').toggleClass('display-flex');
    });
    $('#add-cus-close').click(function (e) {
        e.preventDefault();
        $('.main-cashier__add-cus').toggleClass('display-flex');
    });

    $('#add-cus-open1').click(function (e) {
        e.preventDefault();
        $('.main-cashier__add-costs').toggleClass('display-flex');
    });
    $('#add-cus-close1').click(function (e) {
        e.preventDefault();
        $('.main-cashier__add-costs').toggleClass('display-flex');
    });


    $('#add-cus-open2').click(function (e) {
        e.preventDefault();
        $('.main-cashier__add-prepayment').toggleClass('display-flex');
    });
    $('#add-cus-close2').click(function (e) {
        e.preventDefault();
        $('.main-cashier__add-prepayment').toggleClass('display-flex');
    });


    $('.menu-bottom__burger-link').click(function (e) {
        e.preventDefault();
        $('.menu-bottom__list').toggleClass('display-block');
    });


    $('.popup__close').click(function (e) {
        e.preventDefault();
        $('.popup').removeClass('display-flex');
    });
    $('#close-change').click(function (e) {
        e.preventDefault();
        $('.popup__close-change').addClass('display-flex');
    });
    $('#sell').click(function (e) {
        e.preventDefault();
        $('.popup__sell').addClass('display-flex');
    });
    $('#make-return').click(function (e) {
        e.preventDefault();
        $('#return').addClass('display-block');
        $('#sell').addClass('display-none');
    });

    $('#cash-pay').click(function (e) {
        e.preventDefault();
        $(this).toggleClass('active');
        $('#card-pay').toggleClass('active');
        $('.change-block').toggleClass('display-none');
    });

    $('#sell-cash').click(function (e) {
        e.preventDefault();
        $('#success-cash-hint').addClass('display-block');
        $(this).addClass('display-none');
    });
    $('#sell-card').click(function (e) {
        e.preventDefault();
        $('.popup__content--card').addClass('display-flex');
    });
    $('#sell-card-success').click(function (e) {
        e.preventDefault();
        $('#success-card-hint').addClass('display-block');
        $('#sell-card').addClass('display-none');
        $('.popup__content--card').removeClass('display-flex');
    });
    $('#sell-card-unsuccess').click(function (e) {
        e.preventDefault();
        $('.popup__content--card').removeClass('display-flex');
    });


    $('.menu__link--drop').click(function (e) {
        e.preventDefault();
        $(this).siblings('.menu__drop').toggleClass('display-block');
    });
    $('.edit-dots__button').click(function () {
        $(this).siblings('.edit-dots__list').toggleClass('display-block');
    });


    $('.nav-burger').click(function (e) {
        e.preventDefault();
        $('.menu-wrapper').toggleClass('display-block');
    });


    $('.button-controls').click(function (e) {
        e.preventDefault();
        $('.set-list').toggleClass('display-flex');
    });

});
$(function () {
    (function quantityProducts() {
        var $quantityArrowMinus = $(".input-nstr--minus");
        var $quantityArrowPlus = $(".input-nstr--plus");

        $quantityArrowMinus.mousedown(quantityMinus);
        $quantityArrowPlus.mousedown(quantityPlus);

        function quantityMinus() {
            var $quantityNum = $(this).siblings('.input__input');
            if ($quantityNum.val() > 0) {
                $quantityNum.val(+$quantityNum.val() - 1);
            }
        }

        function quantityPlus() {
            var $quantityNum = $(this).siblings('.input__input');
            $quantityNum.val(+$quantityNum.val() + 1);
        }
    })();
});
$(function () {
    (function countProducts() {
        var $quantityArrowPlus = $(".card-good");

        $quantityArrowPlus.mousedown(quantityPlus);

        function quantityPlus() {
            var $quantityNum = $(this).children('.card-good__count');
            if ($quantityNum.val() >= 0) {
                $quantityNum.val(+$quantityNum.val() + 1);
                $quantityNum.addClass('active');
            }
        }
    })();
});
$(document).ready(function () {
    $(".tabs").lightTabs();
});
(function ($) {
    jQuery.fn.lightTabs = function (options) {

        var createTabs = function () {
            tabs = this;
            i = 0;

            showPage = function (i) {
                $(tabs).children(".change-block").hide();
                $(tabs).children(".change-block").eq(i).show();
                $(tabs).children("ul").children("li").removeClass("active");
                $(tabs).children("ul").children("li").eq(i).addClass("active");
            }

            showPage(0);

            $(tabs).children("ul").children("li").each(function (index, element) {
                $(element).attr("data-page", i);
                i++;
            });

            $(tabs).children("ul").children("li").click(function () {
                showPage(parseInt($(this).attr("data-page")));
            });
        };
        return this.each(createTabs);
    };
})(jQuery);
$('.my-select').niceSelect();
$('.mini-select').niceSelect();
$('.filter-select__select').niceSelect();
