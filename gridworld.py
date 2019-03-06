from tiles3 import tiles, IHT, tileswrap


'''
This is where I will be getting my hands dirty with function approximation things for RL
'''



internal_hash = IHT(5)

print(internal_hash.count())

test=tiles(internal_hash,4,[20,20],[5,4])
print(test)


test2 = tiles(internal_hash,4,[20,20],[1,4])
print('test2',test2)

test3 = tiles(internal_hash, 4, [5,5])
print(test3)