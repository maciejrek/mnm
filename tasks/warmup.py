def warmup_one(input_data: str):
    if not isinstance(input_data, str):
        return "Wrong input data"

    input_data = input_data.lower()
    result = ['', '']
    for index, sign in enumerate(input_data):
        result[0] += sign.lower() if index % 2 == 0 else sign.upper()
        result[1] += sign.upper() if index % 2 == 0 else sign.lower()
    return result
