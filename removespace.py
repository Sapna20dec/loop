# a = 'nav_gurukul'
# i = 1
# while i < 2:
#     print(a.replace("_", ""))
#     i = i+1


a = 'nav_navgurukul'
for i in range(0, len(a)):
    if str.isalpha(a[i:]):
        a = a[i:]
        break
print(a)
