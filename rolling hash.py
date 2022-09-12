key = 256 - 1 #[0,255]
real_flag = ""
fake_flag = 1317748575983887541099
#print(hex(key))
while fake_flag > 0:
#    null = fake_flag & hex(key)
    null = fake_flag & 0xff
    real_flag += chr(null)
    fake_flag = fake_flag - null
    fake_flag = fake_flag >> 8

print(real_flag[::-1])
