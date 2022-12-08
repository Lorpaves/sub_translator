# 字幕翻译工具

### 安装

```shell
git clone https://github.com/Lorpaves/sub_translator.git

cd sub_translator

pip install -r requirements.txt

```

### 使用示例

```python
import pysubs2 as pysub
import translators.server as tss
import SubTranslator

sub_ts = SubTranslator.SubTranslator(pysub=pysub, tss=tss)
sub_ts.translate_sub(path='./test.srt', file_name = './save.srt',
                     from_language='en', to_language='zh')

```

### 参数说明

```python
SubTranslator
if_duration (bool: Default False) # if need to set translate duration, set this to True
duration (int) # duration
if_ignore_empty_query (bool: Default True) # if the text was empty, set True to ignore the text, else will throw error
if_ignore_limit_of_length (bool: Default True)  # Default limited length is 1500, set to True to ignore the error
if_use_cn_host (bool: Default True)  # use cn host or not
server (str: Default "alibaba") # the server that send request to in order to translate the text

SubTranslator.translate_sub
path (string): #path of the subtitle file
file_name (str): # the name used to save the translated subtitle file
from_language (str): # original language
to_language (str): # target language to translate
```

### 命令行参数说明

```shell
options:
  -h, --help            show this help message and exit
  -i INPUT FILE [INPUT FILE ...], --input INPUT FILE [INPUT FILE ...]
                         the server that send request to translate the text
  -o OUTPUT DIRECTORY, --output OUTPUT DIRECTORY
                         the server that send request to translate the text

 advanced options :
   advanced options of the translation

  -s SERVER, --server SERVER
                         the server that send request to translate the text. Defaults to "alibaba"
  -f FROM LANGUAGE, --from-language FROM LANGUAGE
                         original language. Defaults to "en".
  -t TO LANGUAGE, --to-language TO LANGUAGE
                         target language to translate. Defaults to "zh"
  -p PROXY, --proxy PROXY
                         set proxy server of the requests
  -disable, --disable-cn
                         disable local CN host. Defaults to use
  -e, --ignore-empty     ignore the empty translate text. Defaults to not ignore
  -l, --ignore-length    ignore the limited length of the text in one time of translation. Defaults to not
                        ignore
  -d, --set-duration     set translate duration. Defaults to not set the duration
  -dt DURATION, --duration-time DURATION
                         set the translate time. Defaults to set the duration 1 second

 multi files options :
   multi files translate

  -D INPUT DIRECTORY [INPUT DIRECTORY ...], --directory INPUT DIRECTORY [INPUT DIRECTORY ...]

```
