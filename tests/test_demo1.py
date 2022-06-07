# -*- coding: utf-8 -*-
# @FileName: test_demo1.py
# @WorkPath: Api_Pytest
# @FilePath: ~/Desktop/Api_Pytest/tests/test_demo1.py
# @Time    : 2021/08/19 18:29:06
# @Author  : wangkang
# @Contact : xxxx@xx.com
# @Software: vscode

import sys
import os

from requests import models
BASE_DIR = os.path.dirname(os.path.dirname(__file__))  # 获取当前文件上级目录的绝对路径
print(BASE_DIR)
sys.path.append(BASE_DIR)
import pytest

from api.api_rest import AppApi

appAPI = AppApi()  # 创建类对象
model_name = "uic"
# 获取地理位置
@pytest.mark.skip("ok")
def test_get_locations():
    url = model_name+"/pro/locations/get"
    parsed_res = appAPI.public_get(url)
    print(parsed_res)
    datas = parsed_res[0]
    status_code = parsed_res[1]
    assert status_code == 200

# 提交注册请求
def test_register():
    url = model_name+"/pro/user/register/submit"
    data = {"email": "xxxx@qq.com"}
    parsed_res = appAPI.public_post(url,data=data)
    print(parsed_res)
    status_code = parsed_res[1]
    assert status_code == 200

if __name__ == '__main__':
    pytest.main(["-v", "-s", "./tests/test_demo1.py"])
