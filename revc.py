def process(_input):

    result = ''
    for _char in _input:            
        result = _char + result
    print(result)
    return result


process(
    "AAAACCCGGT"
)

