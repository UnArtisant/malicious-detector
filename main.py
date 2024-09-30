'''
Jorge Rodrigo Colín Rubio           | A01662960
Raphaël Marc Joseph Barriet	 	    | A01763686
Nicole Kapellmann Lepine		    | A01664563
'''

def file_to_str(file):
    with open(file, 'r') as f:
        line = f.readline()
        txt = line.replace(",", "")
    return txt

def build_suffix(text): #step 3
    n = len(text)
    suffixes = []
    for i in range(n):
        suffixes.append((text[i:], i))
    suffixes.sort()

    suffixes_index = []
    for suffix in suffixes:
        suffixes_index.append(suffix[1])
    return suffixes_index

def build_lcp(text, suffixArray): #step 3
    n = len(text)
    lcp = [0]*n

    def z_function(string):
        n = len(string)
        z_list = [0] * n
        l = 0
        r = 0
        k = 0
        for i in range(1,n):
            if i > r: #normal case
                l = i
                r = i
                while (r < n and string[r-l] == string[r]):
                    r+=1
                z_list[i] = r-l
                r-=1 #goes back one because that last one was false
            elif i <= r:#when the i is within the limits of l -> r  (possibility to reuse the velue)
                k = i - l
                if z_list[k] < r - i + 1: #means that the vale is reusable because all the others coincide
                    z_list[i] = z_list[k] #reuse the value
                else: #make the process again 
                    l = i
                    while (r < n and string[r-l] == string[r]):
                        r+=1
                    z_list[i] = r-l
                    r-=1
        return z_list
    
    for i in range(1, n):
        suffix_i = text[suffixArray[i]:]
        suffix_j = text[suffixArray[i-1]:]

        suffixI_J = suffix_i + '$' + suffix_j
        z_values = z_function(suffixI_J)
        lcp[i] = z_values[len(suffix_i) + 1]
    return lcp

def longest_common_substring(text1, text2): #step 3
    text_concat = text1 + "#" + text2 + "$"
    suffix_arr = build_suffix(text_concat)
    lcp = build_lcp(text_concat, suffix_arr)

    max_len = 0
    position = 0
    n = len(text1) #length from text 1

    for i in range(1, len(lcp)):
        if(suffix_arr[i]< n) != (suffix_arr[i - 1] < n):
            if lcp[i] > max_len:
                max_len = lcp[i]
                position = suffix_arr[i]
    return text_concat[position:position + max_len]

        

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

    transmission1 = file_to_str("transmission1.txt")
    transmission2 = file_to_str("transmission2.txt")

    print(longest_common_substring(transmission1, transmission2))

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
