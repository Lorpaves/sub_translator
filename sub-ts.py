import os
import pysubs2 as pysub
import translators.server as tss
import SubTranslator
import argparse
import sys
import re


class Wrapper:
    def __init__(self) -> None:
        self.__argv = sys.argv[1:]

        self.argv_parser = argparse.ArgumentParser(description="""\033[4;31m
                                                   
 Easy to use.

\033[0m
                                             """)
        self.argv_group_one = self.argv_parser.add_argument_group(
            '\033[4;31m advanced options \033[0m', '\033[0;33m advanced options of the translation \033[0m')
        self.argv_group_two = self.argv_parser.add_argument_group(
            '\033[4;31m multi files options \033[0m', '\033[0;33m multi files translate \033[0m')

        self.__parser()
        self.__wrapper()

    def __parser(self):
        self.argv_parser.add_argument('-i', '--input', dest='input file',
                                      action='store', type=str, nargs='+', help='\033[0;32m original file, ex: file1 file2 \033[0m', default=None)

        self.argv_group_two.add_argument('-D', '--directory', dest='input directory',
                                         action='store', nargs='+', help='\033[0;32m the server that send request to translate the text \033[0m', default=None)

        self.argv_group_one.add_argument('-s', '--server', dest='server',
                                         action='store', default='alibaba', help='\033[0;32m the server that send request to translate the text. Defaults to "alibaba" \033[0m')
        self.argv_group_one.add_argument('-f', '--from-language', dest='from language',
                                         action='store', default='en', help='\033[0;32m original language. Defaults to "en". \033[0m')
        self.argv_group_one.add_argument('-t', '--to-language', dest='to language',
                                         action='store', default='zh', help='\033[0;32m target language to translate. Defaults to "zh" \033[0m')
        self.argv_group_one.add_argument('-p', '--proxy', dest='proxy',
                                         action='store', help='\033[0;32m set proxy server of the requests \033[0m', default=None, type=str)
        self.argv_group_one.add_argument('-disable', '--disable-cn', dest='if use cn host',
                                         action='store_false', default=True, help='\033[0;32m disable local CN host. Defaults to use \033[0m')
        self.argv_group_one.add_argument('-e', '--ignore-empty', dest='if ignore empty query',
                                         action='store_true', default=False, help='\033[0;32m ignore the empty translate text. Defaults to not ignore \033[0m')
        self.argv_group_one.add_argument('-l', '--ignore-length', dest='if ignore limit of length',
                                         action='store_true', default=False, help='\033[0;32m ignore the limited length of the text in one time of translation. Defaults to not ignore \033[0m')
        self.argv_group_one.add_argument('-d', '--set-duration', dest='if duration',
                                         action='store_true', default=False, help='\033[0;32m set translate duration. Defaults to not set the duration \033[0m')
        self.argv_group_one.add_argument('-dt', '--duration-time', dest='duration',
                                         action='store', default=1, type=int, help='\033[0;32m set the translate time. Defaults to set the duration 1 second \033[0m')
        self.argv_parser.parse_args(
            args=self.__argv, namespace=self)

    def __wrapper(self):
        """_summary_
        Function: parse argument
        """
        self.namespace = {}
        for key, item in self.__dict__.items():
            if not '_' in key:
                self.namespace[key.replace(' ', '_')] = item
        self.namespace = {key: value for key,
                          value in self.namespace.items() if key != 'namespace'}


class utils:

    @staticmethod
    def get_files(files_array: list, **kwargs):
        """_summary_

        Args:
            files_array (list): single file's path in an array

        Returns:
            result(dict): original file path and saved path
        """
        pattern = re.compile('^.+\.+(srt|ass|sub|mpl2|tmp|vtt|ssa|microdvd)$')

        dirs = kwargs.get('dirs', None)
        to_language = kwargs.get('to_language', 'zh')
        result = {'origin': [], 'save': []}
        if files_array:
            result['origin'].extend(files_array)
            for file in files_array:
                index = file.rfind('.')
                result['save'].append(f'{file[:index]}-{to_language}.srt')
        if dirs != None:
            for directory in dirs:
                files = os.listdir(path=directory)
                result['origin'].extend(
                    [f'{directory}/{file}' for file in files if pattern.match(file)])
                # temp = []
                for file in files:
                    if pattern.match(file):
                        index = file.rfind('.')
                        result['save'].append(
                            f'{directory}/{file[:index]}-{to_language}.srt')

                # result['save'].extend(temp)
        print(result)
        return result

    @staticmethod
    def translate_files(original_file: list, translated_file: list, sub_ts, **kwargs):
        from_language = kwargs.get('from_language', 'en')
        to_language = kwargs.get('to_language', 'zh')
        for index, file in enumerate(original_file):
            sub_ts(path=file, file_name=translated_file[index],
                   from_language=from_language, to_language=to_language)


def main():
    a = Wrapper()
    kwargs = a.namespace
    sub = SubTranslator.SubTranslator(pysub=pysub, tss=tss, **kwargs)
    sub_ts = sub.translate_sub
    files = utils.get_files(files_array=kwargs.get(
        'input_file'), dirs=kwargs.get('input_directory'), **kwargs)
    utils.translate_files(
        original_file=files['origin'], translated_file=files['save'], sub_ts=sub_ts, **kwargs)


if __name__ == '__main__':
    main()
