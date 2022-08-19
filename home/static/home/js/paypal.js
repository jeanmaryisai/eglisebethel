const customAmountField = document.querySelector(".donations__form .donations__amount #custom");
const currentAmount = document.querySelectorAll(".donations__form .donations__amount input[type='radio']");
const currentType = document.querySelectorAll(".donations__form .donations__type input[type='radio']");

let amout=0.00;
let bool=true
let ame='anonymous'
let type=false
setInterval(()=>{
    const lame=document.getElementById('custom_name')
    if(lame != ''){
    ame=lame.value}
    const url= document.getElementById("url");
    amout=0.00;
for (var i = 0; i < currentAmount.length; i++) {
    if (currentAmount[i].checked) {
      amout=currentAmount[i].value;
    }
  }
  for (var i = 0; i < currentType.length; i++) {
    if (currentType[i].checked) {
      type=currentType[i].value;
    }
  }
  if(amout==0.00){
    if(customAmountField.value != ''){
    amout=customAmountField.value
    }
  }

  //
  //submitform(url.value)
},1000)

function getToken(name){
    var cookiePair=null;
    if(document.cookie && document.cookie !== ''){
        var cookieArr=document.cookie.split(";");
        for(var i=0; i,cookieArr.length;i++){
            cookiePair=cookieArr[i].trim();
            if(cookiePair.substring(0,name.length+1) === (name+'=')){
                return decodeURIComponent(cookiePair.substring(name.length+1));
            }
        }
    }
    return cookiePair;
}

var csrftoken= getToken('csrftoken');

function submitform(url){
    fetch(url,{
        method:'POST',
        headers:{
            'CONTENT-Type':'application/json',
            'X-CSRFToken':csrftoken
        },
        body:JSON.stringify({'amout':amout,'name':ame,'ismember':type})
    })
    .then((response)=>{
        return response.json()
    })

}

paypal.Buttons({
    
    // Set up the transaction
    createOrder: function(data, actions) {
        return actions.order.create({
            purchase_units: [{
                amount: {
                    value: parseFloat(amout)
                }
            }]
        });
    },

    // Finalize the transaction
    onApprove: function(data, actions) {
        return actions.order.capture().then(function(orderData) {
            // Successful capture! For demo purposes:
            //console.log('Capture result', orderData, JSON.stringify(orderData, null, 2));
            var transaction = orderData.purchase_units[0].payments.captures[0];
            //alert('Transaction '+ transaction.status + ': ' + transaction.id + '\n\nSee console for all available details');
            submitform(url.value);
            
            // Replace the above to show a success message within this page, e.g.
            const ele= document.getElementById('ele')
             const element = document.getElementById('paypal-button-container');
             element.innerHTML = '';
             ele.innerHTML = '<h3>Merci pour votre don. <br><br> Que le Seigneur vous benisse abonadament!</h3>';

            actions.redirect('/home/baylibre');
            location.reload;
          
        });
    }


}).render('#paypal-button-container');