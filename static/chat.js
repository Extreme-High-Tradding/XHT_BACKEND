  
$(function() {
    // When we're using HTTPS, use WSS too.
    var ws_scheme = window.location.protocol == "https:" ? "wss" : "ws";
    var chatsock = new ReconnectingWebSocket(ws_scheme + '://' + window.location.host + "/chat" + window.location.pathname);
    
    chatsock.onmessage = function(message) {
        var data = JSON.parse(message.data);
        $('#chat').append('<tr>' 
            + '<td>' + data.user_id + '</td>' 
            + '<td>' + data.opening_price + '</td>'
            + '<td>' + data.amount_assets + ' </td>'
            + '<td>' + data.asset_id + ' </td>'
            + '<td>' + data.operation_status + ' </td>'
            + '<td>' + data.operation_type + ' </td>'
        + '</tr>');
    };

    $('#chatform').on('submit', function(event) {
        var message = {
            user_id: $('#user').val(),
            price: $('#price').val(),
            amount_assets: $('#amount').val(),
            asset_id: $('#asset').val(),
            operation_status: $('#operation_status').val(),
            operation_type: $('#operation_type').val(),
        }
        chatsock.send(JSON.stringify(message));
        return false;
    });
});
