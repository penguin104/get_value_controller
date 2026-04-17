import time

import get_value

# get_value_controllerクラスのインスタンスを作成
get_value_controller = get_value.get_value_contolloer()

while True:
    print(f"Lスティックの値: {get_value_controller.get_joystick_l_value()}")
    #1秒待機    
    time.sleep(1)
