import time
import random
"""Doc

Thanks to <pysubs2> and <translator> let this tool make sense

------------------------------------------------------------------------------------------

pysubs2: https://pypi.org/project/pysubs2/

pysubs2 is a Python library for editing subtitle files. 
It's based on SubStation Alpha,the native format of Aegisub; 
it also supports 
SubRip (SRT), MicroDVD, MPL2, TMP and WebVTT formats and OpenAI Whisper captions.
detail see: https://pysubs2.readthedocs.io/en/latest/supported-formats.html#native-format-substation-alpha

------------------------------------------------------------------------------------------

translator: https://pypi.org/project/translators/

Translators is a library which aims to bring free, multiple, enjoyable translation to individuals 
and students in Python. It based on the translation interface of Google, Yandex, Microsoft(Bing), 
Baidu, Alibaba, Tencent, NetEase(Youdao), Sogou, Kingsoft(Iciba), Iflytek, Niutrans, Lingvanex,
Naver(Papago), Deepl, Reverso, Itranslate, Caiyun, TranslateCom, Mglip, Utibet, Argos, etc.

------------------------------------------------------------------------------------------

Support extension: SubRip (SRT), MicroDVD(microdvd), WebVTT formats(vtt),Advanced SubStation Alpha v4.0+(ass),SubStation Alpha v4.0(ssa)

The translated file will saved as SRT formats

"""


class SubTranslator:

    def __init__(self, pysub, tss, **kwargs) -> None:
        """_summary_

        Args:
            pysub (pysubs2): Module pysubs2
            tss (translators.server): Module translators.server

        Accept Args:
            if_duration (bool: Default False) if need to set translate duration, set this to True
            duration (int) duration 
            if_ignore_empty_query (bool: Default True) if the text was empty, set True to ignore the text, else will throw error
            if_ignore_limit_of_length (bool: Default True)  Default limited length is 1500, set to True to ignore the error
            if_use_cn_host (bool: Default True)  use cn host or not
            server (str: Default "alibaba") the server that send request to translate the text
        """
        self.__pysub = pysub
        self.__tss = tss
        self.__if_duration = kwargs.get('if_duration', False)
        self.__duration = kwargs.get('duration', 1)
        self.__server = kwargs.get('server', 'random')
        self.__kwargs = kwargs

    def __get_sub(self, path):
        """_summary_

        Args:
            path (string): path of the subtitle file

        Returns:
            sub_event: SSAFile Object
        """
        return self.__pysub.load(path, encoding="utf-8")

    def __format_sub(self, sub_event):
        # sub_string = self.__pysub.SSAFile.to_string(sub_event, 'srt')
        sub_string = sub_event.to_string('srt')
        single_events = sub_string.split('\n\n')
        length = 0
        grouped_strings = []
        event = ''
        for index, single_event in enumerate(single_events):
            length += len(single_event)
            if length < 4500:
                event += single_event + '\n\n'
            if length < 4500 and index == len(single_events) - 1:
                grouped_strings.append(event)
            if length >= 4500:
                grouped_strings.append(event)
                length = 0
                event = '\n\n' + single_event + '\n\n'
        return grouped_strings

    def __translate(self, grouped_strings, switch_duration: int = 20, servers: list = []):
        total = len(grouped_strings)
        translated_subs = []
        server_index = random.randrange(0, len(servers))
        duration = switch_duration
        for index, single_string in enumerate(grouped_strings):
            if (self.__if_duration):
                time.sleep(self.__duration)
            if duration < 0:
                server_index = random.randrange(0, len(servers))
                duration = switch_duration
            try:
                translated_string = self.__tss.translate_text(query_text=single_string,
                                                              translator=servers[server_index],
                                                              **self.__kwargs)
            except self.__tss.TranslatorError:
                raise RuntimeError("""\033[0;33m 服务器请求失败😵‍💫，可能因为频繁请求而导致请求受阻，建议增长请求延迟。设置每次翻译后的停顿时间。
如果是使用国内的翻译服务器，使用cn host。
                
Failed to translate, make sure you set the translation duration time if you get this message.\033[0m
""")
            duration -= 1

            translated_subs.append(translated_string)
            print('\033[0;31m{origin_line}\033[0m \n=>\n \033[0;32m{translated_string}\033[0m'.format(
                origin_line=single_string, translated_string=translated_string))
            print('Current:\033[0;33m {index} \033[0m || \033[0;34m {total} \033[0m' .format(
                index=index + 1, total=total))

        return translated_subs

    def __translate_random(self, grouped_strings, switch_duration: int = 20):
        servers = [
            'alibaba',
            'google',
            'iciba',
            'lingvanex']
        return self.__translate(grouped_strings, switch_duration=switch_duration, servers=servers)

    def __translate_random_custom(self, grouped_strings, switch_duration: int = 20):
        servers = self.__kwargs.get('servers', None)
        if servers:
            return self.__translate(grouped_strings, switch_duration=switch_duration, servers=servers)

    def __translate_alibaba(self, grouped_strings):
        """_summary_

        Args:
            grouped_strings (str): grouped sub string
            from_language (str): original language
            to_language (str): target language to translate

        Returns:
            sub_event: translated sub string stored in an array
        """
        total = len(grouped_strings)
        translated_subs = []
        for index, single_string in enumerate(grouped_strings):
            if (self.__if_duration):
                time.sleep(self.__duration)
            try:
                translated_string = self.__tss.translate_text(translator='alibaba', query_text=single_string,
                                                              **self.__kwargs)
            except self.__tss.TranslatorError:
                raise RuntimeError("""\033[0;33m 服务器请求失败😵‍💫，可能因为频繁请求而导致请求受阻，建议增长请求延迟。设置每次翻译后的停顿时间。
如果是使用国内的翻译服务器，使用cn host。
                
Failed to translate, make sure you set the translation duration time if you get this message.\033[0m
""")
            translated_subs.append(translated_string)
            print('\033[0;31m{origin_line}\033[0m \n=>\n \033[0;32m{translated_string}\033[0m'.format(
                origin_line=single_string, translated_string=translated_string))
            print('Current:\033[0;33m {index} \033[0m || \033[0;34m {total} \033[0m' .format(
                index=index + 1, total=total))

        return translated_subs

    def __translate_google(self, grouped_strings):
        """_summary_

        Args:
            grouped_strings (str): grouped sub string
            from_language (str): original language
            to_language (str): target language to translate

        Returns:
            sub_event: translated sub string stored in an array
        """
        total = len(grouped_strings)
        translated_subs = []
        for index, single_string in enumerate(grouped_strings):
            if (self.__if_duration):
                time.sleep(self.__duration)
            try:
                translated_string = self.__tss.translate_text(translator='google', query_text=single_string,
                                                              **self.__kwargs)
            except self.__tss.TranslatorError:
                raise RuntimeError("""\033[0;33m 服务器请求失败😵‍💫，可能因为频繁请求而导致请求受阻，建议增长请求延迟。设置每次翻译后的停顿时间。
如果是使用国内的翻译服务器，使用cn host。
                
Failed to translate, make sure you set the translation duration time if you get this message.\033[0m
""")
            translated_subs.append(translated_string)
            print('\033[0;31m{origin_line}\033[0m \n=>\n \033[0;32m{translated_string}\033[0m'.format(
                origin_line=single_string, translated_string=translated_string))
            print('Current:\033[0;33m {index} \033[0m || \033[0;34m {total} \033[0m' .format(
                index=index + 1, total=total))

        return translated_subs

    def __translate_argos(self, grouped_strings):
        """_summary_

        Args:
            grouped_strings (str): grouped sub string
            from_language (str): original language
            to_language (str): target language to translate

        Returns:
            sub_event: translated sub string stored in an array
        """
        total = len(grouped_strings)
        translated_subs = []
        for index, single_string in enumerate(grouped_strings):
            if (self.__if_duration):
                time.sleep(self.__duration)
            try:
                translated_string = self.__tss.translate_text(translator='argos', query_text=single_string,
                                                              **self.__kwargs)
            except self.__tss.TranslatorError:
                raise RuntimeError("""\033[0;33m 服务器请求失败😵‍💫，可能因为频繁请求而导致请求受阻，建议增长请求延迟。设置每次翻译后的停顿时间。
如果是使用国内的翻译服务器，使用cn host。
                
Failed to translate, make sure you set the translation duration time if you get this message.\033[0m
""")
            translated_subs.append(translated_string)
            print('\033[0;31m{origin_line}\033[0m \n=>\n \033[0;32m{translated_string}\033[0m'.format(
                origin_line=single_string, translated_string=translated_string))
            print('Current:\033[0;33m {index} \033[0m || \033[0;34m {total} \033[0m' .format(
                index=index + 1, total=total))

        return translated_subs

    def __translate_bing(self, grouped_strings):
        """_summary_
w
        Args:
            grouped_strings (str): grouped sub string
            from_language (str): original language
            to_language (str): target language to translate

        Returns:
            sub_event: translated sub string stored in an array
        """
        total = len(grouped_strings)
        translated_subs = []
        for index, single_string in enumerate(grouped_strings):
            if (self.__if_duration):
                time.sleep(self.__duration)
            try:
                translated_string = self.__tss.translate_text(translator='bing', query_text=single_string,
                                                              **self.__kwargs)
            except self.__tss.TranslatorError:
                raise RuntimeError("""\033[0;33m 服务器请求失败😵‍💫，可能因为频繁请求而导致请求受阻，建议增长请求延迟。设置每次翻译后的停顿时间。
如果是使用国内的翻译服务器，使用cn host。
                
Failed to translate, make sure you set the translation duration time if you get this message.\033[0m
""")
            translated_subs.append(translated_string)
            print('\033[0;31m{origin_line}\033[0m \n=>\n \033[0;32m{translated_string}\033[0m'.format(
                origin_line=single_string, translated_string=translated_string))
            print('Current:\033[0;33m {index} \033[0m || \033[0;34m {total} \033[0m' .format(
                index=index + 1, total=total))

        return translated_subs

    def __translate_caiyun(self, grouped_strings):
        """_summary_

        Args:
            grouped_strings (str): grouped sub string
            from_language (str): original language
            to_language (str): target language to translate

        Returns:
            sub_event: translated sub string stored in an array
        """
        total = len(grouped_strings)
        translated_subs = []
        for index, single_string in enumerate(grouped_strings):
            if (self.__if_duration):
                time.sleep(self.__duration)
            try:
                translated_string = self.__tss.translate_text(translator='caiyun', query_text=single_string,
                                                              **self.__kwargs)
            except self.__tss.TranslatorError:
                raise RuntimeError("""\033[0;33m 服务器请求失败😵‍💫，可能因为频繁请求而导致请求受阻，建议增长请求延迟。设置每次翻译后的停顿时间。
如果是使用国内的翻译服务器，使用cn host。
                
Failed to translate, make sure you set the translation duration time if you get this message.\033[0m
""")
            translated_subs.append(translated_string)
            print('\033[0;31m{origin_line}\033[0m \n=>\n \033[0;32m{translated_string}\033[0m'.format(
                origin_line=single_string, translated_string=translated_string))
            print('Current:\033[0;33m {index} \033[0m || \033[0;34m {total} \033[0m' .format(
                index=index + 1, total=total))

        return translated_subs

    def __translate_lingvanex(self, grouped_strings):
        """_summary_

        Args:
            grouped_strings (str): grouped sub string
            from_language (str): original language
            to_language (str): target language to translate

        Returns:
            sub_event: translated sub string stored in an array
        """
        total = len(grouped_strings)
        translated_subs = []
        for index, single_string in enumerate(grouped_strings):
            if (self.__if_duration):
                time.sleep(self.__duration)
            try:
                translated_string = self.__tss.translate_text(translator='lingvanex', query_text=single_string,
                                                              **self.__kwargs)
            except self.__tss.TranslatorError:
                raise RuntimeError("""\033[0;33m 服务器请求失败😵‍💫，可能因为频繁请求而导致请求受阻，建议增长请求延迟。设置每次翻译后的停顿时间。
如果是使用国内的翻译服务器，使用cn host。
                
Failed to translate, make sure you set the translation duration time if you get this message.\033[0m
""")
            translated_subs.append(translated_string)
            print('\033[0;31m{origin_line}\033[0m \n=>\n \033[0;32m{translated_string}\033[0m'.format(
                origin_line=single_string, translated_string=translated_string))
            print('Current:\033[0;33m {index} \033[0m || \033[0;34m {total} \033[0m' .format(
                index=index + 1, total=total))

        return translated_subs

    def __translate_baidu(self, grouped_strings):
        """_summary_

        Args:
            grouped_strings (str): grouped sub string
            from_language (str): original language
            to_language (str): target language to translate

        Returns:
            sub_event: translated sub string stored in an array
        """
        total = len(grouped_strings)
        translated_subs = []
        for index, single_string in enumerate(grouped_strings):
            if (self.__if_duration):
                time.sleep(self.__duration)
            try:
                translated_string = self.__tss.translate_text(translator='baidu', query_text=single_string,
                                                              **self.__kwargs)
            except self.__tss.TranslatorError:
                raise RuntimeError("""\033[0;33m 服务器请求失败😵‍💫，可能因为频繁请求而导致请求受阻，建议增长请求延迟。设置每次翻译后的停顿时间。
如果是使用国内的翻译服务器，使用cn host。
                
Failed to translate, make sure you set the translation duration time if you get this message.\033[0m
""")
            translated_subs.append(translated_string)
            print('\033[0;31m{origin_line}\033[0m \n=>\n \033[0;32m{translated_string}\033[0m'.format(
                origin_line=single_string, translated_string=translated_string))
            print('Current:\033[0;33m {index} \033[0m || \033[0;34m {total} \033[0m' .format(
                index=index + 1, total=total))

        return translated_subs

    def __translate_iciba(self, grouped_strings):
        """_summary_

        Args:
            grouped_strings (str): grouped sub string
            from_language (str): original language
            to_language (str): target language to translate

        Returns:
            sub_event: translated sub string stored in an array
        """
        total = len(grouped_strings)
        translated_subs = []
        for index, single_string in enumerate(grouped_strings):
            if (self.__if_duration):
                time.sleep(self.__duration)
            try:
                translated_string = self.__tss.translate_text(translator='iciba', query_text=single_string,
                                                              **self.__kwargs)
            except self.__tss.TranslatorError:
                raise RuntimeError("""\033[0;33m 服务器请求失败😵‍💫，可能因为频繁请求而导致请求受阻，建议增长请求延迟。设置每次翻译后的停顿时间。
如果是使用国内的翻译服务器，使用cn host。
                
Failed to translate, make sure you set the translation duration time if you get this message.\033[0m
""")
            translated_subs.append(translated_string)
            print('\033[0;31m{origin_line}\033[0m \n=>\n \033[0;32m{translated_string}\033[0m'.format(
                origin_line=single_string, translated_string=translated_string))
            print('Current:\033[0;33m {index} \033[0m || \033[0;34m {total} \033[0m' .format(
                index=index + 1, total=total))

        return translated_subs

    def __translate_itranslate(self, grouped_strings):
        """_summary_

        Args:
            grouped_strings (str): grouped sub string
            from_language (str): original language
            to_language (str): target language to translate

        Returns:
            sub_event: translated sub string stored in an array
        """
        total = len(grouped_strings)
        translated_subs = []
        for index, single_string in enumerate(grouped_strings):
            if (self.__if_duration):
                time.sleep(self.__duration)
            try:
                translated_string = self.__tss.translate_text(translator='itranslate', query_text=single_string,
                                                              **self.__kwargs)
            except self.__tss.TranslatorError:
                raise RuntimeError("""\033[0;33m 服务器请求失败😵‍💫，可能因为频繁请求而导致请求受阻，建议增长请求延迟。设置每次翻译后的停顿时间。
如果是使用国内的翻译服务器，使用cn host。
                
Failed to translate, make sure you set the translation duration time if you get this message.\033[0m
""")
            translated_subs.append(translated_string)
            print('\033[0;31m{origin_line}\033[0m \n=>\n \033[0;32m{translated_string}\033[0m'.format(
                origin_line=single_string, translated_string=translated_string))
            print('Current:\033[0;33m {index} \033[0m || \033[0;34m {total} \033[0m' .format(
                index=index + 1, total=total))

        return translated_subs

    def __translate_sogou(self, grouped_strings):
        """_summary_

        Args:
            grouped_strings (str): grouped sub string
            from_language (str): original language
            to_language (str): target language to translate

        Returns:
            sub_event: translated sub string stored in an array
        """
        total = len(grouped_strings)
        translated_subs = []
        for index, single_string in enumerate(grouped_strings):
            if (self.__if_duration):
                time.sleep(self.__duration)
            try:
                translated_string = self.__tss.translate_text(translator='sogou', query_text=single_string,
                                                              **self.__kwargs)
            except self.__tss.TranslatorError:
                raise RuntimeError("""\033[0;33m 服务器请求失败😵‍💫，可能因为频繁请求而导致请求受阻，建议增长请求延迟。设置每次翻译后的停顿时间。
如果是使用国内的翻译服务器，使用cn host。
                
Failed to translate, make sure you set the translation duration time if you get this message.\033[0m
""")
            translated_subs.append(translated_string)
            print('\033[0;31m{origin_line}\033[0m \n=>\n \033[0;32m{translated_string}\033[0m'.format(
                origin_line=single_string, translated_string=translated_string))
            print('Current:\033[0;33m {index} \033[0m || \033[0;34m {total} \033[0m' .format(
                index=index + 1, total=total))

        return translated_subs

    def __translate_tencent(self, grouped_strings):
        """_summary_

        Args:
            grouped_strings (str): grouped sub string
            from_language (str): original language
            to_language (str): target language to translate

        Returns:
            sub_event: translated sub string stored in an array
        """
        total = len(grouped_strings)
        translated_subs = []
        for index, single_string in enumerate(grouped_strings):
            if (self.__if_duration):
                time.sleep(self.__duration)
            try:
                translated_string = self.__tss.translate_text(translator='tencent', query_text=single_string,
                                                              **self.__kwargs)
            except self.__tss.TranslatorError:
                raise RuntimeError("""\033[0;33m 服务器请求失败😵‍💫，可能因为频繁请求而导致请求受阻，建议增长请求延迟。设置每次翻译后的停顿时间。
如果是使用国内的翻译服务器，使用cn host。
                
Failed to translate, make sure you set the translation duration time if you get this message.\033[0m
""")
            translated_subs.append(translated_string)
            print('\033[0;31m{origin_line}\033[0m \n=>\n \033[0;32m{translated_string}\033[0m'.format(
                origin_line=single_string, translated_string=translated_string))
            print('Current:\033[0;33m {index} \033[0m || \033[0;34m {total} \033[0m' .format(
                index=index + 1, total=total))

        return translated_subs

    def __write_sub(self, sub_string, file_name: str):
        """_summary_

        Args:
            sub_string (str): string of the sub
            file_name (str): the name used to save the translated subtitle file
        """

        sub_string = '\n'.join(sub_string).replace(
            '-> ', ' --> ').replace('：', ':').replace('-&gt;', ' -->').replace('，', ',')
        sub = self.__pysub.SSAFile.from_string(sub_string, 'srt')
        sub.save(file_name)
        print('\033[4;31m File Saved at {name}\033[0m'.format(name=file_name))

    def translate_sub(self, path: str, file_name: str, **kwargs):
        """_summary_

        Args:
            path (str): path of the subtitle file
            file_name (str): the name used to save the translated subtitle file
            from_language (str, optional): original language. Defaults to 'en'.
            to_language (str, optional): target language to translate. Defaults to 'zh'.
        """

        if self.__server == 'alibaba':
            sub_event = self.__get_sub(path=path)
            grouped_string = self.__format_sub(sub_event=sub_event)
            translated_sub = self.__translate_alibaba(
                grouped_strings=grouped_string)
            self.__write_sub(sub_string=translated_sub, file_name=file_name)
        elif self.__server == 'google':
            sub_event = self.__get_sub(path=path)
            grouped_string = self.__format_sub(sub_event=sub_event)
            translated_sub = self.__translate_google(
                grouped_strings=grouped_string)
            self.__write_sub(sub_string=translated_sub, file_name=file_name)
        elif self.__server == 'bing':
            sub_event = self.__get_sub(path=path)
            grouped_string = self.__format_sub(sub_event=sub_event)
            translated_sub = self.__translate_bing(
                grouped_strings=grouped_string)
            self.__write_sub(sub_string=translated_sub, file_name=file_name)

        elif self.__server == 'baidu':
            sub_event = self.__get_sub(path=path)
            grouped_string = self.__format_sub(sub_event=sub_event)
            translated_sub = self.__translate_baidu(
                grouped_strings=grouped_string)
            self.__write_sub(sub_string=translated_sub, file_name=file_name)

        elif self.__server == 'caiyun':
            sub_event = self.__get_sub(path=path)
            grouped_string = self.__format_sub(sub_event=sub_event)
            translated_sub = self.__translate_caiyun(
                grouped_strings=grouped_string)
            self.__write_sub(sub_string=translated_sub, file_name=file_name)
        elif self.__server == 'lingvanex':
            sub_event = self.__get_sub(path=path)
            grouped_string = self.__format_sub(sub_event=sub_event)
            translated_sub = self.__translate_lingvanex(
                grouped_strings=grouped_string)
            self.__write_sub(sub_string=translated_sub, file_name=file_name)
        elif self.__server == 'argos':
            sub_event = self.__get_sub(path=path)
            grouped_string = self.__format_sub(sub_event=sub_event)
            translated_sub = self.__translate_argos(
                grouped_strings=grouped_string)
            self.__write_sub(sub_string=translated_sub, file_name=file_name)
        elif self.__server == 'iciba':
            sub_event = self.__get_sub(path=path)
            grouped_string = self.__format_sub(sub_event=sub_event)
            translated_sub = self.__translate_iciba(
                grouped_strings=grouped_string)
            self.__write_sub(sub_string=translated_sub, file_name=file_name)
        elif self.__server == 'itranslate':
            sub_event = self.__get_sub(path=path)
            grouped_string = self.__format_sub(sub_event=sub_event)
            translated_sub = self.__translate_itranslate(
                grouped_strings=grouped_string)
            self.__write_sub(sub_string=translated_sub, file_name=file_name)
        elif self.__server == 'sogou':
            sub_event = self.__get_sub(path=path)
            grouped_string = self.__format_sub(sub_event=sub_event)
            translated_sub = self.__translate_sogou(
                grouped_strings=grouped_string)
            self.__write_sub(sub_string=translated_sub, file_name=file_name)
        elif self.__server == 'tencent':
            sub_event = self.__get_sub(path=path)
            grouped_string = self.__format_sub(sub_event=sub_event)
            translated_sub = self.__translate_tencent(
                grouped_strings=grouped_string)
            self.__write_sub(sub_string=translated_sub, file_name=file_name)
        elif self.__server == 'random':
            switch_duration = self.__kwargs.get('switch_duration', 10)
            sub_event = self.__get_sub(path=path)
            grouped_string = self.__format_sub(sub_event=sub_event)
            translated_sub = self.__translate_random(
                grouped_strings=grouped_string, switch_duration=switch_duration)
            self.__write_sub(sub_string=translated_sub, file_name=file_name)
        elif self.__server == 'custom':
            switch_duration = self.__kwargs.get('switch_duration', 10)
            sub_event = self.__get_sub(path=path)
            grouped_string = self.__format_sub(sub_event=sub_event)
            translated_sub = self.__translate_random_custom(
                grouped_strings=grouped_string, switch_duration=switch_duration)
            self.__write_sub(sub_string=translated_sub, file_name=file_name)
