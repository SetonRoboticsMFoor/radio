def on_received_string(receivedString):
    basic.show_string(receivedString)

def on_button_pressed_a():
    radio.send_string("Yes")

def on_button_pressed_b():
    radio.send_string("No")


hello = 1

radio.on_received_string(on_received_string)

input.on_button_pressed(Button.A, on_button_pressed_a)


input.on_button_pressed(Button.B, on_button_pressed_b)

radio.set_group(1)

