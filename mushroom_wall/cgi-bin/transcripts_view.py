# -*- coding: ms949 -*-


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
                            <link rel="stylesheet" href="/css/transcripts.css">
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
                        <li><a href="wall.py">Wall</a></li>
                        <li class="active"><a href="transcripts.py">Files, Transcripts & Search</a></li>
                    </ul>
                </div>
            </div>
        </div>
        <!-- top end -->'''
    return(string)



def start_container():
    string = '''<div class="container">
                    <!-- title -->
                    <h1>Files, Transcripts & Search</h1>'''
    return(string)



def search():
    string = '''<!--  Search -->
                <div class="search">
                    <form id="search-form">
                        <input type="text" id="search-form-input">
                        <input type="submit" value="Search" class="btn">
                    </form>
                </div>'''
    return(string)



def start_transcripts():
    string = '''<!-- Trascripts -->
                <div class="transcripts">'''
    return(string)



def transcript_day(date, link = "#"):
    string = '''<div>
                    <div class="page-header">
                        <h3>''' + date + '''
                            <small>- <a href="''' + link + '''">Read the transcript</a></small>
                        </h3>
                    </div>
                </div>'''
    return(string)



def end_transcripts():
    return('</div>')



def end_container():
    string = '''</div>
                <!-- container end -->    '''
    return(string)



def include_footer():
    string = '''</body>
            </html>'''
    return(string)