from mod_pywebsocket import msgutil
connections = []

def web_socket_do_extra_handshake(request):
    # ��� ������ �޾Ƶ���
    pass

def web_socket_transfer_data(request):
    # ��� Ŭ���̾�Ʈ�� ������ ������ ��
    connections.append(request)
    while True:
        try:
            # Ŭ���̾�Ʈ�κ��� �޽����� ������ ������ ��ٸ�
            message = msgutil.receive_message(request)
        except Exception:
            # ������ ���������Ƿ� ó�� ����
            return
        # ��� Ŭ���̾�Ʈ�� �޽����� ����
        for con in connections:
            try:
                # �޽����� ����
                msgutil.send_message(con, message)
            except Exception:
                # �޽����� ���� �� ���� Ŭ���̾�Ʈ�� ����
                connections.remove(con)
                
