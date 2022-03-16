import requests
import hashlib
import time
from tools.log import log
import json


class Auth(object):

    def base_post(self, username, password):
        # 测试环境帐号
        url = "http://106.75.154.221:8391/api/user/login"
        username = username
        # 使用encode 防止密码中含有中文 把密码进行md5加密
        password = hashlib.md5(password.encode(encoding='UTF-8')).hexdigest()
        # 浮点取整数
        timestamp = int((str(time.time())).split(".")[0])
        headers = {"content-type": "application/json; charset=utf-8"}
        data1 = {
            "username": username,
            "password": password,
            "timestamp": timestamp
        }
        # 由于指定了headers json 可以不用转换
        r1 = requests.post(url=url, json=data1, headers=headers).json()

        try:
            if r1.get("token"):  # 判断是否有能通过键获取值 如果不能会抛key error
                pass
        except KeyError as e:
            log.error(f"报错类型：{e} ，帐号或密码错误 错误信息为：一级登录报错{r1}")
        token = r1["token"]
        return token

    def auth_post(self, url, data2, username, password):
        token = self.base_post(username, password)
        real_token = "Bearer" + " " + token

        headers = {
            "Authorization": real_token
        }
        resp = requests.post(url=url, json=json.loads(data2), headers=headers)
        real_status_code = resp.status_code
        dict_r = resp.json()
        if dict_r.get("error"):
            log.error(
                f" \n账号{username}\n url:{url}\n 密码：{password}\n 请求参数: {data2}\n 返回状态码: {real_status_code}\n 返回值: {dict_r}")
        return dict_r, real_status_code

    @staticmethod
    def register_post(url, data):
        url = url
        data = data
        headers = {"content-type": "application/json; charset=utf-8"}
        res = requests.post(url=url, json=json.loads(data), headers=headers)
        real_status_code = res.status_code
        dict_r = res.json()
        if not dict_r.get("error"):
            log.error(
                f" \n url:{url}\n 请求参数: {data}\n 返回状态码: {real_status_code}\n 返回值: {dict_r}")
        return dict_r, real_status_code


if __name__ == '__main__':
    pass
