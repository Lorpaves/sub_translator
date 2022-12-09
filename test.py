import translators as ts
import translators.server as tss
import pysubs2 as pysub
sub = pysub.load('./2.srt')
sub_string = sub.to_string('srt')
ts_test = tss.translate_text(
    query_text=sub_string, translator='google', from_language='en', to_language='zh')
