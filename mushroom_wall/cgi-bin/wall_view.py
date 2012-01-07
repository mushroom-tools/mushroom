# -*- coding: utf-8 -*-


def response():
    string = 'Content-type: text/html\n\n'
    return(string)




def include_header():
    # <meta charset="UTF-8"> 지우니까 한글이 안 깨져서 일단 지움 ^.^;
    string = '''<!DOCTYPE html>
                    <html>
                        <head>
                        
                            <title>Mushroom</title>
                            
                            <!-- style -->
                            <link rel="stylesheet" href="/css/bootstrap.css">
                            <link rel="stylesheet" href="/css/style.css">
                            <link rel="stylesheet" href="/css/wall.css">
                        </head>
                        <body>'''
    return(string)




def topbar():
    string = '''<!-- topbar -->
        <div class="topbar">
            <div class="fill">
                <div class="container">
                    <a class="brand" href="/index.html">Mushroom</a>
                    <ul class="nav">
                        <li><a href="/index.html">Home</a></li>
                        <li class="active"><a href="wall.py">Wall</a></li>
                        <li><a href="transcripts.py">Transcripts</a></li>
                    </ul>
                </div>
            </div>
        </div>
        <!-- top end -->'''
    return(string)




def start_container():
    string = '''<!-- container -->
                <div class="container-fluid" 
                        ondragenter="onDragEnter(event)"
                        ondragover="onDragOver(event)"
                        ondrop="onDrop(event)">'''
    return(string)




def start_sidebar():
    string = '''<!-- sidebar -->
                <div class="sidebar">
                    <div id="chat-desc-wrapper">
                        <div class="chat-desc-title">
                            <h1>Mushroom Wall</h1>
                        </div>'''
    return(string)




def dropbox_auth():
    string = '''<div class="dropbox-auth alert-message block-message error">
                        <span class="label important">Dropbox Authentication</span>
                        <p>사용할 Dropbox를 설정해주십시오</p>
                        <form id="dropbox-form">
                            <label class="dropbox-form-label">App Key</label>
                            <input class="dropbox-form-controls">
                            <label class="dropbox-form-label">App Secret</label>
                            <input class="dropbox-form-controls">
                            <label class="dropbox-form-label">Access Type</label>
                            <select class="dropbox-form-controls">
                                <option>App Folder</option>
                                <option>Dropbox</option>
                            </select>
                            <input type="submit" class="dropbox-form-btn btn" value="인증하기">
                        </form>
                    </div>'''
    return(string)




def latest_files():
    string = '''<div>
                    <span class="label warning">Latest 2 files</span>
                    <span>&nbsp;&nbsp;<a href="#">more..</a></span>
                    <ul><li><a href="#">시작과제문서.gul</a></li><li><a href="#">사진.jpg</a></li></ul>
                </div>'''
    return(string)




def skype():
    string = '''<div>
                    <span class="label notice">Skype Conference Call</span>
<<<<<<< HEAD
                    <p>웩 ㅠㅜ</p>
=======
                    <form id="dropbox-form" class="form-stacked" action="javascript: alert('skype! ' + $('#skype-ids').val())">
                            <label class="skype-form-label">ID(�޸��� ����)</label>
                            <textarea id="skype-ids" class="skype-form-controls"></textarea>
                            <input type="submit" class="skype-form-btn btn" value="��ȭ�ϱ�">
                        </form>
>>>>>>> 735197ad620df3773bffe8905da1e69b4f9088bf
                </div>'''
    return(string)




def end_sidebar():
    return('</div></div>')




def start_content():
    string = '''<!-- chat -->
                <div class="content">
                    <div id="chat-wrapper">'''
    return(string)



def start_chat_table():
    return('<table id="chat_table" class="chat">')




def message(author, content, datetime, is_text = True, link = None):
    #global pre_author
    
    string = '''<tr class="text_message message">
                    <td class="message_person">
                        <span class="author">'''
    '''
    try:
        pre_author
    except NameError:
        string += author
    else:
        if( pre_author != author ):
            string += author
        
    pre_author = author'''
    
    string += author
    
    string += '''</span>
                    </td>
                    <td class="message_body">
                        <div class="message_body_content">'''
        
    if (is_text):
        string += content
    else:
        string += '<a href="' + link + '" target="_blank">' + content + '</a>'
    
        
    string += '''</div>
                        <span class="message_body_time">''' + datetime + '''</span>
                    </td>
                </tr>'''
    return(string)



def end_chat_table():
    return('</table>')



def dropbox_auth_warning():
    string = '''<!-- warning -->
                <div class="alert-message danger" data-alert="alert">
                    <a class="close" href="#">×</a>
                    <p><strong>알림!</strong>&nbsp;&nbsp;&nbsp;파일 업로드를 위한 Dropbox 인증이 필요합니다. 우측 상단의 폼에서 인증하시기 바랍니다.</p>
                </div>'''
    return(string)




def speak_form():
    string = '''<!-- speak form -->
                <div class="speak">
                    
                    <div>
                        <form id="chat_form" action="javascript: submitMessage()" >
                            <table><tr>
                                <td class="speak_person_td"><input type="text" name="name" id="speak_person" placeholder="name"></td>
                                <td class="speak_body_td"><input type="text" name="content" id="speak_body" placeholder="text here"></td>
                                <td class="speak_send_td"><input type="submit" id="speak_send" class="btn" value="Send Message" disabled></td>
                            </tr></table>
                        </form>
                    </div>
                </div>'''
    return(string)


def end_content():
    return('</div>')


def end_container():
    return('</div>')



def include_footer():
    return('</body></html>')


