if __name__ == "__main__":
    for x in xrange(1,255):
        ip = "192.168.166."
        ip += str(x) + "/32"
        filename = str(x) + ".ips"
        fp = open(filename, "w")

        fp.write(ip)

        fp.close()