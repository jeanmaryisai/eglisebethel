console.log("check")
// We will remove any amount selected (radio button) so the custom (input text) will be the active one
function customAmount() {
    const customAmountField = document.querySelector(".donations__form .donations__amount #custom"); // gets the input text
  
    // if there is no input text accepting the custom value, then the code following the below code won't be executed
    if (!customAmountField) return;
  
    customAmountField.addEventListener("focus", function () {
      console.log("check")
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

  function customname(){
    const customNameField = document.querySelector(".donations__form .donations__name #custom_name");
    if (!customAmountField) return;
    customNameField.addEventListener("focus", function () {
      console.log("check")
      // Getting all amount (radio buttons)
      const currentAmount = document.querySelectorAll(".donations__form .donations__name #annonyme");
  
      
        if (currentAmount.checked) {
          // Remove the current checked
          currentAmount.checked = false;
        }
      
  
    })
  } customname()

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