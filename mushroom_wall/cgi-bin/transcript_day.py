
import wall_view
import wall_model
import cgi

form_data = cgi.FieldStorage()

print(wall_view.response())
print('''<!DOCTYPE html>
        <html>
            <head>
            
                <title>Mushroom</title>
                
                <!-- style -->
                <link rel="stylesheet" href="/css/bootstrap.css">
                <link rel="stylesheet" href="/css/style.css">
                <link rel="stylesheet" href="/css/transcript_day.css">
                <link rel="stylesheet" href="/css/wall.css">
            </head>
            <body>''')




date_split = form_data['date'].value.split('-')

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


print('<h1>' + date_str + '</h1>')


print(wall_view.start_content())

print(wall_view.start_chat_table())

list = wall_model.get_transcript_day(date_split[0], date_split[1], date_split[2])

for msg in list:
    print(wall_view.message(msg[0], msg[1], msg[2]))

#print(wall_view.message('박윤희', '안녕 ㅋㅋ', '03:40 AM'))
#print(wall_view.message('박윤희', '헤헤', '03:40 AM'))
#print(wall_view.message('박윤희', 'ㅎㅎㅎㅎ', '03:40 AM'))
#print(wall_view.message('이하나', '사진.jpg', '03:40 AM', False, 'http://www.google.co.kr/images/nav_logo99.png'))
#print(wall_view.message('이하나', 'ㅋㄷㅋㄷ', '03:40 AM'))
print(wall_view.end_chat_table())
print(wall_view.include_footer())
