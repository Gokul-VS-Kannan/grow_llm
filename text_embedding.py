import numpy as np

text_embedding = np.array([0.23, -0.45, 0.12, 0.89, -0.33, 0.67, 0.01, -0.78])

print('Embedding(text as numbers)', text_embedding)
print('Length',len(text_embedding))
print()


querry_embedding = np.array([0.21, -0.42, 0.15, 0.85, -0.30, 0.70, 0.05, -0.75])

similarity = np.dot(text_embedding, querry_embedding)

print(f'Similarity score : {similarity:.4f}')
print('Higher = more similarity')