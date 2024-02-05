
from name_function_3 import get_formatted_name


def test_first_last_name():
    ''' Do names like 'Aref Abdo'work? '''
    formatted_name = get_formatted_name('aref', 'abdo')
    assert formatted_name == 'Aref Abdo'


 
def test_first_last_middle_name():
    ''' Do names like 'Aref Fatehi Abdo' work? '''  
    formatted_name = get_formatted_name('aref','abdo','fatehi')
    assert formatted_name == 'Aref Fatehi Abdo'
    