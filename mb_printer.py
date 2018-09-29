import sys
import re

class GetMegabytes:
    def __init__(self, text):
        self.text = text

    def string_parse(self):
        template = re.compile(r"(\d*[.,]?\d+).?(гб|gb|мб|mb|kb|кб)", re.IGNORECASE)
        result_search = str(re.search(template, self.text).group())
        try:
            result_search = result_search.replace(',', '.')
        except:
            pass
        result_search = result_search.lower().split(' ')

        s = result_search

        if s[1] == 'гб' or s[1] == 'gb': 
            try: 
                return int(s[0]) * 1024
            except:
                return float(s[0]) * 1024
        elif s[1] == 'мб' or s[1] == 'mb': 
            return s[0]
        elif s[1] == 'кб' or s[1] == 'kb':
            result = round(float(s[0]) / 1024)
            if result % 2 == 0:
                return int(result)
            elif result == 1.0:
                return int(result)
            else:
                return round(float(s[0]) / 1024, 2)
        else:
            return 'Cant convert!'


if __name__ == '__main__':
    obj = GetMegabytes(input())
    print (obj.string_parse())