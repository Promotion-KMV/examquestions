def is_user_role (request, user_role):

    user_groups_list = request.user.groups.values_list('name',flat = True)
    print ('users role is ===', user_role)
    print ('user groups from AUTH ====> ', user_groups_list, ' <===== ')

    status = (True if (user_role in user_groups_list) else False)

    print ('user have this role:', status)

    return status




def user_exam_access_check (request, exam_slug):

    user_orders_queryset = request.user.order_set.all()
    
    user_exam_access_list = []

    for object in user_orders_queryset:
        print ('exam_slug = ',object.exam_link.exam_id)
        user_exam_access_list.append (object.exam_link.exam_id) 

    
    status = (True if (exam_slug in user_exam_access_list) else False)
    
    print ('EXAM ACCESS ==', status)

    return status
