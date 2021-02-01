"""
    有两个人需要找一个时间开会，给你每个人一天中正在开会的时间段，以及他今天愿意开会的时间段，最后给出最小的会议时间，找出两人在剩下的哪些时间可以进行二人会议，符合最小的会议时间
    Sample Input:
    [['9:00', '10:30'], ['12:00', '13:00'], ['16:00', '18:00']]
    ['9:00', '20:00']
    [['10:00', '11:30'], ['12:30', '14:30'], ['14:30', '15:00'],['16:00', '17:00']]
    ['10:00','18:30']
    30

    Sample Output:
    [['11:30', '12:00'], ['15:00', '16:00'], ['18:00', '18:30']]
"""


def process_bound(bound):
    """
        处理每个人的今天可以开会时间段
    """
    bound = bound[1:-1]
    bound = bound.split(',')
    bound = list(map(lambda x: x[1:-1], bound))
    return bound


def process_cal(cal):
    """
        处理每个人的今天会议时间
    """
    cal = cal[2:-2].split('],[')
    cal = list(map(lambda x: x.split(','), cal))
    cal = list(map(lambda x: [s[1:-1] for s in x], cal))
    return cal


def find_spare_time(cal):
    """
        找出空余时间
    """
    res = []
    for i in range(len(cal) - 1):
        if cal[i][1] != cal[i + 1][0]:
            res.append([cal[i][1], cal[i + 1][0]])
    return res


def time_compare(time1, time2):
    if time1 == time2:
        return False
    tmp1 = time1.split(':')
    tmp2 = time2.split(':')
    if tmp1[0] > tmp2[0]:
        return True
    elif tmp1[0] < tmp2[0]:
        return False
    else:
        if tmp1[1] > tmp2[1]:
            return True
        else:
            return False

def time_compare2(time1, time2):
    if time1 == time2:
        return True
    tmp1 = time1.split(':')
    tmp2 = time2.split(':')
    if tmp1[0] > tmp2[0]:
        return True
    elif tmp1[0] < tmp2[0]:
        return False
    else:
        if tmp1[1] > tmp2[1]:
            return True
        else:
            return False

def spare_with_bound(spare, bound, cal):
    """
        补充空余时间
    """
    if cal[-1][1] != bound[1]:
        spare.append([cal[-1][1], bound[1]])
    if cal[0][0] != bound[0]:
        spare.insert(0, [bound[0], cal[0][0]])
    return spare


def compute_time(time1, time2):
    """
        计算两个时间的间隔
        默认time2晚于time1
    """
    tmp1 = time1.split(':')
    tmp2 = time2.split(':')

    if tmp1[0] == tmp2[0]:
        return int(tmp2[1]) - int(tmp1[1])
    else:
        return (60 - int(tmp1[1])) + int(tmp2[1]) + (int(tmp2[0]) - 1 - int(tmp1[0])) * 60


def check_time(spare, minTime):
    res = []
    for t in spare:
        if compute_time(t[0], t[1]) >= minTime:
            res.append(t)
    return res


def get_res(spare1, spare2):
    res = []
    for item1 in spare1:
        for item2 in spare2:
            if time_compare2(item2[1], item1[1]):
                if time_compare2(item1[0], item2[0]):
                    res.append(item1)
                else:
                    if compute_time(item2[0], item1[1]) >= minTime:
                        res.append([item2[0], item1[1]])
            if time_compare2(item2[0], item1[0]):
                continue
            if time_compare2(item1[1], item2[1]):
                if time_compare2(item2[0], item1[0]):
                    res.append(item2)
                else:
                    if compute_time(item1[0], item2[1]) >= minTime:
                        res.append([item1[0], item2[1]])
            if time_compare2(item1[0], item2[0]):
                continue
    return res


if __name__ == "__main__":
    cal1 = input()
    bound1 = input()
    cal2 = input()
    bound2 = input()
    minTime = int(input())

    cal1 = process_cal(cal1)
    cal2 = process_cal(cal2)
    bound1 = process_bound(bound1)
    bound2 = process_bound(bound2)

    spare1 = find_spare_time(cal1)
    spare2 = find_spare_time(cal2)
    spare1 = spare_with_bound(spare1, bound1, cal1)
    spare2 = spare_with_bound(spare2, bound2, cal2)

    spare1 = check_time(spare1, minTime)
    spare2 = check_time(spare2, minTime)
    print("=====================")

    res = get_res(spare1, spare2)
    print(res)
