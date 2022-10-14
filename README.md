# sub_translator
简单的字幕翻译工具

# 安装
```shell
git clone https://github.com/Lorpaves/sub_translator.git

cd sub_translator

pip install -r requirements.txt

```
# 使用示例
打开substranslator.py文件，修改参数
```python
path = 'path_to_subtitle_files'    #字幕文件所在文件夹的绝对路径
files_paths, save_paths = get_path(path)
for index, file_path in enumerate(files_paths):
    subs_event = sub2.load(file_path)
    sub_strings = trans_subs(subs_event, src_lang='en',target_lang='Zh-CN') #src_lang为原文本的语言，target_lang为要翻译成的语言
    save_subs(save_paths[index], sub_strings)
    print(f'{file_path}\n translation done')
print('all translation were done')
```
