import math


a, b, h, m = map(int, input().split())

if m == 0:
    hkaku = h * 30
elif m != 0:
    hkaku = h * 30
    hkaku += m * 2.5
print("hkaku = ", hkaku)
mkaku = m * 6
print("mkaku = ", mkaku)
if hkaku == 0:
    nkaku = 360 - mkaku
elif mkaku == 0:
    nkaku = 360 - hkaku
elif hkaku >= mkaku:
    nkaku = hkaku - mkaku
elif hkaku < mkaku:
    nkaku = mkaku - hkaku
print("nkaku = ", nkaku)

c_2 = pow(a, 2) + pow(b, 2)
c_3 = 2 * a * b * (math.cos(math.radians(nkaku)))
c_4 = c_2 - c_3
print("c_2 = ", c_2)
print("c_3 = ", c_3)
print("c_4 = ", c_4)

c = math.sqrt(c_4)
print('{:.20f}'.format(c))
print(math.cos(nkaku))
