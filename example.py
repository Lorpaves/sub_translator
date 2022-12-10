import pysubs2 as pysub
import translators.server as tss
# import time
import SubTranslator as subts
# servers = [
#     'alibaba',
#     'argos',
#     'bing',
#     'caiyun',
#     'iciba',
#     'itranslate',
#     'niutrans',
#     'mglip',
#     'papago',
#     'reverso',
#     'sogou',
#     'tencent',
#     'translateCom',
#     'utibet',
#     'yandex']
# sub = pysub.load('./test.srt')
# sub_string = sub.to_string('srt')
# for i in servers:
#     print(tss.translate_text(query_text=sub_string,
#           translator=i, if_use_cn_host=True))
#     time.sleep(3)
sub_ts = subts.SubTranslator(
    pysub=pysub, tss=tss, server='alibaba', if_use_cn_host=False)
sub_ts.translate_sub('./test.srt', './save.srt',
                     from_language='en', to_language='zh')
