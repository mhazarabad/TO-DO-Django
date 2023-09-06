
def Get_Json_Data_From_API(request,keyword,on_error_value,part='body'):
    from json import loads as From_Json
    try:
        if part=='body':
            variable=From_Json(request.body.decode("utf-8"))[keyword]
        else:
            variable=request.headers[keyword]
    except:
        variable=on_error_value
    return variable

def Blog_Manager(request,todo_id:str=None):
    from django.http.response import JsonResponse
    from .models import Todo
    print(request.method,todo_id)
    match (request.method, todo_id):
        case ('GET',None):
            page=request.GET.get('page',1)
            todo_list,max_page=Todo.filter_query_with_paginator(page=page)
            return JsonResponse(data={"page":page,"data":[todo.export_to_response for todo in todo_list],"max_page":max_page})
        case ('GET',_):
            from django.core.exceptions import ObjectDoesNotExist
            try:
                todo=Todo.objects.get(id=todo_id)
                return JsonResponse(data={"description":"ok","data":todo.export_to_response},status=200)
            except ObjectDoesNotExist:
                todo=None
                return JsonResponse(data={"description":"todo not found"},status=404)# not found
            except Exception as e:
                # send error to montiro center or add an issue to github
                return JsonResponse(data={},status=500)
        case ('POST',None):
            new_todo_name=Get_Json_Data_From_API(request=request,keyword='name',on_error_value=None)
            new_todo_description=Get_Json_Data_From_API(request=request,keyword='description',on_error_value=None)
            new_todo_start_date=Get_Json_Data_From_API(request=request,keyword='start_date',on_error_value=None)
            new_todo_due_date=Get_Json_Data_From_API(request=request,keyword='due_date',on_error_value=None)
            new_todo_status=Get_Json_Data_From_API(request=request,keyword='status',on_error_value='1')

            if new_todo_name==None:
                return JsonResponse(data={"description":"Field {} is not optional".format("name")},status=400)
            try:
                new_todo_start_date_datetime_obj=new_todo_start_date if new_todo_start_date==None else Todo.create_datetime_object_from_string(datetime_string=new_todo_start_date)
            except Exception as e:
                return JsonResponse(data={"description":"Error in {}: {}".format("start_date field",str(e))},status=400)
            
            try:
                new_todo_due_date_datetime_obj=new_todo_due_date if new_todo_due_date==None else Todo.create_datetime_object_from_string(datetime_string=new_todo_due_date)
            except Exception as e:
                return JsonResponse(data={"description":"Error in {}: {}".format("due_date field",str(e))},status=400)

            try:
                new_todo=Todo.objects.create(
                    name=str(new_todo_name)[:100],
                    description=str(new_todo_description),
                    start_date=new_todo_start_date_datetime_obj,
                    due_date=new_todo_due_date_datetime_obj,
                    status=Todo.get_status_id(unknown_status=new_todo_status,status_choices=Todo.STATUS_CHOICES)
                )
            except Exception as e:
                return JsonResponse(data={"description":"Error in saving Todo: {}".format(str(e))},status=400)

            return JsonResponse(data={"description":"todo created","data":new_todo.export_to_response},status=200)

        case ('PUT',_):
            todo_new_name=Get_Json_Data_From_API(request=request,keyword='name',on_error_value=None)
            todo_new_description=Get_Json_Data_From_API(request=request,keyword='description',on_error_value=None)
            todo_new_start_date=Get_Json_Data_From_API(request=request,keyword='start_date',on_error_value=None)
            todo_new_due_date=Get_Json_Data_From_API(request=request,keyword='due_date',on_error_value=None)
            todo_new_status=Get_Json_Data_From_API(request=request,keyword='status',on_error_value=None)

            if todo_id == None:
                return JsonResponse(data={"description":"todo id is not optional"},status=400)
            
            from django.core.exceptions import ObjectDoesNotExist
            try:
                todo=Todo.objects.get(id=todo_id)
            except ObjectDoesNotExist:
                return JsonResponse(data={"description":"todo not found"})
            except Exception as e:
                # send error to montiro center or add an issue to github
                return JsonResponse(data={},status=500)

            todo_got_new_data=False

            if todo_new_name!=None:
                todo.name=str(todo_new_name)[:100]
                todo_got_new_data=True

            if todo_new_description!=None:
                todo.description=str(todo_new_description)
                todo_got_new_data=True

            if todo_new_status:
                todo.status=Todo.get_status_id(unknown_status=todo_new_status,status_choices=Todo.STATUS_CHOICES)
                todo_got_new_data=True

            if todo_new_start_date!=None:
                try:
                    todo_new_start_date_datetime_object=Todo.create_datetime_object_from_string(datetime_string=todo_new_start_date)
                except Exception as e:
                    return JsonResponse(data={"description":"Error in {}: {}".format("start_date field",str(e))},status=400)
                todo.start_date=todo_new_start_date_datetime_object
                todo_got_new_data=True

            if todo_new_due_date!=None:
                try:
                    todo_new_due_date_datetime_object=Todo.create_datetime_object_from_string(datetime_string=todo_new_due_date)
                except Exception as e:
                    return JsonResponse(data={"description":"Error in {}: {}".format("due_date field",str(e))},status=400)
                todo.due_date=todo_new_due_date_datetime_object
                todo_got_new_data=True

            if todo_got_new_data:
                try:
                    todo.save()
                except Exception as e:
                    return JsonResponse(data={"description":"Error in saving Todo: {}".format(str(e))},status=400)
                return JsonResponse(data={"description":"todo updated successfuly","data":todo.export_to_response},status=200)
            return JsonResponse(data={"description":"todo got no change","data":todo.export_to_response},status=200)

        case ('DELETE',_):

            if todo_id == None:
                return JsonResponse(data={"description":"todo id is not optional"},status=400)
            
            from django.core.exceptions import ObjectDoesNotExist
            try:
                todo=Todo.objects.get(id=todo_id)
            except ObjectDoesNotExist:
                return JsonResponse(data={"description":"todo not found"})
            except Exception as e:
                # send error to montiro center or add an issue to github
                return JsonResponse(data={},status=500)
            
            try:
                todo.delete()
            except Exception as e:
                return JsonResponse(data={"description":"Error in deleting Todo: {}".format(str(e))},status=400)
            
            return JsonResponse(data={"description":"todo deleted successfuly"},status=200) 
        
    return JsonResponse(data={},status=405)# method not allowed
    
    
    


