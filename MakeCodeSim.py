import time


##
#
# Classes for interactive Calliope control elements.
#
##


class Button:
    A = "a"
    B = "b"


class TouchPin:
    P0 = "p0"
    P1 = "p1"
    P2 = "p2"
    P3 = "p3"


def test_func():
    print("Testing")


class input_sim:
    state = 0

    @staticmethod
    def button_is_pressed(char_to_test: str) -> bool:
        # print("char_to_test", char_to_test)
        input_string = input("Press any button.")
        # print("input_string", input_string)

        return char_to_test == input_string


class BasicSim:
    def __init__(self, forever_test_count=5):
        self.state = 0  # 0 = läuft, 1 = stoppen
        self.forever = int(forever_test_count)

    def forever(self, func_to_run):
        try:
            while self.state == 0:
                func_to_run()
        except KeyboardInterrupt:
            print("Exiting forever loop.")
            
    def forever_test(self, func_to_run):
        for i in range(0, self.forever):
            func_to_run()       

    @staticmethod
    def show_string(string_value: str) -> None:
        print(string_value)

    @staticmethod
    def show_number(int_value: int) -> None:
        print(int_value)

    @staticmethod
    def pause(time_to_sleep: int) -> None:
        time.sleep(time_to_sleep)

    @staticmethod
    def clear_screen() -> None:
        print("")
