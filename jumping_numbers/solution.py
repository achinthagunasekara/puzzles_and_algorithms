"""
Find jumping numbers.
"""

def get_jumping_numbers(integer):
    """
    Get jumping numbers between 0 and given integer.
    Args:
        integer (int): Integer to check up to.
    Return:
        String: String of all jumping numbers.
    """
    current_int = 0
    jumping_ints = []
    int_list = list(str(integer))
    return int_list

INPUT = [
    10,
    50
]

for integer in INPUT:
    print get_jumping_numbers(integer=integer)
    print '======'
