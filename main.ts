radio.onReceivedString(function on_received_string(receivedString: string) {
    basic.showString(receivedString)
})
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    radio.sendString("Yes")
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    radio.sendString("No")
})
radio.setGroup(1)
