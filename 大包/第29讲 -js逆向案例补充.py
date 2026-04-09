# 有道案例
# https://fanyi.youdao.com/
# 1.抓包找到加密字段
# 2.通过加密字段名进⾏初步定位打断点进⾏调试(借助vscode)
# 3.通过python执⾏调试好得js代码
# 4.携带加密之后以及其他的参数发送请求
# 微信公众平台
# https://mp.weixin.qq.com/
# 1.通过抓包找到加密字段： pwd
# 2.通过查看请求调⽤栈的⽅式 (通过对⽐不同栈的pwd的变化情况)
# 调⽤加密函数的位置：
# pwd: m(n.pwd.substr(0, 16))
# 我们需要做的是把加密部分的代码扒出来
# 通过调⽤的位置进⼊到具体的加密位置
# ⼀步⼀步通过报错进⾏调试直⾄代码没有报错并且有你想要的结果
# 3.通过python调⽤js代码
# 4.携带其他的参数发送请求(暂时不⽤做)
# 房天下
# https://passport.fang.com/
# 1.通过抓包找到加密字段： pwd
# 2. search
# 加密函数调⽤的位置：
# pwd: encryptedString(key_to_encode, that.password.val()),通过调⽤位置能够进⼊到具体加密的地⽅
# 什么样的情况下可以复制整个js⽂件：
# 如果你发现你⼀直在这个js⽂件⾥⾯复制代码 并且 这个js⽂件不是很⻓
# 通过调试得到了密⽂密码
# 3.通过python调⽤js⽂件
# 闪职
# http://shanzhi.spbeen.com/login/
# 1.输⼊错误的账号和密码找登录接⼝：
# http://shanzhi.spbeen.com/login/是post请求
# 从中找到加密字段：password
# 2.通过search或者通过栈的⽅式找加密代码
# 如果打开js⽂件之后看到是eval开头的就证明这个js⽂件很有可能是被加密处理了的
# 还原之后的：
# function doLogin() {
#   // password_old 加密之前的明⽂密码
#   var password_old =$("#MemberPassword").val();
#   var encrypt = new JSEncrypt();
#   //⼀般来说pk指向的是公钥
#   var public_key = $("#pk").val();
#   // setPublicKey想到RSA算法
#   encrypt.setPublicKey(public_key);
#   var pass_new = encrypt.encrypt(password_old);
# }
# 如果抠出来的代码虽然没有报错但是不是你想要的或者连抠都抠不出来
# 可以暂时放弃抠代码想想别的⽅法：
# 1.通过python重构加密算法
# 2.通过js环境 安装某⼀些库 借助库⾥⾯⾃带的加密算法进⾏加密
# ⼀般来说⽹站不会对核⼼的加密算法做修改最多只会对加密之前或者加密之后的密码做些⼩调整
# js解密：
# http://www.ab173.com/enc/eval_package.php

# python重构加密算法
# # pip install pycryptodome -i https://pypi.tuna.tsinghua.edu.cn/simple
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 as cry_pksc1_v1_5
import base64
def encrypto(pk, password):
    """
    python重构RSA加密
    : param pk: 公钥
    : param password: 待加密的明⽂密码
    : return: 加密之后的密⽂密码
    """
    public_key = "-----BEGIN PUBLIC KEY-----\n{}\n-----END PUBLIC KEY-----". format(pk)
    #导⼊公钥返回⼀个RSA秘钥对象
    rsakey = RSA.importKey(public_key)
    # 对需要加密的内容进⾏PKCS#1 v1.5加密
    cipher = cry_pksc1_v1_5.new(rsakey)
    # 使⽤公钥加密密码 密码必须是⼆进制
    miwen_encode = cipher.encrypt(password.encode())
    # 再使⽤ Base64 对类似字节的对象进⾏编码
    cipher_text = base64.b64encode(miwen_encode).decode()
    return cipher_text























