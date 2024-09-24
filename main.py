def file_to_str(file):
    with open(file, 'r') as f:
        line = f.readline()
        txt = line.replace(",", "")
    return txt


def build_lps(pattern):
    lps = [0] * len(pattern)
    length = 0
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


def kmp_search(pattern, text):
    lps = build_lps(pattern)
    i = 0  # index for text
    j = 0  # index for pattern
    count = 0
    while i < len(text):
        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == len(pattern):  # full match found
            count += 1
            j = lps[j - 1]  # reset j to check for overlapping matches

        elif i < len(text) and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return count


def main():
    malicious_txt = ["transmission1.txt", "transmission2.txt"]
    files_txt = ["mcode2.txt", "mcode1.txt", "mcode3.txt"]

    for malicious in malicious_txt:
        size_malicious = len(malicious)
        for file in files_txt:
            size = 0
            total = len(files_txt)
            malicious_code = file_to_str(malicious)
            txt = file_to_str(file)
            size += kmp_search(malicious_code, txt)
            size += kmp_search(malicious_code[::1], txt)
            percentage = round(size_malicious / total, 2)
            print(f"total malicious code : {percentage}%, number of occurence of malicous code : {size}")


if __name__ == '__main__':
    main()
