"""
encoding:   -*- coding: utf-8 -*-
@Time           :  2025/9/15 23:58
@Project_Name   :  FuyaoCountdown
@Author         :  lhw
@File_Name      :  countdown.py

功能描述

实现步骤

"""
import datetime
import time
from datetime import timedelta
import threading
from threading import Thread
from typing import Callable, Any
import inspect
from FuyaoCountdown import logger

TIME_FORMAT = "%Y-%m-%d %H:%M:%S"


def handleDateFormat(dt: str) -> tuple:
    """
    处理日期格式
    :param dt: 日期字符串
    :return: 年, 月, 日
    """
    dates = dt.split("-")
    if len(dates) < 3:
        raise ValueError("日期格式错误,正确: yyyy-mm-dd")

    if not dates[0] or not dates[1] or not dates[2]:
        raise ValueError("日期格式错误,检查年月日是否填写正确")

    return int(dates[0]), int(dates[1]), int(dates[2])


class Countdown:

    def __init__(
            self,
            date: datetime = datetime.datetime.now().date(),
            hour: int = 5,
            minute: int = 20,
            second: int = 0,
            nextTime: bool = True,
    ):
        """
        :param date: 日期
        :param hour: 小时
        :param minute: 分钟
        :param second: 秒
        :param nextTime: 当前目标时间到达后是否执行到下一个目标时间
        """

        # 检查date类型是否为str,为str放行,否则更改为str
        date = str(date) if type(date) is not str else date

        year, month, day = handleDateFormat(date)

        self.target = datetime.datetime(year, month, day, hour, minute, second)

        # logger.info(self.target)

        self.date = date
        self.hour = self.target.hour
        self.minute = self.target.minute
        self.second = self.target.second

        self.nextTime = nextTime

    def execJob(
            self,
            job: Callable[..., Any],
            *args
    ):
        """
        执行任务
        :param job: 任务函数
        :param args: 函数的参数
        :return:
        """

        logger.info("===定时任务已经启动===")

        logger.info(f"目标时间: {self.target}; 任务启动时间: {datetime.datetime.now().strftime(TIME_FORMAT)}")

        jobSig = inspect.signature(job)
        jobParams = jobSig.parameters

        while True:

            now = datetime.datetime.now()

            if now > self.target:
                if not self.nextTime:
                    logger.info("不执行到下一个的目标时间...")
                    break
                self.target += timedelta(days=1)
                logger.info(f"当前时间超过目标时间 ==> 目标天数已经更改: {self.target}")
                continue

            diff = self.target - now
            secondCount = int(diff.total_seconds())

            if secondCount <= 0:
                print(f"目标时间已到达: {self.target}")
                logger.info("===开始执行任务===")

                startTime = time.time()

                if len(jobParams) > 0:
                    job(*args)
                else:
                    job()

                endTime = time.time()

                logger.info(f"{job.__name__}执行完毕, 耗时:{endTime - startTime}")

            # 格式化显示倒计时
            hours, remainder = divmod(secondCount, 3600)
            minutes, seconds = divmod(remainder, 60)

            print(f"\r距离目标时间还有: {hours:02d}:{minutes:02d}:{seconds:02d}", end="", flush=True)

            # 每秒检查一次
            time.sleep(1)

    def threadExecutor(
            self,
            useTread: bool = True,
            job: Callable[..., Any] = None,
            jobArgs: tuple = (),
            *args,
            **kwargs,
    ):
        """
        使用线程执行任务
        :param useTread: 是否新开线程
        :param job: 被执行的任务函数
        :param jobArgs: 任务函数的参数
        :param args: 当前函数的参数
        :param kwargs:
        :return:
        """

        if useTread:
            logger.info("使用新线程执行任务,当前线程可执行其他任务")
            thread = Thread(
                target=self.execJob,
                name="FuyaoCountdown-0",
                args=(job,) + jobArgs,
                daemon=False,
            )

            thread.start()

            logger.info(f"目标任务已经在新线程中执行: {thread.name}")

            # thread.join()

            return thread

        else:
            logger.info(f"目标任务在当前线程执行: {threading.main_thread().name}")
            self.execJob(job, jobArgs)

            return None
