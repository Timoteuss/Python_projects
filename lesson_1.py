import math


vinishko_1 = 0

kotik_1 = "Murzik"

print(vinishko_1 * kotik_1)

i_1 = 1
i_2 = 11
i_3 = 7
i_4 = 22
i_5 = 159

s_1 = i_2 + i_4
m_1 = i_2 - i_3
print("s_1 =", s_1)
print("m_1 =", m_1)
# while True:
#     print(1)

u_1 = i_3 + i_2
d_1 = i_5 / i_2
do_1 = i_5 // i_2
dop_1 = i_1 % i_2

print("u_1 =", u_1)
print("d_1 =", d_1)
print("do_1 =", do_1)
print("dop_1 =", dop_1)

sq = i_3 ** i_2
print("sq =", sq)

mm = math.sqrt(49)
mm1 = int(math.sqrt(49))

print("mm =", mm, type(mm))
print("mm1 =", mm1, type(mm1))
print(round(3.75, 1))
print(round(3.75))

zz = 10
print("zz =", zz)
zz += 2
print("zz =", zz)
zz *= 2
print("zz =", zz)
zz *= 2
print("zz =", zz)

pp = math.floor(3.14)
# pp1 = math.sail(3.14)

print("Округление в меньшую сторону - ", pp)
# print("Округление в большую сторону - ", pp1)

bb = True
ff = False

if i_2:
    print("Hello i_2")

ee = i_3 > 10
ee1 = i_3 < 10

print(ee)
print(ee1)
print(i_3 == 7)

# если условие правда, то первое выражение, если ложь, то второе
# if - точка входа в сравнение , elif - промежуточные точки, else - точка выхода, если ни одно из значений не было True
if pp == 1:
    print("Hello world")
elif pp == 77:
    print("Hello 77")
elif pp == 7:
    print("Hello 7")
elif pp == 3:
    print("Krasavchik")
else:
    print("Fatal mistake")