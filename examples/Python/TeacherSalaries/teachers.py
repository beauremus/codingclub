import csv

files = ['teachers-2014.csv', 'teachers-2015.csv', 'teachers-2016.csv']

for file in files:
    edus = []

    with open(file, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            edus.append(row)

    rts = filter(lambda t: float(t['FTE']) > 0.5 and t['Job Title'] == "Regular Teacher", edus)
    sals = map(lambda t: float(t['FTE Annual Salary'].replace(',','')), rts)
    avg_fas = reduce(lambda x,y: x+y, sals) / len(sals)
    print "%s %-64s (%5d): %6.2f" %(file,"Regular Teacher",len(sals),avg_fas)

    ps = filter(lambda t: t['FTE'] > 0.5 and t['Job Title'] == "Principal", edus)
    sals = map(lambda t: float(t['FTE Annual Salary'].replace(',','')), ps)
    avg_fas = reduce(lambda x,y: x+y, sals) / len(sals)
    print "%s %-64s (%5d): %6.2f\n" %(file,"Principal",len(sals),avg_fas)