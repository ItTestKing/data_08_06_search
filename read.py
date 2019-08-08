from con_sql import Sql
import os


class ReadFile(object):
    files_path = Sql().get_file_path()
    file_path = None

    def check_path(self, path):
        #检查路径是否存在，不在返回1，存在返回路径。
        if os.path.exists(path):
            return path
        else:
            return 1

    def read_file(self):
        count =0
        for path in self.files_path:
            self.file_path = self.files_path[path]
            if self.check_path(self.file_path) != 1:
                # 统计行数
                try:
                   for line in open(self.file_path,'r',encoding='UTF-8'):
                        count += 1

                except Exception as e:
                    print(e)
                print("行数为：==========={}\n".format(count))
                #打印内容
                try:
                    with open(self.file_path, 'r+',encoding='UTF-8')as file:
                        return file.read()
                except Exception as e:
                    print(e)


ReadFile().read_file()
