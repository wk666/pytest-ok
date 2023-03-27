# 请求接口的封装

import requests

baseurl = "https://gateway.kimpper-test.com/"
headers = {
    "content-type": "application/json;charset=utf-8",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"
}


class AppApi():
    def public_get(self, url, data=None, timeout=None):
        url = baseurl + url
        try:
            r = requests.get(url, params=data, headers=headers, timeout=timeout)
            status_code = r.status_code
            r.raise_for_status()  # 如果code不是200就报异常
            datas = r.json()
            # print(datas)
            return datas, status_code
        except Exception as e:
            print(e, "request_fail")

    def public_post(self, url, data=None, timeout=None):
        url = baseurl + url
        print(url)
        headers1 = {
            "content-type": "application/json;charset=utf-8",
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36",
            "x-captcha": "ticket=t03z88ynBTiW7CRpDJ4IZzd1cPWkvQljR221KXau294FjY8VS58d_3mr_EPx_1DMklJr3YA5DVbRN9m0pp1SFNE6nu83VDgLhohreSDMYHY4Zd5pDcyrDBqTw**&appid=2084155421&randstr=@Gu2&ret=0"
        }
        try:
            r = requests.post(url, json=data, headers=headers1, timeout=timeout)
            print(r.text)
            status_code = r.status_code
            # r.raise_for_status()
            datas = r.json()
            # print(datas)
            return datas, status_code
        except Exception as e:
            print(e, "request_fail")
