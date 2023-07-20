import tagging
from django.db.models import QuerySet
from django.shortcuts import render

from django.http import HttpResponse, Http404
from tagging.managers import ModelTagManager, ModelTaggedItemManager
from tagging.models import Tag, TaggedItem

from taggyWaggy.models import Thingie


def index(request):
    return render(request, "index.html")


def tag_OR_query(model, tags):
    result = TaggedItem.objects.none()
    for tag in tags:
        result = result.union(TaggedItem.objects.get_by_model(model, tag))

    return result


def search_results(request):
    search_terms = []
    all_thingies_found = []

    if request.method == 'POST':
        search_terms = request.POST['search_terms']
        thingies_by_name = Thingie.objects.filter(name__icontains=search_terms)
        tags = tagging.models.get_tag_list(search_terms)
        thingies_by_tag = tag_OR_query(Thingie, tags)
        all_thingies_found = thingies_by_name.union(thingies_by_tag).order_by('name')

        context = {
            'search_terms': search_terms,
            'all_thingies_found': all_thingies_found
        }

        return render(request, "search_results.html", context)


def thingie_list(request):
    return render(request, 'thingie_list.html', context={"thingies_found": Thingie.objects.all()})


def thingie_view(request, thingie_id):
    try:
        thingie = Thingie.objects.get(pk=thingie_id)

    except Thingie.DoesNotExist:
        raise Http404("That rule does not exist")
    context = {
        'thingie': thingie,
    }
    return render(request, 'thingie_view.html', context=context)
