var updateBtns = document.getElementsByClassName('update-cart')

for (i = 0; i < updateBtns.length; i++) {
  updateBtns[i].addEventListener('click', function(){
    var productId = this.dataset.product
    var action = this.dataset.action
    console.log('productId:', productId, 'Action:', action)
    console.log('USER:', user)

    if (user == 'AnonymousUser'){
      addCookieItem(productId, action)
    }
    else{
      updateUserOrder(productId, action)
    }
  })
}


function updateUserOrder(productId, action){
  console.log('User is authenticated, sending data...')

    docheckout().then((response) => {

          var url = '/update_item/'

    fetch(url
      , {
      method:'POST',
      headers:({
        'Content-Type':'application/json',
        'X-CSRFToken':csrftoken,
        'authorization': +accessToken,
      }), 
      body: JSON.stringify({"productId": productId, "action": action}),
      dataType: "json"
    }
    )
    .then((response) => {
       return response.json();
    })
    .then((data) => {
        location.reload()
    });


    });


}


var updateBtns = document.getElementsByClassName('shipping-info')

for (i = 0; i < updateBtns.length; i++) {
  updateBtns[i].addEventListener('click', function(){
    var productId = this.dataset.product
    var action = this.dataset.action
    console.log('customer:', customer, 'Action:', action)
    console.log('USER:', user)

    if (user == 'AnonymousUser'){
      addCookieItem(customer, action)
    }
    else{
      updateUserOrder(customer, action)
    }
  })
}



function updateShippingOrder(customer, action){
  console.log('User is authenticated, sending data...')

    var url = '/process_order/'

    fetch(url
      , {
      method:'POST',
      headers:({
        'Content-Type':'application/json',
        'X-CSRFToken':csrftoken,
      }), 
      body: JSON.stringify({"customer": customer, "action": action}),
      dataType: "json"
    }
    )
    .then((response) => {
       return response.json();
    })
    .then((data) => {
        location.reload()
    });
}

