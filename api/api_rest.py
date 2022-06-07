# 请求接口的封装

import requests

baseurl = "https://test-api.kanquanbu.com/"
headers = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"
}


class AppApi():
    def public_get(self, url, data=None, timeout=None):
        url = baseurl + url
        try:
            r = requests.get(url, params=data, headers=headers, timeout=timeout)
            status_code = r.status_code
            r.raise_for_status()  # 如果不是code不是200就报异常
            datas = r.json()
            # print(datas)
        except Exception as e:
            print(e, "request_fail")
        else:
            print("no error")
        finally:
            print("不论是否有异常,最终一定会执行这里")
        return (datas, status_code)

    def public_post(self, url, data=None, timeout=None):
        url = baseurl + url
        try:
            r = requests.post(url, data=data, headers=headers, timeout=timeout)
            status_code = r.status_code
            r.raise_for_status()
            datas = r.json()
            # print(datas)
        except Exception as e:
            print(e, "request_fail")
        else:
            print("no error")
        finally:
            print("不论是否有异常,最终一定会执行这里")
        return (datas, status_code)
