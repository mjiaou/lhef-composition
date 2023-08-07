if __name__ == '__main__':
    f = open("new_eventfile.dat", "r")

    diagram_dict = {}

    for x in f:
        if x == '<event>\n':
            event_info = f.readline().split()
            diagram = ""
            for i in range(int(event_info[0])):
                line = f.readline().split()
                diagram += line[0]+","

            if diagram in diagram_dict:
                diagram_dict[diagram] += 1
            else:
                diagram_dict[diagram] = 1

    total = 0
    percentage_dict = {}
    for key in diagram_dict:
        total += diagram_dict[key]

    for key in diagram_dict:
        percentage_dict[key] = diagram_dict[key] / total

    print(diagram_dict)
    print(percentage_dict)
    print("\nOut of %d events:" % total)

    for key in diagram_dict:
        print(key + ": " + str(diagram_dict[key]) + ", which is " + str(percentage_dict[key]) + "% of the total counts")

    f.close()
