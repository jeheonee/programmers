def solution(id_list, report, k):
    reported = {a : 0 for a in id_list}
    id_count = [0] * len(id_list)

    report = list(set(report))
    for x in report:
        reported[x.split()[1]] += 1

    for x in report:
        if reported[x.split()[1]] >= k:
            id_count[id_list.index(x.split()[0])] += 1
    return id_count 