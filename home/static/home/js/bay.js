
// We will remove any amount selected (radio button) so the custom (input text) will be the active one
function customAmount() {
    const customAmountField = document.querySelector(".donations__form .donations__amount #custom"); // gets the input text
  
    // if there is no input text accepting the custom value, then the code following the below code won't be executed
    if (!customAmountField) return;
  
    customAmountField.addEventListener("focus", function () {
  
      // Getting all amount (radio buttons)
      const currentAmount = document.querySelectorAll(".donations__form .donations__amount input[type='radio']");
  
      for (var i = 0; i < currentAmount.length; i++) {
        if (currentAmount[i].checked) {
          // Remove the current checked
          currentAmount[i].checked = false;
        }
      }
  
    })
  }
  customAmount();
  console.log('hello world')
  // Showing the credit card form
  function showCardForm() {
    // Button for the credit card
    const creditCardSelector = document.querySelectorAll(".donations__form .donations__payment input[type='radio']");
    // Form for the credit card
    const creditCardForm = document.querySelector(".donations__form .credit-card-payment-form");
    // PayPal link
    const paypalLink = document.querySelector(".donations__form .paypal-link");
    // Credit card image (jQuery card plugin)
    const creditCardImage = document.querySelector(".donations .card-wrapper");
  
    for (var i = 0; i < creditCardSelector.length; i++) {
  
      creditCardSelector[i].addEventListener("click", function () {
        var values = this.id; // credit-card or paypal
  
        if (values === "credit-card") {
          creditCardForm.classList.add("active"); // shows donation form
          creditCardImage.classList.add("active"); // shows a credit card image generate by the JQuery card plugin (does not show on smaller devices such as phone and tablet in portrait mode)
  
          paypalLink.classList.remove("active"); // hides the PayPal option
  
        } else {
          creditCardForm.classList.remove("active"); // hides donation form
          creditCardImage.classList.remove("active"); // hides the credit card image generate by the JQuery card plugin
  
          paypalLink.classList.add("active"); // shows the PayPal option
        }
      })
    }
  
  }
  showCardForm();
  
  // Credit card - Donation page
  // Using JQuery Card plugin
  
  var donations = new Card({
    // a selector or DOM element for the form where users will
    // be entering their information
    form: '.donations__form', // *required*
    // a selector or DOM element for the container
    // where you want the card to appear
    container: '.card-wrapper', // *required*
  
    formSelectors: {
      numberInput: 'input#card-number-payment', // optional — default input[name="number"]
      expiryInput: 'input#card-expiration-payment', // optional — default input[name="expiry"]
      cvcInput: 'input#card-ccv-payment', // optional — default input[name="cvc"]
      nameInput: 'input#name-on-card' // optional - defaults input[name="name"]
    },
  
    width: 200, // optional — default 350px
    formatting: true, // optional - default true
  
    // Strings for translation - optional
    messages: {
      validDate: 'valid\ndate', // optional - default 'valid\nthru'
      monthYear: 'mm/yyyy', // optional - default 'month/year'
    },
  
    // Default placeholders for rendered fields - optional
    placeholders: {
      number: '•••• •••• •••• ••••',
      name: 'Full Name',
      expiry: '••/••',
      cvc: '•••'
    },
  
    masks: {
      cardNumber: '•' // optional - mask card number
    },
  });