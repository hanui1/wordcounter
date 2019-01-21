from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'wordcount/home.html')

def about(request):
    return render(request, 'wordcount/about.html')

def count(request):
    full_text = request.GET['fulltext']
    word_list = full_text.split()

    word_dictionary = {} #dictionary 선언

    #키-값(key-value)

    for word in word_list:
        if word in word_dictionary:
            # Increase
            word_dictionary[word] += 1
        else:
            # add to the dictionary
            word_dictionary[word] = 1
            #값[키]?
    
    return render(request, 'wordcount/count.html', {'fulltext': full_text, 'total':len(word), 'dictionary':word_dictionary.items()})
    #word_dictionary.items() 까지 적어야 키+value값까지 출력 됨. items()안적으면 키만 출력 됨