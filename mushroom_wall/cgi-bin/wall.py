#! /usr/local/bin/python3
# -*- coding: ms949 -*-


import wall_view
import wall_model

print(wall_view.response())
print(wall_view.include_header())
print(wall_view.topbar())
print(wall_view.start_container())
print(wall_view.start_sidebar())

# dropbox �����ߴ��� �˻��غ��� ��������
#print(wall_view.dropbox_auth())


#print(wall_view.latest_files())
print(wall_view.skype())
print(wall_view.end_sidebar())


print(wall_view.start_content())

print(wall_view.start_chat_table())

list = wall_model.get_transcript_all()

for msg in list:
    print(wall_view.message(msg[0], msg[1], msg[2]))

#print(wall_view.message('������', '�ȳ� ����', '03:40 AM'))
#print(wall_view.message('������', '����', '03:40 AM'))
#print(wall_view.message('������', '��������', '03:40 AM'))
#print(wall_view.message('���ϳ�', '����.jpg', '03:40 AM', False, 'http://www.google.co.kr/images/nav_logo99.png'))
#print(wall_view.message('���ϳ�', '��������', '03:40 AM'))
print(wall_view.end_chat_table())

# dropbox �����ߴ��� �˻��غ��� ��������
#print(wall_view.dropbox_auth_warning())


print(wall_view.speak_form())
print(wall_view.end_content())



print(wall_view.end_container())

#javascript �߰�
print('<script type="text/javascript">window.scrollBy(0, document.body.scrollHeight);</script>')
print('<script type="text/javascript" src="/lib/jquery-1.6.4.js"></script>')
print('<script type="text/javascript" src="/lib/bootstrap-alerts.js"></script>')
print('<script type="text/javascript" src="/js/wall.js"></script>')
print('<script type="text/javascript" src="/js/websocket.js"></script>')

print(wall_view.include_footer())
