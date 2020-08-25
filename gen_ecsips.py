if __name__ == "__main__":
    ecsinfo = "192.168.1.1 1\n"
    dnatinfo = "192.168.166.3 172.16.0.1 0 0 0 0\n"
    for x in xrange(1,255):
        ip = "192.168.166."
        ip += str(x) + "/32"
        filename = str(x) + ".ecs.ips"
        fp = open(filename, "w")

        fp.write(ecsinfo)
        fp.write(dnatinfo)
        fp.write(ip)

        fp.close()