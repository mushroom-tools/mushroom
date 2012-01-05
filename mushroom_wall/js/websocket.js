
var server_addr = "ws://211.189.19.225/chat"
var ws = new WebSocket(server_addr);
						
						
ws.onmessage = function(event){	// 메시지 수신
	alert(event.data);
};


ws.onopen = function(event){	// 서버와 연결됨
	alert('connect');
	$('#speak_send').removeAttr('disabled');
};
		
				
ws.onclose = function(event){	// 서버와 통신 끊김
	alert('disconnect');
	$('#speak_send').attr('disabled', 'disabled');
};


function submitMessage(){
	var name = $('#speak_person').val();
	var message = $('#speak_body').val();
	
	// 서버로 메시지 보냄
	//ws.send({'name': name, 'content': message});
	ws.send(name + "###" + message);
}