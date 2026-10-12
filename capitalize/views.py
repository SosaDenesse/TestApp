from django.shortcuts import render

# Create your views here.
def index(request):
    capitalized_text = ""

    if request.method == "POST":
        # user submits text through a POST request
        user_text = request.POST.get("text")
        capitalized_text = user_text.upper()

    return render(
        request, "capitalize/index.html",
        {"capitalized_text": capitalized_text}
    )
