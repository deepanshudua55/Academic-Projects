import math


def get_similarity(count_matrix1, count_matrix2):

    matrix1_keys = count_matrix1.keys()
    matrix2_keys = count_matrix2.keys()
    common_words = list(set(matrix1_keys).intersection(matrix1_keys))

    cross_product = 0
    for word in common_words:
        if word in count_matrix1 and word in count_matrix2:
            cross_product += (count_matrix1[word] * count_matrix2[word])

    sum_matrix1 = 0
    sum_matrix2 = 0

    for word in matrix1_keys:
        sum_matrix1 += count_matrix1[word]**2
    for word in matrix2_keys:
        sum_matrix2 += count_matrix2[word]**2

    magnitude = math.sqrt(sum_matrix1) * math.sqrt(sum_matrix2)

    if not magnitude:
        return 0.0
    else:
        divide = float(cross_product) / magnitude
        return round(divide, 2)