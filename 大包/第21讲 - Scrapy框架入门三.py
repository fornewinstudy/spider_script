# Scrapy框架-案例
# 分析网站
#   1.目标网站：腾讯招聘
#   2.需求：
#     。爬取招聘岗位信息(岗位名称和工作要求)
#     。翻页
#     。虚假url
#       https://careers.tencent.com/search.html?pcid=40001
#    3.数据动态加载
#     。简单抓包
#     。真实url；
#       https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1653804847510&countryId=&cityId=&bgIds=&productId=&categoryId=40001001,40001002,40001003,40001004,40001005,40001006&parentCategoryId=&attrId=&keyword=&pageIndex=2&pageSize=10&language=zh-cn&area=cn
#      。详情页url
#        虚假url
#        https://careers.tencent.com/jobdesc.html?postId=1494740047826526208
#        真实url
#        https://careers.tencent.com/tencentcareer/api/post/ByPostId?timestamp=1653805210719&postId=1494740047826526208&language=zh-cn
#      4.爬取思路
#       1.第一页url
#       2.解析第一页上每一个岗位Postid(岗位名称)
#       3.构造每个岗位详情页url
#       4.解析详情页url, 提取工作要求

# 实现步骤
#   1.创建项目
#     scrapy startproject tencent
#   2.创建爬虫文件
#     cd tencent
#     scrapy genspider txzhaop example.com
#   3.定义itme
#   4.Spider
#     。定义爬取网站的逻辑
#     。分析爬取下来的页面
#     。Scrapy类分析
#       1、name
#       2、allowed_domins 域名
#       3、start_urls 是一个列表
#       4、custom_settings：一个字典  专属于本spider的配置  这个配置会覆盖项目全局配置，配置需要在初始化前更新，定义类变量
#    5.Requset对象
#      。url:请求网址
#      。callback:回调函数
#      。method: 请求方法 默认get
#      。headers:请求头
#      。body:请求主体
#      。cookies:
#      。meta:携带额外参数
#      。encoding:utf-8
#      。priority:请求优先级
#      。dont_filter:reqest不去重 设置True 默认False 是去重
#      。errback:错误处理方法
#      。flags：请求的标志
#      。cb_kwargs:回调方法的额外参数
#      。Post
#        1.
#     6.Requset请求
#      。url
#      。status:状态码
#      。headers
#      。request：
#      。body:ResponseBody通常指的就是访问⽹⻚后得到的⽹页源代码结果，但注意是bytes类型
#      。certicate:通过代表一个SSL整书对象
#      。ip_address：代表服务器地址
#      。urljson：是对url的一个处理方法，可以传入当前页面的相对url，该方法处理返回的是绝对urlhttps://www.baidu.com+page/1/ = https://www.baidu.com/page/1/
#      。follow/follow_all：是⼀个根据url来⽣成后续Request的⽅法,和直接结构Requset不同的是，该方法接收的url可以是相对的url，不需要一定是绝对url
#      。test:
#      。encoding
#      。selector
#      。xpath()
#      。css()
#      。json():2.2以后版本更新的方法 直接将text属性转为json对象




























