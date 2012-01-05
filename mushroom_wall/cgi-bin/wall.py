# -*- coding: ms949 -*-


import wall_view
import wall_model

print(wall_view.response())
print(wall_view.include_header())
print(wall_view.topbar())
print(wall_view.start_container())
print(wall_view.start_sidebar())

# dropbox 인증했는지 검사해보고 안했으면
print(wall_view.dropbox_auth())


print(wall_view.latest_files())
print(wall_view.skype())
print(wall_view.end_sidebar())


print(wall_view.start_content())

print(wall_view.start_chat_table())
print(wall_view.message('박윤희', '안녕 ㅋㅋ', '03:40 AM'))
print(wall_view.message('박윤희', '헤헤', '03:40 AM'))
print(wall_view.message('박윤희', 'ㅎㅎㅎㅎ', '03:40 AM'))
print(wall_view.message('이하나', '사진.jpg', '03:40 AM', False, 'http://www.google.co.kr/images/nav_logo99.png'))
print(wall_view.message('이하나', 'ㅋㄷㅋㄷ', '03:40 AM'))
print(wall_view.end_chat_table())

# dropbox 인증했는지 검사해보고 안했으면
print(wall_view.dropbox_auth_warning())


print(wall_view.speak_form())
print(wall_view.end_content())



print(wall_view.end_container())

#javascript 추가
print('<script type="text/javascript" src="/lib/jquery-1.6.4.js"></script>')
print('<script type="text/javascript" src="/js/websocket.js"></script>')

print(wall_view.include_footer())