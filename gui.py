# コントローラの値をリアルタイムで表示するGUI
import flet as ft
import get_value
import threading

# fletのページを作成
def main(page: ft.Page):
    page.title = "コントローラ状態リアルタイム表示"
    # windowのサイズを設定
    page.window.width = 800
    page.window.height = 800
    # appbarを作成
    page.appbar = ft.AppBar(
        title=ft.Text(
            "コントローラ状態リアルタイム表示",
            size=20,
            ),
        center_title=True, # タイトルを中央に配置
        bgcolor=ft.Colors.BLUE_500,
        color=ft.Colors.WHITE,
    )

    # get_value_contolloerのインスタンスを作成
    get_value_controller = get_value.get_value_contolloer()

    # コントローラの値を表示させるカードを作成
    cards = []

    # 各種ボタンの状態を表示するカード

    # ボタンの状態を表示させるContainer

    b_button = ft.Container(
        width=50,
        height=50,
        bgcolor= ft.Colors.BLUE if get_value_controller.get_button_value(0) else ft.Colors.GREY_300,
        content=ft.Text("B", size=20,color=ft.Colors.WHITE),
        alignment=ft.alignment.center,
    )
    a_button = ft.Container(
        width=50,
        height=50,
        bgcolor= ft.Colors.BLUE if get_value_controller.get_button_value(1) else ft.Colors.GREY_300,
        content=ft.Text("A", size=20,color=ft.Colors.WHITE),
        alignment=ft.alignment.center,
    )
    y_button = ft.Container(
        width=50,
        height=50,
        bgcolor= ft.Colors.BLUE if get_value_controller.get_button_value(2) else ft.Colors.GREY_300,
        content=ft.Text("Y", size=20,color=ft.Colors.WHITE),
        alignment=ft.alignment.center,
    )
    x_button = ft.Container(
        width=50,
        height=50,
        bgcolor= ft.Colors.BLUE if get_value_controller.get_button_value(3) else ft.Colors.GREY_300,
        content=ft.Text("X", size=20,color=ft.Colors.WHITE),
        alignment=ft.alignment.center,
    )

    # 右側のボタン
    right_buttons_card = ft.Container(
        width=350,
        height=250,
        # padding=ft.Padding(30,30,30,30),
        content=ft.Card(
            content=ft.Container(
                padding=ft.Padding(20,20,20,20),
                content=ft.Column(
                    controls=[
                        ft.Text("右側のボタンの状態"),
                        ft.Column(
                            controls=[
                                ft.Row(
                                    controls=[
                                        ft.Container(width=50, height=50),  # スペース
                                        x_button,
                                        ft.Container(width=50, height=50),  # スペース
                                    ],
                                    alignment=ft.MainAxisAlignment.CENTER,
                                ),
                                ft.Row(
                                    controls=[
                                        y_button,
                                        ft.Container(width=50, height=50),  # スペース
                                        a_button,
                                    ],
                                    alignment=ft.MainAxisAlignment.CENTER,
                                ),
                                ft.Row(
                                    controls=[
                                        ft.Container(width=50, height=50),  # スペース
                                        b_button,
                                        ft.Container(width=50, height=50),  # スペース
                                    ],
                                    alignment=ft.MainAxisAlignment.CENTER,
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),
                    ],
                ),
            ),           
            width=350,
            height=50,
        ),
    )

    cards.append(right_buttons_card)

    # 十字キーの状態を表示するContainer
    hat_values = get_value_controller.get_hat_value()
    up_button = ft.Container(
        width=50,
        height=50,
        bgcolor= ft.Colors.BLUE if hat_values[1] else ft.Colors.GREY_300,
        content=ft.Text("↑", size=20,color=ft.Colors.WHITE),
        alignment=ft.alignment.center,
    )
    down_button = ft.Container(
        width=50,
        height=50,
        bgcolor= ft.Colors.BLUE if hat_values[3] else ft.Colors.GREY_300,
        content=ft.Text("↓", size=20,color=ft.Colors.WHITE),
        alignment=ft.alignment.center,
    )
    left_button = ft.Container(
        width=50,
        height=50,
        bgcolor= ft.Colors.BLUE if hat_values[2] else ft.Colors.GREY_300,
        content=ft.Text("←", size=20,color=ft.Colors.WHITE),
        alignment=ft.alignment.center,
    )
    right_button = ft.Container(
        width=50,
        height=50,
        bgcolor= ft.Colors.BLUE if hat_values[0] else ft.Colors.GREY_300,
        content=ft.Text("→", size=20,color=ft.Colors.WHITE),
        alignment=ft.alignment.center,
    )

    # 十字キーのカード
    d_pad_card = ft.Container(
        width=350,
        height=250,
        # padding=ft.Padding(30,30,30,30),
        content=ft.Card(
            content=ft.Container(
                padding=ft.Padding(20,20,20,20),
                content=ft.Column(
                    controls=[
                        ft.Text("十字キーの状態"),
                        ft.Column(
                            controls=[
                                ft.Row(
                                    controls=[
                                        ft.Container(width=50, height=50),  # スペース
                                        up_button,
                                        ft.Container(width=50, height=50),  # スペース
                                    ],
                                    alignment=ft.MainAxisAlignment.CENTER,
                                ),
                                ft.Row(
                                    controls=[
                                        left_button,
                                        ft.Container(width=50, height=50),  # スペース
                                        right_button,
                                    ],
                                    alignment=ft.MainAxisAlignment.CENTER,
                                ),
                                ft.Row(
                                    controls=[
                                        ft.Container(width=50, height=50),  # スペース
                                        down_button,
                                        ft.Container(width=50, height=50),  # スペース
                                    ],
                                    alignment=ft.MainAxisAlignment.CENTER,
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),
                    ],
                ),
            ),           
            width=350,
            height=50,
        ),
    )

    cards.append(d_pad_card)
    l_stick_progress_bar_x = ft.ProgressBar(
        width=200,
        height=20,
        value=0,
    )
    l_stick_progress_bar_y = ft.ProgressBar(
        width=200,
        height=20,
        value=0,
    )
    r_stick_progress_bar_x = ft.ProgressBar(
        width=200,
        height=20,
        value=0,
    )
    r_stick_progress_bar_y = ft.ProgressBar(
        width=200,
        height=20,
        value=0,
    )

    l_stick_card = ft.Container(
        width=350,
        height=150,
        # padding=ft.Padding(30,30,30,30),
        content=ft.Card(
            content=ft.Container(
                padding=ft.Padding(20,20,20,20),
                content=ft.Column(
                    controls=[
                        ft.Text("Lスティックの値"),
                        # x軸とy軸の値を表示するためのProgressBarを作成
                        # x軸の値を表示するProgressBar
                        ft.Row(
                            controls=[
                                ft.Text("x軸"),
                                l_stick_progress_bar_x,
                            ]
                        ),
                        # y軸の値を表示するProgressBar
                        ft.Row(
                            controls=[
                                ft.Text("y軸"),
                                l_stick_progress_bar_y,
                            ]
                        ),
                    ],
                ),
            ),           
            width=350,
            height=50,
        ),
    )
    cards.append(l_stick_card)

    # 右スティックのカードを作成
    r_stick_card = ft.Container(
            width=350,
            height=150,
            # padding=ft.Padding(30,30,30,30),
            content=ft.Card(
                content=ft.Container(
                padding=ft.Padding(20,20,20,20),
                    content=ft.Column(
                        controls=[
                            ft.Text("Rスティックの値"),                    
                        ft.Row(
                            controls=[
                                ft.Text("x軸"),
                                r_stick_progress_bar_x,
                            ]
                        ),
                        ft.Row(
                            controls=[
                                ft.Text("y軸"),
                                r_stick_progress_bar_y,
                            ]
                        ),
                    ]
                ),
                width=350,
                height=50,
            ),
        )
    )
    cards.append(r_stick_card)

    # 右トリガーと左トリガーのカードを作成
    # トリガーの値を表示するProgressBarを作成
    l_trigger = ft.ProgressBar(
        width=200, 
        height=20,
        value=0,
    )
    r_trigger = ft.ProgressBar(
        width=200,
        height=20,
        value=0,
    )

    #l_switchとr_switchのコンテナを作成
    # l_switch = ft.Container(
    #     width= 150,
    #     height=40,
    #     bgcolor=ft.Colors.BLUE if get_value_controller.get_l_switch_value() else ft.Colors.GREY_300,
    #     content=ft.Text("Lスイッチ", size=20, color=ft.Colors.WHITE),
    #     alignment=ft.alignment.center, 
    # )
    # r_switch = ft.Container(
    #     width= 150,
    #     height=40,
    #     bgcolor=ft.Colors.BLUE if get_value_controller.get_r_switch_value() else ft.Colors.GREY_300,
    #     content=ft.Text("Rスイッチ", size=20, color=ft.Colors.WHITE),
    #     alignment=ft.alignment.center, 
    # )  

    l_trigger_card = ft.Container(
        width=350,
        height=150,
        # padding=ft.Padding(30,30,30,30),
        content=ft.Card(
            content=ft.Container(
                padding=ft.Padding(20,20,20,20),
                content=ft.Column(
                    controls=[ft.Text("Lトリガーの値"), l_trigger],
                    expand=True,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
            ),
            width=350,
            height=50,
        ),
    )
    cards.append(l_trigger_card)

    r_trigger_card = ft.Container(
        width=350,
        height=150,
        # padding=ft.Padding(30,30,30,30),
        content=ft.Card(
            content=ft.Container(
                padding=ft.Padding(20,20,20,20),
                content=ft.Column(
                    controls=[ft.Text("Rトリガーの値"), r_trigger],
                    expand=True,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
            ),
            width=350,
            height=50,
        ),
    )
    cards.append(r_trigger_card)

    # カードレイアウトを作成

    cards_layout = ft.Column(
        controls=[
            ft.Row(
                controls=[ 
                    l_trigger_card,
                    r_trigger_card,
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            ft.Row(
                controls=[ 
                    d_pad_card,
                    right_buttons_card,
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ), 
            ft.Row(
                controls=[
                    l_stick_card,
                    r_stick_card,
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
        ]
    )



    # カードをページに追加
    page.add(cards_layout)

    # 定期的にコントローラの値を更新する関数
    def update_controller_values():
        import time
        while True:
            try:
                # 左スティックの値を取得
                l_stick_values = get_value_controller.get_joystick_l_value()
                l_stick_progress_bar_x.value = (l_stick_values[0] + 1) / 2
                l_stick_progress_bar_y.value = (l_stick_values[1] + 1) / 2
                
                # 右スティックの値を取得
                r_stick_values = get_value_controller.get_joystick_r_value()
                r_stick_progress_bar_x.value = (r_stick_values[0] + 1) / 2
                r_stick_progress_bar_y.value = (r_stick_values[1] + 1) / 2
                
                # ボタンの状態を更新
                a_button.bgcolor = ft.Colors.BLUE if get_value_controller.get_button_value(1) else ft.Colors.GREY_300
                b_button.bgcolor = ft.Colors.BLUE if get_value_controller.get_button_value(0) else ft.Colors.GREY_300
                x_button.bgcolor = ft.Colors.BLUE if get_value_controller.get_button_value(3) else ft.Colors.GREY_300
                y_button.bgcolor = ft.Colors.BLUE if get_value_controller.get_button_value(2) else ft.Colors.GREY_300
                
                # 十字キーの状態を更新
                hat_values = get_value_controller.get_hat_value()
                up_button.bgcolor = ft.Colors.BLUE if hat_values[1] else ft.Colors.GREY_300
                down_button.bgcolor = ft.Colors.BLUE if hat_values[3] else ft.Colors.GREY_300
                left_button.bgcolor = ft.Colors.BLUE if hat_values[2] else ft.Colors.GREY_300
                right_button.bgcolor = ft.Colors.BLUE if hat_values[0] else ft.Colors.GREY_300

                # トリガーの状態を更新
                l_trigger.value = (get_value_controller.get_l_trigger_value() + 1) / 2
                r_trigger.value = (get_value_controller.get_r_trigger_value() + 1) / 2  
                # スイッチの状態を更新
                # l_switch.bgcolor = ft.Colors.BLUE if get_value_controller.get_l_switch_value() else ft.Colors.GREY_300
                # r_switch.bgcolor = ft.Colors.BLUE if get_value_controller.get_r_switch_value() else ft.Colors.GREY_300
                page.update()
                time.sleep(0.05)
            except Exception as e:
                print(f"Error: {e}")
                break

    update_thread = threading.Thread(target=update_controller_values, daemon=True)
    update_thread.start()

# mainの実行
if __name__ == "__main__":
    ft.app(target=main) 