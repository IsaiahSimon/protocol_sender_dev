from microbit import *
import radio
import speech

radio.on()
radio.config(group=55)
set_volume(20)

alphabet = ["A", "B", "C", "D", "F", "H", "K", "M", "N", "O", "P", "R",]
alphIndex = 0
message = "X"

pronounceDictionary = {
    "A": "AE4AE5Y8",
    "B": "BIYIY4IY3",
    "C": "SIYIY4IY3",
    "D": "DIYIY4IY3",
    "F": "EH4F6F4",
    "H": "/HEH7IY6CH7SH8",
    "K": "Q8K2EH6EH7Y",
    "M": "EH8M6M6",
    "N": "EH8EH5N5N8",
    "O": "OH8OH7OH6OH8",
    "P": "P8P7IY8IY6IY4IY5IY7",
    "R": "AH4R5R7R8",
    "X": "START"
}

display.show(alphabet[alphIndex])

while True:
    if button_a.is_pressed() == 1:
        alphIndex = alphIndex - 1
        if alphIndex < 0:
            alphIndex = len(alphabet)-1;
        print(alphabet[alphIndex], alphIndex)
        display.show(alphabet[alphIndex])
        sleep(125)

    if button_b.is_pressed() == 1:
        alphIndex = alphIndex + 1
        if alphIndex > len(alphabet)-1:
            alphIndex = 0;
        print(alphabet[alphIndex], alphIndex)
        display.show(alphabet[alphIndex])
        sleep(125)

    if button_a.is_pressed() == 1 and button_b.is_pressed() == 1:
        print('sending ' + alphabet[alphIndex] + '...')
        radio.send(alphabet[alphIndex])
        sleep(125)
        display.show(alphabet[alphIndex])
        sleep(125)
        print(alphabet[alphIndex] + ' was sent!')

    message = radio.receive()

    if message == "ok":
        display.show(Image.YES)
        print(alphabet[alphIndex] + ' was received properly!')

    if message:
        radio.send("ok")
        print('We got a message: ' + message)

        display.scroll(message)
        # print(str(pronounceDictionary[message]))
        # speech.pronounce(pronounceDictionary[message])
        speech.say(message)
        display.show(message)

    sleep(125)
