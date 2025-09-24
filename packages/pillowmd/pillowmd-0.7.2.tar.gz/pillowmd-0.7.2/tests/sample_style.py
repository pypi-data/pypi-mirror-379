import pillowmd
import os
import time
from pathlib import Path

"""
切换style例
"""

def run():
    md = """# 一级标题
## 二级标题
### 三级标题

> 引用一级
>> 引用二级
>>> 引用三级
……

**加粗**~~删除线~~
[链接](http://baidu.com)

* 无序
* 列表

1. 有序
2. 列表

这是`行中代码`与$行中表达式：\\sin^2(\\pi)\\times\\cos^2(\\pi)$

|这|是|表|格|
|---|---|---|---|
|这是|表格里面的|元素|些|
|当然|可以|不止有一行|的元素|

```这是行中代码块
这是代码块里的内容
```

$$
这是行间latex表达式：\\sin^2(\\pi)\\times\\cos^2(\\pi)$
$$"""
    style = pillowmd.SampleStyles.STYLE1
    style.Render(md).image.show()

    t = time.time()

    for i in range(100):
        style.Render(md).image
    
    print("渲染100次耗时：", time.time() - t)