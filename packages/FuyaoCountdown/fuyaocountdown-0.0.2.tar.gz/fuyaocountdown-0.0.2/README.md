# Countdown
python第三方库，实现到达目标时间执行函数

# 安装
``pip isntall FuyaoCountdown``

# 使用
```python
from FuyaoCountdown.countdown import Countdown


def job():
    print("job is running")


if __name__ == '__main__':
    cd = Countdown("2025-09-16", 5, 20)

    cd.threadExecutor(True, job)


```

## 参数说明
```text

Countdown(
    date: str 日期,如 "2025-09-16",
    hour: int 小时,如 5
    minute: int 分钟,如 20
    second: int 秒,如 0
    nextTime: bool 当前目标时间到达后是否继续进行倒计时任务(明天的目标时间)
)

Countdown.threadExecutor(
    useThread: bool 是否启用新线程
    job: Callable[..., Any]  可调用的任意对象/函数(任务对象)
    jobArgs: tuple  任务对象所需的参数
)

```


# 项目结构
```text
Countdown  项目名
    src  源代码
        FuyaoCountdown  软件包
    pyproject.toml  打包信息
    README.md  说明文件
    


```


# 更新日志

## v0.0.1
1.支持新线程执行任务

## v0.0.2
修复bug：
1.修复函数传参少的问题
2.修复传入datetime.date类型数据无法解析的问题
3.修复控制台输出不换行的问题

更新：
1.添加对执行到下一个目标时间的可选参数
