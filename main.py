import aircv as ac
import pyautogui
from PIL import ImageGrab


# 识别签到滑块位置
def match_img(img_source, img_search, threshold=0.5):
    img_provider = ac.imread(img_source)
    img_target = ac.imread(img_search)

    match_result = ac.find_template(img_provider, img_target, threshold)
    if match_result is not None:
        match_result['shape'] = (img_provider[1], img_provider[0])  # 0为高，1为宽

    return match_result


# 拖动签到滑块
def drag(start_x, start_y, drag_distance):
    pyautogui.moveTo(start_x, start_y, 0.5)
    pyautogui.dragRel(drag_distance, 0, 0.5)


# 全屏截图
def screen_shot():
    img = ImageGrab.grab()
    img.save("screenshot.png")


# 获取目标按钮的中心
def get_center(pos_rectangle):
    pos_x = 0
    pos_y = 0
    for index in range(len(pos_rectangle["rectangle"])):
        pos_x += pos_rectangle["rectangle"][index][0]
        pos_y += pos_rectangle["rectangle"][index][1]
    return [pos_x / 4, pos_y / 4]

while 1:
    screen_shot()
    pos = match_img("screenshot.png", "target.png")
    print(pos)
    if pos["confidence"] > 0.9:
        print("检测到目标，开始拖动")
        center = get_center(pos)
        print(center)
        drag(center[0], center[1], 300)
