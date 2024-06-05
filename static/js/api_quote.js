

document.getElementById('quote-form').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent the default form submission
});


function getImage(){
    background = document.getElementById("background");
    if(background.checked){
        background = "1"
    }
    else{
        background = "0"
    }

    tags = document.getElementById("tags").value;
    font = document.getElementById("font").value;

    payload = {
        background: background,
        tags: tags,
        font: font
    };

    $.ajax({
        url: '/get_api_quote',
        type: 'POST',
        xhrFields: {
            responseType: 'blob'
        },
        contentType: 'application/json',
        data: JSON.stringify(payload),
        success: function(blob){
            url = URL.createObjectURL(blob);
            document.getElementById("images-wrapper").innerHTML += `<img src='${url}' class='image'>`;
        }
    });
}