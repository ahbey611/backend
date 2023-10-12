# -*- coding: utf-8 -*-
import re

def register_params_check(content: dict):
    """
    进行参数检查
    """

    # 验证用户名
    # 用户账号为长度 5-12 的字母串加数字，且必须包含这两种类型，所有字母串必须在数字前面，大写字母和小写字母均合法
    if "username" in content:
        username = content["username"]
        if not re.match(r"^(?=.*[a-zA-Z]+)(?=.*\d+$)[a-zA-Z\d]{5,12}$", username):
            return "username", False

    # 验证密码
    # 用户密码为长度 8-15 的字符串，由大写、小写字母、数字和标点符号组成且必须包含这四种类型，有效的标点符号为-_*^
    if "password" in content:
        password = content["password"]
        if not re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[-_*^])[a-zA-Z\d\-_*^]{8,15}$", password):
            return "password", False

    # 验证手机号
    # 用户的手机号的格式为+[区号].[手机号]，其中区号必须为两位数字，手机号必须为 12 位数字，例如+12.123456789012
    if "mobile" in content:
        mobile = content["mobile"]
        if not re.match(r"^\+\d{2}\.\d{12}$", mobile):
            return "mobile", False

    # 验证个人地址链接
    # 用户的个人地址链接包含协议和域名两部分
    # 协议部分必须为 http:// 或者 https://
    # 域名部分包含 1 到多个点 .，表示以点 . 分隔的标签序列，且总长度不超过 48 个字符（包含 .）。标签序列只能由下列字符组成：
    # 大小写字母 A 到 Z 和 a 到 z
    # 数字 0 到 9，但最后一段顶级域名不能是纯数字（如 163.com 可以但 163.126 不可以）
    # 连字符-，但不能作为首尾字符
    if "url" in content:
        url = content["url"]
        result = re.match(r"^(http://|https://)(([a-zA-Z\d]+(?:-[a-zA-Z\d]+|[a-zA-Z\d]*).?)+)$", url)
        if not result:
            return "url",False
        # 没有最后一段顶级域名
        if result[2] == result[3]:
            return "url", False
        # 长度过长
        if len(result[2]) > 48 or len(result[2]) < 1:
            return "url", False
        # 顶级域名为数字
        if result[3].isdigit():
            return "url", False

    # magic_number为非负数 int 数值，可选参数（在设计测试用例时无需考虑最大值上界）
    # 如果 magic_number 缺失，请为 content 添加默认值为 0 的 magic_number 字段
    if "magic_number" in content:
        magic_number = content["magic_number"]
        # 有数字以外的字符
        if type(magic_number) == str:
            if not magic_number.isdigit():
                return "magic_number", False
        # 非整数
        if type(magic_number) == float:
            return "magic_number", False
        # 非正数
        if int(magic_number) < 0:
            return "magic_number", False

    # 补0
    if "magic_number" not in content:
        content["magic_number"] = 0

    return "ok", True
