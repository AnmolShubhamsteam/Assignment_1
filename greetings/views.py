from django.shortcuts import render

def greetings(request):
    return render(request,"greetings.html",{})

def square(request,pk):
    squares={}
    for i in range(1,pk+1):
        squares[i]=pow(i,2)
    context={"squares":squares.items()}
    return render(request,"square.html",context)

def table(request, pk, sk):
    table_n = {}
    for i in range(1, sk + 1):
        index = str(pk) + "*" + str(i)
        table_n[index] = pk * i
    context = {"tables": table_n.items()}
    return render(request, "table.html", context)

def count_vowel(request,pk):
    text=pk.lower()
    li=['a','e','i','o','u']
    vli=[i for i in text if i in li]
    cli=[i for i in text if i not in li and i.isalpha()]
    context={"v":len(vli),'c':len(cli),"vli":vli,"cli":cli}
    return render(request,"alpha.html",context)

def book_reviews(request):
    books={"a":"abcde","b":"defgh","c":"ijkl","d":"mnop"}
    context={"books":books.items()}
    return render(request,"book_review.html",context)
