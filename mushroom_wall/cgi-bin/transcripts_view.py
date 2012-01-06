#! /usr/local/bin/python3
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
                        <li class="active"><a href="transcripts.py">Transcripts</a></li>
                    </ul>
                </div>
            </div>
        </div>
        <!-- top end -->'''
    return(string)



def start_container():
    string = '''<div class="container">
                    <!-- title -->
                    <h1>Transcripts</h1>'''
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
    
    date_split = date.split('-')

    if(date_split[1] == '01'):
        date_str = 'January'
    elif(date_split[1] == '02'):
        date_str = 'Februry'
    elif(date_split[1] == '03'):
        date_str = 'March'
    elif(date_split[1] == '04'):
        date_str = 'April'
    elif(date_split[1] == '05'):
        date_str = 'May'
    elif(date_split[1] == '06'):
        date_str = 'June'
    elif(date_split[1] == '07'):
        date_str = 'July'
    elif(date_split[1] == '08'):
        date_str = 'August'
    elif(date_split[1] == '09'):
        date_str = 'October'
    elif(date_split[1] == '10'):
        date_str = 'September'
    elif(date_split[1] == '11'):
        date_str = 'November'
    else:
        date_str = 'December'
    
    date_str += ' ' + date_split[2] + ', ' + date_split[0]
    
    
    string = '''<div>
                    <div class="page-header">
                        <h3>''' + date_str + '''
                            <small>- <a href="''' + link + '''" target="_blank">Read the transcript</a></small>
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
