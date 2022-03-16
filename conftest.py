""" 2.1 conftest.py文件名不能修改
        conftest.py文件中存放项目所有的fixture
        方便对fixture管理和维护
    2.2 在conftest.py定义函数
        在函数前添加@pytest.fixture()装饰器
        在测试用例的函数中传入fixture标识的函数名。
提示：conftest.py文件放在项目的根目录，作用域是全局的。
    conftest.py文件放在某一个包下，作用域只在该包内。
"""
import pytest


@pytest.fixture()
def login():
    print("登录成功")
    username = "you"
    yield username
    print("后置动作")


@pytest.fixture()
def dele():
    print("删除成功")
    username = "fei"
    yield username
    print("删除成功后置动作")


# 由于AI中台是和两个用户有关所以
@pytest.fixture(scope="session")
def get_token():
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
        yield token
        print("会话级别的teardown结束")
