file_name = "names.txt"
f = open(file_name, "w+")
f.write("Ada,Alan,Isabella,Lizbeth,Abigail,Meltem,Gülcan")
f.close()

file_name2 = "surnames.txt"
f2 = open(file_name2, "w+")
f2.write("Lovelace,Turing,Cortez,Bathory,Red,Arnhen,Keriti")
f2.close()


def transform_to_row(infile, outfile):
    with open(infile, "r") as reader:
        content = reader.read()
        new_content = content.replace(",", "\n")
    outfilename = outfile + ".txt"
    with open(outfilename, "w") as writer:
        writer.write(new_content)


transform_to_row("names.txt", "names_in_row")

transform_to_row("surnames.txt", "surnames_in_row")


def add_greeting(infile, outfile):
    outfilename = outfile + ".txt"
    newline = ""
    with open(infile, "r") as reader:
        for line in reader:
            newline += "Hello " + line.strip() + "\n"
    with open(outfilename, "w") as writer:
        writer.write(newline)


add_greeting("names_in_row.txt", "plus_greetings")


def strip_greetings(infile, outfile):
    outfilename = outfile + ".txt"
    strip = ""
    with open(infile, "r") as reader:
        for line in reader:
            strip += line.replace("Hello ", "")
    with open(outfilename, "w") as writer:
        writer.write(strip)


strip_greetings("plus_greetings.txt", "without_greetings")


def combine_files(file1, file2, outfile):
    outfilename = outfile + ".txt"
    with open(file1, "r") as reader1:
        line_count1 = 0
        for line in reader1:
            if line != "\n":
                line_count1 += 1
    with open(file2, "r") as reader2:
        line_count2 = 0
        for line in reader2:
            if line != "\n":
                line_count2 += 1
    if line_count1 == line_count2:
        with open(file1, "r") as r1:
            with open(file2, "r") as r2:
                with open(outfilename, "w") as w3:
                    f1l = r1.readlines()
                    f2l = r2.readlines()
                    for line1, line2 in zip(f1l, f2l):
                        w3.write("{} {}\n".format(line1.rstrip(), line2.rstrip()))
    else:
        print("The files", file1, "and", file2, "do not have the same amount of lines and cannot be combined.")


combine_files("plus_greetings.txt", "surnames_in_row.txt", "merge")
combine_files("names.txt", "names_in_row.txt", "merge2")
