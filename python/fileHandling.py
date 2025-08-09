def writing(filename,text):
    f = open(filename, "w")
    f.write(text)
    f.close()
def append(filename,text):
    f = open(filename, "a")
    f.write(text)
    f.close()
def reading(filename):
    try:
        f = open(filename, "r")
        text = f.read()
        print(text)
        f.close()
    except FileNotFoundError as e:
        print(e)
def search(filename,word):
    try:
        f = open("example.txt","r")
        count_line = 0
        for line in f.readlines():
            count_line+=1
            strlist = line.split(" ")
            word_count = 0
            for w in strlist:
                word_count+=1
                if word == w:
                    f.close()
                    return (count_line,word_count)
        else:
            f.close()
            return None
        
    except FileNotFoundError as e:
        print(e)

    


s = "Global Market Research & Intelligence A leading global market research firm delivering in-depth insights across a wide range of industries, with a strong presence in the USA, Europe, Southeast Asia, the UK, GCC, and Asia. Explore Research Reports Request Custom Research 5000+ Published Reports 50+ Industries Covered 25+ Regions Covered" 
# append("example.txt",s)

# t = search('example.txt','range')
# print(t)