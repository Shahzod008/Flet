from flet import (app, SnackBar, Column, CrossAxisAlignment, MainAxisAlignment, Text, TextButton, colors, icons, Page,
                  ButtonStyle, NavigationBar, NavigationDestination, AppBar, Row, Container,  MaterialState,
                  RoundedRectangleBorder, TextField, ElevatedButton, alignment, IconButton, CircleAvatar, ListView)
from sqlite3 import connect


def main(page: Page):
    page.bgcolor = "black"

    def shorts_rils_page(e):
        page.clean()
        page.navigation_bar = nav_main_search_profile_new_post
        page.appbar = None
        page.update()

    def new_post_page(e):
        page.clean()
        page.navigation_bar = nav_main_search_profile_new_post
        page.appbar = None
        page.update()

    def show_settings_page(e):
        page.clean()
        page.navigation_bar = nav_main_search_profile_new_post
        appbar("Настройка")
        page.update()

    def show_main_page(e):
        page.clean()
        page.navigation_bar = nav_main_search_profile_new_post
        page.appbar = main_page_appbar
        page.update()

    def show_chat_page(e):
        page.clean()
        appbar("Юзер наме")
        page.update()

    def show_notification_page(e):
        page.clean()
        appbar("Уведомления")
        page.navigation_bar = None
        page.add(Text("чат"))
        page.update()

    def show_search_page(e):
        page.clean()
        page.appbar = None
        page.add(name_input, lv, data_not_found)
        page.navigation_bar = nav_main_search_profile_new_post
        page.update()

    def show_profile_page(e):
        page.clean()
        page.navigation_bar = nav_main_search_profile_new_post
        page.appbar = show_profile_page_appbar
        page.add(show_profile_page_add)
        page.update()

    def reg_auth():
        page.clean()
        reg_auth_panel(text="Регистрация", btn_reg_auth=btn_reg)
        page.navigation_bar = nav_reg_auth
        page.vertical_alignment = MainAxisAlignment.CENTER
        page.horizontal_alignment = MainAxisAlignment.CENTER
        page.update()

    def register(e):
        conn = connect("basa.db")
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS users ("
                    "id INTEGER PRIMARY KEY AUTOINCREMENT,"
                    "username TEXT, "
                    "password TEXT);")
        cur.execute("SELECT * FROM users WHERE username=?", (user_name.value,))
        if cur.fetchone() is not None:
            page.snack_bar = SnackBar(Text("Пользователь с таким логином уже зарегистрирован."))
            page.snack_bar.open = True
            page.update()
        else:
            cur.execute("INSERT INTO users (username, password) VALUES(?, ?);",
                        (user_name.value, user_password.value))
            show_main_page(e)
            conn.commit()
            page.update()
        conn.close()

    def auth(e):
        conn = connect('basa.db')
        cur = conn.cursor()
        cur.execute("SELECT * FROM users WHERE username=? AND password=?",
                    (user_name.value, user_password.value))
        if cur.fetchone() is not None:
            page.snack_bar = SnackBar(Text("Успешная авторизация"), duration=1000)
            page.snack_bar.open = True
            show_main_page(e)
            page.update()
        else:
            page.snack_bar = SnackBar(Text("Неверно введенные данные!"), duration=1000)
            page.snack_bar.open = True
            page.update()
        conn.commit()
        conn.close()

    def navigate_reg_auth(e):
        index = page.navigation_bar.selected_index
        page.clean()
        if index == 0:
            user_name.value = ""
            user_password.value = ""
            reg_auth_panel(text="Регистрация", btn_reg_auth=btn_reg)
            page.update()
        elif index == 1:
            user_name.value = ""
            user_password.value = ""
            reg_auth_panel(text="Авторизация", btn_reg_auth=btn_auth)
            page.update()
        page.update()

    def navigate_index(e):
        index = page.navigation_bar.selected_index
        page.clean()
        if index == 0:
            show_main_page(e)
            page.update()
        elif index == 1:
            show_search_page(e)
            page.update()
        elif index == 2:
            new_post_page(e)
            page.update()
        elif index == 3:
            shorts_rils_page(e)
            page.update()
        elif index == 4:
            show_profile_page(e)
            page.update()
        page.update()

    def validate(e):
        if all([user_name.value, user_password.value]):
            btn_reg.disabled = False
            btn_auth.disabled = False
            page.update()
        else:
            btn_reg.disabled = True
            btn_auth.disabled = True
            page.update()
        page.update()

    def fetch_users(search_name):
        conn = connect('basa.db')
        cursor = conn.cursor()
        cursor.execute("SELECT username FROM users WHERE username LIKE ?", ('%' + search_name + '%',))
        rows = cursor.fetchall()
        conn.close()
        usernames = [row[0] for row in rows]
        return usernames

    def input_search(e):
        search_name = name_input.value.lower()
        my_filer = fetch_users(search_name)
        lv.controls = []

        if not name_input.value == "":
            if len(my_filer) > 0:
                data_not_found.visible = False
                for x in my_filer:
                    lv.controls.append(
                        TextButton(
                            x,
                            height=60,
                            style=ButtonStyle(
                                shape={
                                    MaterialState.HOVERED: RoundedRectangleBorder(radius=0),
                                    MaterialState.DEFAULT: RoundedRectangleBorder(radius=0),
                                }
                            ), expand=True))
                page.update()
                lv.visible = True
                page.update()
            else:
                data_not_found.visible = True
                page.update()
            page.update()
        page.update()

    def reg_auth_panel(text, btn_reg_auth):
        page.add(
            Row(
                controls=[
                    Column(
                        controls=[
                            Text(
                                value=text,
                                size=20,
                            ),
                            user_name,
                            user_password,
                            btn_reg_auth,
                        ],
                        horizontal_alignment=CrossAxisAlignment.CENTER, spacing=20
                    )
                ],
                alignment=MainAxisAlignment.CENTER))

    def appbar(text):
        page.appbar = AppBar(
            leading=Container(
                Row([
                    IconButton(
                        icons.ARROW_BACK_IOS,
                        on_click=show_profile_page
                    ),
                    Text(
                        value=text,
                    )
                ], spacing=-4)
            ),
            bgcolor=colors.BLACK,
            color="white"
        )

    user_name = TextField(
        label="Имя пользователя",
        border_color="white",
        on_change=validate
    )

    user_password = TextField(
        label="Пароль",
        password=True,
        can_reveal_password=True,
        border_color="white",
        on_change=validate
    )

    btn_reg = ElevatedButton(
        text="Зарегистрироваться",
        on_click=register,
        disabled=True,
        color="black",
        bgcolor="white",
        width=300,
        height=50,
        style=ButtonStyle(shape=RoundedRectangleBorder(radius=10))
    )

    btn_auth = ElevatedButton(
        text="Авторизироваться",
        on_click=auth,
        disabled=True,
        color="black",
        bgcolor="white",
        width=300,
        height=50,
        style=ButtonStyle(shape=RoundedRectangleBorder(radius=10))
    )

    nav_reg_auth = NavigationBar(
        destinations=[
            NavigationDestination(
                icon=icons.VERIFIED_USER,
                label="Регистрация",
            ),
            NavigationDestination(
                icon=icons.VERIFIED_USER_OUTLINED,
                label="Войти"
            )
        ],
        on_change=navigate_reg_auth,
        bgcolor="black"
    )

    nav_main_search_profile_new_post = NavigationBar(
        destinations=[
            NavigationDestination(icon=icons.HOME),
            NavigationDestination(icon=icons.SEARCH),
            NavigationDestination(icon=icons.ADD_BOX),
            NavigationDestination(icon=icons.VIDEO_COLLECTION),
            NavigationDestination(icon=icons.SUPERVISED_USER_CIRCLE),
        ],
        on_change=navigate_index,
        bgcolor="black",
    )

    name_input = TextField(
        label="Поиск",
        on_change=input_search,
        border_color="white"
    )

    data_not_found = Text(
        value="Такой пользователь не был найден",
        size=20
    )

    lv = ListView(
        expand=True,
        spacing=10
    )

    data_not_found.visible = False

    show_profile_page_add = Column(
        controls=[
            Row(
                controls=[
                    Column(
                        controls=[
                            CircleAvatar(
                                foreground_image_url="https://avatars.githubusercontent.com/u/5041459?s=88&v=4",
                                width=100, height=100),
                        ], alignment=alignment.center
                    ),
                    Column(
                        controls=[
                            Text("Публикация"),
                            Text("0"),
                        ], horizontal_alignment=CrossAxisAlignment.CENTER
                    ),
                    Column(
                        controls=[
                            Text("Подписчики"),
                            Text("10"),
                        ], horizontal_alignment=CrossAxisAlignment.CENTER
                    ),
                    Column(
                        controls=[
                            Text("Подписки"),
                            Text("12")
                        ], horizontal_alignment=CrossAxisAlignment.CENTER
                    ),
                ], alignment=MainAxisAlignment.SPACE_EVENLY,
            ),
        ], expand=1, horizontal_alignment=CrossAxisAlignment.CENTER
    )

    show_profile_page_appbar = AppBar(
            title=Text(
                value="user_name",
            ),
            bgcolor=colors.BLACK,
            actions=[
                IconButton(icons.ALTERNATE_EMAIL,
                           url="https://play.google.com/store/apps/details?id=com.instagram.barcelona&hl=ru&gl=US"),
                IconButton(icons.MENU, on_click=show_settings_page)
            ],
            color="white"
        )

    main_page_appbar = AppBar(
            title=Text(
                value="Instagram"
            ),
            bgcolor=colors.BLACK,
            actions=[
                IconButton(icons.FAVORITE_BORDER_OUTLINED, on_click=show_notification_page),
                IconButton(icons.CHAT_ROUNDED, on_click=show_chat_page)
            ],
            color="white"
        )

    reg_auth()


app(target=main)
