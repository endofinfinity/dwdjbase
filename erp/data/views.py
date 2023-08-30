from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.http import HttpResponse



# Create your views here.
def index(request):
    # return HttpResponse("ok")
    '''
    request: Any, 请求
    template_name: Any, 模板名字
    context: Any = None, 替代
    content_type: Any = None,
    status: Any = None,
    using: Any = None) ->
    '''
    context = {
        "name": "三国",
        "lll": "快看看"
    }
    return render(request, 'data/index.html', context)

    # return redirect("http://www.baidu.com")