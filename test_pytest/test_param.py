

import pytest

def sum(a,b):
    return a +b



@pytest.mark.parametrize("input1,input2,output",

                         [(3,4,7),
                          (2,3,5),
                          (2,2,4),(3,4,6)




                          ])
def test_calc_1(input1,input2,output):

    result =  sum(input1,input2)
    assert result == output