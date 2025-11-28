import time


##
#
# Classes for interactive Calliope control elements.
#
##

last_pressed_button = None
butten_input_was_processed = False


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
    last_pressed_button = None
    button_input_was_processed = False

    @staticmethod
    def button_is_pressed(char_to_test: str) -> bool:
        if input_sim.button_input_was_processed:
            input_sim.last_pressed_button = None
            input_sim.button_input_was_processed = False
            return False

        if input_sim.last_pressed_button is None:
            input_string = input("Press any button (z.B. a/b): ").strip().lower()
            input_sim.last_pressed_button = input_string

        if char_to_test == input_sim.last_pressed_button:
            input_sim.button_input_was_processed = True
            return True
        else:
            # Falscher Button, aber noch NICHT verarbeitet – vielleicht passt die Eingabe
            # zur nächsten Abfrage in diesem Schleifendurchlauf.
            return False

        
class BasicSim:
    def __init__(self, forever_test_count=7):
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
        time.sleep(0.001*time_to_sleep)

    @staticmethod
    def clear_screen() -> None:
        print("")
