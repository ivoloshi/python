##########################################
# NAME: Maya Voloshin
# ID: 322853680
# login: mayavolo
# DESCRIPTION: ex5
##########################################

import sys
import traceback
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
    return None


def read_wordlist_file(filename):
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


def read_matrix_file(filename):
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
    if not len(matrix):
        return counter
    for col in range(len(matrix[0])):
        line_list = []
        for row in range(len(matrix)):
            line_list.append(matrix[row][col])
        counter = update_counter(counter, line_list, word)
    return counter


def update_counter(counter, line_list, word):
    """
        updates counter for the occurrences of the word
        :param counter: the searched word
        :param line_list: the char matrix that is searches in
        :param word:word to search
        :return: counter
    """
    line = ''.join(line_list)

    if len(line) > 0:
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
    if not len(matrix):
        return counter
    for col in range(len(matrix[0])):
        line_list = []
        for row in range(len(matrix) - 1, -1, -1):
            line_list.append(matrix[row][col])
        counter = update_counter(counter, line_list, word)

    return counter


def diag_up_right_direction_search_word(word, matrix):
    """
    searches for the occurrences of the word in the "up_right" direction only
    :param word: the searched word
    :param matrix: the char matrix that is searches in
    :return: number of occurrences in the up direction
    """
    counter = 0
    if not len(matrix):
        return counter
    if len(matrix) == 1 and len(word) == 1:
        return left_direction_search_word(word, matrix)
    for k in range(len(matrix)):
        col = 0
        line_list = []
        row = k

        while row >= 0 and col < len(matrix[0]):
            #   print(f'row = {row} col = {col}')
            line_list.append(matrix[row][col])
            row -= 1
            col += 1
        counter = set_counter(counter, line_list, word)

    for k in range(1, len(matrix)):

        line_list = []
        row = len(matrix) - 1
        col = k

        while col < len(matrix[0]):
            line_list.append(matrix[row][col])
            row -= 1
            col += 1
        counter = set_counter(counter, line_list, word)

    return counter


def set_counter(counter, line_list, word):
    """
    sets counter
    :param counter:
    :param line_list:
    :param word:
    :return:
    """
    if len(line_list) > 0:
        line = ''.join(line_list)
        counter += count_occurrences_in_string(line, word)
    return counter


def diag_down_left_direction_search_word(word, matrix):
    """
    searches for the occurrences of the word in the "down_left" direction only
    :param word: the searched word
     :param matrix: the char matrix that is searches in
    :return: number of occurrences in the up direction
     """
    counter = 0

    if not len(matrix):
        return counter
    if len(matrix) == 1 and len(word) == 1:
        return left_direction_search_word(word, matrix)

    for k in range(len(matrix)):
        col = 0
        line_list = []
        row = k

        while row >= 0 and col < len(matrix[0]):
            #   print(f'row = {row} col = {col}')
            line_list.append(matrix[row][col])
            row -= 1
            col += 1
        counter = update_counter_with_reverse_line(counter, line_list, word)

    for k in range(1, len(matrix)):
        line_list = []
        row = len(matrix) - 1
        col = k

        while col < len(matrix[0]):
            line_list.append(matrix[row][col])
            row -= 1
            col += 1
        counter = update_counter_with_reverse_line(counter, line_list, word)
    return counter


def update_counter_with_reverse_line(counter, line_list, word):
    """
    updates counter
    :param counter:
    :param line_list:
    :param word:
    :return:
    """
    if len(line_list) > 0:
        line = ''.join(line_list)
        reverse_line = line[::-1]
        counter += count_occurrences_in_string(reverse_line, word)
    return counter


def diag_down_right_direction_search_word(word, matrix):
    """
        searches for the occurrences of the word in the "up_right" direction only
        :param word: the searched word
         :param matrix: the char matrix that is searches in
        :return: number of occurrences in the up direction
     """
    counter = 0
    if not len(matrix):
        return counter
    if len(matrix) == 1 and len(word) == 1:
        return left_direction_search_word(word, matrix)

    for i in range(len(matrix)):

        line_list = []
        for j in range(0, len(matrix) - i):
            if len(matrix[i + j]) <= j:
                break
            line_list += matrix[i + j][j]
        if len(line_list) > 0:
            line = ''.join(line_list)
            counter += count_occurrences_in_string(line, word)

    for i in range(1, len(matrix[0])):
        line_list = []
        for j in range(0, len(matrix[0]) - i):
            if len(matrix[0]) < i + j or j >= len(matrix):
                break
            line_list += matrix[j][i + j]
        if len(line_list):
            line = ''.join(line_list)
            counter += count_occurrences_in_string(line, word)
            # print(line)
    return counter


def diag_up_left_direction_search_word(word, matrix):
    """
       :param word:
       :param  matrix:
       :return:
    """
    counter = 0
    if not len(matrix):
        return counter
    if len(matrix) == 1 and len(word) == 1:
        return left_direction_search_word(word, matrix)

    for i in range(len(matrix)):

        line_list = []
        for j in range(0, len(matrix) - i):
            if len(matrix[i + j]) <= j:
                break
            line_list += matrix[i + j][j]
        if len(line_list) > 0:
            line = ''.join(line_list)
            reverse_line = line[::-1]
            counter += count_occurrences_in_string(reverse_line, word)

    for i in range(1, len(matrix[0])):

        line_list = []
        for j in range(0, len(matrix[0]) - i):
            if len(matrix[0]) < i + j or j >= len(matrix):
                break
            line_list += matrix[j][i + j]
        if len(line_list):
            line = ''.join(line_list)
            reverse_line = line[::-1]
            counter += count_occurrences_in_string(reverse_line, word)

    return counter


def simplify_directions(directions):
    """
    creates set of directions
    :param directions:
    :return:
    """
    final_directions = set()
    for i in range(len(directions)):
        final_directions.add(directions[i])
    return final_directions


def find_words_in_matrix(word_list, matrix, directions):
    """
    finds words in matrix
    :param word_list:
    :param matrix:
    :param directions:
    :return:
    """
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
        if not count:
            continue
        if word in words_dict.keys():
            words_dict[word] += count
        else:
            words_dict[word] = count

    for w in words_dict.keys():
        if words_dict[w] != 0:
            res_words_list.append((w, words_dict[w]))

    return res_words_list


def write_output_file(results, output_filename):
    """
    :param results:
    :param output_filename:
    :return:
    """
    file = open(output_filename, 'w')
    for pair in results:
        word, count = pair
        file.write(f'{word},{count}\n')
    file.close()


def main(word_file, matrix_file, output_file, directions):
    """
    :param word_file:
    :param matrix_file:
    :param output_file:
    :param directions:
    :return:
    """
    args = [word_file, matrix_file, output_file, directions]
    if check_input_args(args) is not None:
        print(check_input_args(args))
        return
    words_list = read_wordlist_file(word_file)
    matrix = read_matrix_file(matrix_file)
    if not len(matrix):
        return
    word_and_count_pairs = find_words_in_matrix(words_list, matrix, directions)
    write_output_file(word_and_count_pairs, output_file)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
