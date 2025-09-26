# 本项目可以将latex公式转换成中文
使用:
```
from latex_to_zh import convert
text = r'\begin{cases} x + y = 5 \\ x - y = 3 \\ x - y = 3 \end{cases}'
result = convert(text)
print(result)
```
目前支持的公式比较少
欢迎提交需要支持的公式
