test_data = {"KRAS": ["1-14/14"],
             "TP53": ["1-5/18", "6-10/18", "11-18/18"],
             "CCNE1": ["1-2/12", "5-12/12"],
             "ERBB2": ["", ""]}


def string_to_list(input_string: str):
    """
    string range to list functionality
    taken from https://www.geeksforgeeks.org/python-convert-string-ranges-to-list/
    """
    return sum(((list(range(*[int(b) + c
                              for c, b in enumerate(a.split('-'))]))
                 if '-' in a else [int(a)]) for a in input_string.split(', ')), [])


def split_string(input_string: str):
    """
    Split string to the range part ('x'-'y'), and total part
    :param input_string:
    :return: string with range part and int with total
    (range part will be handled by string_to_list method)
    """
    if not isinstance(input_string, str):
        return "Wrong input data"
    if input_string == "":
        return False
    first, second = input_string.split("/")
    return first, int(second)


def is_gene_continuously_amplified(input_data: dict):
    """
    Check if genes in input data are continuously amplified
    :return: Dict of gene:status pairs
    """
    if not isinstance(input_data, dict):
        return "Wrong input data"
    result = dict()

    for key, val in input_data.items():
        tab = list()
        total = 0
        for string in val:
            res = split_string(string)
            if not res:
                total = -1
                break
            first, total = res
            tab.extend(string_to_list(first))
        result[key] = len(tab) == total
    return result


def print_results():
    """
    Auxiliary function to print results
    """
    print(is_gene_continuously_amplified(test_data))
