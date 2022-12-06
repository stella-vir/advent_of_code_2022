input = '''1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
'''
'''
output = 24000 = 7 + 8 + 9
split('/n') sum = sum([0], [1]) max = (max, sum)
'''

parsing = input.split('\n\n')
print(parsing)


sum = 0
for i, p in enumerate(parsing):
    p = p.splitlines()
    print(p, type(p))
    res = [ sum(p[x : x + 3]) for x in range(0, len(p), 3)]
    # for num in p:
    #     sum += int(num)
    #     print('sum', sum)
    #     sum = 0





# end
