# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import re


class DaomuPipeline:
    def process_item(self, item, spider):
        # print(item)

        # 子文件夹路径
        dir_path = './novel/{}/'.format(item['first_title'])
        # 对小标题的章节名进行替换
        item['second_title'] = re.sub(r'[\\\/\:\*\?\<\>\| ]', "_", item['second_title'])

        # 小说存储的完整路径
        file_path = dir_path + item['second_title'] + ".text"
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(item['content'])
        return item


