$(document).ready(function() {

    $('#searchTxt').change(function() {
        let inputVal = search.value.toLowerCase();
        let noteCards = document.getElementsByClassName('noteCard');

        Array.from(noteCards).forEach(function(element) {
            let cardTxt = element.getElementsByTagName('p')[1].innerHTML.toLowerCase();

            if (cardTxt.includes(inputVal)) {
                element.style.display = "block";
            } else {
                element.style.display = "none";
            }
        })
    });
});