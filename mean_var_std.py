import numpy as np

minha_lista = [0,1,2,3,4,5,6,7,8]

def calculate(lista):
    # Verifica se a lista tem 9 elementos
    if len(lista) != 9:
        raise TypeError("A lista deve conter exatamente 9 números")
    
    # Verifica se todos os elementos são números
    if not all(isinstance(x, (int, float)) for x in lista):
        raise TypeError("Todos os elementos devem ser números")
    
    # Cria a matriz 3x3 a partir da lista
    array3x3 = np.array(lista).reshape(3, 3)

    # Cria o dicionário com as operações desejadas
    dicionario = {
        'mean': [np.round(np.mean(array3x3, axis=0), 2).tolist(), np.round(np.mean(array3x3, axis=1), 2).tolist(), np.round(np.mean(array3x3), 2).tolist()],
        'variance': [np.round(np.var(array3x3, axis=0), 2).tolist(), np.round(np.var(array3x3, axis=1), 2).tolist(), np.round(np.var(array3x3), 2).tolist()],
        'standard deviation': [np.round(np.std(array3x3, axis=0), 2).tolist(), np.round(np.std(array3x3, axis=1), 2).tolist(), np.round(np.std(array3x3), 2).tolist()],
        'max': [np.max(array3x3, axis=0).tolist(), np.max(array3x3, axis=1).tolist(), np.max(array3x3).tolist()],
        'min': [np.min(array3x3, axis=0).tolist(), np.min(array3x3, axis=1).tolist(), np.min(array3x3).tolist()],
        'sum': [np.sum(array3x3, axis=0).tolist(), np.sum(array3x3, axis=1).tolist(), np.sum(array3x3).tolist()]
    }

    return dicionario

print(calculate(minha_lista))
