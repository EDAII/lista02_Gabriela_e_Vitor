from random import *
import os
import time

def generate_vector(size, intervals):
    random_vector = []
    for i in range(size):
        new_element = randint(0,intervals)
        random_vector.append(new_element)
    return random_vector

def selection_sort(vector):
    start_time = time.time()
    for i in range(len(vector)):
        smaller_index = i
        for j in range(i+1,len(vector)):
            if vector[j] < vector[smaller_index]:
                smaller_index = j
        if smaller_index != i:
            aux = vector[smaller_index]
            vector[smaller_index] = vector[i]
            vector[i] = aux
    elapsed_time = time.time() - start_time
    print('Tempo: ' + str(elapsed_time) + 's')

def insertion_sort(vector):
    start_time = time.time()
    for i in range(1,len(vector)):
        j = i
        while((j!=0) and (vector[j] < vector[j-1])):
            aux = vector[j]
            vector.pop(j)
            vector.insert(j-1, aux)
            j = j -1
    elapsed_time = time.time() - start_time
    print('Tempo: ' + str(elapsed_time) + 's')

def bubble_sort(vector):
    start_time = time.time()
    change = True
    while(change):
        change = False
        for i in range(0,len(vector)-1):
            if(vector[i] > vector[i+1]):
                aux = vector[i+1]
                vector[i+1] = vector[i]
                vector[i] = aux
                change = True
    elapsed_time = time.time() - start_time
    print('Tempo: ' + str(elapsed_time) + 's')

def shell_sort(vector):
    start_time = time.time()
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
    elapsed_time = time.time() - start_time
    print('Tempo: ' + str(elapsed_time) + 's')

def menu():
    os.system('clear')
    print('=============== Menu ===============\n')
    print('Insira os valores para gerar seu vetor\n\n')
    vector_size = int(input('Tamanho do vetor: '))
    intervals = int(input('\nMaior numero possivel do vetor: '))

    v_selection = generate_vector(vector_size, intervals)
    v_insertion = generate_vector(vector_size, intervals)
    v_bubble = generate_vector(vector_size, intervals)
    v_shell = generate_vector(vector_size, intervals)

    os.system('clear')
    print('=============== Resultado ===============\n\n')
    if vector_size < 50:
        print('Selection sort:')
        print('Vetor: '+  str(v_selection))
        selection_sort(v_selection)
        print('Vetor ordenado: ' + str(v_selection))

        print('\nInsertion sort:')
        print('Vetor: '+ str(v_insertion))
        insertion_sort(v_insertion)
        print('Vetor ordenado: '+str(v_insertion))

        print('\nBubble sort:')
        print('Vetor: '+ str(v_bubble))
        bubble_sort(v_bubble)
        print('Vetor ordenado: '+str(v_insertion))

        print('\nShell sort:')
        print('Vetor: '+ str(v_shell))
        shell_sort(v_shell)
        print('Vetor ordenado: '+str(v_shell))
    else:
        print('OBS.:Os vetores estao muito grandes para serem mostrados na tela\n')
        print('Selection sort:')
        selection_sort(v_selection)

        print('\nInsertion sort:')
        insertion_sort(v_insertion)

        print('\nBubble sort:')
        bubble_sort(v_bubble)

        print('\nShell sort:')
        shell_sort(v_shell)
menu()
