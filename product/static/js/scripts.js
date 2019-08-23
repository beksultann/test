$(document).ready(function () {
    /*var form = $('#form_buying_product');
    form.on('submit', function (e) {
        e.preventDefault();
        console.log('working');
        console.log(form);
        var number = $('#number').val();
        var submit_btn = $('#submit_btn');
        var product_id = submit_btn.data("product_id");
        var product_name = submit_btn.data("name");
        var product_price = submit_btn.data("price");

        var sum = number * product_price;

        $('.table-sidebar-wrapper table').append('<tr>' +
            '<td>' + product_name + '</td>' +
            '<td>' + product_price + '</td>' +
            '<td>' + number + '</td>' +
            '<td>' + 'скидка' + '</td>' +
            '<td>' + sum + '</td>' +
            '<td class="table-sidebar__delete-tr"></td>' +
            '</tr>'
        )
        ;
    });*/

        $('.block__col').each(function(){
            var number = $(this).find('.card-good__count').val();
            var product_name = $(this).find('.add-to-cart').data("name");
                var product_price = $(this).find('.add-to-cart').data("price");
                var sum = number * product_price;
            $(this).find('.add-to-cart').click(function(){
                $('.table-sidebar-wrapper table').append('<tr>' +
            '<td>' + product_name + '</td>' +
            '<td>' + product_price + '</td>' +
            '<td>' + number + '</td>' +
            '<td>' + 'скидка' + '</td>' +
            '<td>' + sum + '</td>' +
            '<td class="table-sidebar__delete-tr"></td>' +
            '</tr>'
        )
            });
        });

    $(document).on('click', 'table-sidebar__delete-tr', function (e) {
        e.preventDefault();
        $(this).closest('tr').remove();
    })
});
