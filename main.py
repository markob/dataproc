from sdproc import recommendations
from sdproc import sdproc

import pydelicious

def run_analisys():
    return sdproc.top_matches(recommendations.critics, 'Lisa Rose')

def run_ext_analisys():
    return pydelicious.get_popular(tag='programming')


if __name__ == '__main__':
    res = run_ext_analisys()
    print(res)