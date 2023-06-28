with open("aha","r") as readhex:
    hex_list = readhex.readlines()
    b_data = b''
    for i in range(len(hex_list)):
        hex_data = hex_list[i].replace('\n','')
        b_data += bytes.fromhex(hex_data)
    with open("wuhu.db", "wb") as file:
        file.write(b_data)
