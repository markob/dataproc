from sdproc import recommendations
from sdproc import sdproc

import pydelicious

def run_analisys():
    return sdproc.top_matches(recommendations.critics, 'Lisa Rose')

def run_ext_analisys():
    return init_user_dict('programming')


def init_user_dict(tag, count=5):
    user_dict = {}

    for p1 in pydelicious.get_popular(tag)[0:count]:
        for p2 in pydelicious.get_urlposts(p1['url']):
            user = p2['user']
            user_dict[user] = {}

    return user_dict



if __name__ == '__main__':
    res = run_ext_analisys()
    print(res)