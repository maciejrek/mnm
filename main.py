from tasks.dev_2 import print_results as dev_2
from tasks.dev_1 import print_results as dev_1
from tasks.dev_3 import DnaSequence

if __name__ == '__main__':
    # dev_2()
    # dev_1()
    # """
    # This should be in test files but i'm getting short on time - i'll add tests in overtime
    # """
    # # Negative cases
    # try:
    #     a = DnaSequence(sequence="abc")
    # except ValueError as e:
    #     print(e)
    #
    # try:
    #     a = DnaSequence(sequence="ATCGN", file="sequence_file.txt")
    # except TypeError as e:
    #     print(e)
    #
    # # Positive cases from sequence
    # b = DnaSequence(sequence="ATCGN")
    # b.print_sequence()
    # b.print_sequence_reverse()
    # b.extend_sequence(3)
    # b.print_sequence()
    # b.trim_sequence(2)
    # b.print_sequence()
    #
    # # Positive cases from file
    # c = DnaSequence(file='sequence_file.txt')
    # c.print_sequence()
    # c.print_sequence_reverse()
    # c.extend_sequence(3)
    # c.print_sequence()
    # c.trim_sequence(2)
    # c.print_sequence()
    pass
