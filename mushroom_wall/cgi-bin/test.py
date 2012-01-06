
import transcripts_view
import wall_model

str = ''
#for d in wall_model.get_transcript_all():
 #   str += 'hi '

print(transcripts_view.response())
print(transcripts_view.include_header())
print('wwww')
list = wall_model.get_transcript_day_list()
print(list)
print(list[0])
i = 0
while i< len(list):
    print(transcripts_view.transcript_day(strr, '#'))
print('</body></html>')
