import random
from tetris_shapes import SHAPES 

def get_random_shape():
    return random.choice(SHAPES)


def rotate(shape):
    # Obtenemos las dimensiones de la figura
    rows = len(shape)
    cols = len(shape[0])

        # Creamos una nueva matriz vacía para la figura rotada
    rotated_shape = [[0] * rows for _ in range(cols)]

        # Rotamos la figura
    for i in range(rows):
        for j in range(cols):
            rotated_shape[j][rows - 1 - i] = shape[i][j]
    
    return rotated_shape


def get_reference(shape):
    rows = len(shape)
    cols = len(shape[0])
    # reference = [[0] * rows for _ in range(cols)]

    # for j in range(rows):
    #     for i in range(cols):

    reference = []
    for j in range(rows):
        for i in range(cols):
            if shape[j][i] == 1:
                reference.append((j, i))
            
    return reference


def main():
    shape = SHAPES[5]
    count = 0
    rotated_shape = None
    reference = None

    while count <= 4:
        
        if rotated_shape is None and reference is None:
            print(shape)
            print(get_reference(shape))
            print()
        else:
            print(rotated_shape)
            print(reference)
            print()


        if rotated_shape is None and reference is None:
            # rotated_shape = rotate(shape)
            rotated_shape = rotate(shape)
            reference = get_reference(rotated_shape)
        else:
            rotated_shape = rotate(rotated_shape)
            reference = get_reference(rotated_shape)
            # rotated_shape = rotate(rotated_shape)

        count += 1


main()
