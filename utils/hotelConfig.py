import configparser, sys, os


def getFilePath(filename):
    basepath = "/cfg"
    dirname = os.path.dirname(basepath)
    print("directory - ", dirname)
    return os.path.join(basepath, filename)


def readConfigFile(filename):
    parser = configparser.ConfigParser()
    parser.read(getFilePath(filename))
    return parser


parser = readConfigFile("config.ini")
for sect in parser.sections():
    for k, v in parser.items(sect):
        print(k, v)
