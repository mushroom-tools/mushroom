# -*- coding: ms949 -*-


import transcripts_view
import wall_model

print(transcripts_view.response())
print(transcripts_view.include_header())
print(transcripts_view.topbar())
print(transcripts_view.start_container())
print(transcripts_view.search())        # search���� ã�� ���.....

print(transcripts_view.start_transcripts())

# db���� �����ͼ� ���
print(transcripts_view.transcript_day('Saturday, December 17, 2011', 'http://www.google.co.kr'))
print(transcripts_view.transcript_day('Saturday, December 17, 2011', '#'))

print(transcripts_view.end_transcripts())
print(transcripts_view.end_container())


# javascript �߰�

print(transcripts_view.include_footer())