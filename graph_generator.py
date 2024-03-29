import matplotlib.pyplot as plt
import csv

x1 = []
y1 = []
a1 = []
b1 = []
c1 = []
d1 = []

with open('./aho-corasick/benchmark_aho_text_length.txt','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    count = 0
    for row in plots:
        count += 1
        x1.append(int(row[0])*2)
        y1.append(int(row[1]))
        c1.append(int(row[0])*2)
        d1.append(int(row[0])*2*2.5)

with open('./karp-rabin/benchmark_rabin_text_length.txt','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    count = 0
    for row in plots:
        count += 1
        a1.append(int(row[0])*2)
        b1.append(int(row[1]))
        
plt.plot(x1,y1, label='Aho corasick')
plt.plot(a1,b1, label='Rabin Karp')
plt.plot(c1,d1, label='Linear Graph y=2.5*x')
plt.xlabel('Size (x * 10^4 characters)')
plt.ylabel('Time (ms)')
plt.title('Increasing Text Length')
plt.legend()
plt.show()

x2 = []
y2 = []
a2 = []
b2 = []
c2 = []
d2 = []

with open('./aho-corasick/benchmark_aho_pattern_length.txt','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    count = 0
    for row in plots:
        count += 1
        x2.append(int(row[0]))
        y2.append(int(row[1]))
        a2.append(int(row[0]))
        b2.append(int(row[0]) + 100)

with open('./karp-rabin/benchmark_rabin_pattern_length.txt','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    count = 0
    for row in plots:
        count += 1
        c2.append(int(row[0]))
        d2.append(int(row[1]))

plt.plot(x2,y2, label='Aho corasick')
plt.plot(c2,d2, label='Rabin Karp')
plt.plot(a2,b2, label='Linear Graph y=x+100')
plt.xlabel('Size of pattern (characters)')
plt.ylabel('Time (ms)')
plt.title('Increasing Pattern Length')
plt.legend()
plt.show()

x3 = []
y3 = []
a3 = []
b3 = []
c3 = []
d3 = []

with open('./aho-corasick/benchmark_aho_pattern_count.txt','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    count = 0
    for row in plots:
        count += 1
        x3.append(int(row[0]))
        y3.append(int(row[1]))
        a3.append(int(row[0]))
        b3.append(int(row[0])+100)

with open('./karp-rabin/benchmark_rabin_pattern_count.txt','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    count = 0
    for row in plots:
        count += 1
        c3.append(int(row[0]))
        d3.append(int(row[1]))

plt.plot(x3,y3, label='Aho corasick')
plt.plot(c3,d3, label='Rabin Karp')
plt.plot(a3,b3, label='Linear Graph y=x+100')
plt.xlabel('Size of pattern (characters)')
plt.ylabel('Time (ms)')
plt.title('Increasing Pattern count')
plt.legend()
plt.show()
