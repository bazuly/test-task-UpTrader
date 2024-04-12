from django import template
from menu.models import MenuItem


register = template.Library()

"""
Фильтрация данных по статусу allowed/forbidden. 
Создаем вложенность в меню"
"""


@register.inclusion_tag("menu.html", takes_context=True)  # принимаем контекст шаблона
def draw_menu(context, menu_name):
    objects = MenuItem.objects.filter(menu__name=menu_name, status="Allowed")
    objects_dict = {}
    for menu_object in objects:
        # если нет родительского элемента
        # то он становится корневым элементом в меню
        if menu_object.parent is None:
            objects_dict[str(menu_object.id)] = {"item": menu_object, "subitems": []}
        else:
            objects_dict[str(menu_object.parent_id)]["subitems"].append(menu_object)

    result = {"menu_name": menu_name, "data": list(objects_dict.values())}
    return {"result": result}
    