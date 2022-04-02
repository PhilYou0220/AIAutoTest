"""使用带参装饰器记录接口请求时长和调用记录"""
from functools import wraps
from time import time


def outer(func):
    @wraps(func)  # 使函数名还是原来的函数名 而不是inner
    def inner(*args, **kwargs):
        start_time = time()
        status_code, dict_expect_return_data, real_status_code, dict_return_data = func(*args, **kwargs)
        end_time = time()
        duration = end_time - start_time
        __a = f"接口 {func.__name__} 共耗时:{duration}秒"
        with open(file="../log/api.log", mode="a", encoding="utf-8") as f:
            f.write(__a)
        return status_code, dict_expect_return_data, real_status_code, dict_return_data

    return inner
