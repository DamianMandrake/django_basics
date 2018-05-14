from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist


def ret_obj_or_raise_404(objectclass, integer_id, request):
    try:
        return objectclass.get(id=integer_id)
    except ObjectDoesNotExist as d:
        print(d)
        return render(request, "404.html", status=404)

