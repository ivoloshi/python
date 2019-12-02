##########################################
# NAME: Maya Voloshin
# ID: 322853680
# login: mayavolo
# DESCRIPTION: ex5
##########################################

import sys
import os

def check_input_args(args):
    """
    checks if the given arguments exist and are legal
    :param args: the files
    :return: none if everything is legal, a message if not
    """

    # Checking if there are four parameters as requested
    if len(args) != 4:
        message = 'The Number of Parameters is not suitable'
        return message

    if not os.path.isfile(args[0]):
        message = "Word file does not exist"
        return message

    if not os.path.isfile(args[1]):
        message = "Matrix file does not exist"
        return message

    # Checking if the given directions are legal
    legal_directions = {'u', 'd', 'r', 'l', 'w', 'x', 'y', 'z'}
    for i in range(len(args[3])):
        if not args[3][i] in legal_directions:
            message = "The directions are illegal"
            return message
    return

def read_wordlist_file(filename):  # OKAYYYYYYYYYYYYYYY
    """
    returns a list of words from the given file
    :param filename: word list text file
    :return: word list
    """
    words_list = []
    f = open(filename)
    line = f.readline()
    words_list.append(line.strip())
    # use the read line to read further.
    # If the file is not empty keep reading one line
    # at a time, till the file is empty
    while line:
        line = f.readline()
        words_list.append(line.strip())
    f.close()
    words_list.pop()
    return words_list


def read_matrix_file(filename):  # OKAYYYYYY
    """
    creates and returns a list of lists from the given char matrix
    :param filename: a char matrix text file
    :return: a list of char lists
    """
    matrix_list = []
    f = open(filename)
    line = f.readline().strip()
    split_chars = line.split(',')
    matrix_list.append(split_chars)
    while line:
        line = f.readline().strip()
        split_chars = line.split(',')
        matrix_list.append(split_chars)
    f.close()
    matrix_list.pop()
    return matrix_list


def count_occurrences_in_string(string, substring):
    """
    searches for all of the occurrences of a substring in a string
    :param string: the string that we search in
    :param substring: the substring that is searched
    :return: number of the substring occurrences
    """
    count = 0
    start = 0
    if len(substring) > len(string):
        return count

    while start < len(string):
        flag = string.find(substring, start)
        if flag != -1:
            start = flag + 1
            count += 1
        else:
            return count
    return count


def right_direction_search_word(word, matrix):
    """
    searches for the occurrences of the word in the right direction only
    :param word: the searched word
    :param matrix: the char matrix that is searches in
    :return: number of occurrences in the right direction
    """
    counter = 0
    for row in range(len(matrix)):
        line = ''.join(matrix[row])
        counter += count_occurrences_in_string(line, word)
    return counter


def left_direction_search_word(word, matrix):
    """
        searches for the occurrences of the word in the left direction only
        :param word: the searched word
        :param matrix: the char matrix that is searches in
        :return: number of occurrences in the left direction
        """
    counter = 0
    for row in range(len(matrix)):
        line = ''.join(matrix[row])
        reverse_line = line[::-1]
        counter += count_occurrences_in_string(reverse_line, word)
    return counter


def down_direction_search_word(word, matrix):
    """
    searches for the occurrences of the word in the "down" direction only
    :param word: the searched word
    :param matrix: the char matrix that is searches in
    :return: number of occurrences in the down direction
    """
    counter = 0
    for col in range(len(matrix[0])):
        line_list = []
        for row in range(len(matrix)):
            line_list.append(matrix[row][col])
        line = ''.join(line_list)
        counter += count_occurrences_in_string(line, word)
    return counter


def up_direction_search_word(word, matrix):
    """
    searches for the occurrences of the word in the "up" direction only
    :param word: the searched word
    :param matrix: the char matrix that is searches in
    :return: number of occurrences in the up direction
    """
    counter = 0
    for col in range(len(matrix[0])):
        line_list = []
        for row in range(len(matrix) - 1, -1, -1):
            line_list.append(matrix[row][col])
        line = ''.join(line_list)
        counter += count_occurrences_in_string(line, word)
    return counter


def diag_up_right_direction_search_word(word, matrix):
    counter = 0
    row = 0
    col = 0

    for i in range(len(matrix)):
        col = 0
        line_list = []
        row = i
        #  print(f'i = {i}')
        while (row + col) == i and row >= 0 and col < len(matrix[0]):
            #  print(f'row = {row} col = {col}')
            line_list.append(matrix[row][col])
            row -= 1
            col += 1
        line = ''.join(line_list)
        #  print(f'line = {line}')
        counter += count_occurrences_in_string(line, word)

    for i in range(1, len(matrix[0])):
        col = i
        row = len(matrix) - 1
        s = col + row
        line_list = []
        while (row + col) == s and row >= 0 and col < len(matrix[0]):
            line_list.append(matrix[row][col])
            row -= 1
            col += 1
        line = ''.join(line_list)
        # print(f'line = {line}')
        counter += count_occurrences_in_string(line, word)
    return counter


def diag_down_left_direction_search_word(word, matrix):
    counter = 0
    row = 0
    col = 0

    for i in range(len(matrix)):
        col = 0
        line_list = []
        row = i
        while (row + col) == i and row >= 0 and col < len(matrix[0]):
            line_list.append(matrix[row][col])
            row -= 1
            col += 1
        line = ''.join(line_list)
        reverse_line = line[::-1]
        counter += count_occurrences_in_string(reverse_line, word)

    for i in range(1, len(matrix[0])):
        col = i
        row = len(matrix) - 1
        s = col + row
        line_list = []
        while (row + col) == s and row >= 0 and col < len(matrix[0]):
            line_list.append(matrix[row][col])
            row -= 1
            col += 1
        line = ''.join(line_list)
        reverse_line = line[::-1]
        counter += count_occurrences_in_string(reverse_line, word)
    return counter


def diag_up_left_direction_search_word(word, matrix):
    counter = 0
    row = len(matrix)
    col = 0

    for i in range(len(matrix[0])):
        line_list = []
        row = len(matrix) - 1
        col = i
        while row >= 0 and col >= 0:
            line_list.append(matrix[row][col])
            row -= 1
            col -= 1
        line = ''.join(line_list)
        counter += count_occurrences_in_string(line, word)

    for i in range(len(matrix[0]) - 1, -1, -1):
        line_list = []
        row = i
        col = len(matrix[0]) - 1
        while is_valid_index(col, row, matrix):
            line_list.append(matrix[row][col])
            row -= 1
            col -= 1
        line = ''.join(line_list)
        counter += count_occurrences_in_string(line, word)

    return counter


def diag_down_right_direction_search_word(word, matrix):
    counter = 0
    row = len(matrix)
    col = 0

    for i in range(len(matrix[0])):
        line_list = []
        row = len(matrix) - 1
        col = i

        while is_valid_index(col, row, matrix):
            line_list.append(matrix[row][col])
            row -= 1
            col -= 1
        line = ''.join(line_list)
        reverse_line = line[::-1]
        counter += count_occurrences_in_string(reverse_line, word)

    for i in range(len(matrix[0]) - 1, -1, -1):
        line_list = []
        row = i
        col = len(matrix[0]) - 1
        while is_valid_index(col, row, matrix):
            line_list.append(matrix[row][col])
            row -= 1
            col -= 1
        line = ''.join(line_list)
        reverse_line = line[::-1]
        counter += count_occurrences_in_string(reverse_line, word)

    return counter


def is_valid_index(col, row, matrix):
    return row >= 0 and col >= 0 and row < len(matrix) and col < len(matrix[0])


def simplify_directions(directions):
    final_directions = set()
    for char in directions:
        final_directions.add(char)
    return final_directions


def find_words_in_matrix(word_list, matrix, directions):
    final_directions = simplify_directions(directions)
    words_dict = {}
    res_words_list = []
    for word in word_list:
        count = 0
        for direction in final_directions:
            if direction == 'u':
                count += up_direction_search_word(word, matrix)
            elif direction == 'd':
                count += down_direction_search_word(word, matrix)
            elif direction == 'r':
                count += right_direction_search_word(word, matrix)
            elif direction == 'l':
                count += left_direction_search_word(word, matrix)
            elif direction == 'w':
                count += diag_up_right_direction_search_word(word, matrix)
            elif direction == 'x':
                count += diag_up_left_direction_search_word(word, matrix)
            elif direction == 'y':
                count += diag_down_right_direction_search_word(word, matrix)
            elif direction == 'z':
                count += diag_down_left_direction_search_word(word, matrix)
        if count > 0:
            words_dict.update({word: count})
            res_words_list.append((word, count))
    return res_words_list


def write_output_file(results, output_filename):
    file = open(output_filename, 'w')
    for pair in results:
        word, count = pair
        file.write(f'{word},{count}\n')
    file.close()


def main(word_file, matrix_file, output_file, directions):
    args = [word_file, matrix_file, output_file, directions]
    if check_input_args(args) is not None:
        print(check_input_args(args))
        return
    words_list = read_wordlist_file(word_file)
    matrix = read_matrix_file(matrix_file)
    word_and_count_pairs = find_words_in_matrix(words_list, matrix, directions)
    write_output_file(word_and_count_pairs, output_file)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])

'''
wordi = 'app'
matrixi = read_matrix_file("mat.txt")
print(diag_down_right_direction_search_word(wordi, matrixi))
print(diag_down_left_direction_search_word(wordi, matrixi))
print(diag_up_left_direction_search_word(wordi, matrixi))
print(diag_up_right_direction_search_word(wordi, matrixi))
print(left_direction_search_word(wordi, matrixi))
print(right_direction_search_word(wordi, matrixi))
print(up_direction_search_word(wordi, matrixi))
print(down_direction_search_word(wordi, matrixi)) '''
