def file_to_str(file):
    with open(file, 'r') as f:
        line = f.readline()
        txt = line.replace(",", "")
    return txt

def build_suffix(text): #for the last part
    n = len(text)
    suffixes = []
    for i in range(n):
        suffixes.append((text[i:], i))
    suffixes.sort()

    suffixes_index = []
    for suffix in suffixes:
        suffixes_index.append(suffix[1])
    return suffixes_index

#def build_lcp(text, suffixArray):



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

#def find_longest_common_substring(text1, text2):


def kmp_search(pattern, text):
    lps = build_lps(pattern)
    n = len(text)  # len for the text
    i = 0  # index for text
    j = 0  # index for pattern
    result = []
    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == len(pattern):  # full match found
            result.append(i)
            j = lps[j - 1]  # reset j to check for overlapping matches

        elif i < len(text) and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return result

def main():
    malicious_txt = ["transmission1.txt", "transmission2.txt"]
    files_txt = ["mcode1.txt", "mcode2.txt", "mcode3.txt"]

    for malicious in malicious_txt:
        for file in files_txt:
            malicious_code = file_to_str(malicious)
            txt = file_to_str(file)
            occurrences = []
            occurrences += kmp_search(malicious_code, txt)
            occurrences += kmp_search(malicious_code[::1], txt)
            if len(occurrences) > 0:
                print(f"True : the file {file} contains the code ({malicious_code}) contained in the file {malicious} ")
            else:
                print(
                    f"False : the file {file} doesn't contains the code ({malicious_code}) contained in the file {malicious} ")
            for occurrence in occurrences:
                print(
                    f"startPosition: {occurrence}, endPosition: {occurrence + len(malicious_code)} (for {file} file) ")
            print("\n")


if __name__ == '__main__':
    main()
