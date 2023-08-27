import hashlib
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt





@csrf_exempt
def calculate_hash(request):
    emp = ""
    hash_algorithms = {
            'MD5': hashlib.md5,
            'SHA-1': hashlib.sha1,
            'SHA-256': hashlib.sha256,
            'SHA-384': hashlib.sha384,
            'SHA-512': hashlib.sha512
        }
    if request.method == 'POST':
        data = request.POST.get('data')
        file = request.FILES.get('file')
        
        hash_algorithms = {
            'MD5': hashlib.md5,
            'SHA-1': hashlib.sha1,
            'SHA-256': hashlib.sha256,
            'SHA-384': hashlib.sha384,
            'SHA-512': hashlib.sha512
        }

        results = {}

        if file:
            file_data = file.read()
            for algorithm_name, algorithm_func in hash_algorithms.items():
                hash_obj = algorithm_func()
                hash_obj.update(file_data)
                file_hash = hash_obj.hexdigest()
                results[algorithm_name] = file_hash

        elif data:
            for algorithm_name, algorithm_func in hash_algorithms.items():
                hash_obj = algorithm_func(data.encode('utf-8'))
                data_hash = hash_obj.hexdigest()
                results[algorithm_name] = data_hash
        emp = "value"
        return render(request, 'hashapp/index.html', {'results': results})
    teste = "testing"
    return render(request, 'hashapp/index.html',{'vide' : emp , 'results' : hash_algorithms} )