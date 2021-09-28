gta = [
    'ffff',
    {'k': {'one': (23, 454, 77, 'UU'),
           'yelp': ['heeo',
                    {'yirtual': {'g': (12, 45, 8), 'a': ['yuu', 'poo']}
                     }
                    ]
           },
     'another':[34, 43, ('tt', 'yy')]

     }
]
print("========================================")
print(gta[1]['k']['one'])
print("========================================")
print(gta[1]['k']['yelp'][1]['yirtual']['a'])

print("========================================")
for i in gta[1]['k']['one']:
    print(i)



POSTION_CHOICES = (
    ('mng','Manager'),
    ('dev','Devloper'),
    ('tst','Tester')
)

# dict by key
# list or tuple by index

print("========================================")
# print(POSTION_CHOICES[0][1])
# print(POSTION_CHOICES[1][1])
# print(POSTION_CHOICES[2][1])
# print(POSTION_CHOICES[0][0])
# print(POSTION_CHOICES[1][0])
# print(POSTION_CHOICES[2][0])
print("========================================")

for i in POSTION_CHOICES:
    print(i[0],i[1])




HOICES = [
    ['mng','Manager'],
    ['dev','Devloper'],
    ['tst','Tester']
]

print(HOICES[0][1])
print(HOICES[1][1])
print(HOICES[2][1])
print(HOICES[0][0])
print(HOICES[1][0])
print(HOICES[2][0])

print("========================================")
for k in HOICES:
    print(k[0],k[1])



print(dir(POSTION_CHOICES))
print(dir(HOICES))