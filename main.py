from numerati import colabfilt
from numerati import filtdata
from numerati import recommender

if __name__ == '__main__':
    print(colabfilt.recommend('Angelica', filtdata.users))

    print(colabfilt.pearson(filtdata.users['Angelica'], filtdata.users['Bill']))
    print(colabfilt.pearson(filtdata.users['Angelica'], filtdata.users['Hailey']))
    print(colabfilt.pearson(filtdata.users['Angelica'], filtdata.users['Jordyn']))

    r = recommender.recommender(filtdata.users)
    print(r.recommend('Jordyn'))

    r.loadBookDB('data/BX-Dump/')
    r.recommend('171118')
    r.userRatings('171118', 5)