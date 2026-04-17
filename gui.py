# コントローラの値をリアルタイムで表示するGUI
import flet as ft
import get_value
import threading

# fletのページを作成
def main(page: ft.Page):
    page.title = "コントローラの値表示"
    # windowのサイズを設定
    page.window_width = 400
    page.window_height = 300
    # appbarを作成
    page.appbar = ft.AppBar(
        title=ft.Text(
            "コントローラの値表示",
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
        height=450,
        padding=ft.Padding(30,30,30,30),
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
            height=450,
            padding=ft.Padding(30,30,30,30),
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

    row_cards = ft.Row(
        controls=cards,
        alignment=ft.MainAxisAlignment.CENTER,
    )

    # カードをページに追加
    page.add(row_cards)

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
                
                page.update()
                time.sleep(0.05)  # 50msごとに更新
            except Exception as e:
                print(f"Error: {e}")
                break

    # バックグラウンドスレッドで値の更新を開始
    update_thread = threading.Thread(target=update_controller_values, daemon=True)
    update_thread.start()

# mainの実行
if __name__ == "__main__":
    ft.app(target=main) 