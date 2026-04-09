# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class ZuoyejiuPipeline:
    f = open('bk.csv', 'a', encoding='utf-8')
    f.write('标题,街区,街道\n')
    def process_item(self, item, spider):
        # 写入的是字符串，你有多少个头就加多少个{}
        self.f.write('{},{},{}\n'.format(item['title'],item['region'],item['block']))
        return item

    def close_spider(self,spider):
        self.f.close()
        print("数据已保存完毕")
