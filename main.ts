radio.onReceivedNumber(function on_received_number(receivedNumber: number) {
    
    scrollbit.clear()
    brightness = 50
    if (receivedNumber == 0) {
        status = 0
    } else if (receivedNumber == 1) {
        status = 1
    } else if (receivedNumber == 2) {
        brightness = 100
        status = 2
    } else {
        status = 999
    }
    
})
let brightness = 0
let status = 0
scrollbit.clear()
scrollbit.setUpsideDown(true)
scrollbit.show()
radio.setGroup(1)
status = 0
brightness = 50
basic.forever(function on_forever() {
    if (status == 0) {
        scrollbit.setImage(images.createBigImage(`
            . # # . # . . . # .
            # . . . # . . . . .
            # . . . # # # . # .
            # . . . # . # . # .
            . # # . # . # . # .
            `), 0, 1, brightness)
        scrollbit.setImage(images.createImage(`
            # . . # .
            # . . # .
            # . . # .
            # . . # .
            . # . . #
            `), 10, 1, brightness)
    } else if (status == 1) {
        scrollbit.setImage(images.createBigImage(`
            # . . . # . . . . .
            # . # . # . . # . .
            # . # . # . # . # .
            # . # . # . # . # .
            . # . # . . . # . .
            `), 0, 1, brightness)
        scrollbit.setImage(images.createBigImage(`
            . . . # . . . . . .
            . # . # . # . . . .
            # . . # # . . . . .
            # . . # # . . . . .
            # . . # . # . . . .
            `), 10, 1, brightness)
    } else if (status == 2) {
        scrollbit.setImage(images.createBigImage(`
            # . . . # . # . # .
            # . . . . . # . # .
            # . . . # . # . # .
            # . . . # . # . # .
            # # # . # . . # . .
            `), 0, 1, brightness)
        scrollbit.setImage(images.createBigImage(`
            . # # . . # . . . .
            # . . # . # . . . .
            # # # # . # . . . .
            # . . . . . . . . .
            . # # . . # . . . .
            `), 10, 1, brightness)
    } else {
        scrollbit.setImage(images.createBigImage(`
            # # # . . . . . . .
            # . . . . # . . # .
            # # . . # . . # . .
            # . . . # . . # . .
            # # # . # . . # . .
            `), 0, 1, brightness)
        scrollbit.setImage(images.createBigImage(`
            . . . . . . . . . .
            . # . . . # . . . .
            # . # . # . . . . .
            # . # . # . . . . .
            . # . . # . . . . .
            `), 10, 1, brightness)
    }
    
    scrollbit.show()
})
