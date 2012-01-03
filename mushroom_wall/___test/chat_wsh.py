from mod_pywebsocket import msgutil
connections = []

def web_socket_do_extra_handshake(request):
    # 모든 접속을 받아들임
    pass

def web_socket_transfer_data(request):
    # 모든 클라이언트의 접속을 저장해 둠
    connections.append(request)
    while True:
        try:
            # 클라이언트로부터 메시지를 수신할 때까지 기다림
            message = msgutil.receive_message(request)
        except Exception:
            # 접속이 끊어졌으므로 처리 종료
            return
        # 모든 클라이언트로 메시지를 보냄
        for con in connections:
            try:
                # 메시지를 보냄
                msgutil.send_message(con, message)
            except Exception:
                # 메시지를 보낼 수 없는 클라이언트는 제외
                connections.remove(con)
                
