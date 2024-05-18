window.onload = function() {
    var form = document.querySelector('form');
    form.style.opacity = 0;
    setTimeout(function() {
        form.style.opacity = 1;
    }, 500);
};

document.getElementById('submit-btn').addEventListener('click', function(e) {
    var message = document.getElementById('message').value;
    if (!message) {
        e.preventDefault();
        alert('Please enter a message.');
    } else {
        // Animate the submit button
        this.classList.add('btn-clicked');
        setTimeout(() => this.classList.remove('btn-clicked'), 400);
    }
});
document.getElementById('clear-btn').addEventListener('click', function() {
    // Clear the message input and prediction result
    document.getElementById('message').value = '';
    document.getElementById('prediction').textContent = '';
    
    // Animate the container from left to right
    var container = document.querySelector('.container');
    container.style.transform = 'translateX(-100%)';
    setTimeout(function() {
        container.style.transform = 'none';
    }, 500);
});
