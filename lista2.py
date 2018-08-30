from random import *

def generate_vector():
    random_vector = []
    for i in range(10):
        new_element = randint(0,100)
        random_vector.append(new_element)
    return random_vector


def selection_sort(vector):
    for i in range(len(vector)):
        smaller_index = i
        for j in range(i+1,len(vector)):
            if vector[j] < vector[smaller_index]:
                smaller_index = j
        if smaller_index != i:
            aux = v[smaller_index]
            v[smaller_index] = v[i]
            v[i] = aux

def insertion_sort(vector):
    for i in range(1,len(vector)):
        j = i
        while((j!=0) and (vector[j] < vector[j-1])):
            aux = vector[j]
            vector.pop(j)
            vector.insert(j-1, aux)
            j = j -1

v = generate_vector()
print (v)
# selection_sort(v)
insertion_sort(v)
print (v)
