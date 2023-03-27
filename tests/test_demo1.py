# -*- coding: utf-8 -*-
# @FileName: test_demo1.py
# @WorkPath: Api_Pytest
# @FilePath: ~/Desktop/Api_Pytest/tests/test_demo1.py
# @Time    : 2021/08/19 18:29:06
# @Author  : wangkang
# @Contact : xxxx@xx.com
# @Software: vscode
import json
import sys
import os

from requests import models

BASE_DIR = os.path.dirname(os.path.dirname(__file__))  # 获取当前文件上级目录的绝对路径
print(BASE_DIR)
sys.path.append(BASE_DIR)
import pytest

from api.api_rest import AppApi

appAPI = AppApi()  # 创建类对象
model_name = "pro-uic"


# @pytest.mark.skip("ok")
# 提交注册请求
def test_register():
    url = model_name + "/pro/user/register/submit"
    data = {"email": "1806755030@qq.com"}
    parsed_res = appAPI.public_post(url, data)
    print(parsed_res,"=======")
    status_code = parsed_res[1]
    assert status_code == 200


if __name__ == '__main__':
    pytest.main(["-v", "-s", "./tests/test_demo1.py"])
