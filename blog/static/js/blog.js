
function like(id) {
    $.ajax({
        url : "comments/" + id + "/like", // the endpoint
        type : "POST", // http method

        // handle a successful response
        success : function(json) {
            counter_id = '#likecounter_' + json.comment_pk
            $(counter_id).html(json.likes); // remove the value from the input
            console.log(json); // log the returned json to the console
        },

        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
};

function dislike(id) {
    $.ajax({
        url : "comments/" + id + "/dislike", // the endpoint
        type : "POST", // http method

        // handle a successful response
        success : function(json) {
            counter_id = '#dislikecounter_' + json.comment_pk
            $(counter_id).html(json.dislikes); // remove the value from the input
            console.log(json); // log the returned json to the console
        },

        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
};

$('.like').on('click', function(event){
    event.preventDefault();
    like(this.getAttribute("data-id"))
});

$('.dislike').on('click', function(event){
    event.preventDefault();
    dislike(this.getAttribute("data-id"))
});