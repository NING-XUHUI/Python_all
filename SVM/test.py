import os



def extractLetters(path):
    x = []
    y = []
    for root, sub_dirs, files in os.walk(path):
        for dirs in sub_dirs:
            for fileName in os.listdir(path + '/' + dirs):
                print(fileName)
                x.append(fileName)
                y.append(dirs)
    return x, y

if __name__ == "__main__":
    path = './data'
    x, y = extractLetters(path)
    print(x[:10])
    print(y[:10])