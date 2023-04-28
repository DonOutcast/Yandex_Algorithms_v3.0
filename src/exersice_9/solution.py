def summa_matrix():
    rows, columns, query = map(int, input().split())
    temp = []
    print(query)
    for i in range(rows):
        str_ = list(map(int, input().split()))
        for number in range(1, len(str_)):
            str_[number] = str_[number] + str_[number - 1]
        temp.append(str_)
    print(temp)
    # for i in range(query):
    #     x1, y1, x2, y2 = map(int, input().split())
    #     x1 -= 1
    #     y1 -= 1
    #     x2 -= 1
    #     y2 -= 1
    #     result = 0
    #     while x1 <= x2:
    #         result += temp[x1][y2] - (temp[x1][y1 - 1] if y1 != 0 else 0)
    #         x1 += 1
    #     print(result)



# matrix = [[random.randrange(0, 10) for a in range(5)] for b in range(3)]
#     for i in matrix:
#         for j in i:
#             print(j, end=" ")
#         print()
if __name__ == "__main__":
    summa_matrix()