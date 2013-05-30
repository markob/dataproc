import math


def sim_euclid(prefs, person1, person2):
    si = {}

    for it in prefs[person1]:
        if it in prefs[person2]:
            si[it] = 1

    if len(si) == 0: return 0.0

    sum_of_squares = 0.0
    for it in prefs[person1]:
        if it in prefs[person2]:
            sum_of_squares = sum_of_squares + pow(prefs[person1][it] - prefs[person2][it], 2)

    return 1 / (1 + math.sqrt(sum_of_squares))


def sim_pearson(prefs, person1, person2):
    si = {}

    for it in prefs[person1]:
        if it in prefs[person2]:
            si[it] = 1

    n = len(si)
    if n == 0: return 0.0

    sum1 = sum([prefs[person1][it] for it in si])
    sum2 = sum([prefs[person2][it] for it in si])

    sum1sq = sum([pow(prefs[person1][it], 2) for it in si])
    sum2sq = sum([pow(prefs[person2][it], 2) for it in si])

    psum = sum([prefs[person1][it] * prefs[person2][it] for it in si])
    num = psum - (sum1 * sum2 / n)
    den = math.sqrt((sum1sq - pow(sum1, 2) / n) * (sum2sq - pow(sum2, 2) / n))
    if den == 0: return 0.0
    return num / den


def tanimoto_distance(prefs, set1, set2):
    a, b, c = len(set1), len(set2), 0

    for it in set1:
        if it in set2:
            c += 1

    return float(c) / (a + b - c)


def top_matches(prefs, person, n=5, similarity=sim_pearson):
    scores = [(similarity(prefs, person, other), other) for other in prefs if other != person]

    scores.sort()
    scores.reverse()
    return scores[0:n]


def get_recommendation(prefs, person, similarity=sim_pearson):
    totals = {}
    sim_sums = {}
    for other in prefs:
        if other == person: continue
        sim = similarity(prefs, person, other)

        if sim <= 0: continue
        for item in prefs[other]:
            if item not in prefs[person] or prefs[person][item] == 0:
                totals.setdefault(item, 0)
                totals[item] += prefs[other][item] * sim
                sim_sums.setdefault(item, 0)
                sim_sums[item] += sim

    rankings = [(total / sim_sums[item], item) for item, total in totals.items()]
    rankings.sort()
    rankings.reverse()
    return rankings


def transform_prefs(prefs):
    result = {}

    for person in prefs:
        for item in prefs[person]:
            result.setdefault(item, {})
            result[item][person] = prefs[person][item]

    return result
