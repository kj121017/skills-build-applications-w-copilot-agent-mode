from django.http import JsonResponse

def api_root(request):
    return JsonResponse({
        "message": "Welcome to the Octofit API!",
        "url": "https://supreme-broccoli-x5xxgq499x97h6r69-8000.app.github.dev"
    })