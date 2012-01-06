
var server_addr = "ws://211.189.19.225/chat"
var ws = new WebSocket(server_addr);
						
						
ws.onmessage = function(event){	// 메시지 수신
	//alert(event.data);
	addMessage(event.data);
};


ws.onopen = function(event){	// 서버와 연결됨
	//alert('connect');
	$('#speak_send').removeAttr('disabled');
};
		
				
ws.onclose = function(event){	// 서버와 통신 끊김
	//alert('disconnect');
	$('#speak_send').attr('disabled', 'disabled');
};


function submitMessage(is_text){
	is_text = (typeof(is_text) != 'undefined') ? is_text : 1;
	var name = $('#speak_person').val();
	var message = $('#speak_body').val();
		
	var d = new Date();

	var s =
	    leadingZeros(d.getFullYear(), 4) + '-' +
	    leadingZeros(d.getMonth() + 1, 2) + '-' +
	    leadingZeros(d.getDate(), 2) + ' ' +
	
	    leadingZeros(d.getHours(), 2) + ':' +
	    leadingZeros(d.getMinutes(), 2) + ':' +
	    leadingZeros(d.getSeconds(), 2);
	
		
	// 채팅 서버로 메시지 보냄
	str = "{'name': '" + name + "', 'content': '" + message + "', 'datetime': '" + s + "', 'is_text': " + is_text +"}";
	ws.send(str);
	
		
	// db에 저장
	$.ajax({
	  url: 'put_msg_to_db.py',
	  data: {'name': name, 'content': message},
	  success: function(){}
	});
			
	$('#speak_body').val('');
}

function leadingZeros(n, digits) {
  var zero = '';
  n = n.toString();

  if (n.length < digits) {
    for (i = 0; i < digits - n.length; i++)
      zero += '0';
  }
  return zero + n;
}