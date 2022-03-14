import wikipedia


def yield_querys(queries):
    for elt in queries:
        print(elt)
        try:
            wiki_res = wikipedia.summary(elt, sentences=2,auto_suggest=False, redirect=True)
        except:
            wiki_res = "No result found"
            print("Wikipedia error")
            
        yield {'question': elt, 'answer': wiki_res} 