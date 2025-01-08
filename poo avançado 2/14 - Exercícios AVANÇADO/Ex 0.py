'''
Calculadora de Matrizes
Crie uma calculadora de matrizes que permita ao usuário realizar operações como adição, subtração e multiplicação de matrizes. 
Você pode implementar uma interface simples em linha de comando onde o usuário insere as dimensões e os elementos das matrizes, e em seguida escolhe a operação desejada.
'''
class MatrixCalculator:
    @staticmethod
    def add(matrix1, matrix2):
        if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
            raise ValueError("Matrizes de tamanhos diferentes não podem ser somadas.")
        result = []
        for i in range(len(matrix1)):
            row = []
            for j in range(len(matrix1[0])):
                row.append(matrix1[i][j] + matrix2[i][j])
            result.append(row)
        return result

    @staticmethod
    def subtract(matrix1, matrix2):
        if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
            raise ValueError("Matrizes de tamanhos diferentes não podem ser subtraídas.")
        result = []
        for i in range(len(matrix1)):
            row = []
            for j in range(len(matrix1[0])):
                row.append(matrix1[i][j] - matrix2[i][j])
            result.append(row)
        return result

    @staticmethod
    def multiply(matrix1, matrix2):
        if len(matrix1[0]) != len(matrix2):
            raise ValueError("Número de colunas da primeira matriz deve ser igual ao número de linhas da segunda matriz.")
        result = []
        for i in range(len(matrix1)):
            row = []
            for j in range(len(matrix2[0])):
                total = 0
                for k in range(len(matrix2)):
                    total += matrix1[i][k] * matrix2[k][j]
                row.append(total)
            result.append(row)
        return result

# Exemplo de uso:
matrix1 = [[1, 2], [3, 4]]
matrix2 = [[5, 6], [7, 8]]
result_add = MatrixCalculator.add(matrix1, matrix2)
result_subtract = MatrixCalculator.subtract(matrix1, matrix2)
result_multiply = MatrixCalculator.multiply(matrix1, matrix2)
print("Soma:", result_add)
print("Subtração:", result_subtract)
print("Multiplicação:", result_multiply)
