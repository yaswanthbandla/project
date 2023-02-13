class City:
    def __init__(self, city_id, state_name, city_name, covidbeds, avlblcovbeds, ventilbeds, avlblventilbeds):
        self.city_id = city_id
        self.state_name = state_name
        self.city_name = city_name
        self.covidbeds = covidbeds
        self.avlblcovbeds = avlblcovbeds
        self.ventilbeds = ventilbeds
        self.avlblventilbeds = avlblventilbeds


class CovBedsAnalysis:
    def __init__(self, analysis_name, city_list):
        self.analysis_name = analysis_name
        self.city_list = city_list

    def get_StateWiseAvlblBedStats(self):
        s = []
        for i in range(len(self.city_list)):
            s.append(self.city_list[i].state_name)
        s = list(set(s))
        s.sort()
        a = []
        for i in range(len(s)):
            b = []
            b.append(s[i])
            ta, tv = 0, 0
            for j in range(len(self.city_list)):
                if (self.city_list[j].state_name == s[i]):
                    ta += self.city_list[j].avlblcovbeds
                    tv += self.city_list[j].avlblventilbeds
            b.append(ta)
            b.append(tv)
            a.append(b)
        return a

    def get_CitiesWithMoreThanAvgOccupiedbeds(self, state):
        ava, avv, c = 0.0, 0.0, 0
        for i in range(len(self.city_list)):
            if (self.city_list[i].state_name == state):
                ava += self.city_list[i].covidbeds - self.city_list[i].avlblcovbeds
                avv += self.city_list[i].ventilbeds - self.city_list[i].avlblventilbeds
                c += 1
        if (ava != 0 and avv != 0 and c != 0):
            ava /= c
            avv /= c
        city = dict()
        for i in range(len(self.city_list)):
            if (self.city_list[i].state_name.lower() == state):
                x = []
                if ((self.city_list[i].covidbeds - self.city_list[i].avlblcovbeds) > ava and (self.city_list[i].ventilbeds - self.city_list[i].avlblventilbeds) > avv and avv != 0 and ava != 0):
                    x.append(self.city_list[i].covidbeds - self.city_list[i].avlblcovbeds)
                    x.append(self.city_list[i].ventilbeds - self.city_list[i].avlblventilbeds)
                    city[self.city_list[i].city_name] = x
        if (len(city) == 0):
            return 0
        return city


n = int(input())
d = []
for i in range(n):
    city_id = int(input())
    state_name = input()
    city_name = input()
    covidbeds = int(input())
    avlblcovbeds = int(input())
    ventilbeds = int(input())
    avlblventilbeds = int(input())
    C = City(city_id, state_name, city_name, covidbeds, avlblcovbeds, ventilbeds, avlblventilbeds)
    d.append(C)
state = input()
state = state.lower()
F = CovBedsAnalysis("TOTAL", d)
h = F.get_StateWiseAvlblBedStats()
for i in range(len(h)):
    print(*h[i])
q = F.get_CitiesWithMoreThanAvgOccupiedbeds(state)
if q == 0:
    print("No city available")
else:
    for i in q:
        print(i, *q[i])

