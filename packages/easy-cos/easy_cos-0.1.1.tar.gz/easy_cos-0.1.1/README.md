# easy_cos

让数据流动变得简单！Make data flow!
```bash
pip install easy_cos==0.1.0 --index-url https://pypi.tuna.tsinghua.edu.cn/simple
#
pip install easy_cos==0.1.0 --index-url https://pypi.org/simple  #清华等其他镜像源可能同步慢
```


这个库的开发是包含了大部分常用的 tos脚本操作，避免许多重复代码。以及让很多新入职的同事能够快速用起来我们的数据。


```python
COS_CONFIG = {
    'secret_id': f'{os.environ["COS_SECRET_ID"]}',
    'secret_key': f'{os.environ["COS_SECRET_KEY"]}',
    'region': f'{os.environ["COS_REGION"]}',
}
```
<br>
<br>
<br>