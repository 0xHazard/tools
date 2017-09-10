def route(data):
    bin_list = list(map(lambda ip: "".join("{0:08b}".format(int(octet)) for octet in ip.split('.')), data))
    mask = 32
    while len(set(i[:mask] for i in bin_list)) > 1:
        mask -= 1
    bin_net = bin_list[0][:mask].ljust(32, '0')
    net = ".".join(str(int(bin_net[i:i+8], 2)) for i in range(0, 32, 8))
    return "{}/{}".format(net, mask)

print(route(["172.16.12.0", "172.16.13.0", "172.16.14.0", "172.16.15.0"]))
print(route(["172.16.12.0", "172.16.13.0", "172.155.43.9"]))