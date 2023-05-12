"""
    <HNUST Campus Network Automatic Login Script.>
    Copyright (C) <2023>  <HpLeapfrog>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

#python3
#_*_ coding:utf-8 _*_
#python3
#_*_ coding:utf-8 _*_
import json
import re
import urllib.request


def extract_dict(s) -> list:
    """Extract all valid dicts from a string.

    Args:
        s (str): A string possibly containing dicts.

    Returns:
        A list containing all valid dicts.

    """
    results = []
    s_ = ' '.join(s.split('\n')).strip()
    exp = re.compile(r'(\{.*?\})')
    for i in exp.findall(s_):
        try:
            results.append(json.loads(i))
        except json.JSONDecodeError:
            pass
    return results

UserName = "22020000000" # 账号
PassWord = "0000000"  # 密码
Operators = "" # 运营商选择：电信“telecom”，移动“cmcc”，联通“unicom”，校园网为空值

get_ip = "http://login.hnust.cn/drcom/chkstatus?callback=dr1002"
wlanIp = urllib.request.urlopen(get_ip)
wlanIpStr = wlanIp.read().decode("gbk")
wlanIpStr = str(wlanIpStr).strip()

wlanIpStr_= extract_dict(wlanIpStr)
wlan = wlanIpStr_[0]['v46ip']

api_link = "http://login.hnust.cn:801/eportal/?c=Portal&a=login&callback=dr1004&login_method=1&user_account=,0,"+ \
 UserName + Operators + "&user_password=" + PassWord +"&wlan_user_ip=" + wlan + \
"&wlan_user_ipv6=&wlan_user_mac=000000000000&wlan_ac_ip=&wlan_ac_name=&jsVersion=3.3.3"

response = urllib.request.urlopen(api_link)
print(response.read().decode("gbk"))
