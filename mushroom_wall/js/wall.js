
function addMessage(msg_data)
{
	var json = eval("("+msg_data+")");
	var link = "#";
	
	
	var str = '<tr class="text_message message">' + 
		    		'<td class="message_person">' +
		    			'<span class="author">' + json.name + '</span>' +
		    		'</td>' + 
		    		'<td class="message_body">' + 
		    			'<div class="message_body_content">';
		    			
	//if( json.is_text ){
		str += json.content;
	//}else{
		//str += '<a href="' + link + '" target="_blank">' + json.content + '</a>';
	//}
		    	str += '</div>' +
		    			'<span class="message_body_time">&nbsp;&nbsp;' + json.datetime + '</span>' +
		    		'</td>' +
		      '</tr>';	
	
	$('#chat_table').append(str);
	window.scrollBy(0, document.body.scrollHeight);
}


