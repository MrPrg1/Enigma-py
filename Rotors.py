import pickle


alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ !@#$%^&*()_+-=~`1234567890,./:;"|][{}₮₯₰₱₲₳₴₵₶₷₸₹₺₻₼₽₾₿℅ℓ№℗™Ω℮⅍ⅎ⅓ↄ←↑→↓↔↕∂∆∏∑√∞∩∫≈≠≡≤≥⌂⌐⌠⌡─│┌┐└☺♪♫♯ⱠⱡⱢⱣⱤⱥⱦⱧ☻'
password = 'rsapopauya'

p1 = password[0]
p2 = password[1]
p3 = password[2]
p4 = password[3]
p5 = password[4]
p6 = password[5]
p7 = password[6]
p8 = password[7]
p9 = password[8]
p10 = password[9]


t1 = alphabet.index(p1)
r1r = alphabet[t1:]
b1b = alphabet[:t1]
r1 = r1r + b1b



t2 = alphabet.index(p2)
r2r = alphabet[t2:]
b2b = alphabet[:t2]
r2 = r2r + b2b



t3 = alphabet.index(p3)
r3r = alphabet[t3:]
b3b = alphabet[:t3]
r3 = r3r + b3b



t4 = alphabet.index(p4)
r4r = alphabet[t4:]
b4b = alphabet[:t4]
r4 = r4r + b4b



t5 = alphabet.index(p5)
r5r = alphabet[t5:]
b5b = alphabet[:t5]
r5 = r5r + b5b



t6 = alphabet.index(p6)
r6r = alphabet[t6:]
b6b = alphabet[:t6]
r6 = r6r + b6b



t7 = alphabet.index(p7)
r7r = alphabet[t7:]
b7b = alphabet[:t7]
r7 = r7r + b7b



t8 = alphabet.index(p8)
r8r = alphabet[t8:]
b8b = alphabet[:t8]
r8 = r8r + b8b



t9 = alphabet.index(p9)
r9r = alphabet[t9:]
b9b = alphabet[:t9]
r9 = r9r + b9b



t10 = alphabet.index(p10)
r10r = alphabet[t10:]
b10b = alphabet[:t10]
r10 = r10r + b10b


f = open('./todays_rotor_state.enigma', 'wb')
pickle.dump((r1, r2, r3, r4, r5, r6, r7, r8, r9, r10), f)
f.close()

