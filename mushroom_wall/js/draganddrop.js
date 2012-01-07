
function onDrop(event){

	var files = event.dataTransfer.files;
	var temp = "";

	for (var i=0; i < files.length; i++) {
		var file = files[i];
		temp += file.name + " ";
	};

	//document.getElementById('file_msg').innerHTML = temp;
	//alert(temp);
	$('#speak_body').val(temp);
	
	submitMessage(0);

	// 드롭이 처리된 후 이벤트 버블링을 막음
	event.stopPropagation();
}

function onDragOver(event){
	// 드롭을 받아들이도록 기본 상태를 취소함
	event.preventDefault();
}

function onDragEnter(event){				
	if(event.dataTransfer.files.length > 0){
		event.preventDefault();
	}
}