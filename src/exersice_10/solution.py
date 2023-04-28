def delete_literal():
    word = input()
    m_alb = {}
    for i in range(len(word)):
        if word[i] in m_alb.keys():
            m_alb[word[i]] += (len(word) - i) * (i + 1)
        else:
            m_alb[word[i]] = (len(word) - i) * (i + 1)

    for key, value in dict(sorted(m_alb.items())).items():
        print(key + ":", value)


if __name__ == "__main__":
    delete_literal()
