import re
lis = {"2022000001" : 9.1,
       "2022000002" : 4,
       "2022000003" : 3.2,
       "2022000004" : 5.3,
       "2022000005" : 1.2,
       "2022000006" : 2.4}
lis["2022000007"] = 10
print("{}\n{}".format(len([i for i in re.findall(r"\d+", str(lis)) if float(i) >= 2.5 and float(i) <= 3.5]), {x: y for x, y in lis.items() if y >= 2}))