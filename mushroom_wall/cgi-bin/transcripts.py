#! /usr/local/bin/python3

# -*- coding: ms949 -*-


import transcripts_view
import wall_model

print(transcripts_view.response())
print(transcripts_view.include_header())
print(transcripts_view.topbar())
print(transcripts_view.start_container())
#print(transcripts_view.search())        # search���� ã�� ���.....

print(transcripts_view.start_transcripts())


# db���� �����ͼ� ���
list = wall_model.get_transcript_day_list()
i = 0
while i< len(list):
    print(transcripts_view.transcript_day(list[i], 'transcript_day.py?date=' + list[i]))
    i+= 1
    

print(transcripts_view.end_transcripts())
print(transcripts_view.end_container())



# javascript �߰�

print(transcripts_view.include_footer())
