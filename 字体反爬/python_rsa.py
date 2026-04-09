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
pk = 'MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDaP+rYm6rqTMP565UmMU6YXq46KtAN3zwDSO8LNa15p0lJfsaY8jXY7iLsZqQZrGYr2Aayp6hYZy+Q+AMB/VUiSpD9ojPyOQ7r9jsf9jZbTOL4kj6iLZn37fEhp4eLvRgy5EJCyQoFyLCsgLechBTlYl2eA95C3j4ZUFhiV6WFHQIDAQAB'
r = encrypto(pk,'123456')
print(r)
