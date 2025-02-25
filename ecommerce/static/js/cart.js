// static/js/cart.js
// This file can be used to enhance cart functionality.
// For now, we’ll just log a message when the Place Order button is clicked.
document.addEventListener('DOMContentLoaded', function() {
    const orderButton = document.querySelector('button[onclick]');
    if (orderButton) {
        orderButton.addEventListener('click', function() {
            console.log('Order process initiated...');
        });
    }
});
