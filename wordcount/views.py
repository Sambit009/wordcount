from django.http import HttpResponse
from django.shortcuts import render
import operator
def homepage(request):
	return HttpResponse("<h1>This is homepage</h1>")

def contact(request):
	return HttpResponse("<h1>This is contact us page</h1>")
	
def index(request):
	return render(request,"index.html")
def count(request):
	data=request.GET['fulltextarea']
	word_list=data.split()
	length=len(word_list)
	print(length)
	worddictionary={}
	for word in word_list:
		if word in worddictionary:
			worddictionary[word]+=1
		else:
			worddictionary[word]=1
	sorted_list=sorted(worddictionary.items(),key=operator.itemgetter(1),reverse=True)
	print(sorted_list)
	return render(request,"count.html",{'fulltext':data,'words':length,'worddictionary':sorted_list})
	
