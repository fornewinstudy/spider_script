# 在cmd里面如果要跨盘符cd /d D:\zgqpycharm\爬虫基础代码\js

# 使⽤js进⾏加密
# // 1. cd 进项⽬⽬录
# // 2. 做国内资源映射： npm install -g cnpm -- registry=https://registry.npm.taobao.org ( 如果在之前做过就不需要 )
# 如果有碰到报错：
# npm ERR! the command again as root/Administrator.
# 以管理员的身份运⾏终端
# // 3. cnpm install node-jsencrypt

# 总结
# 1. 抓包 找到加密字段
# 2. 搜索加密字段名 或者通过栈 找到加密的⼤致位置 在可疑的地⽅打上断点 通过vscode和浏览器进⾏调试调试到没有报错并且有你想要的结果
# 如果碰到没有办法抠的代码 或者说抠出来之后 没有你想要的结果
#  - 要么通过python重构算法
#  -要么通过js进⾏加密(处理)
#  - 要⼩⼼加密前或者是加密之后的密码是否有做处理
# 3. 通过 python 执⾏js代码 (如果需要传⼊多个参数 *args)
# 4. 带上所有参数发送请求 python 重构各种算法 :
# https://www.cnblogs.com/pythonywy/p/13999474.html
# JS逆向-Cryptojs库AES/DES/RSA算法(需要安装的库以及基本使⽤介绍)：
# https://blog.csdn.net/weixin_43411585/article/details/108788483?spm=1001.2101.3001.6650.7&utm_medium=distribute.pc_relevant.none-task%02blog-2%7Edefault%7EBlogCommendFromBaidu%7Edefault-7-108788483-blog%02121732881.pc_relevant_default&depth_1-utm_source=distribute.pc_relevant.none-task-blog%022%7Edefault%7EBlogCommendFromBaidu%7Edefault-7-108788483-blog%02121732881.pc_relevant_default&utm_relevant_index=13

# ⽆限debugger的处理⽅式
# 1.在debugger前⾯右击 --> 选中"Add conditional breakpoint..."-->输⼊false-->回⻋(前⾯出现⻩⾊的标志才算设置成功)
# 2.在debugger前⾯右击 --> 选中"Never pause here"(前⾯出现⻩⾊的标志才算设置成功)
# 3.直接让所有断点都失效

# JS字体反爬
# ⼀、原理解释
# 1.找到两者的桥梁(字体⽂件)
# 如何确定以及找到字体⽂件：
#  -先在elements⾥⾯找到出现乱码的标签
#  -去style⾥⾯找到font-family
#  -如果说有多个font-family尝试把前⾯的沟去掉
#  -确定之后先去源码⾥⾯搜索如果源码⾥⾯找不到就去search⾥⾯找
#  - xxx.ttf或者xxx.woff
# 2.从字体⽂件中挖掘映射关系（是怎么把乱码变成数字的）
# 3.通过映射关系去⽹⻚源码中做替换

# ⼆、常⽤⼯具介绍
# 1.在线字体编辑软件
# https://font.qqe2.com/
# 2.本地⼯具
# win：FontCreatorSetup
# mac：IconFontPreview
# 3.fontTools
# pip install fontTools -i https://pypi.tuna.tsinghua.edu.cn/simple

# 三、总结
# 通过字体软件我们能够看到 数字 跟 name和code-points之间的联系
# 字体软件是我们找映射关系的⼯具
# 通过python将字体⽂件保存成了⼀个xml⽂件 我们能够看到⾥⾯的name和code
# 我们是能够通过python提取出name和code
# {'xxxx': 1, 'yyyy': 2.......}





