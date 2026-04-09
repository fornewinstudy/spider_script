# scrapy-redis分布式
# redis基本数据结构
#  .列表:lpush rpush lpop rpop 先进先出 先进后出
#  .集合:无序而且不重复 实现随机排序而且不重复的爬取队列(重点)
#  .有序集合:实现有一定优先级的调度队列
# 环境要求
#  .scrapy(要求2.5.1 最好不要安装最新的)
#  .scrapy-redis
#  .crawlspider -> RedisCrawlSpider
#  .scrapy.spider -> RedisSpider
# 源码分析
#  .self.key = '%(spider)s:items'
#  .key = self.key % {'spider': spider.name}
#  .spider是爬虫对象
#  .spider.name 爬虫文件的名字:dmoz
#  .key = '%(spider)s:items' % {'spider': dmoz}
#  .key = 'dmoz:items'
#  .added如果为0 证明请求是存在的
#  .added如果为1 证明请求是部存在的
#  .return added == 0 请求存在返回True 如果不存在 返回False


# 案例演示
#  .先通过的scrapy实现
#  .在改写成分布式
#  .爬取需求:爬取全套小说内容
#  .创建一级一级的文件

#  .'./novel/盗墓笔记1：七星鲁王宫/七星鲁王 第一张 血尸.text'
import re
import os

# 大标题
first_title = "盗墓笔记1：七星鲁王宫"

# 小标题
second_title = "七星鲁王 第一章 血尸"

# 先对不能出现再文件名中的字符做替换 一般都是英文状态下的
nue_first_title = re.sub(r'[\\\/\:\*\?\<\>\| ]', "_",first_title)
nue_second_title = re.sub(r'[\\\/\:\*\?\<\>\| ]', "_",second_title)
print(nue_first_title)
print(nue_second_title)

# 创建文件文件夹
# 大标题是需要生成的 小标题(具体的文件)是不需要生成的
# 生成文件路径
dir_path = './novel/{}/'.format(nue_first_title)
# 根据文件路径进行创建
# 在创建之前需要进行判断
if not os.path.exists(dir_path):
    #如果有 就创建
    os.makedirs(dir_path)

# 将小说具体内容写入到text文件里面
file_path = dir_path + second_title + ".text"
with open(file_path, 'w', encoding='utf-8') as f:
    f.write('七星鲁王 第一章 血尸')


# 一级页面：获取大标题和二级页面的链接
# contains 模糊匹配
# a_list = //[contains(@id, "menu-item-")]/a
# for a in a_list:
#     # 获取大标题
#     first_title = a.xpath('./text()').get()
#     # 获取二级页面的链接
#     second_title = a.xpath('./@href').get()

# 二级页面：获取小标题和三级页面的链接
# a_list = response.xpath('//article/a')
# for a in a_list:
#     # 获取大标题
#     second_title = a.xpath('./text()').get()
#     # 获取二级页面的链接
#     third_title = a.xpath('./@href').get()

# 三级页面：获取小说的具体内容
# content_lst = response.xpath('//article[@class="article-content"]/p/text').getall()
# '\n'.join(content_lst)

# 把普通的scrapy改写成分布式
#  . 导入from scrapy_redis.spiders import RedisSpider
#  . 把scrapy.Spider修改为RedisSpider
#  . 注释start_urls 添加redis_key
# 在settings中修改
#  . 需要改(ua)
#  . USER_AGENT = 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36'
#  . 指定去重方式 给请求对象去重
#  . DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
#  . 设置调度器
#  . SCHEDULER = "scrapy_redis.scheduler.Scheduler"
#  . 队列中的内容是否进行持久保留
#  . True redis关闭的时候数据会保留
#  . False 不会保留
#  . SCHEDULER_PERSIST = True
# 将数据保存到redis中
#  . 'scrapy_redis.pipelines.RedisPipeline': 400,

# 文件运行是要间接的给一个url
#  . lpush daomuniji http://www.daomubiji.com/
#  如果要强制性暂停按ctrl+c








