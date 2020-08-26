  
$(function() {
    // When we're using HTTPS, use WSS too.
    var ws_scheme = window.location.protocol == "https:" ? "wss" : "ws";
    var chatsock = new ReconnectingWebSocket(ws_scheme + '://' + window.location.host + "/chat" + window.location.pathname);
    
    chatsock.onmessage = function(message) {
        var data = JSON.parse(message.data);
        $('#chat').append('<tr>' 
            + '<td>' + data.timestamp + '</td>' 
            + '<td>' + data.handle + '</td>'
            + '<td>' + data.message + ' </td>'
            + '<td>' + data.user + ' </td>'
            + '<td>' + data.amount + ' </td>'
            + '<td>' + data.price + ' </td>'
        + '</tr>');
    };

    $('#chatform').on('submit', function(event) {
        var message = {
            handle: $('#handle').val(),
            message: $('#message').val(),
            user: $('#user').val(),
            amount: $('#amount').val(),
            price: $('#price').val(),
        }
        chatsock.send(JSON.stringify(message));
        return false;
    });
});
