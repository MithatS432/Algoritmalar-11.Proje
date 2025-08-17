def rabin_karp(text, pattern, d=256, q=101):
    n, m = len(text), len(pattern)
    p_hash = 0  # pattern hash
    t_hash = 0  # text hash
    h = pow(d, m-1) % q
    matches = []

    # İlk hash değerlerini hesapla
    for i in range(m):
        p_hash = (d * p_hash + ord(pattern[i])) % q
        t_hash = (d * t_hash + ord(text[i])) % q

    # Kaydırma yap
    for i in range(n - m + 1):
        if p_hash == t_hash:  # hash eşleşirse
            if text[i:i+m] == pattern:  # karakter karakter kontrol
                matches.append(i)

        if i < n - m:
            t_hash = (d * (t_hash - ord(text[i]) * h) + ord(text[i + m])) % q
            if t_hash < 0:
                t_hash += q
    return matches


text = "GEEKS FOR GEEKS"
pattern = "GEEK"
print("Rabin-Karp sonuçları:", rabin_karp(text, pattern))
