def process(_input):

    result = ""
    for _char in _input:
        if _char == "T":
            result += "U"
        else:
            result += _char
    print(result)
    return result


process(
    "CATGGGGCATGACTACGCATTGCATACCGCAGCACTGATTCGCAGTCTTACGCTCTGACACTTCAAATCTCATCGCCTAAGTAGAAGTCAGTCCCGCCCCCCATACGTTGCGCTATGAGGGTCAAGCTGCCACGTTCGGCCCTCTCTATAACATCTAAGGCGCGCATGCACGCCGGTCTTCAATCAAGGCTGAAAGCATGACGCTGAGGTTCCCAAACCGCGATGCATCTGTTTCTTGACAACCACCGCAACAGATTCTGGCACTGTACCTAACACAATTTCCAGGTGTATCCTACCGTGGCTCACTAAACAGAATTATAGTAGTGGCATGTTTCACCTATATTTTATTAGGAGGTCGAGTACCTCGTTCGCCACTTGATCGTAGGTTAAGTGGCCTTCACACGCGTTCCTTTGCCATAACTTATTACGTGATCAGTAAAATTGCGTGGTTTTACGCGAAATGCCGGGAATGCTTTCCAGGTCCCGTGCATCCTCTGATCAAAGTGGATGGAGTGGGTACCGACGAGGAACCGCAATTGAGTGAACCTCGATCCGAGCACTGCTTCCGTCTGTCCTATCCCCATTGTAGCATGACATAGCCCTGAGACACTCGCCTTCGACTGAGGCCGTCGAATTAGACCCAATTTGTGAGTGATGATAAACCACTACAATTTCTGAGGCCAGGAAACCCGATGGTAACAAACCTATACTGCCTCACGGCCCATATTGAGCATACCCTCGAAGCACTAATAGTGAACGGATAGGTTGGCTCCCATGCTATTAAACATAGCTAAAGCAATCCGGTCCCAGTCACTAATCAAATTTAACGCAAACAATGTGGCTTGCCGCGATAACTGTACCCCAAGGTCGCAGGCCCAGGATGGGAATGCTAGGTTGGCTTCTTAGAACCAGAATTACGATATGACAGTTCGCGCAATATATAAGATGTCTCCCCTATTGTGGCTGGGCGTCCTGTC"
)
