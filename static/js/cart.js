$(document).ready(function() {
    const order_total = $('#order-total');

    $('.order-qty').each(function(){
        console.log(this)
        if ($(this).text() == 1){
           $(this).closest('td').find('#remove-one-item').removeClass('remove-one-item').css('opacity', '0.5') 
        }
    })

    $('td').on('click', '.remove-one-item', function(e) {
        order_qty = $(this).closest('td').find('.order-qty');
        order_id = $(this).closest('td').find('.order-id').val();
        $.ajax({
            url:'/cart/remove_one/' + order_id,
            success: function(data){
                order_qty.text(data['qty']);
                order_total.text(data['total']);
                if (data['qty'] == 1) {
                    order_qty.closest('td').find('#remove-one-item').removeClass('remove-one-item').css('opacity', '0.5')
                }
            }
        })
    })

    $('td').on('click', '.add-one-item', function(e) {
        order_qty = $(this).closest('td').find('.order-qty');
        order_id = $(this).closest('td').find('.order-id').val();
        $.ajax({
            url:'/cart/add_one/' + order_id,
            success: function(data){
                order_qty.text(data['qty']);
                order_total.text(data['total']);
                if (data['qty'] > 1) {
                    order_qty.closest('td').find('#remove-one-item').addClass('remove-one-item').css('opacity', '1')
                }
            }
        })
    })
})