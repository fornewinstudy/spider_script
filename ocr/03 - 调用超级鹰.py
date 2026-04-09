from chaojiying import Chaojiying_Client

chaojiying = Chaojiying_Client('20201212', '153503', '933459')
im = open('a.jpg', 'rb').read()
pic_str = chaojiying.PostPic(im, 1902)["pic_str"]
















