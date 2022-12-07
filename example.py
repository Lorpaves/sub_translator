import pysubs2 as pysub
import translators.server as tss
import SubTranslator

sub_ts = SubTranslator.SubTranslator(pysub=pysub, tss=tss, server='alibaba',if_use_cn_host=False)
sub_ts.translate_sub('./test.srt', './save.srt',
                     from_language='en', to_language='zh')
