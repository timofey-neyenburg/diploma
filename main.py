import dearpygui.dearpygui as dpg


WIN_W = 1280
WIN_H = 720


app_context = {}


def _mk_handler(callable):
    def _(sender, app_data):
        callable()
    return _


def _startup():
    dpg.create_context()
    dpg.create_viewport(
        title='Calculator',
        width=WIN_W,
        height=WIN_H,
        resizable=False,
    )


def _finalize():
    dpg.setup_dearpygui()

    with dpg.font_registry():
        print("ok")
        with dpg.font("./notomono-regular.ttf", 18, default_font=True, tag="font-ru"):
            dpg.add_font_range_hint(dpg.mvFontRangeHint_Cyrillic)
            dpg.bind_font("font-ru")

    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()


def draw_consumer_card(parent):
    with dpg.child_window(parent=parent, autosize_x=True, height=200, resizable_y=False, ):
        dpg.add_text("Баня")


def gui():
    with dpg.window(
        label="Водопотребление",
        width=WIN_W,
        height=WIN_H,
        no_resize=True,
        no_collapse=True,
        collapsed=False,
        on_close=_mk_handler(exit),
    ):
        with dpg.group(horizontal=True):
            with dpg.child_window(width=500):
                with dpg.child_window(width=480, height=600, border=False):
                    dpg.add_text("Тип потребителя")
                    dpg.add_combo(["Баня"], default_value="Баня")
                    dpg.add_spacer(height=5)
                    dpg.add_text("Норма расхода воды")
                    dpg.add_spacer(height=5)
                    dpg.add_text("В сутки наибольшего потребления")
                    dpg.add_text("Общая (в том числе горячей) q^tot_u")
                    dpg.add_input_int()
                    dpg.add_text("Горячей qhu")
                    dpg.add_input_int()

                with dpg.child_window(
                    width=480,
                    height=50,
                    resizable_y=False,
                    resizable_x=False,
                    border=False,
                ):
                    with dpg.group(horizontal=True) as group:
                        pass


            with dpg.child_window() as cw:
                dpg.add_text("Добавленные потребители:")

            dpg.add_button(
                label="Добавить",
                height=30,
                width=200,
                parent=group,
                callback=lambda _, __: draw_consumer_card(cw),
            )

            dpg.add_button(
                label="Сформировать отчет",
                height=30,
                width=200,
                parent=group,
                callback=lambda _, __: draw_consumer_card(cw),
            )

            with dpg.theme() as container_theme:
                with dpg.theme_component(dpg.mvGroup): #dpg.mvAll):
                    # dpg.add_theme_color(dpg.mvThemeCol_FrameBg, (150, 100, 100), category=dpg.mvThemeCat_Core)
                    # dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 5, category=dpg.mvThemeCat_Core)
                    dpg.add_theme_color(dpg.mvThemeCol_ChildBg, (100, 0, 240), category=dpg.mvThemeCat_Core)

                dpg.bind_item_theme(cw, container_theme)

def main():
    _startup()
    gui()
    _finalize()


if __name__ == "__main__":
    main()
