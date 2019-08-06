import psutil
import os
from sys import argv


class Search():
    dis_name = []
    path = argv[1]
    search_file_name = argv[2]
    search_dir_name = None
    search_disc_name = None
    search_disc = None

    def disc_name(self):
        # 判断要搜索的盘符是否存在，disc是要传入的参数。

        if isinstance(self.path, str):
            if len(self.path) > 1:
                if os.path.exists(self.path):
                    return self.path
                else:
                    print("您输入的路径不存在")
                    return 0

            if len(self.path) == 1:
                disc_name = self.path.upper()
                disc_names = psutil.disk_partitions()
                for disc in disc_names:
                    disc_devices = (disc.device).replace(':\\', '')
                    self.dis_name.append(disc_devices)
                if disc_name in self.dis_name:
                    discname = disc_name + ':\\\\'
                    return discname
                else:
                    print("没有这个盘符")
                    return 0
        else:
            print("请输入字符")
            return 0

    def search_file(self):

        if self.disc_name() == 0:
            pass
        else:
            self.search_disc_name = self.disc_name()

            for parent, dirname, filenames in os.walk(self.search_disc_name, followlinks=True):
                for filename in filenames:
                    file_path = os.path.join(parent, filename)
                    if filename == self.search_file_name:
                        print(filename)
                        print(file_path, '\n')
            print("指定盘符：{} 搜索完毕".format(self.search_disc_name))


# Search().disc_name("12")
Search().search_file()
