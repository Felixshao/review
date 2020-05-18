import cv2
import numpy as np
from matplotlib import pyplot as plt
from pylab import *
from matplotlib.font_manager import FontProperties
import time
from selenium import webdriver
from selenium.webdriver import ActionChains


font = FontProperties(fname=r"c:\Windows\Fonts\simsun.ttc", size=14)
splier_path = '..\\img\\splier.png'
splier_grey_path = '..\\img\\splier_grey.png'
s_path = '..\\img\\s.png'

def generate_img():
    """图片生成"""
    # 生成图片,cv2.imread方法，存入图片路径
    img = cv2.imread('..\\img\\splier.png')
    # 生成灰色图片,cv2.imread方法，存入图片路径和flags(0代表灰色图片)
    imggrey = cv2.imread('..\\img\\splier.png', 0)
    # 展示原图，cv2.imshow方法在窗口中展示图片，传入参数：窗口名和生成的图片对象
    cv2.imshow('img', img)
    # 展示灰色图片
    cv2.imshow('imggrey', imggrey)
    # 等待图片关闭
    cv2.waitKey()
    # 保存图片,cv2.imwrite方法，传参：图片路径和生成的图片对象
    cv2.imwrite('..\\img\\splier_grey.png', imggrey)

def img_window():
    """图像窗口设置"""
    img = cv2.imread(splier_path)
    # 新建窗口,传参：窗口名称、窗口属性（cv2.WINDOW_AUTOSIZE(根据图像大小创建窗口大小)， cv2.WINDOW_NORMAL(可自定义调整大小)）
    cv2.namedWindow('new window', cv2.WINDOW_NORMAL)

    cv2.imshow('new window', img)
    cv2.waitKey()
    # 关闭窗口，传参：窗口名称
    cv2.destroyWindow('new window')

def img_atter():
    """获取图像属性"""
    img = cv2.imread(splier_path)
    imggrey =cv2.imread(splier_path, 0)
    # 获取图片属性，图片的宽、高、通道(非彩色图不返回通道)
    sp1 = img.shape
    sp2 = imggrey.shape

    print(sp1, ' ', sp2)
    # 获取图像像素数目
    imgsize = img.size
    imggreysize = imggrey.size
    print(imgsize, '  ', imggreysize)
    # 获取图像数据类型
    ty = img.dtype
    ty2 = imggrey.dtype
    print(ty, '   ', ty2)

def generate_air_img():
    """生成指定空图像"""
    img = cv2.imread(splier_path)
    # 设置空图和原图属性一致, 传参：tuple(宽、高、通道)和图像数据类型(如：uint8)
    img_zero = np.zeros(img.shape, img.dtype)
    img_zero2 = np.zeros((200, 300, 3), np.uint8)

    cv2.imshow('img', img)
    cv2.imshow('img_zero', img_zero)
    cv2.imshow('img_zero2', img_zero2)
    cv2.waitKey()

def access_img():
    """访问和操作图像像素"""
    img = cv2.imread(splier_path)

    # 获取图片位置，并打印出此块区域颜色
    nump = img[50, 50]
    print(nump)
    # 设置图像位置指定像素值
    img[50, 100] = (0, 0, 255)
    # 设置图像指定矩形块像素值，[y轴0-50， x轴1-100]
    img[0:50, 1:100] = (0, 0, 255)
    # 设置图像指定矩形块指定通道（0(b)， 1(g)， 2(r)）的像素值
    img[0:50, 50:100, 0] = 255
    img[100:150, 150:200, 1] = 255
    img[200:250, 250:300, 2] = 255
    cv2.imshow('img', img)
    cv2.waitKey()

def img_aisle():
    """图像3通道合并和分离"""
    img = cv2.imread(splier_path)
    # 三通道分离，split方法，传参：生成的图片对象
    b, g, r = cv2.split(img)
    # 三通道合并，merge方法
    merged = cv2.merge([b, g, r])
    print(b[10, 10], g[10, 10], r[10, 10], merged[10, 10])
    cv2.imshow('blue', b)
    cv2.imshow('green', g)
    cv2.imshow('red', r)
    cv2.imshow('merged', merged)
    cv2.waitKey()

def img_print_text():
    """图像上填入文字"""
    img = cv2.imread(splier_path)

    # 写入文字，传参：生成的图像对象、文本、文字左下角坐标、字体、字体大小、文字颜色
    cv2.putText(img, 'print some text to img', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255))

    cv2.imshow('img', img)
    cv2.waitKey()

def img_zoom():
    """图像缩放"""

    img = cv2.imread(splier_path)
    print(img.shape)
    # 图像缩放，resize方法，传参：图像对象、宽高
    imgg = cv2.resize(img, (568, 554))

    cv2.imshow('imgg', imgg)
    cv2.waitKey()

def img_convert_grey():
    """图像灰化转换"""
    # 载入图像
    img = cv2.imread(splier_path)
    # 显示原始图像
    fig = plt.figure()
    subplot(121)
    plt.gray()

    im2 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # OpenCV采用BGR排列顺序,需要转换一下.
    imshow(im2)
    title(u'彩色图', fontproperties=font)
    axis('off')
    # 显示灰度化图像
    # 颜色空间转换
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    plt.subplot(122)
    plt.gray()
    imshow(gray)
    title(u'灰度图', fontproperties=font)
    axis('off')
    show()


def canny_test1():
    """canny"""
    lowThreshold = 0
    maxThreshold = 500

    def canny_low_threshold(intial):
        blur = cv2.GaussianBlur(img, (3, 3), 0)
        canny = cv2.Canny(blur, intial, lowThreshold)
        cv2.imshow('canny', canny)

    def canny_max_threshold(intial):
        blur = cv2.GaussianBlur(img, (3, 3), 0)
        canny = cv2.Canny(blur, intial, maxThreshold)
        cv2.imshow('canny', canny)

    img = cv2.imread(splier_path, 0)
    cv2.namedWindow('canny', cv2.WINDOW_NORMAL | cv2.WINDOW_KEEPRATIO)

    cv2.createTrackbar('min', 'canny', lowThreshold, 500, canny_low_threshold)
    cv2.createTrackbar('max', 'canny', maxThreshold, 1000, canny_max_threshold)
    canny_low_threshold(0)
    # canny_max_threshold(0)

    if cv2.waitKey(0) == 27:
        cv2.destroyAllWindows()

def canny_test2(imgPath1, imgPath2):
        imgs = []
        # 原始图像，用于展示
        sou_img1 = cv2.imread(imgPath1)
        sou_img2 = cv2.imread(imgPath2)

        # 原始图像，灰度
        # 最小阈值100,最大阈值500
        img1 = cv2.imread(imgPath1, 0)
        blur1 = cv2.GaussianBlur(img1, (3, 3), 0)
        canny1 = cv2.Canny(blur1, 100, 500)
        cv2.imwrite('..\\img\\temp1.png', canny1)

        img2 = cv2.imread(imgPath2, 0)
        blur2 = cv2.GaussianBlur(img2, (3, 3), 0)
        canny2 = cv2.Canny(blur2, 100, 500)
        cv2.imwrite('..\\img\\temp2.png', canny2)

        target = cv2.imread('..\\img\\temp1.png')
        template = cv2.imread('..\\img\\temp2.png')

        # 调整显示大小
        target_temp = cv2.resize(sou_img1, (350, 200))
        target_temp = cv2.copyMakeBorder(target_temp, 5, 5, 5, 5, cv2.BORDER_CONSTANT, value=[255, 255, 255])

        template_temp = cv2.resize(sou_img2, (200, 200))
        template_temp = cv2.copyMakeBorder(template_temp, 5, 5, 5, 5, cv2.BORDER_CONSTANT, value=[255, 255, 255])

        imgs.append(target_temp)
        imgs.append(template_temp)

        theight, twidth = template.shape[:2]

        # 匹配拼图
        result = cv2.matchTemplate(target, template, cv2.TM_CCOEFF_NORMED)

        # 归一化
        cv2.normalize(result, result, 0, 1, cv2.NORM_MINMAX, -1)

        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

        # 匹配后结果画圈
        cv2.rectangle(target, max_loc, (max_loc[0] + twidth, max_loc[1] + theight), (0, 0, 255), 2)

        target_temp_n = cv2.resize(target, (350, 200))
        target_temp_n = cv2.copyMakeBorder(target_temp_n, 5, 5, 5, 5, cv2.BORDER_CONSTANT, value=[255, 255, 255])

        imgs.append(target_temp_n)

        imstack = np.hstack(imgs)

        # cv2.imshow('stack' + str(max_loc), imstack)
        print('匹配完毕')
        return max_loc
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()


def test():
    # 新建selenium浏览器对象，后面是geckodriver.exe下载后本地路径
    browser = webdriver.Chrome()

    # 网站登陆页面
    url = 'https://admin.xiaoe-tech.com/login_page?reg_source=0101&xeuti=ituex#/acount'

    # 浏览器访问登录页面
    browser.get(url)

    handle = browser.current_window_handle
    print(handle, type(handle))
    # 等待3s用于加载脚本文件
    browser.implicitly_wait(3)

    # 点击登陆按钮，弹出滑动验证码
    browser.find_element_by_xpath('//div[@class="phoneWrapper"]/div/input').send_keys('15779582092')
    browser.find_element_by_xpath('//div[@class="passwordWrapper"]/div/input').send_keys('123456')
    btn = browser.find_element_by_class_name('login-btn')
    btn.click()
    frame = browser.find_element_by_id('tcaptcha_iframe')
    browser.switch_to.frame(frame)

    def get_move():
        # 获取iframe元素，切到iframe
        time.sleep(1)

        # 获取背景图src
        targetUrl = browser.find_element_by_id('slideBg').get_attribute('src')

        # 获取拼图src
        tempUrl = browser.find_element_by_id('slideBlock').get_attribute('src')

        # 新建标签页
        browser.execute_script("window.open('');")
        # 切换到新标签页
        browser.switch_to.window(browser.window_handles[1])

        # 访问背景图src
        browser.get(targetUrl)
        time.sleep(3)
        # 截图
        browser.save_screenshot('..\\img\\temp_target.png')

        w = 680
        h = 390

        img = cv2.imread('..\\img\\temp_target.png')

        size = img.shape

        top = int((size[0] - h) / 2)
        height = int(h + ((size[0] - h) / 2))
        left = int((size[1] - w) / 2)
        width = int(w + ((size[1] - w) / 2))

        cropped = img[top:height, left:width]

        # 裁剪尺寸
        cv2.imwrite('..\\img\\temp_target_crop.png', cropped)

        # 新建标签页
        browser.execute_script("window.open('');")

        browser.switch_to.window(browser.window_handles[2])

        browser.get(tempUrl)
        time.sleep(3)

        browser.save_screenshot('..\\img\\temp_temp.png')

        w = 136
        h = 136

        img = cv2.imread('..\\img\\temp_temp.png')

        size = img.shape

        top = int((size[0] - h) / 2)
        height = int(h + ((size[0] - h) / 2))
        left = int((size[1] - w) / 2)
        width = int(w + ((size[1] - w) / 2))

        cropped = img[top:height, left:width]

        cv2.imwrite('..\\img\\temp_temp_crop.png', cropped)

        browser.switch_to.window(handle)
        time.sleep(2)
        browser.switch_to.frame('tcaptcha_iframe')

        # 模糊匹配两张图片
        move = canny_test2('..\\img\\temp_target_crop.png', '..\\img\\temp_temp_crop.png')
        # 计算出拖动距离
        distance = int(move[0] / 2 - 27.5) + 2

        draggable = browser.find_element_by_id('tcaptcha_drag_thumb')

        ActionChains(browser).click_and_hold(draggable).perform()

        # 拖动
        if distance % 10 == 0:
            num = 10
        else:
            num = 11
        n = int(distance / 10)
        # 控制速度
        for i in range(num):
            if i == 10:
                n = distance % 10
            ActionChains(browser).move_by_offset(xoffset=n, yoffset=0).perform()
        ActionChains(browser).release().perform()

        time.sleep(2)
        if isEleExist(browser, 'slideBg'):
            get_move()
    get_move()
    time.sleep(10)

def isEleExist(browser, id):
    try:
        browser.find_element_by_id(id)
        return True
    except:
        return False


if __name__ == '__main__':
    test()
    # (10, 68)
    # canny_test2()
