# -*- coding: ms949 -*-


import transcripts_view
import wall_model

print(transcripts_view.response())
print(transcripts_view.include_header())
print(transcripts_view.topbar())
print(transcripts_view.start_container())
print(transcripts_view.search())        # search에서 찾는 기능.....

print(transcripts_view.start_transcripts())

# db에서 가져와서 출력
print(transcripts_view.transcript_day('Saturday, December 17, 2011', 'http://www.google.co.kr'))
print(transcripts_view.transcript_day('Saturday, December 17, 2011', '#'))

print(transcripts_view.end_transcripts())
print(transcripts_view.end_container())


# javascript 추가

print(transcripts_view.include_footer())