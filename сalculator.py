from flet import (app, Page, Container, Row, Column, ElevatedButton, TextField, MainAxisAlignment,
                  TextAlign, InputBorder)


def main(page: Page):
    page.window_width = 300
    page.window_height = 350
    page.window_resizable = False
    page.bgcolor = "BLACK"

    page.add(
        Container(
            Column(
                controls=[
                    TextField(value="0", text_align=TextAlign.RIGHT, border=InputBorder.NONE, text_size=35),
                    Row(
                        controls=[
                            ElevatedButton(text="AC", color="white", bgcolor="#828181",),
                            ElevatedButton(text="+/-", color="white", bgcolor="#828181",),
                            ElevatedButton(text="%", color="white", bgcolor="#828181",),
                            ElevatedButton(text="/", color="white", bgcolor="ORANGE",),
                        ],
                        alignment=MainAxisAlignment.SPACE_AROUND
                    ),
                    Row(
                        controls=[
                            ElevatedButton(text="7", color="white", bgcolor="#2e2e2e",),
                            ElevatedButton(text="8", color="white", bgcolor="#2e2e2e",),
                            ElevatedButton(text="9", color="white", bgcolor="#2e2e2e",),
                            ElevatedButton(text="X", color="white", bgcolor="ORANGE",),
                        ],
                        alignment=MainAxisAlignment.SPACE_AROUND
                    ),
                    Row(
                        controls=[
                            ElevatedButton(text="4", color="white", bgcolor="#2e2e2e",),
                            ElevatedButton(text="5", color="white", bgcolor="#2e2e2e",),
                            ElevatedButton(text="6", color="white", bgcolor="#2e2e2e",),
                            ElevatedButton(text="-", color="white", bgcolor="ORANGE",),

                        ],
                        alignment=MainAxisAlignment.SPACE_AROUND
                    ),
                    Row(
                        controls=[
                            ElevatedButton(text="1", color="white", bgcolor="#2e2e2e",),
                            ElevatedButton(text="2", color="white", bgcolor="#2e2e2e",),
                            ElevatedButton(text="3", color="white", bgcolor="#2e2e2e",),
                            ElevatedButton(text="+", color="white", bgcolor="ORANGE",),
                        ],
                        alignment=MainAxisAlignment.SPACE_AROUND
                    ),
                    Row(
                        controls=[
                            ElevatedButton(text="0", color="white", bgcolor="ORANGE", width=120),
                            ElevatedButton(text=".", color="white", bgcolor="ORANGE",),
                            ElevatedButton(text="=", color="white", bgcolor="ORANGE",),
                        ],
                        alignment=MainAxisAlignment.SPACE_AROUND
                    )
                ], alignment=MainAxisAlignment.END,
            )
        )
    )


if __name__ == '__main__':
    app(target=main)
