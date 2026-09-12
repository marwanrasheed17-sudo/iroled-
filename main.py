def on_ir_button_ok_pressed():
    pass
makerbit.on_ir_button(IrButton.OK, IrButtonAction.PRESSED, on_ir_button_ok_pressed)

OLED.init(128, 64)

def on_forever():
    pass
basic.forever(on_forever)
