
  $(document).ready(function(){

// Total price of Products in Cart
    const totalPriceOfProductFunction = function(){

        const totalPriceOfProduct = document.querySelectorAll(".total_product_price");

        let total_Cart_price = 0;
        let total_product__price = 0;
        totalPriceOfProduct.forEach(function(el){
        total_product__price = total_product__price + Number.parseInt(el.querySelector("p").innerText.replace(/^\$/, "").trim());
        })
        console.log(total_product__price)
        total_Cart_price =  total_product__price
        document.querySelector(".total_cart_price h5 strong").innerText = "$ "+total_Cart_price;

    }

//   Calculate the item price based on the total number of quantity and price of product
    const calculatePriceQuantity = function(context,value){
        $(context).parent(".quantity").parent(".div_plus_one")[0].querySelector(".plus_one").innerText = value;
        product_price = $(context).parent(".quantity")
        .parent(".div_plus_one").parent(".cart-row")[0].querySelector(".product_price p").innerText
        const inputWithOutDollar = product_price.replace(/^\$/, "").trim();
        console.log(inputWithOutDollar)
        total = value*inputWithOutDollar;
        $(context).parent(".quantity")
        .parent(".div_plus_one").parent(".cart-row")[0]
        .querySelector(".total_product_price p").innerText = total
    }

    const updateCartQuantity = function(context,value){
        let cart_id = $(context).attr("data-cart-id")
        console.log("hello world")
        $.ajax(
        {
        type:"GET",
        url: "/update_quantity",
        data:{
             cart_id: cart_id,
             product_quantity:value

        },
        success: function( data )
        {
        console.log(data)
//            $( '#message-cart-init' ).text(data);
////            $( '#message-cart' ).text(data);
        }
     }
     )
    }
// increase quantity
    $(".add_quantity").click(function(){
        let price;
    //   Get the price
        plus_one = $(this).parent(".quantity").parent(".div_plus_one")[0].innerText//.text();
        plus_one = plus_one.trim();
        plus_one = Number.parseInt(plus_one)+1;
        console.log(plus_one)
        calculatePriceQuantity(this,plus_one)
        totalPriceOfProductFunction();
//        updateCartQuantity(this,plus_one);
        let cart_id = $(this).attr("data-cart-id")
        $.ajax(
                {
                type:"GET",
                url: "/update_quantity",
                data:{
                     cart_id: cart_id,
                     product_quantity:plus_one

                },
                success: function( data )
                {
                    console.log(data)
        //            $( '#message-cart-init' ).text(data);
        ////            $( '#message-cart' ).text(data);
                }
             }
             )
    })

// decrease quantity
    $(".sub_quantity").click(function(){
        let minus_one;
    //   Get the price
        minus_one = $(this).parent(".quantity").parent(".div_plus_one")[0].innerText//.text();
        minus_one = minus_one.trim();
        minus_one = Number.parseInt(minus_one)-1;
        if(minus_one < 1){
        minus_one = 1
        }
        calculatePriceQuantity(this, minus_one)
        totalPriceOfProductFunction();
         let cart_id = $(this).attr("data-cart-id")
        $.ajax(
                {
                type:"GET",
                url: "/update_quantity",
                data:{
                     cart_id: cart_id,
                     product_quantity:minus_one

                },
                success: function( data )
                {
                    console.log(data)
        //            $( '#message-cart-init' ).text(data);
        ////            $( '#message-cart' ).text(data);
                }
             }
             )    })



    $.ajax(
    {
        type:"GET",
        url: "/all_cart",
        success: function( data )
        {
        console.log(data)
            $( '#message-cart-init' ).text(data);
//            $( '#message-cart' ).text(data);
        }
     }
     )
    $('.product_id').click(function(){
    let product_no;
    product_no = $(this).attr("data-product-id");
    $.ajax(
    {
        type:"GET",
        url: "/add_product_to_cart",
        data:{
                 product_id: product_no
        },
        success: function( data )
        {
        console.log(data)
            $( '#message-cart-init' ).text(data);
//            $( '#message-cart' ).text(data);
        }
     }
     )
   });
//
//    $('.checkout').click(function(){
//        let product_quantity;
//        product_quantity = $(this).(".quantity").innerText;
//        $.ajax({
//            type:"GET",
//            url: "/checkout",
//            data:{
//                quantity: product_quantity
//            },
//            success: function( data )
//            {
//                $( '#quantity').text(data);
//            }
//        })
//
//    });

});
