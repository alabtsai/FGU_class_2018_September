
def print_twice(bruce):
    print(bruce)
    print(bruce)

def cat_twice(part1,part2):
    cat=part1+part2
    print('in cat_twice', cat)
    print_twice(cat)

line1='aaa'
line2='bbb'
cat_twice(line1,line2)
