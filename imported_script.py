
from typing import Optional, Union


print('some python script for import to webpage')

def imported_function(maximum: int, built_seq: Optional[list[int]]=None):
    """
    Some function to test importing to pyscript
    """
    if built_seq is None:
        built_seq = [1, 1]
    if len(built_seq) >= maximum:
        return built_seq
    built_seq.append(sum([built_seq[-2], built_seq[-1]]))
    return imported_function(maximum=maximum, built_seq=built_seq)

if __name__ == "__main__":
    raise SystemExit(imported_function(7))
