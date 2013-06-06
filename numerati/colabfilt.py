import math

def manhattan(rating1, rating2):
    distance= 0
    for key in rating1:
        if key in rating2:
            distance += abs(rating1[key] - rating2[key])

    return distance


def minkowski(rating1, rating2, r):
    distance = 0;
    for key in rating1:
        if key in rating2:
            distance += math.pow(abs(rating1[key] - rating2[key]), r)
    return math.pow(distance, 1/float(r))


def euclidean(rating1, rating2):
    minkowski(rating1, rating2, 2)


def pearson(rating1, rating2):
    n = 0
    sum_x = 0.0
    sum_y = 0.0
    sum_xy = 0.0
    sum_x2 = 0.0
    sum_y2 = 0.0

    for key in rating1:
        if key in rating2:
            n += 1

            x = rating1[key]
            y = rating2[key]

            sum_x += x
            sum_y += y
            sum_xy += x*y
            sum_x2 += x*x
            sum_y2 += y*y

    den = math.sqrt((sum_x2 - sum_x*sum_x/n)*(sum_y2 - sum_y*sum_y/n))
    if den == 0: return 0.0

    return (sum_xy - sum_x*sum_y/n)/den


def comp_nearest_neighbor(username, users, calculate_distance=euclidean):
    distances = []
    for user in users:
        if user != username:
            distance = calculate_distance(users[user], users[username])
            distances.append((distance, user))

    distances.sort()
    return distances


def recommend(username, users):
    nearest = comp_nearest_neighbor(username, users)[0][1]
    recommendations = []

    # now find bands neighbor rated that user didn't
    neighbor_ratings = users[nearest]
    user_ratings = users[username]

    for artist in neighbor_ratings:
        if not artist in user_ratings:
            recommendations.append((artist, neighbor_ratings[artist]))

    # using the fn sorted for variety - sort is more efficient
    return sorted(recommendations, key=lambda artist_tuple: artist_tuple[1], reverse = True)