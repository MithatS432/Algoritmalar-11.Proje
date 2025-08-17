def compute_lps(pattern):
    """ LPS (Longest Prefix Suffix) tablosunu hesaplar """
    lps = [0] * len(pattern)
    length = 0  # önceki en uzun prefix-suffix
    i = 1

    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps


def KMP_search(text, pattern):
    lps = compute_lps(pattern)
    i = j = 0  # i -> text index, j -> pattern index
    matches = []

    while i < len(text):
        if text[i] == pattern[j]:
            i += 1
            j += 1
        if j == len(pattern):
            matches.append(i - j)
            j = lps[j - 1]
        elif i < len(text) and text[i] != pattern[j]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return matches


text = "ABABDABACDABABCABAB"
pattern = "ABABCABAB"
print("KMP sonuçları:", KMP_search(text, pattern))
