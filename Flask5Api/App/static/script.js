var ENTER_KEY = 13;
function new_message(e) {
    var $textarea =$('#message-textarea');
    var message_body=$textarea.val().trim();  //获取消息正文
    if(e.which == ENTER_KEY
        // && ! e.shiftKey &&message_body
    ){
        e.preventDefault(); //阻止默认行为 即换行
        socket.emit('new message',message_body); //发送事件，传入消息正文
        $textarea.val('')//清空输入行
    }
}