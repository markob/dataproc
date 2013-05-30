import pydelicious
import sdproc
import time

class DeliciousStat(object):

    def __init__(self, tag):
        # nothing to do with empty tag
        if tag is None: return None
        self._tag = tag

        # get info on actual tag
        self._init_user_dict()

        # generate appropriate data set
        self._fill_items()

        # calculate similar items
        self._calc_similar_items()


    def _init_user_dict(self, count=5):
        user_dict = {}

        for p1 in pydelicious.get_popular(tag=self._tag)[0:count]:
            for p2 in pydelicious.get_urlposts(p1['url']):
                user = p2['user']
                user_dict[user] = {}

        if __debug__: print(user_dict)
        self._usr_dict = user_dict


    def _fill_items(self):
        all_items = {}

        for user in self._usr_dict:
            posts = []

            for i in range(3):
                try:
                    posts = pydelicious.get_userposts(user)
                    break
                except:
                    print "User " + user + " error, trying again."
                    time.sleep(4)

            for post in posts:
                url = post['url']
                self._usr_dict[user][url] = 1.0
                all_items[url] = 1

        for ratings in self._usr_dict.values():
            for item in all_items:
                if item not in ratings:
                    all_items[item] = 0.0
                    ratings[item] = 0.0

        if __debug__: print(all_items)
        self._all_items = all_items


    def _calc_similar_items(self, n=10):
        result = {}
        item_prefs = sdproc.transform_prefs(self._usr_dict)

        count = 0
        for item in item_prefs:
            # update process status
            count += 1
            if count%100 == 0: print "%d / %d" % (count, len(item_prefs))

            scores = sdproc.top_matches(item_prefs, item, n=n, similarity=sdproc.sim_euclid)
            result[item] = scores

        if __debug__: print(result)
        self._sim_items = result


    def get_usr_list(self):
        return self._usr_dict.keys()


    def get_recommendations(self, usr):
        return sdproc.get_recommendation(self._usr_dict, usr)


    def get_top_matches(self, usr):
        return sdproc.top_matches(self._usr_dict, usr)
