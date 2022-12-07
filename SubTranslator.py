
import time


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
        self.__if_ignore_empty_query = kwargs.get(
            'if_ignore_empty_query', True)
        self.__if_ignore_limit_of_length = kwargs.get(
            'if_ignore_limit_of_length', True)
        self.__if_use_cn_host = kwargs.get('if_use_cn_host', True)
        self.__server = kwargs.get('server', 'alibaba')

    def __get_sub(self, path):
        """_summary_

        Args:
            path (string): path of the subtitle file

        Returns:
            sub_event: SSAFile Object
        """
        return self.__pysub.load(path)

    def __format_sub(self, sub_event):
        sub_string = self.__pysub.SSAFile.to_string(sub_event, 'srt')
        single_events = sub_string.split('\n\n')
        length = 0
        grouped_strings = []
        event = ''
        for single_event in single_events:
            length += len(single_event)
            event += single_event + '\n\n'
            if length > 1000:
                grouped_strings.append(event)
                length = 0
                event = single_event + '\n\n'
        return grouped_strings

    def __translate_alibaba(self, grouped_strings, from_language: str, to_language: str):
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
            translated_string = self.__tss.alibaba(query_text=single_string,
                                                 from_language=from_language, to_language=to_language,
                                                 if_ignore_empty_query=self.__if_ignore_empty_query,
                                                 if_ignore_limit_of_length=self.__if_ignore_limit_of_length,
                                                 if_use_cn_host=self.__if_use_cn_host)
            translated_subs.append(translated_string)
            print('\033[0;31m{origin_line}\033[0m \n=>\n \033[0;32m{translated_string}\033[0m'.format(
                origin_line=single_string, translated_string=translated_string))
            print('Current:\033[0;33m {index} \033[0m || \033[0;34m {total} \033[0m' .format(
                index=index + 1, total=total))

        return translated_subs

    def __translate_google(self, grouped_strings, from_language: str, to_language: str):
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
            translated_string = self.__tss.google(query_text=single_string,
                                                 from_language=from_language, to_language=to_language,
                                                 if_ignore_empty_query=self.__if_ignore_empty_query,
                                                 if_ignore_limit_of_length=self.__if_ignore_limit_of_length,
                                                 if_use_cn_host=self.__if_use_cn_host)
            translated_subs.append(translated_string)
            print('\033[0;31m{origin_line}\033[0m \n=>\n \033[0;32m{translated_string}\033[0m'.format(
                origin_line=single_string, translated_string=translated_string))
            print('Current:\033[0;33m {index} \033[0m || \033[0;34m {total} \033[0m' .format(
                index=index + 1, total=total))

        return translated_subs

    def __translate_yandex(self, grouped_strings, from_language: str, to_language: str):
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
            translated_string = self.__tss.yandex(query_text=single_string,
                                                 from_language=from_language, to_language=to_language,
                                                 if_ignore_empty_query=self.__if_ignore_empty_query,
                                                 if_ignore_limit_of_length=self.__if_ignore_limit_of_length,
                                                 if_use_cn_host=self.__if_use_cn_host)
            translated_subs.append(translated_string)
            print('\033[0;31m{origin_line}\033[0m \n=>\n \033[0;32m{translated_string}\033[0m'.format(
                origin_line=single_string, translated_string=translated_string))
            print('Current:\033[0;33m {index} \033[0m || \033[0;34m {total} \033[0m' .format(
                index=index + 1, total=total))

        return translated_subs

    def __translate_argos(self, grouped_strings, from_language: str, to_language: str):
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
            translated_string = self.__tss.argos(query_text=single_string,
                                                 from_language=from_language, to_language=to_language,
                                                 if_ignore_empty_query=self.__if_ignore_empty_query,
                                                 if_ignore_limit_of_length=self.__if_ignore_limit_of_length,
                                                 if_use_cn_host=self.__if_use_cn_host)
            translated_subs.append(translated_string)
            print('\033[0;31m{origin_line}\033[0m \n=>\n \033[0;32m{translated_string}\033[0m'.format(
                origin_line=single_string, translated_string=translated_string))
            print('Current:\033[0;33m {index} \033[0m || \033[0;34m {total} \033[0m' .format(
                index=index + 1, total=total))

        return translated_subs

    def __translate_bing(self, grouped_strings, from_language: str, to_language: str):
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
            translated_string = self.__tss.bing(query_text=single_string,
                                                 from_language=from_language, to_language=to_language,
                                                 if_ignore_empty_query=self.__if_ignore_empty_query,
                                                 if_ignore_limit_of_length=self.__if_ignore_limit_of_length,
                                                 if_use_cn_host=self.__if_use_cn_host)
            translated_subs.append(translated_string)
            print('\033[0;31m{origin_line}\033[0m \n=>\n \033[0;32m{translated_string}\033[0m'.format(
                origin_line=single_string, translated_string=translated_string))
            print('Current:\033[0;33m {index} \033[0m || \033[0;34m {total} \033[0m' .format(
                index=index + 1, total=total))

        return translated_subs

    def __translate_caiyun(self, grouped_strings, from_language: str, to_language: str):
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
            translated_string = self.__tss.caiyun(query_text=single_string,
                                                 from_language=from_language, to_language=to_language,
                                                 if_ignore_empty_query=self.__if_ignore_empty_query,
                                                 if_ignore_limit_of_length=self.__if_ignore_limit_of_length,
                                                 if_use_cn_host=self.__if_use_cn_host)
            translated_subs.append(translated_string)
            print('\033[0;31m{origin_line}\033[0m \n=>\n \033[0;32m{translated_string}\033[0m'.format(
                origin_line=single_string, translated_string=translated_string))
            print('Current:\033[0;33m {index} \033[0m || \033[0;34m {total} \033[0m' .format(
                index=index + 1, total=total))

        return translated_subs

    def __translate_lingvanex(self, grouped_strings, from_language: str, to_language: str):
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
            translated_string = self.__tss.lingvanex(query_text=single_string,
                                                 from_language=from_language, to_language=to_language,
                                                 if_ignore_empty_query=self.__if_ignore_empty_query,
                                                 if_ignore_limit_of_length=self.__if_ignore_limit_of_length,
                                                 if_use_cn_host=self.__if_use_cn_host)
            translated_subs.append(translated_string)
            print('\033[0;31m{origin_line}\033[0m \n=>\n \033[0;32m{translated_string}\033[0m'.format(
                origin_line=single_string, translated_string=translated_string))
            print('Current:\033[0;33m {index} \033[0m || \033[0;34m {total} \033[0m' .format(
                index=index + 1, total=total))

        return translated_subs

    def __translate_baidu(self, grouped_strings, from_language: str, to_language: str):
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
            translated_string = self.__tss.baidu(query_text=single_string,
                                                 from_language=from_language, to_language=to_language,
                                                 if_ignore_empty_query=self.__if_ignore_empty_query,
                                                 if_ignore_limit_of_length=self.__if_ignore_limit_of_length,
                                                 if_use_cn_host=self.__if_use_cn_host)
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
        
        sub_string = ''.join(sub_string).replace('-> ', ' --> ').replace('：',':').replace('-&gt;', ' -->').replace('，',',')
        sub = self.__pysub.SSAFile.from_string(sub_string, 'srt')
        sub.save(file_name)
        print('\033[4;32m File Saved at {name}\033[0m'.format(name=file_name))

    def translate_sub(self, path: str, file_name: str, from_language: str = 'en', to_language: str = 'zh'):
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
                grouped_strings=grouped_string, from_language=from_language, to_language=to_language)
            self.__write_sub(sub_string=translated_sub, file_name=file_name)
        elif self.__server == 'google':
            sub_event = self.__get_sub(path=path)
            grouped_string = self.__format_sub(sub_event=sub_event)
            translated_sub = self.__translate_google(
                grouped_strings=grouped_string, from_language=from_language, to_language=to_language)
            self.__write_sub(sub_string=translated_sub, file_name=file_name)
        elif self.__server == 'yandex':
            sub_event = self.__get_sub(path=path)
            grouped_string = self.__format_sub(sub_event=sub_event)
            translated_sub = self.__translate_yandex(
                grouped_strings=grouped_string, from_language=from_language, to_language=to_language)
            self.__write_sub(sub_string=translated_sub, file_name=file_name)
        elif self.__server == 'bing':
            sub_event = self.__get_sub(path=path)
            grouped_string = self.__format_sub(sub_event=sub_event)
            translated_sub = self.__translate_bing(
                grouped_strings=grouped_string, from_language=from_language, to_language=to_language)
            self.__write_sub(sub_string=translated_sub, file_name=file_name)

        elif self.__server == 'baidu':
            sub_event = self.__get_sub(path=path)
            grouped_string = self.__format_sub(sub_event=sub_event)
            translated_sub = self.__translate_baidu(
                grouped_strings=grouped_string, from_language=from_language, to_language=to_language)
            self.__write_sub(sub_string=translated_sub, file_name=file_name)

        elif self.__server == 'caiyun':
            sub_event = self.__get_sub(path=path)
            grouped_string = self.__format_sub(sub_event=sub_event)
            translated_sub = self.__translate_caiyun(
                grouped_strings=grouped_string, from_language=from_language, to_language=to_language)
            self.__write_sub(sub_string=translated_sub, file_name=file_name)
        elif self.__server == 'lingvanex':
            sub_event = self.__get_sub(path=path)
            grouped_string = self.__format_sub(sub_event=sub_event)
            translated_sub = self.__translate_lingvanex(
                grouped_strings=grouped_string, from_language=from_language, to_language=to_language)
            self.__write_sub(sub_string=translated_sub, file_name=file_name)
        elif self.__server == 'argos':
            sub_event = self.__get_sub(path=path)
            grouped_string = self.__format_sub(sub_event=sub_event)
            translated_sub = self.__translate_argos(
                grouped_strings=grouped_string, from_language=from_language, to_language=to_language)
            self.__write_sub(sub_string=translated_sub, file_name=file_name)
