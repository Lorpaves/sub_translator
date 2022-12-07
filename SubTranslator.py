import pysubs2
import translators.server
import time


class SubTranslator:

    def __init__(self, pysub: pysubs2, tss: translators.server, **kwargs) -> None:
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
        self.__server = kwargs.get('translate_server', 'alibaba')

    def __get_sub(self, path):
        """_summary_

        Args:
            path (string): path of the subtitle file

        Returns:
            sub_event: SSAFile Object
        """
        return self.__pysub.load(path)

    def __translate_alibaba(self, sub_event: pysubs2.SSAEvent, from_language: str, to_language: str):
        """_summary_

        Args:
            sub_event (pysubs2.SSAEvent): pysubs2 object
            from_language (str): original language
            to_language (str): target language to translate

        Returns:
            sub_event: translated sub object
        """
        total_lines = len(sub_event)
        for index, line in enumerate(sub_event):
            if (self.__if_duration):
                time.sleep(self.__duration)
            temp = line.text
            translated_line = self.__tss.alibaba(query_text=line.text,
                                                 from_language=from_language, to_language=to_language,
                                                 if_ignore_empty_query=self.__if_ignore_empty_query,
                                                 if_ignore_limit_of_length=self.__if_ignore_limit_of_length,
                                                 if_use_cn_host=self.__if_use_cn_host)
            line.text = translated_line
            print('\033[0;31m{origin_line}\033[0m => \033[0;32m{translated_line}\033[0m'.format(
                origin_line=temp, translated_line=line.text))
            print('Current:\033[0;33m {index} \033[0m || \033[0;34m {total} \033[0m' .format(
                index=index, total=total_lines))

        return sub_event

    def __translate_google(self, sub_event: pysubs2.SSAEvent, from_language: str, to_language: str):
        """_summary_

        Args:
            sub_event (pysubs2.SSAEvent): pysubs2 object
            from_language (str): original language
            to_language (str): target language to translate

        Returns:
            sub_event: translated sub object
        """
        total_lines = len(sub_event)
        for index, line in enumerate(sub_event):
            if (self.__if_duration):
                time.sleep(self.__duration)
            temp = line.text
            translated_line = self.__tss.google(query_text=line.text,
                                                from_language=from_language, to_language=to_language,
                                                if_ignore_empty_query=self.__if_ignore_empty_query,
                                                if_ignore_limit_of_length=self.__if_ignore_limit_of_length,
                                                if_use_cn_host=self.__if_use_cn_host)
            line.text = translated_line
            print('\033[0;31m{origin_line}\033[0m => \033[0;32m{translated_line}\033[0m'.format(
                origin_line=temp, translated_line=line.text))
            print('Current:\033[0;33m {index} \033[0m || \033[0;34m {total} \033[0m' .format(
                index=index, total=total_lines))

        return sub_event

    def __translate_yandex(self, sub_event: pysubs2.SSAEvent, from_language: str, to_language: str):
        """_summary_

        Args:
            sub_event (pysubs2.SSAEvent): pysubs2 object
            from_language (str): original language
            to_language (str): target language to translate

        Returns:
            sub_event: translated sub object
        """
        total_lines = len(sub_event)
        for index, line in enumerate(sub_event):
            if (self.__if_duration):
                time.sleep(self.__duration)
            temp = line.text
            translated_line = self.__tss.yandex(query_text=line.text,
                                                from_language=from_language, to_language=to_language,
                                                if_ignore_empty_query=self.__if_ignore_empty_query,
                                                if_ignore_limit_of_length=self.__if_ignore_limit_of_length,
                                                if_use_cn_host=self.__if_use_cn_host)
            line.text = translated_line
            print('\033[0;31m{origin_line}\033[0m => \033[0;32m{translated_line}\033[0m'.format(
                origin_line=temp, translated_line=line.text))
            print('Current:\033[0;33m {index} \033[0m || \033[0;34m {total} \033[0m' .format(
                index=index, total=total_lines))
        return sub_event

    def __translate_argos(self, sub_event: pysubs2.SSAEvent, from_language: str, to_language: str):
        """_summary_

        Args:
            sub_event (pysubs2.SSAEvent): pysubs2 object
            from_language (str): original language
            to_language (str): target language to translate

        Returns:
            sub_event: translated sub object
        """
        total_lines = len(sub_event)
        for index, line in enumerate(sub_event):
            if (self.__if_duration):
                time.sleep(self.__duration)
            temp = line.text
            translated_line = self.__tss.argos(query_text=line.text,
                                               from_language=from_language, to_language=to_language,
                                               if_ignore_empty_query=self.__if_ignore_empty_query,
                                               if_ignore_limit_of_length=self.__if_ignore_limit_of_length,
                                               if_use_cn_host=self.__if_use_cn_host)
            line.text = translated_line
            print('\033[0;31m{origin_line}\033[0m => \033[0;32m{translated_line}\033[0m'.format(
                origin_line=temp, translated_line=line.text))
            print('Current:\033[0;33m {index} \033[0m || \033[0;34m {total} \033[0m' .format(
                index=index, total=total_lines))
        return sub_event

    def __translate_bing(self, sub_event: pysubs2.SSAEvent, from_language: str, to_language: str):
        """_summary_

        Args:
            sub_event (pysubs2.SSAEvent): pysubs2 object
            from_language (str): original language
            to_language (str): target language to translate

        Returns:
            sub_event: translated sub object
        """
        total_lines = len(sub_event)
        for index, line in enumerate(sub_event):
            if (self.__if_duration):
                time.sleep(self.__duration)
            temp = line.text
            translated_line = self.__tss.bing(query_text=line.text,
                                              from_language=from_language, to_language=to_language,
                                              if_ignore_empty_query=self.__if_ignore_empty_query,
                                              if_ignore_limit_of_length=self.__if_ignore_limit_of_length,
                                              if_use_cn_host=self.__if_use_cn_host)
            line.text = translated_line
            print('\033[0;31m{origin_line}\033[0m => \033[0;32m{translated_line}\033[0m'.format(
                origin_line=temp, translated_line=line.text))
            print('Current:\033[0;33m {index} \033[0m || \033[0;34m {total} \033[0m' .format(
                index=index, total=total_lines))
        return sub_event

    def __translate_caiyun(self, sub_event: pysubs2.SSAEvent, from_language: str, to_language: str):
        """_summary_

        Args:
            sub_event (pysubs2.SSAEvent): pysubs2 object
            from_language (str): original language
            to_language (str): target language to translate

        Returns:
            sub_event: translated sub object
        """
        total_lines = len(sub_event)
        for index, line in enumerate(sub_event):
            if (self.__if_duration):
                time.sleep(self.__duration)
            temp = line.text
            translated_line = self.__tss.caiyun(query_text=line.text,
                                                from_language=from_language, to_language=to_language,
                                                if_ignore_empty_query=self.__if_ignore_empty_query,
                                                if_ignore_limit_of_length=self.__if_ignore_limit_of_length,
                                                if_use_cn_host=self.__if_use_cn_host)
            line.text = translated_line
            print('\033[0;31m{origin_line}\033[0m => \033[0;32m{translated_line}\033[0m'.format(
                origin_line=temp, translated_line=line.text))
            print('Current:\033[0;33m {index} \033[0m || \033[0;34m {total} \033[0m' .format(
                index=index, total=total_lines))
        return sub_event

    def __translate_lingvanex(self, sub_event: pysubs2.SSAEvent, from_language: str, to_language: str):
        """_summary_

        Args:
            sub_event (pysubs2.SSAEvent): pysubs2 object
            from_language (str): original language
            to_language (str): target language to translate

        Returns:
            sub_event: translated sub object
        """
        total_lines = len(sub_event)
        for index, line in enumerate(sub_event):
            if (self.__if_duration):
                time.sleep(self.__duration)
            temp = line.text
            translated_line = self.__tss.lingvanex(query_text=line.text,
                                                   from_language=from_language, to_language=to_language,
                                                   if_ignore_empty_query=self.__if_ignore_empty_query,
                                                   if_ignore_limit_of_length=self.__if_ignore_limit_of_length,
                                                   if_use_cn_host=self.__if_use_cn_host)
            line.text = translated_line
            print('\033[0;31m{origin_line}\033[0m => \033[0;32m{translated_line}\033[0m'.format(
                origin_line=temp, translated_line=line.text))
            print('Current:\033[0;33m {index} \033[0m || \033[0;34m {total} \033[0m' .format(
                index=index, total=total_lines))
        return sub_event

    def __translate_argos(self, sub_event: pysubs2.SSAEvent, from_language: str, to_language: str):
        """_summary_

        Args:
            sub_event (pysubs2.SSAEvent): pysubs2 object
            from_language (str): original language
            to_language (str): target language to translate

        Returns:
            sub_event: translated sub object
        """

        total_lines = len(sub_event)
        for index, line in enumerate(sub_event):
            if (self.__if_duration):
                time.sleep(self.__duration)
            temp = line.text
            translated_line = self.__tss.argos(query_text=line.text,
                                               from_language=from_language, to_language=to_language,
                                               if_ignore_empty_query=self.__if_ignore_empty_query,
                                               if_ignore_limit_of_length=self.__if_ignore_limit_of_length,
                                               if_use_cn_host=self.__if_use_cn_host)
            line.text = translated_line
            print('\033[0;31m{origin_line}\033[0m => \033[0;32m{translated_line}\033[0m'.format(
                origin_line=temp, translated_line=line.text))
            print('Current:\033[0;33m {index} \033[0m || \033[0;34m {total} \033[0m' .format(
                index=index, total=total_lines))
        return sub_event

    def __translate_baidu(self, sub_event: pysubs2.SSAEvent, from_language: str, to_language: str):
        """_summary_

        Args:
            sub_event (pysubs2.SSAEvent): pysubs2 object
            from_language (str): original language
            to_language (str): target language to translate

        Returns:
            sub_event: translated sub object
        """

        total_lines = len(sub_event)
        for index, line in enumerate(sub_event):
            if (self.__if_duration):
                time.sleep(self.__duration)
            temp = line.text
            translated_line = self.__tss.baidu(query_text=line.text,
                                               from_language=from_language, to_language=to_language,
                                               if_ignore_empty_query=self.__if_ignore_empty_query,
                                               if_ignore_limit_of_length=self.__if_ignore_limit_of_length,
                                               if_use_cn_host=self.__if_use_cn_host)
            line.text = translated_line
            print('\033[0;31m{origin_line}\033[0m => \033[0;32m{translated_line}\033[0m'.format(
                origin_line=temp, translated_line=line.text))
            print('Current:\033[0;33m {index} \033[0m || \033[0;34m {total} \033[0m' .format(
                index=index, total=total_lines))
        return sub_event

    def __write_sub(self, sub_event: pysubs2.SSAEvent, file_name: str):
        """_summary_

        Args:
            sub_event (pysubs2.SSAEvent): pysubs2 object
            file_name (str): the name used to save the translated subtitle file
        """
        sub_event.save(file_name)
        print('\033[4;32m File Saved as {name}\033[0m'.format(name=file_name))

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
            translated_sub = self.__translate_alibaba(
                sub_event=sub_event, from_language=from_language, to_language=to_language)
            self.__write_sub(sub_event=translated_sub, file_name=file_name)
        elif self.__server == 'google':
            sub_event = self.__get_sub(path=path)
            translated_sub = self.__translate_google(
                sub_event=sub_event, from_language=from_language, to_language=to_language)
            self.__write_sub(sub_event=translated_sub, file_name=file_name)
        elif self.__server == 'yandex':
            sub_event = self.__get_sub(path=path)
            translated_sub = self.__translate_yandex(
                sub_event=sub_event, from_language=from_language, to_language=to_language)
            self.__write_sub(sub_event=translated_sub, file_name=file_name)
        elif self.__server == 'bing':
            sub_event = self.__get_sub(path=path)
            translated_sub = self.__translate_bing(
                sub_event=sub_event, from_language=from_language, to_language=to_language)
            self.__write_sub(sub_event=translated_sub, file_name=file_name)

        elif self.__server == 'baidu':
            sub_event = self.__get_sub(path=path)
            translated_sub = self.__translate_baidu(
                sub_event=sub_event, from_language=from_language, to_language=to_language)
            self.__write_sub(sub_event=translated_sub, file_name=file_name)

        elif self.__server == 'caiyun':
            sub_event = self.__get_sub(path=path)
            translated_sub = self.__translate_caiyun(
                sub_event=sub_event, from_language=from_language, to_language=to_language)
            self.__write_sub(sub_event=translated_sub, file_name=file_name)
        elif self.__server == 'lingvanex':
            sub_event = self.__get_sub(path=path)
            translated_sub = self.__translate_lingvanex(
                sub_event=sub_event, from_language=from_language, to_language=to_language)
            self.__write_sub(sub_event=translated_sub, file_name=file_name)
        elif self.__server == 'argos':
            sub_event = self.__get_sub(path=path)
            translated_sub = self.__translate_argos(
                sub_event=sub_event, from_language=from_language, to_language=to_language)
            self.__write_sub(sub_event=translated_sub, file_name=file_name)
