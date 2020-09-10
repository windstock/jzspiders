from base_spider import SpiderBase


class DingDemo(SpiderBase):
    def ding_crawl_information(self):
        self._spider_init()
        msg = ''
        from scripts.utils import org_tablecode_map
        for tablename, info in org_tablecode_map.items():
            chiname, tablecode = info[0], info[1]
            sql = '''SELECT count(id) as inc_count FROM {} WHERE OrgTableCode = {} and {} > date_sub(CURDATE(), interval 1 day);'''.format \
                ("OriginSpiderAll", tablecode, "CreateTime")
            print(sql)
            inc_count = self.spider_client.select_one(sql).get("inc_count")
            msg += '{} 今日新增 {}\n'.format(chiname, inc_count)
        # TODO 计算总计新增

        sql2 = ''''''

        print(msg)


if __name__ == '__main__':
    DingDemo().ding_crawl_information()