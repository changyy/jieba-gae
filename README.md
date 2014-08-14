Init
=========
```
$ git clone --recursive https://github.com/changyy/jieba-gae.git
$ mkdir -p jieba-gae/tmp
$ python jieba-gae/init_jieba_at_console.py 
Building Trie..., from /path/jieba-gae/jieba/jieba/dict.txt
dumping model to file cache /path/jieba-gae/tmp/jieba.cache
loading model cost 3.25067281723 seconds.
Trie has been built succesfully.
Full Mode: 我/ 来到/ 北京/ 清华/ 清华大学/ 华大/ 大学
Default Mode: 我/ 来到/ 北京/ 清华大学
他, 来到, 了, 网易, 杭研, 大厦
小明, 硕士, 毕业, 于, 中国, 科学, 学院, 科学院, 中国科学院, 计算, 计算所, ，, 后, 在, 日本, 京都, 大学, 日本京都大学, 深造
```

Google App Engines - Localhsot API Usage:
=========
```
$ wget -qO- http://localhost:port/                                                                
{"status": false}

$ wget -qO- --post-data "in=我来到北京清华大学" http://localhost:port/ | python -mjson.tool
{
    "out": [
        "\u6211",
        "\u6765\u5230",
        "\u5317\u4eac",
        "\u6e05\u534e",
        "\u6e05\u534e\u5927\u5b66",
        "\u534e\u5927",
        "\u5927\u5b66"
    ],
    "status": true
}
```

Google App Engines online default instance:
=========

- Building Trie..., from /base/data/home/apps/s~project/##############/jieba/jieba/dict.txt
- Exceeded soft private memory limit of 128 MB with 157 MB after servicing 0 requests total
- This request caused a new process to be started for your application, and thus caused your application code to be loaded for the first time. This request may thus take longer and use more CPU than a typical request for your application.
- While handling this request, the process that handled this request was found to be using too much memory and was terminated. This is likely to cause a new process to be used for the next request to your application. If you see this message frequently, you may have a memory leak in your application.

Google App Engines Limits
=========
- https://developers.google.com/appengine/docs/python/backends/#Python_Properties_of_backends
- https://developers.google.com/appengine/docs/python/config/backends#Python_Instance_classes
