from django.shortcuts import render
from django.views import generic

from service.models import DishType, Dish, Cook


def index(request):
    num_dish = Dish.objects.count()
    num_dish_type = DishType.objects.count()
    num_cooks = Cook.objects.count()
    context = {
        "num_dish": num_dish,
        "num_dish_type": num_dish_type,
        "num_cooks": num_cooks
    }
    return render(request, "service/index.html", context=context)


class DishTypeListView(generic.ListView):
    model = DishType


class DishListView(generic.ListView):
    model = Dish
    template_name = "service/dish_list.html"
    queryset = Dish.objects.select_related("cooks")


class DishDetailView(generic.DeleteView):
    pass


class CookListView(generic.ListView):
    model = Cook


class CookDetailView(generic.DetailView):
    pass
