import numpy as np

score =[87, 90, 95, 98, 89]

score_array = np.array([87, 90, 95, 78, 89])

print(f'Python list : {score}')
print(f'Numpy array : {score_array}')
print()
print('Type:',type(score))
print('Type:',type(score_array))

curved = score_array + 5
print(curved)

scaled = score_array * 0.9
print(scaled)

print('average :', score_array.mean())
print('maximum :', score_array.max())
print('minimum :', score_array.min())
print('total :', score_array.sum())
