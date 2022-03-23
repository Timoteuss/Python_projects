# a = 'Let\'s write a string as "s"'
#
# print(a)

# q = open('text2.txt', encoding='utf-8')
# r1 = q.read()
# list_znk = ['(', ')', '"', '\n']
# for i in list_znk:
#     r1 = r1.replace(i, '')
# print(r1)
#
# r2 = r1.split()
# print(r2)
#
# new_text = ' '.join(r2)
# print(new_text)
# q.close()

enter = input('Your name: ')
s = 'Hello %s, I am Python' % enter

print(s)

var = 'srtoka'

s1 = 'Hello {}, I am {}'.format(enter, 'Python')
s2 = 'Hello {1}, I am {0}'.format(enter, 'Python')
s3 = f'Hello {enter}, I can do it in f-string {len(var)}'

print(s1, s2)
print(s3)

