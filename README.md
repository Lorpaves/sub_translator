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
if_duration (bool: Default False) if need to set translate duration, set this to True
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
