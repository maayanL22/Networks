

def main():
    mac_address = input("Please enter a MAC address:\n")
    maclist = mac_address.split(':')
    if len(maclist) != 6:
        print("invalid")
        return
    for mac in maclist:
        if len(mac) != 2:
            print("Invalid")
            return
        for c in mac:
            if not 47 < ord(c) < 58 and not 64 < ord(c) < 91 and not 96 < ord(c) < 123:
                print("Invalid")
                return

    print("Valid")
    ventor = maclist[0] + ":" + maclist[1] + ":" + maclist[2]
    print("Ventor number:", ventor)
    fir = maclist[0]
    # print(fir)
    res = "{0:08b}".format(int(fir, 16))
    sfir = str(res)
    firl = list(sfir)
    l = len(firl)
    # print(firl)
    if firl[l - 1] == '0':
        print("Unicast")
    else:
        print("Multicast")


if __name__ == '__main__':
    main()
