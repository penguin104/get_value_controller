import pygame
# import time


#  ジョイスティックの状態を保存するクラス
class joy_status:
    def __init__(self):
        # ジョイスティックの状態を保存する配列[x軸, y軸]
        self.l_stick = [0,0]
        self.r_stick = [0,0]
        # ハットスイッチの状態を保存する変数
        self.hat_l = 0
        self.hat_r = 0
        self.hat_d = 0
        self.hat_u = 0
        # ボタンの状態を保存する配列
        self.buttons = [0,0,0,0,0,0,0,0,0,0,0,0]

# コントローラの値を取得するクラス
class get_value_contolloer:
    def __init__(self):
        self.pygame = pygame
        pygame.init()
        pygame.joystick.init()
        
        self.joy = pygame.joystick.Joystick(0)
        self.joy.init()
        
        
    # ジョイスティックの値を取得する関数 -> Lスティックの[x軸, y軸]
    def get_joystick_l_value(self):
        
        pygame.event.pump()
        self.joy_status = joy_status()
        self.joy_status.l_stick[0] = self.joy.get_axis(0)
        self.joy_status.l_stick[1] = self.joy.get_axis(1)
        # print(f"l_stick: {self.joy_status.l_stick}")
        return self.joy_status.l_stick

    # ジョイスティックの値を取得する関数 -> Rスティックの[x軸, y軸]
    def get_joystick_r_value(self):
        pygame.event.pump()
        self.joy_status = joy_status()
        self.joy_status.r_stick[0] = self.joy.get_axis(2)
        self.joy_status.r_stick[1] = self.joy.get_axis(3)
        # print(f"l_stick: {self.joy_status.r_stick}")

        return self.joy_status.r_stick

    # トリガーの値を取得する関数 -> Lトリガー
    def get_l_trigger_value(self):
        pygame.event.pump()
        if self.joy.get_numaxes() > 4:
            return self.joy.get_axis(4)
        return 0.0

    # トリガーの値を取得する関数 -> Rトリガー
    def get_r_trigger_value(self):
        pygame.event.pump()
        if self.joy.get_numaxes() > 5:
            return self.joy.get_axis(5)
        return 0.0
    
    def get_l_switch_value(self):
        pygame.event.pump()
        if self.joy.get_numbuttons() > 4 and self.get_button_value(4):
            return True
        if self.joy.get_numbuttons() > 6 and self.get_button_value(6):
            return True
        if self.joy.get_numaxes() > 4:
            axis_value = self.joy.get_axis(4)
            return axis_value > 0.5
        return False
    
    def get_r_switch_value(self):
        pygame.event.pump()
        if self.joy.get_numbuttons() > 5 and self.get_button_value(5):
            return True
        if self.joy.get_numbuttons() > 7 and self.get_button_value(7):
            return True
        if self.joy.get_numaxes() > 5:
            axis_value = self.joy.get_axis(5)
            return axis_value > 0.5
        return False
    
    
    # ハットスイッチの値を取得する関数 (十字キー)
    def get_hat_value(self):
        pygame.event.pump()
        self.joy_status = joy_status()

        def try_button_mapping(mapping):
            num_buttons = self.joy.get_numbuttons()
            if all(index < num_buttons for index in mapping.values()):
                values = {name: self.joy.get_button(idx) for name, idx in mapping.items()}
                if any(values.values()):
                    self.joy_status.hat_u = bool(values.get("up", False))
                    self.joy_status.hat_r = bool(values.get("right", False))
                    self.joy_status.hat_d = bool(values.get("down", False))
                    self.joy_status.hat_l = bool(values.get("left", False))
                    return True
            return False

        try:
            if self.joy.get_numhats() > 0:
                hat = self.joy.get_hat(0)
                self.joy_status.hat_l = hat[0] == -1
                self.joy_status.hat_r = hat[0] == 1
                self.joy_status.hat_d = hat[1] == -1
                self.joy_status.hat_u = hat[1] == 1
            else:
                axis_detected = False
                if self.joy.get_numaxes() > 6:
                    axis6 = self.joy.get_axis(6)
                    axis7 = self.joy.get_axis(7) if self.joy.get_numaxes() > 7 else 0
                    self.joy_status.hat_l = axis6 < -0.5
                    self.joy_status.hat_r = axis6 > 0.5
                    self.joy_status.hat_d = axis7 < -0.5
                    self.joy_status.hat_u = axis7 > 0.5
                    axis_detected = any([
                        self.joy_status.hat_l,
                        self.joy_status.hat_r,
                        self.joy_status.hat_d,
                        self.joy_status.hat_u,
                    ])

                if not axis_detected:
                    # PS4のD-padがボタンとして実装される場合へのフォールバック
                    candidates = [
                        {"up": 12, "right": 15, "down": 13, "left": 14},
                        {"up": 13, "right": 15, "down": 14, "left": 16},
                        {"up": 10, "right": 11, "down": 12, "left": 13},
                        {"up": 7, "right": 8, "down": 9, "left": 10},
                    ]
                    for mapping in candidates:
                        if try_button_mapping(mapping):
                            break
                    else:
                        self.joy_status.hat_l = False
                        self.joy_status.hat_r = False
                        self.joy_status.hat_d = False
                        self.joy_status.hat_u = False
        except pygame.error:
            self.joy_status.hat_l = False
            self.joy_status.hat_r = False
            self.joy_status.hat_d = False
            self.joy_status.hat_u = False

        return [
            self.joy_status.hat_l,
            self.joy_status.hat_r,
            self.joy_status.hat_d,
            self.joy_status.hat_u,
        ]
    
    # 個別のボタンを取得する関数
    # button_numは0から11までの整数で、対応するボタンの値を取得する
    # ボタンの種類は以下の通り
    # 0: Aボタン
    # 1: Bボタン
    # 2: Xボタン
    # 3: Yボタン
    # 4: LBボタン
    # 5: RBボタン
    # 6: Backボタン
    # 7: Startボタン
    # 8: Lスティックボタン
    # 9: Rスティックボタン
    # 10: Xboxボタン
    # 11: その他のボタン
    def get_button_value(self, button_num):
        pygame.event.pump()
        self.joy_status = joy_status()
        self.joy_status.buttons[button_num] = self.joy.get_button(button_num) == 1
        return self.joy_status.buttons[button_num] 

