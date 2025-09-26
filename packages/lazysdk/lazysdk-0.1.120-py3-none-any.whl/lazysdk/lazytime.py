#!/usr/bin/env python3
# coding = utf8
"""
@ Author : ZeroSeeker
@ e-mail : zeroseeker@foxmail.com
@ GitHub : https://github.com/ZeroSeeker
@ Gitee : https://gitee.com/ZeroSeeker
"""
import requests
import datetime
import pytz
import time
import copy
import sys
import re


def get_datetime_from_str(
        string: str
):
    """
    从字符串中识别出时间
    目前这个模块还不完备
    """
    findres = dict()
    find_datetime = re.findall(pattern=r'(\d\d\d\d-[0-1]\d-[0-3]\d [0-2]\d:[0-5]\d:[0-5]\d)', string=string)
    findres['datetime'] = find_datetime
    find_time = re.findall(pattern=r'([0-2]\d:[0-5]\d:[0-5]\d)', string=string)
    findres['time'] = find_time
    return findres


def get_utc_datetime(
        f: str = '%Y-%m-%dT%H:%M:%SZ'
):
    """
    获取utc时间
    """
    utc_datetime_str = datetime.datetime.utcnow().strftime(f)
    return utc_datetime_str


def get_utc_timestamp():
    """
    获取utc时间的时间戳
    """
    utc_timestamp_str = datetime.datetime.utcnow().timestamp()
    return utc_timestamp_str


def get_utc_time_dict(
        f: str = '%Y-%m-%dT%H:%M:%SZ'
):
    """
    获取utc时间的时间和时间戳字典
    """
    utc_time_now = datetime.datetime.utcnow()
    utc_datetime_str = utc_time_now.strftime(f)
    utc_timestamp_str = utc_time_now.timestamp()
    return {'utc_datetime_str': utc_datetime_str, 'utc_timestamp_str': utc_timestamp_str}


def get_year(
        date_input: str = None,  # 输入日期
        date_delimiter: str = "-"  # 日期分隔符
):
    """
    获取当前系统的当前时间：年份
    :return: 2018
    """
    if date_input is None:
        year = datetime.datetime.now().year
    else:
        a1 = date_input.find(date_delimiter, 0)
        year = int(date_input[0:a1])
    return year


def get_month(
        date_input: str = None,  # 输入日期
        date_delimiter: str = "-"  # 日期分隔符
):
    """
    获取当前系统的当前时间：月份
    :return: 8
    """
    if date_input is None:
        month = datetime.datetime.now().month
    else:
        date = str(date_input)
        a1 = date.find(date_delimiter, 0)
        a2 = date.find(date_delimiter, a1 + 1)
        month = int(date[a1 + 1:a2])
    return month


def get_day(
        date_input: str = None,  # 输入日期
        date_delimiter: str = "-"  # 日期分隔符
):
    """
    获取当前系统的当前时间：日数
    :return: 1
    """
    if date_input is None:
        day = datetime.datetime.now().day
    else:
        date = str(date_input)
        a1 = date.find(date_delimiter, 0)
        a2 = date.find(date_delimiter, a1 + 1)
        day = int(date[a2 + 1:len(date)])
    return day


def get_hour(
        target=None
) -> int:
    """
    获取当前系统的当前时间：小时数（24小时制）
    :return: 14
    """
    if not target:
        return datetime.datetime.now().hour
    else:
        if isinstance(target, datetime.datetime):
            return target.hour
        elif isinstance(target, str):
            get_res = get_datetime_from_str(string=target)
            if get_res.get("time"):
                return int(get_res.get("time")[0].split(':')[0])
        else:
            return -1


def get_minute():
    """
    获取当前系统的当前时间：分钟数
    :return: 28
    """
    minute = datetime.datetime.now().minute
    return minute


def get_second():
    """
    获取当前系统的当前时间：秒数
    :return: 23
    """
    second = datetime.datetime.now().second
    return second


def get_time(
        f: str = '%H:%M:%S'
):
    """
    获取当前系统的当前时间格式的时间，精确到秒且只有时间
    :return: 14:20:41
    """
    inner_now = datetime.datetime.now()
    data_time = inner_now.strftime(f)
    return data_time


def get_datetime(
        f: str = '%Y-%m-%d %H:%M:%S',
        utc: bool = False
):
    """
    获取当前系统的当前时间格式的时间，精确到秒
    :return: 2018-08-01 14:18:31
    """
    if utc:
        inner_now = datetime.datetime.now(pytz.utc)
    else:
        inner_now = datetime.datetime.now()
    data_time = inner_now.strftime(f)
    return data_time


def get_datetime_full():
    """
    获取当前系统的当前时间格式的时间，精确度最高
    :return: 2018-08-01 14:16:50.611705
    """
    inner_now = datetime.datetime.now()
    return inner_now


def get_datetime_str_int(
        f: str = '%Y%m%d%H%M%S'
):
    """
    获取当前系统的当前时间格式的时间，精确到秒
    :return: 20180801141831
    """
    inner_now = datetime.datetime.now()
    data_time = inner_now.strftime(f)
    return data_time


def get_relative_date(
        num: int = 0
):
    """
    获取当前系统当前时间的相对时间：日期，num为0表示当日，num为负数表示向历史推算的天数，num为正数表示向未来推算的天数
    :param num:
    :return: 2018-08-01
    """
    today = datetime.date.today()
    date = today - datetime.timedelta(days=-num)
    return date


def get_relative_datetime(
        num: int = 0,
        f: str = '%Y-%m-%d %H:%M:%S'
):
    """
    【计划弃用】
    获取当前系统当前时间的相对时间：日期，num为0表示当日，num为负数表示向历史推算的天数，num为正数表示向未来推算的天数
    :param num:
    :param f: 格式
    :return: 2021-04-23 17:23:27
    """
    today = datetime.datetime.now()
    date = today - datetime.timedelta(days=-num)
    return date.strftime(f)


def get_datetime_relative(
        days: int = 0,
        f: str = '%Y-%m-%d %H:%M:%S'
) -> str:
    """
    获取当前系统当前时间的相对时间

    :param days: 0表示当日，num为负数表示向历史推算的天数，num为正数表示向未来推算的天数
    :param f: 格式
    :return: 形如 2022-06-07 12:16:52 的字符串
    """
    target_date = datetime.datetime.now() - datetime.timedelta(days=-days)
    return target_date.strftime(f)


def get_datetime_relative_min(
        days: int = 0,
        f: str = '%Y-%m-%d %H:%M:%S'
) -> str:
    """
    获取当前系统当前时间的相对时间 的一天的 开始时间，例如：2022-06-07 00:00:00

    :param days: 0表示当日，num为负数表示向历史推算的天数，num为正数表示向未来推算的天数
    :param f: 格式
    :return: 形如 2022-06-07 00:00:00 的字符串
    """
    target_date = datetime.date.today() - datetime.timedelta(days=-days)
    return datetime.datetime.combine(
        date=target_date,
        time=datetime.time.min
    ).strftime(f)


def get_datetime_relative_max(
        days: int = 0,
        f: str = '%Y-%m-%d %H:%M:%S'
) -> str:
    """
    获取当前系统当前时间的相对时间 的一天的 结束时间，例如：2022-06-07 23:59:59

    :param days: 0表示当日，num为负数表示向历史推算的天数，num为正数表示向未来推算的天数
    :param f: 格式
    :return: 形如 2022-06-07 23:59:59 的字符串
    """
    target_date = datetime.date.today() - datetime.timedelta(days=-days)
    return datetime.datetime.combine(
        date=target_date,
        time=datetime.time.max
    ).strftime(f)


def get_timestamp():
    """
    获取当前系统的当前时间戳格式的时间，返回的类型为int
    :return: 1533104393
    """
    inner_now = time.time()
    return int(inner_now)


def get_timestamp2datetime(
        timestamp: int = None,
        f: str = "%Y-%m-%d %H:%M:%S",
        zero_to_none: bool = True,
        utc: bool = False
):
    """
    将时间戳转换为datetime时间
    :param timestamp: 同时支持字符串和数字格式
    :param f:
    :param zero_to_none: 将0转换为空值
    :param utc: 是否为utc时间
    :return: 2018-08-01 14:19:53
    """
    if timestamp is not None:
        if timestamp == 0 and zero_to_none is True:
            return
        else:
            if utc:
                time_array = time.gmtime(timestamp)
            else:
                time_array = time.localtime(timestamp)

            date_time = time.strftime(f, time_array)
            return date_time
    else:
        return


def get_timestamp2date(
        timestamp: int = None,
        f: str = "%Y-%m-%d",
        zero_to_none: bool = True,
        utc: bool = False
):
    """
    将时间戳转换为datetime时间
    默认将输入转换为int
    :param timestamp:
    :param f:
    :param zero_to_none: 将0转换为空值
    :param utc: 是否为utc时间
    :return: 2018-08-01 14:19:53
    """
    if timestamp is not None:
        if timestamp == 0 and zero_to_none is True:
            return
        else:
            if utc:
                time_array = time.gmtime(timestamp)
            else:
                time_array = time.localtime(timestamp)
            date_time = time.strftime(f, time_array)
            return date_time
    else:
        return


def get_date2timestamp(
        date: str,
        f: str = "%Y-%m-%d"
):
    """
    将日期转换为对应日期的0点的时间戳
    :param date:
    :param f:
    :return: 1533052800
    """
    time_array = time.strptime(date, f)
    timestamp = int(time.mktime(time_array))
    return timestamp


def get_datetime2timestamp(
        data: str,
        f: str = "%Y-%m-%d %H:%M:%S"
):
    time_array = time.strptime(data, f)
    timestamp = int(time.mktime(time_array))
    return timestamp


def get_datetime2date(
        datetime_str,
        f: str = '%Y-%m-%d'
) -> str:
    """
    datetime->date
    """
    temp = copy.deepcopy(datetime_str)  # 复制一份防止发生更改
    if isinstance(temp, str):
        datetime_timestamp = get_datetime2timestamp(temp)
        date_str = get_timestamp2date(datetime_timestamp)
        return date_str
    elif isinstance(temp, datetime.datetime):
        return temp.strftime(f)
    else:
        return temp


def timestamp_day_num_start(
        num: int = 0
):
    """
    换算出相对时间的当日开始时间的时间戳
    :param num:
    :return: 1533052800（2018-08-01 00:00:00）
    """
    inner = get_relative_date(num=num)
    return get_date2timestamp(str(inner))


def timestamp_day_num_end(
        num: int = 0
):
    """
    换算出相对时间的当日结束时间的时间戳
    :param num:
    :return: 1533139199（2018-08-01 23:59:59）
    """
    inner = get_relative_date(num=num+1)
    return get_date2timestamp(str(inner))-1


def get_format_date(
        date_ori: str,
        date_delimiter: str = '-',  # 日期分隔符号
):
    """
    将以'-'连接的字符串的日期格式化为日期格式
    :param date_ori:
    :param date_delimiter:
    :return: 2018-01-01
    """
    a1 = date_ori.find(date_delimiter, 0)
    a2 = date_ori.find(date_delimiter, a1+1)
    year = int(date_ori[0:a1])
    month = int(date_ori[a1+1:a2])
    day = int(date_ori[a2+1:len(date_ori)])
    format_date = datetime.date(year, month, day)
    return format_date


def get_format_date_2(
        date_ori: str
):
    """
    将以的字符串的日期格式化为日期格式:20200602
    按照位置分
    :param date_ori:
    :return: 2018-01-01
    """
    year = int(date_ori[0:4])
    month = int(date_ori[4:6])
    day = int(date_ori[6:8])
    format_date = datetime.date(year, month, day)
    return format_date


def get_format_datetime(
        datetime_ori: str,
        date_delimiter: str = '-',  # 日期分隔符号
        space_delimiter: str = " ",  # 空格分隔符号
        time_delimiter: str = ':'  # 时间分隔符号
):
    """
    将以'-'连接的字符串的日期格式化为日期格式
    :param datetime_ori:
    :param date_delimiter: 日期分隔符号
    :param space_delimiter: 空格分隔符号
    :param time_delimiter: 时间分隔符号
    :return: 2018-01-01
    """
    date_str, time_str = datetime_ori.split(space_delimiter)

    date_str = str(date_str)
    d1 = date_str.find(date_delimiter, 0)
    d2 = date_str.find(date_delimiter, d1+1)
    year_num = int(date_str[0:d1])
    month_num = int(date_str[d1+1:d2])
    day_num = int(date_str[d2+1:len(date_str)])

    time_str = str(time_str)
    t1 = time_str.find(time_delimiter, 0)
    t2 = time_str.find(time_delimiter, t1 + 1)
    hour_num = int(time_str[0:t1])
    minute_num = int(time_str[t1 + 1:t2])
    second_num = int(time_str[t2 + 1:len(time_str)])

    format_date = datetime.datetime(year_num, month_num, day_num, hour_num, minute_num, second_num)
    return format_date


def time_gap_seconds(
        start_time: str,
        end_time: str
):
    """
    计算两个时间的间隔秒数
    :param start_time:
    :param end_time:
    :return:
    """
    start_time_f = get_format_datetime(start_time)
    end_time_f = get_format_datetime(end_time)
    return (end_time_f - start_time_f).seconds


def time_gap_days(
        start_time: str,
        end_time: str
):
    """
    计算两个时间的间隔天数
    :param start_time:
    :param end_time:
    :return:
    """
    start_time_f = get_format_date(start_time)
    end_time_f = get_format_date(end_time)
    return (end_time_f - start_time_f).days


def get_add_date(
        date_input,
        num: int = 0,
        f: str = '%Y-%m-%d'
):
    """
    计算指定日期（date_ori）的相对日期
    :param date_input: 输入的指定日期，类型支持str、datetime.date，例如：2022-01-01
    :param num: 偏移天数，-1表示向过去偏移一天，1表示向未来偏移1天，0表示当天，默认值为0
    :param f: 输出时间格式
    :return: 2018-01-02
    """
    if isinstance(date_input, str):
        date = get_format_date(date_input)
    elif isinstance(date_input, datetime.date):
        date = date_input
    else:
        return
    delta = datetime.timedelta(days=num)
    n_days = date + delta
    date_add = n_days.strftime(f)
    return date_add


def get_timestamp_interval_seconds(
        timestamp: int
):
    """
    计算指定时间戳距离当前系统的当前时间的秒数，正数表示未来时间，负数表示过去时间
    :param timestamp:
    :return: 30830
    """
    inner_now = time.time()
    res = timestamp - int(inner_now)
    return res


def count_down(
        num: int
):
    """
    倒数计时器，按照指定的秒数原地倒计时刷新数字
    :param num:
    :return:
    """
    count = 0
    while count < num:
        n_count = num - count
        sys.stdout.write("\r%d " % n_count)
        sys.stdout.flush()
        time.sleep(1)
        count += 1


def running_controller(
        start_running_time: str,
        end_running_time: str,
        start_running_time_f: str = '%H:%M:%S',
        end_running_time_f: str = '%H:%M:%S'
):
    """
    判断系统时间是否落在设定的时间区间内，是则输出True，否则输出False
    :param start_running_time:
    :param end_running_time:
    :param start_running_time_f:
    :param end_running_time_f:
    :return:
    """
    if (start_running_time is None) and (end_running_time is None):
        return True
    else:
        inner_now = datetime.datetime.strptime(str(get_time()), "%H:%M:%S")
        inner_start = datetime.datetime.strptime(start_running_time, start_running_time_f)
        inner_end = datetime.datetime.strptime(end_running_time, end_running_time_f)

        if (inner_now >= inner_start) and (inner_now < inner_end):
            return True
        else:
            return False


def now():
    inner_now = datetime.datetime.now()
    return inner_now


def date_string(
        date=now(),
        f: str = '%Y-%m-%d'
):
    """
    将输入的时间转换为日期格式的字符串，如果不传入参数将取当前系统时间
    :param date:
    :return:
    """
    date_string_in = date.strftime(f)
    return date_string_in


def time_string(
        date=now(),
        f: str = '%Y-%m-%d %H-%M-%S'
):
    time_string_in = date.strftime(f)
    return time_string_in


def datetime_string(
        date=now(),
        f: str = '%Y-%m-%d %H-%M-%S'
):
    time_string_in = date.strftime(f)
    return time_string_in


def datetime_string_chs(
        date=now(),
        f: str = '%Y年%m月%d日%H时%M分%S秒'
):
    time_string_in = date.strftime(f)
    return time_string_in


def date_str_list(
        start_date: str = None,
        end_date: str = None,
        start_days: int = None,
        end_days: int = None
):
    # 生成起止时间之间的时间序列
    current_day = datetime.date.today()

    if start_date:
        start_date_f = get_format_date(start_date)
    elif start_days:
        start_date_f = current_day + datetime.timedelta(days=start_days)
    else:
        start_date_f = current_day

    if end_date:
        end_date_f = get_format_date(end_date)
    elif end_days:
        end_date_f = current_day + datetime.timedelta(days=end_days)
    else:
        end_date_f = current_day
    # print(start_date_f, '-->', end_date_f)
    date_list = list()
    date_list.append(str(start_date_f))
    added_date = start_date_f
    while True:
        added_date = get_add_date(added_date, 1)
        added_date_f = get_format_date(added_date)
        if added_date_f > end_date_f:
            break
        else:
            date_list.append(str(added_date))
    return date_list


def get_date_list(
        start_date: str = None,
        end_date: str = None,
        start_days: int = None,
        end_days: int = None
):
    return date_str_list(
        start_date=start_date,
        end_date=end_date,
        start_days=start_days,
        end_days=end_days
    )


def date_str_list_form_now(
        day_num: int = 1
):
    start_date = get_add_date(date_string(), -day_num)
    end_date = date_string()
    res_list = date_str_list(
        start_date=start_date,
        end_date=end_date
    )
    return res_list


def get_normalized_date_string(
        days: int = 0,
        f: str = '%Y-%m-%d %H:%M:%S'
):
    """
    获取多少天以前的时间字符串
    :param days: 多少天以前
    :return: 时间字符串(xxxx-xx-xx xx:xx:xx)
    """
    current_time = datetime.datetime.now()
    target_time = current_time - datetime.timedelta(days=days)
    normalized_target_time = target_time.strftime(f)
    return normalized_target_time


def get_data_date_string(
        days: int = 0,
        f: str = '%Y-%m-%d'
):
    """
    获取多少天以前的时间字符串
    :param days: 多少天以前
    :return: 时间字符串(xxxx-xx-xx)
    """
    current_time = datetime.datetime.now()
    target_time = current_time - datetime.timedelta(days=days)
    date_time = target_time.strftime(f)
    return date_time


def get_date_string(
        days: int = 0,
        f: str = '%Y-%m-%d',
        utc: bool = False
):
    """
    获取多少天以后的时间字符串
    :param days: 多少天以后，正数向未来计算，负数向历史计算，0是当天
    :param f:
    :param utc:
    :return: 时间字符串(xxxx-xx-xx)
    """
    if utc:
        current_time = datetime.datetime.now(tz=pytz.utc)
    else:
        current_time = datetime.datetime.now()
    target_time = current_time + datetime.timedelta(days=days)
    date_str = target_time.strftime(f)
    return date_str


def time_day_num_start(
        num: int = 0
):
    """
    换算出相对时间的当日开始时间的时间
    :param num:
    :return: 2018-08-01 00:00:00
    """
    now = datetime.datetime.now()
    return now - datetime.timedelta(
        days=num,
        hours=now.hour,
        minutes=now.minute,
        seconds=now.second,
        microseconds=now.microsecond
    )


def time_day_num_end(
        num: int = 0
):
    """
    换算出相对时间的当日结束时间的时间
    :param num:
    :return: 2018-08-01 23:59:59
    """
    now = datetime.datetime.now()
    return now - datetime.timedelta(
        days=num - 1,
        hours=now.hour,
        minutes=now.minute,
        seconds=now.second + 1,
        microseconds=now.microsecond
    )


def timestamp_list_splitter(
        timestamp_list: list,
        n: int = 2
):
    # 时间戳范围拆分器
    """
    输入timestamp_list：[[start,end]]，splitter_num：2
    执行将list中的每段时间按照设定的份数拆分，拆分为粗略拆分，

    :return:
    """
    t_list_new = list()
    for each_t_list in timestamp_list:
        a = each_t_list[0]  # 获取开始时间戳
        b = each_t_list[1]  # 获取结束时间戳
        if (b - a) > 1:  # 当数字间隔大于1的时候才有拆分意义
            m = round((b - a)/n, 0)  # 计算加值数
            if m > 0:
                pass
            elif m == 0:
                m = 1
            else:
                continue
            t_list_new_temp = [[a, int(a + m)], [int(a + m + 1), b]]
            t_list_new.extend(t_list_new_temp)
        else:
            t_list_new.extend([each_t_list])
    return t_list_new


def date_gap_splitter(
        start_date: str,  # 开始日期
        end_date: str,  # 结束日期
        splitter_gap: int = 1,  # 拆分计算间隔
        successive: bool = False  # 结果是否连续
):
    """
    时间拆分器，将按照起止时间和间隔时间拆分时间段
    拆分从前向后拆分
    :return:
    """
    day_gap = time_gap_days(start_date, end_date)
    if splitter_gap >= day_gap:
        return [[start_date, end_date]]
    else:
        res_list = list()
        start_date_temp = start_date
        add_count = 0
        while True:
            end_date_temp = get_add_date(start_date_temp, splitter_gap)
            day_gap -= splitter_gap
            finish_num = get_date2timestamp(end_date) - get_date2timestamp(end_date_temp)
            if finish_num <= 0:
                res_list.append([str(start_date_temp), str(end_date)])
                break
            else:
                res_list.append([str(start_date_temp), str(end_date_temp)])
                if successive is True:
                    start_date_temp = copy.deepcopy(end_date_temp)
                else:
                    start_date_temp = get_add_date(end_date_temp, 1)
            add_count += 1
        return res_list


def get_time_duration(
        duration: int
):
    # 计算秒数的时长
    # start_duration = - 8 * 60 * 60  # 固定值
    temp_datetime = datetime.datetime(1970, 1, 1) + datetime.timedelta(seconds=duration)
    # temp_datetime = get_timestamp2datetime(duration + start_duration)  # 计算1970-01-01 00：00：00 后指定秒的日期
    temp_date, temp_time = str(temp_datetime).split(' ')  # 分割日期和时间
    temp_day = time_gap_days(start_time='1970-01-01', end_time=temp_date)  # 计算天数间隔
    if temp_day == 0:
        duration_str = temp_time
    else:
        duration_str = '%sd %s' % (temp_day, temp_time)
    res = {
        'duration_days': temp_day,
        'duration_time': temp_time,
        'duration_str': duration_str,
        'duration': duration
    }
    return res


def print_t(
        text
):
    print("%s >> %s" % ((datetime.datetime.now()), text))


def utc_format(
        utc_time=None,
        timezone_local="Asia/shanghai",
        input_format="%Y-%m-%dT%H:%M:%S.%fZ",
        output_format="%Y-%m-%d %H:%M:%S"
):
    if utc_time is None:
        utc_time = datetime.datetime.utcnow()
    else:
        pass
    local_tz = pytz.timezone(timezone_local)
    if isinstance(utc_time, datetime.datetime) is True:
        utc_datetime = utc_time
    else:
        utc_datetime = datetime.datetime.strptime(utc_time, input_format)
    utc_timestamp = utc_datetime.timestamp()
    utc_datetime_str = utc_datetime.strftime("%Y-%m-%dT%H:%M:%S.%fZ")

    local_datetime = utc_datetime.replace(tzinfo=pytz.utc).astimezone(local_tz)
    local_timestamp = local_datetime.timestamp()
    local_datetime_str = local_datetime.strftime(output_format)
    res = {
        'utc_timestamp': int(utc_timestamp),
        'utc_timestamp_m': int(utc_timestamp * 1000),
        'utc_datetime_str': utc_datetime_str,
        'local_timestamp': int(local_timestamp),
        'local_timestamp_m': int(local_timestamp * 1000),
        'local_datetime_str': local_datetime_str,
    }
    return res


def get_file_name(
        date_delimiter: str = '-',  # 日期分隔符号
        space_delimiter: str = "+",  # 空格分隔符号
        time_delimiter: str = '-'  # 时间分隔符号
):
    """
    获取当前系统的当前时间格式的时间，精确到秒
    :return: 2018年08月01日 14时18分31秒
    """
    inner_now = datetime.datetime.now()
    f_list = ['%Y', date_delimiter, '%m', date_delimiter, '%d', space_delimiter, '%H', time_delimiter, '%M', time_delimiter, '%S']
    f_str = ''.join(f_list)
    data_time = inner_now.strftime(f_str)
    return data_time


def format_seconds(
        input_seconds,
        output_type: type = str
):
    """
    输入秒数，以时间形式输出
    """
    seconds = int(input_seconds)
    microseconds = (input_seconds * 1000000) % 1000000  # 精确到微秒
    format_time = datetime.timedelta(
        days=0,
        seconds=seconds,  # 秒
        microseconds=microseconds  # 微秒
    )
    if output_type:
        return output_type(format_time)
    else:
        return format_time


def get_gap_days(
        date1: str,
        date2: str,
        data1_f: str = '%Y-%m-%d',
        data2_f: str = '%Y-%m-%d'
):
    """
    计算两个日期之间相差的天数
    """
    date1_date = datetime.datetime.strptime(date1, data1_f).date()
    date2_date = datetime.datetime.strptime(date2, data2_f).date()
    days = (date2_date - date1_date).days
    return days


def time_limit(
        end_datetime: str
):
    """
    时间限制
    截止时间例如：2023-07-01 12:00:00
    """
    url = 'http://api.m.taobao.com/rest/api3.do?api=mtop.common.getTimestamp'  # 网络取时
    res = requests.get(url=url)
    net_t = res.json()['data']['t']
    end_date_t = get_datetime2timestamp(end_datetime)
    if end_date_t * 1000 > int(net_t):
        seconds_left = end_date_t - int(net_t)/1000
        print(f'剩余有效时长：{format_seconds(int(seconds_left))}')
        return
    else:
        while True:
            print('软件已失效，请联系开发者～')
            time.sleep(1)


def wait_hour(
        hour: int,
        sleep=0.01
):
    """
    等待 小时整点，如果当前时间是指定的小时，将退出，否则将持续等待
    hour为0-24的整数
    sleep为等待检查的间隔时间
    """
    while True:
        if datetime.datetime.now().hour == hour:
            break
        else:
            time.sleep(sleep)


def get_weekday():
    """
    获取当前时间的星期序列，星期1为1，星期日为7
    """
    return datetime.datetime.now().weekday() + 1


def get_recent_days_date(
        num_start: int = -1,
        num_end: int = 0
) -> list:
    """
    获取指定前推天数的日期列表
    """
    return date_str_list(
        start_date=get_date_string(days=num_start),
        end_date=get_date_string(days=num_end)
    )


def network_timestamp():
    """
    获取网络时间，精确到毫秒
    """
    url = 'https://api.m.taobao.com/rest/api3.do?api=mtop.common.getTimestamp'  # 淘宝网络取时
    res = requests.get(url=url)
    net_t = res.json()['data']['t']  # 精确到毫秒的时间戳
    return int(net_t)


def str2datetime(
        input_str,
        input_str_format: str = 'YYmmdd',
        output_str_format: str = '%Y-%m-%d %H:%M:%S.%f',
):
    """
    将输入的字符串按照既定格式格式化后输出
    :param input_str: 输入的字符串
    :param input_str_format: 输入的字符串格式，例如：YYmmdd
    :param output_str_format: 输出的字符串格式，例如：%Y-%m-%d %H:%M:%S.%f
    """
    year_str = ""
    month_str = ""
    day_str = ""
    hour_str = ""
    minute_str = ""
    second_str = ""

    for index in range(len(input_str_format)):
        index_str = input_str_format[index]
        if index_str == 'Y':
            year_str += input_str[index]
        elif index_str == 'm':
            month_str += input_str[index]
        elif index_str == 'd':
            day_str += input_str[index]
        elif index_str == 'H':
            hour_str += input_str[index]
        elif index_str == 'M':
            minute_str += input_str[index]
        elif index_str == 'S':
            second_str += input_str[index]
        else:
            continue

    if year_str:
        year_int = int(year_str)
    else:
        year_int = None

    if month_str:
        month_int = int(month_str)
    else:
        month_int = None

    if day_str:
        day_int = int(day_str)
    else:
        day_int = None

    if hour_str:
        hour_int = int(hour_str)
    else:
        hour_int = 0

    if minute_str:
        minute_int = int(minute_str)
    else:
        minute_int = 0

    if second_str:
        second_int = int(second_str)
    else:
        second_int = 0

    return datetime.datetime(
        year=year_int,
        month=month_int,
        day=day_int,
        hour=hour_int,
        minute=minute_int,
        second=second_int
    ).strftime(output_str_format)


if __name__ == '__main__':
    res = str2datetime(input_str="20250101123456", input_str_format="YYYYmmdd")
    print(res)