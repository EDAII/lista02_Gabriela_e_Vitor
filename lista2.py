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

def bubble_sort(vector):
    change = True
    while(change):
        change = False
        for i in range(0,len(vector)-1):
            if(vector[i] > vector[i+1]):
                aux = vector[i+1]
                vector[i+1] = vector[i]
                vector[i] = aux
                change = True

def shell_sort(vector):
    gap = int(len(vector)/2)
    size = len(vector)

    while(gap > 0):
        for i in range(gap,size):
            temp = vector[i]
            j = i
            while(j >= gap and (vector[j-gap] > temp)):
                vector[j] = vector[j-gap]
                j-= gap
            vector[j] = temp
        gap = int(gap/2)



v = generate_vector()
print (v)
# selection_sort(v)
#insertion_sort(v)
#bubble_sort(v)
shell_sort(v)
print (v)
