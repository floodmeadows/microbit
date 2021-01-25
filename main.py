def on_received_number(receivedNumber):
    global brightness, status
    scrollbit.clear()
    brightness = 50
    if receivedNumber == 0:
        status = 0
    elif receivedNumber == 1:
        status = 1
    elif receivedNumber == 2:
        brightness = 100
        status = 2
    else:
        status = 999
radio.on_received_number(on_received_number)

brightness = 0
status = 0
scrollbit.clear()
scrollbit.set_upside_down(True)
scrollbit.show()
radio.set_group(1)
status = 0
brightness = 50

def on_forever():
    if status == 0:
        scrollbit.set_image(images.create_big_image("""
            . # # . # . . . # .
            # . . . # . . . . .
            # . . . # # # . # .
            # . . . # . # . # .
            . # # . # . # . # .
            """),
            0,
            1,
            brightness)
        scrollbit.set_image(images.create_image("""
            # . . # .
            # . . # .
            # . . # .
            # . . # .
            . # . . #
            """),
            10,
            1,
            brightness)
    elif status == 1:
        scrollbit.set_image(images.create_big_image("""
            # . . . # . . . . .
            # . # . # . . # . .
            # . # . # . # . # .
            # . # . # . # . # .
            . # . # . . . # . .
            """),
            0,
            1,
            brightness)
        scrollbit.set_image(images.create_big_image("""
            . . . # . . . . . .
            . # . # . # . . . .
            # . . # # . . . . .
            # . . # # . . . . .
            # . . # . # . . . .
            """),
            10,
            1,
            brightness)
    elif status == 2:
        scrollbit.set_image(images.create_big_image("""
            # . . . # . # . # .
            # . . . . . # . # .
            # . . . # . # . # .
            # . . . # . # . # .
            # # # . # . . # . .
            """),
            0,
            1,
            brightness)
        scrollbit.set_image(images.create_big_image("""
            . # # . . # . . . .
            # . . # . # . . . .
            # # # # . # . . . .
            # . . . . . . . . .
            . # # . . # . . . .
            """),
            10,
            1,
            brightness)
    else:
        scrollbit.set_image(images.create_big_image("""
            # # # . . . . . . .
            # . . . . # . . # .
            # # . . # . . # . .
            # . . . # . . # . .
            # # # . # . . # . .
            """),
            0,
            1,
            brightness)
        scrollbit.set_image(images.create_big_image("""
            . . . . . . . . . .
            . # . . . # . . . .
            # . # . # . . . . .
            # . # . # . . . . .
            . # . . # . . . . .
            """),
            10,
            1,
            brightness)
    scrollbit.show()
basic.forever(on_forever)
