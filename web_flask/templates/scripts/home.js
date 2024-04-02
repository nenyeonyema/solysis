document.addEventListener("DOMContentLoaded", function() {
    const divs = document.querySelectorAll('.moving-div');
    let delay = 0;

    divs.forEach((div, index) => {
        setTimeout(() => {
            div.style.right = '0';  /* Move the div to the left */
        }, delay);

        delay += 500;  /* Increase delay for each div */
    });
});