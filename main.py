from sdproc import delicious
import random

if __name__ == '__main__':
    stat = delicious.DeliciousStat('linux')

    usr_list = stat.get_usr_list()
    usr = usr_list[random.randint(0, len(usr_list) - 1)]

    print usr
    print stat.get_top_matches(usr)
    print stat.get_recommendations(usr)
