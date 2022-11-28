from microbit import *
import radio                     # Import Radio Functions
import speech

radio.on()                       # Turn the Radio on
radio.config(group=55)
set_volume(20)

# Store alphabet
alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]       
alphIndex = 0                    # Initialise the index variable

# Pronounciations are adjustable using the documentation
# https://microbit-micropython.readthedocs.io/en/v2-docs/speech.html
pronounceDictionary = {
    "A": "AE4AE5Y8",
    "B": "BIYIY4IY3",
    "C": "SIYIY4IY3",
    "D": "DIYIY4IY3",
    "E": "IYIYIY4IY3",
    "F": "EH4F6F4",
    "G": "J8IYIY8IY7IY6IY4IY3IY2",
    "H": "/HEH7IY6CH7SH8",
    "I": "AY8",
    "J": "J8EH6EH7Y",
    "K": "Q8K2EH6EH7Y",
    "L": "EHL3", 
    "M": "EH8M6M6",
    "N": "EH8EH5N5N8",
    "O": "OH8OH7OH6OH8",
    "P": "P8P7IY8IY6IY4IY5IY7",
    "Q": "KYUW4",
    "R": "AH4R5R7R8",
    "S": "EH4S7S8",
    "T": "T8IY4IY6",
    "U": "YUX6UX4",
    "V": "VIY4IY3IY2",
    "W": "DUH4B UHL YUX6UX4",
    "X": "EH4KSS7",
    "Y": "WAHAY8",
    "Z": "ZZIYIY4IY2"
}

display.show(alphabet[alphIndex])                       # Display currently indexed character 

while True: 
    if button_a.is_pressed() == 1:                      # Check if button A is pressed
        alphIndex = alphIndex - 1                       # If it is decrement the Alphabet index
        if alphIndex < 0:                               # Check if alphIndex is still in range
            alphIndex = len(alphabet)-1;                # Reset index to last index
        print(alphabet[alphIndex], alphIndex)
        display.show(alphabet[alphIndex])               # Display Indexed Character 
        sleep(125)  
    
    if button_b.is_pressed() == 1:                      # Check if button B is pressed
        alphIndex = alphIndex + 1                       # If it is increment the Alphabet index
        if alphIndex > len(alphabet)-1:                 # Check if alphIndex is still in range
            alphIndex = 0;                              # Reset index to zero
        print(alphabet[alphIndex], alphIndex)
        display.show(alphabet[alphIndex])               # Display Indexed Character 
        sleep(125)                                      # sleep for debouncing
    
    # if button_a.is_pressed and button_b.is_pressed() == 1:                      # Check if button B is pressed
    #     radio.send(alphabet[alphIndex])                 # Send current character
    #     sleep(125)                                      # sleep for debouncing

    if pin0.is_touched():                                 # Change this conditional to A+B button before flashing to microbit
        print('sending ' + alphabet[alphIndex] + '...')
        radio.send(alphabet[alphIndex])                 # Send current character
        sleep(125)
        display.show(alphabet[alphIndex])
        sleep(125)
        print(alphabet[alphIndex] + ' was sent!')
        
    message = radio.receive() 

    if message == "ok":
        display.show(Image.YES)
        print(alphabet[alphIndex] + ' was received properly!')                   
        
    if message:                                        # if there is a message        
        #send back a confirmation
        radio.send("ok")
        print('We got a message: ' + message)
        
        display.scroll(message)                        # Scroll the incoming character
        speech.pronounce(pronounceDictionary[message])
        display.show(message)

    sleep(125)                                          # sleep to save cycles
    



