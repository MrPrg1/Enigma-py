import pickle

alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ !@#$%^&*()_+-=~`1234567890,./:;"|][{}₮₯₰₱₲₳₴₵₶₷₸₹₺₻₼₽₾₿℅ℓ№℗™Ω℮⅍ⅎ⅓ↄ←↑→↓↔↕∂∆∏∑√∞∩∫≈≠≡≤≥⌂⌐⌠⌡─│┌┐└☺♪♫♯ⱠⱡⱢⱣⱤⱥⱦⱧ☻'



f = open('./todays_rotor_state.enigma', 'rb')
r1, r2, r3, r4, r5, r6, r7, r8, r9, r10 = pickle.load(f)
f.close()


def reflector(c):
    return alphabet[len(alphabet)-alphabet.find(c)-1]

def enigma_one_char(c):
    c1 = r1[alphabet.find(c)]
    c2 = r2[alphabet.find(c1)]
    c3 = r3[alphabet.find(c2)]
    c4 = r4[alphabet.find(c3)]
    c5 = r5[alphabet.find(c4)]
    c6 = r6[alphabet.find(c5)]
    c7 = r7[alphabet.find(c6)]
    c8 = r8[alphabet.find(c7)]
    c9 = r9[alphabet.find(c8)]
    c10 = r10[alphabet.find(c9)]
    reflected = reflector(c10)
    c10 = alphabet[r10.find(reflected)]
    c9 = alphabet[r9.find(c10)]
    c8 = alphabet[r8.find(c9)]
    c7 = alphabet[r7.find(c8)]
    c6 = alphabet[r6.find(c7)]
    c5 = alphabet[r5.find(c6)]
    c4 = alphabet[r4.find(c5)]
    c3 = alphabet[r3.find(c4)]
    c2 = alphabet[r2.find(c3)]
    c1 = alphabet[r1.find(c2)]

    return c1

plain = input('Lotfan Peyghame Morede Nazar Ra Vared Konid : ')
cipher = ''


for c in plain:
    cipher += enigma_one_char(c)

print(cipher)
