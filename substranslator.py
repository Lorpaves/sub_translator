# -*- coding: utf-8 -*-

from copy import deepcopy
import pysubs2 as sub2
import os
import translators as ts


# get the sub information

#虽然这个方法更快，但是原文和翻译后的文本句子长度对不上，没办法一一对应字幕时间，所以放弃这个方法。
# def get_sub_info(sub_events):

#     """
#     get the sub information 
#     return: 
#         sub_texts: all sentences of sub
#         nums: the numbers of which line each sentence at 
#     """
#     lines = []
#     texts = []
#     string = ''
#     nums = []
#     _index = []
#     for index, text in enumerate(sub_events):
#         lines.append(text.text)
#         if text.text.endswith('.') or text.text.endswith('?'):
#             string += f' {"".join(text.text)}'  
#             texts.append(string)
#             _index.append(index)
#             nums.append(_index)
#             _index = []
#             string = ''
#         else:
#             string += f' {"".join({text.text})}'
#             _index.append(index)
#     return ''.join(texts), nums, lines

#main translation function

def get_sub_text(sub_event):
    return [line.text for line in sub_event]

def get_translated_content(sub_event, src_lang='en',target_lang='Zh-CN'):

    sub_content = get_sub_text(sub_event)
    translated_content = []
    for line in sub_content:
        translated_text = ts.google(query_text=line,from_language=src_lang,to_language=target_lang)
        time.sleep(1)   #避免频繁请求出现ssl错误。 如果出现ssl请求错误，调整这里的访问延迟
        print(translated_text)
        translated_content.append(translated_text)
    return [line for line in translated_content if line]
import time
def trans_subs(sub_event, src_lang='en',target_lang='Zh-CN'):
    modifited_srt = sub_event.to_string('srt')
    result = get_translated_content(sub_event,src_lang=src_lang,target_lang=target_lang)
    source_content = get_sub_text(sub_event)
    translated_content = deepcopy(modifited_srt)
    for index, line in enumerate(result):
        translated_content = translated_content.replace(source_content[index], line)
    return translated_content   #return translated content as a srt formated string.
                                #返回字幕格式的字符串

#save the translated subtitle file
#保存翻译好的字幕文件
def save_subs(save_path, sub_string):
    modified_subs = sub2.SSAFile.from_string(sub_string)
    modified_subs.save(save_path)

#get the sub files paths
#获取文件路径
def get_path(file_path, source_exten:str):
    
    '''
    目前只测试过翻译srt格式的字幕文件，翻译后保存的格式为ass

    '''
    """ 
    parameter:
        file_path: 
            main directory contains all subtitle files  字幕文件所在的文件夹的绝对路径
        source_exten:
            source file extension   字幕文件的拓展名：比如.srt/.ass/。。。
    
    return: 
        tuple: (files_path, files_name)
            files_path: 
                all source subtitle files path
            files_name:
                path of where to save each file
        
    """
    roots = []
    dirs = []
    files = []
    for root, dir_, file in os.walk(file_path):
        roots.append(root)
        dirs.append(dir_)
        files.append(file)
    files_copy = []
    roots_copy = []
    #将只有文件的文件夹储存在roots_copy里，其中文件夹对应的文件储存在files_copy里
    for index, file in enumerate(files):
        if len(file):
            files_copy.append(file)
            roots_copy.append(roots[index])

    files_path = []
    files_name = []
    for index, root in enumerate(roots_copy):
        files_path.extend(root + '\\' + file for file in files_copy[index] if source_exten in file)
        files_name.extend(root + '\\' + file.replace(source_exten,'.ass') for file in files_copy[index] if source_exten in file) #保存字幕文件为ass格式文件，避免出现信息丢失。
    return files_path, files_name


if __name__ == '__main__':
    #需要修改的参数： [path] [sub_string](src_lang, target_lang)
    path = 'path to subtitle files => directory'    #字幕文件所在文件夹的绝对路径
    files_paths, save_paths = get_path(path,source_exten='.srt')    #source_exten: 文件拓展名 
    
    for index, file_path in enumerate(files_paths):
        subs_event = sub2.load(file_path)

        #src_lang为原文本的语言，target_lang为要翻译成的语言
        sub_strings = trans_subs(subs_event, src_lang='en',target_lang='Zh-CN')
        save_subs(save_paths[index], sub_strings)
        print(f'{file_path}\n translation done')
    print('all translations were done')
