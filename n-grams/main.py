import re


# !!
def n_grams_litery(file, n):
    '''
    Funkcja pobiera nazwę pliku i jak ma byc n-gram
    Analizuje i przetwarza tekst
    Wypisuje statystyki n-gramow
    '''
    with open(file, 'r') as f:
        grams = []
        freq = {}
        for line in f:
            line = line.lower()
            line = re.sub(r'[^a-ząćęłńóśżź ]', '', line)
            # z otrzymanych lliter tworz n-gramy
            grams += [
                line[i:i + n] for i in range(len(line) - n + 1)
                if line[i:i + n] != '  '
            ]  # + 1, żeby dodało ostatni człon
        for gram in grams:
            if gram in freq:
                freq[gram] += 1
            else:
                freq[gram] = 1
        for key, value in freq.items():
            print(f"'{key}': {value}\n")


# unfinished
def n_grams_sylaby(file, n):
    with open(file, 'r') as f:
        vowels = ['a', 'ą', 'e', 'ę', 'i', 'y', 'o', 'u', 'ó']
        digraphs = ['ch', 'cz', 'dz', 'dź', 'dż', 'sz', 'rz']
        syllables = []
        grams = []
        freq = {}
        for line in f:
            line = line.lower()
            line = re.sub(r'[^a-ząćęłńóśżź ]', '', line)
            line = line.split(' ')
            # nie bierze pod uwage ostatniej sylaby
            for word in line:
                # ile samoglosek juz bylo
                count = 0
                # pozycje samoglosek
                pos = []
                # indeks aktualnej samogloski
                l_index = 0
                # pozycja ostatniego podzialu
                i = 0
                for char in word:
                    if char in vowels:
                        count += 1
                        pos.append(l_index)
                    if count == 2:
                        # and l_index != len(word) - 1
                        # slicing w miejscu sum(pos)
                        vowel_pos = int(sum(pos) / 2)
                        syllables.append(word[i:vowel_pos])
                        i = vowel_pos
                        count -= 1
                        pos.pop(0)
                    c = sum(el in vowels for el in word[i:len(word)])
                    if count == 1 and word[i:len(word)] in ['nie', 'au']:
                        syllables.append(word[i:len(word)])
                    l_index += 1
            print(syllables)
            grams += [
                syllables[i:i + n] for i in range(len(syllables) - n + 1)
            ]
        for gram in grams:
            gram = " ".join([str(item) for item in gram])
            if gram in freq:
                freq[gram] += 1
            else:
                freq[gram] = 1
        for key, value in freq.items():
            print(f"'{key}': {value}\n")


def n_grams_slowa(file, n):
    with open(file, 'r') as f:
        grams = []
        freq = {}
        for line in f:
            line = line.lower()
            line = re.sub(r'[^a-ząćęłńóśżź ]', '', line)
            line = line.split(' ')
            grams += [
                line[i:i + n] for i in range(len(line) - n + 1)
                if line[i:i + n] != ' '
            ]
        for gram in grams:
            gram = " ".join([str(item) for item in gram])
            if gram in freq:
                freq[gram] += 1
            else:
                freq[gram] = 1
        for key, value in freq.items():
            print(f"'{key}': {value}\n")


# typ: litery, sylaby, slowa

n_grams_litery('pol1.txt', 2)

# n_grams_sylaby('zd.txt', 2)

# n_grams_slowa('pol1.txt', 2)
