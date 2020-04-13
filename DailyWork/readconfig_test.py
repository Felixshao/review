import os
import configparser

path = 'D:\\study\\python\\review'

config = configparser.ConfigParser()
config_path = os.path.join(path, 'config', 'config.ini')
config.read(config_path, encoding='utf-8')


class operate_Config():

    def get_path(self, name):
        value = config.get('Path', name)
        return value

    def get_http(self, name):
        value = config.get('Http', name)
        bool = config.has_section('http')   # has_section方法，判断配置组是否存在，返回bool变量
        sections = config.sections()      # sections()获取配置文件中所有配置组名
        print(config.options('Http'))   # options()获取指定配置组所有options，存入list
        values = config.items('Http')
        return values

    def get_mysql(self):
        """
        获取mysql配置数据，并存入字典返回
        :return: values_dict;返回字典
        """
        values = config.items('Mysql')
        values_dict = {}
        for i in values:
            values_dict[i[0]] = i[1]

        return values_dict


if __name__ == '__main__':

    config1 = operate_Config()
    # values = config1.get_http('port')
    # print(config1.get_path('path'))
    # print(config1.get_http('port'))
    print(config1.get_mysql())