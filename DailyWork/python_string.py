# _*_ config: utf-8 _*_
# python3字符串

print('1\a2')
print('1\0002')
print('1\f2')
print('1\v2')

print('jnk'.capitalize())   # 首字符大写
print('jnk'.center(20, '#'))   # 返回指定宽度，不足使用填充符补充
print('1234321234'.count('2'))      # 统计字符在字符串出现次数
print('qwert'.endswith('t'))    # 判断字符串是否以指定字符结尾
print('qwert'.endswith('e', 2, 3))  # 传参：字符/字符串， 开始匹配位置、结束匹配位置，判断字符/字符串是否与匹配位置字符一致
print('12320'.isdigit(), '12356'.isnumeric())   # 判断字符串是否只包含数字
print('23,.dwd'.islower())  # 判断字符串是否包含英文字符，且都是小写
print('zhe shi yi ge biao ti!'.title())     # 标题化字符串
print('Zhe Shi Yi Ge Biao Ti!'.istitle())   # 判断是否为标题