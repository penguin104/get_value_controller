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
        print(f"l_stick: {self.joy_status.l_stick}")
        return self.joy_status.l_stick

    # ジョイスティックの値を取得する関数 -> Rスティックの[x軸, y軸]
    def get_joystick_r_value(self):
        pygame.event.pump()
        self.joy_status = joy_status()
        self.joy_status.r_stick[0] = self.joy.get_axis(2)
        self.joy_status.r_stick[1] = self.joy.get_axis(3)
        print(f"l_stick: {self.joy_status.r_stick}")

        return self.joy_status.r_stick
    
    
    # ハットスイッチの値を取得する関数
    def get_hat_value(self):
        self.joy_status = joy_status()
        self.joy_status.hat_l = self.joy.get_hat(0)[0] == -1
        self.joy_status.hat_r = self.joy.get_hat(0)[0] == 1
        self.joy_status.hat_d = self.joy.get_hat(0)[1] == -1
        self.joy_status.hat_u = self.joy.get_hat(0)[1] == 1
        return [self.joy_status.hat_l, self.joy_status.hat_r, self.joy_status.hat_d, self.joy_status.hat_u]
    
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
        self.joy_status = joy_status()
        self.joy_status.buttons[button_num] = self.joy.get_button(button_num) == 1
        return self.joy_status.buttons[button_num] 

