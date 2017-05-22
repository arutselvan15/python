'''
:Author: Arutselvan Muthusamy
:Contact: arut.selvan15@gmail.com
'''
__updated__ = 'yyyy-MM-dd'

def count_substring(string, sub_string):
    '''Get count of substring in main string
        string = 'ABCDCDC'
        sub_string = 'CDC'
        
        count = count_substring(string, sub_string)
        print (count)
    '''
    index = count = 0
    while index < len(string):
        print(index)
        index = string.find(sub_string, index, len(string))
        if index >= 0:
            count += 1
            index += 1
        else:
            break
    return count

if __name__ == '__main__':
    string = 'ABCDCDC'
    sub_string = 'CDC'
    count_substring(string, sub_string)