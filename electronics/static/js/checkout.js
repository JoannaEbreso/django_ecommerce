
  $(document).ready(function(){

    const product_price= document.querySelectorAll(".cart-row");
    let total = 0;
    product_price.forEach(function(el){
       const product_price_value = el.querySelector(".product_price_checkout").innerText.trim();
       console.log(product_price_value)
       const quantity_checkout = el.querySelector(".quantity_checkout").innerText.trim();
              console.log(quantity_checkout)

       const product_cal_quantity = Number.parseInt(product_price_value) * Number.parseInt(quantity_checkout);
                     console.log(product_cal_quantity)

       total = total + product_cal_quantity;
    });
    const total_price = document.querySelector(".total_price");
    console.log(total)
    total_price.innerText = " "+total;

});
