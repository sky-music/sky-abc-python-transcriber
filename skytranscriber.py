
input_letters = ['Q', 'W', 'E', 'R', 'T', 'A', 'S', 'D', 'F', 'G', 'Z', 'X', 'C', 'V', 'B']
valid_tokens = input_letters + ['(', ')', ' ']
rows = ['A', 'B', 'C']

input_letter_mappings = {}

# Match keyboard to piano grid mapping

for row in rows:
    for column in range(1, 5+1):
        note = row + str(column)
        letter = input_letters.pop(0)
        input_letter_mappings[letter] = note

print('NEW SONG')
song_name = input('Enter name for song: ')

song_file = open(song_name + '.html','w+')
song_file.write("<!DOCTYPE html>\n<html>\n<head>\n<title>My Sky Song</title><style>body {margin: 50px; font-size: 30px; font-family: monospace; line-height: 50px;}span {width: 100px; height: 100px; border-radius: 20px;}.row-A {background-color: #8ed5ff;}.row-B {background-color: #f1a3ff;}.row-C {background-color: #ffa59b;}h1 {font-family: \"Avenir\";}</style></head>")
song_file.write("<body>\n")
song_file.write("<h1>" + song_name + "</h1>" + '\n')

line = input('New line: ')
while line:

    is_invalid_line = False

    result = ''
    current_row = ''
    for token in line.upper():
        if token not in valid_tokens:
            print('Error: Invalid tokens, only QWERT ASDFG ZXCVB ( ) and spaces allowed.')
            break

        else:
            if token in input_letter_mappings.keys():
                note = input_letter_mappings[token]
                current_row = note[0]
                # Style using div
                node_name = "<span class=\"row-" + current_row + "\">" + note + '</span> '
            else:
                note = token
                # Style using div
                node_name = "<span class=\"marker\">" + note + '</span> '

            result += node_name



    song_file.write(result + '<br />' + '\n')


    line = input('New line: ')
    previous_note = ''

print("Done. Please check the file with the name of the song.")
song_file.write("</body>\n</html>")
song_file.close()
