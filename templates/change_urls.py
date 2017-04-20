import glob

files = glob.glob('*.html')

for f in files:
    print f
    text = open(f).read()
    #tmp = text.split(".html'")[:-1]
    #htmls = [t.split("'")[-1] for t in tmp]
    tmp = text.split('.html"')[:-1]
    htmls = [t.split('"')[-1] for t in tmp]
    print len(htmls)
    for html in htmls:
        print "'"+html+".html'", '=>', '{{url_for("'+html+'")}}'
        text = text.replace('"'+html+'.html"', '{{url_for("'+html+'")}}')
        print text
    boop = open(f, 'w')
    boop.write(text)
    boop.close()

