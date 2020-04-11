import os

def execCmd(cmd):
    r = os.popen(cmd)
    text = r.read()
    r.close()
    return text


if __name__ == "__main__":
    execCmd("scrapy crawl HemnetSpider")