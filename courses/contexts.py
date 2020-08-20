def user_groups(request):
    groups = []
    user = request.user
    if user.is_authenticated:
        groups = list(user.groups.values_list('name',flat = True))
    return {'groups': groups}


def purchased_courses(request):
    purchased_courses = []
    if request.user.is_authenticated:
        purchased_courses =  [purchase.course for purchase in request.user.purchase_set.all()]
    return {'purchased_courses': purchased_courses}