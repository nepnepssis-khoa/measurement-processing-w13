import csv

# We start by creating all of our variables.

blade_data = []
blade_count = 0
old_light_value = 0
old_time = 0
THRESHOLD = 120
pulse_data = []
pulse_start = 0
pulse_end = 0

morse_data = []
morse_short = 0.02
morse_long = 0.06
morse_threshold = 0.005
morse_word_threshold = 0.06
morse_letter_data = [[]]
letter_data = []

letters = {
    "A": [1, 3],
    "B": [3, 1, 1, 1],
    "C": [3, 1, 3, 1],
    "D": [3, 1, 1],
    "E": [1],
    "F": [3, 1, 1, 1],
    "G": [3, 3, 1],
    "H": [1, 1, 1, 1],
    "I": [1, 1],
    "J": [1, 3, 3, 3],
    "K": [3, 1, 3],
    "L": [1, 3, 1, 1],
    "M": [3, 3],
    "N": [3, 1],
    "O": [3, 3, 3],
    "P": [1, 3, 3, 1],
    "Q": [3, 3, 1, 3],
    "R": [1, 3, 1],
    "S": [1, 1, 1],
    "T": [3],
    "U": [1, 1, 3],
    "V": [1, 1, 1, 3],
    "W": [1, 3, 3],
    "X": [3, 1, 1, 3],
    "Y": [3, 1, 3, 3],
    "Z": [3, 3, 1, 1]
}


def morse_function(pulse):
    morse_pulse = 0
    if (pulse < morse_short + morse_threshold
            and pulse > morse_short - morse_threshold):
        morse_pulse = 1
    if (pulse < morse_long + morse_threshold
            and pulse > morse_long - morse_threshold):
        morse_pulse = 3
    return morse_pulse


def morse_spacer(space_list, append_list):
    row = 0
    for ele in space_list:
        if (ele != 'space'):
            append_list[row].append(ele)
        else:
            append_list.append([])
            row += 1


def morse_translate(spaced_morse_list, morse_code, letter_list):

    for letter in spaced_morse_list:
        for key in morse_code:
            if (letter == morse_code[key]):
                letter_list.append(key)


with open('morse_light_raw.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    # For each row in our data:
    for row in csv_reader:
        # Read the raw light value as an integer
        raw_light_value = int(row[1])
        current_time = float(row[0])

        # Here, you need to write code that stores a thresholded value into the current_light_value variable.
        if (raw_light_value > THRESHOLD):
            current_light_value = 1
        else:
            current_light_value = 0

        # Paste your code from the previous sketch that counts pulses of thresholded data using current_light_value here:
        if (current_light_value != old_light_value):
            if (current_light_value == 1):
                blade_count += 1
                pulse_start = current_time
            else:
                pulse_end = current_time
                pulse_width = current_time - pulse_start
                pulse_data.append([row[0], pulse_width])

                cur_morse_pulse = morse_function(pulse_width)
                if (morse_data):
                    if (current_time -
                        (cur_morse_pulse * morse_short + morse_word_threshold)
                            > old_time):
                        morse_data.append("space")

                morse_data.append(cur_morse_pulse)

                old_morse_pulse = cur_morse_pulse
                old_time = current_time

        old_light_value = current_light_value

        blade_data.append([row[0], current_light_value])

        line_count += 1
    print(f'Processed {line_count} lines.')
    morse_spacer(morse_data, morse_letter_data)
    print(morse_letter_data)
    morse_translate(morse_letter_data, letters, letter_data)
    print(letter_data)

    compressed = ""
    for i in letter_data:
        compressed += i
    print(compressed)

# Now that we have processed the raw data, create a new CSV file that has the blade count vs. time data
f = open("morse_data_output.csv", "w")
for row in blade_data:
    f.write("{0},{1}\n".format(row[0], row[1]))
f.close()

g = open("pulse_data_output.csv", "w")
for row in pulse_data:
    g.write("{0},{1}\n".format(row[0], row[1]))
g.close()
