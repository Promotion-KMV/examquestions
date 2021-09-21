from django.http.response import JsonResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from PIL import Image, ImageDraw, ImageFont
from django.http import JsonResponse
import json

from django.contrib.auth.decorators import login_required

from .forms import CreatNewUserForm, LoginForm
from .auth import is_user_role, user_exam_access_check



from .models import Vendor
from .models import Exam
from .models import Question
from .models import Order



def home_view(request):
    queryset_1 = Vendor.objects.all()
    queryset_2 = Exam.objects.all()
    context = {
        "object_list_1": queryset_1,
        "object_list_2": queryset_2
    }

    return render(request, 'template_home_2.html',context)


def logout_view(request):
    logout (request)
    return redirect('login')


def register_view (request):
    form = CreatNewUserForm()

    if request.method == 'POST':
        form = CreatNewUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')



    context = {'form':form}
    return render(request, 'template_register.html',context)


def login_view(request):
    print("******login 1 ******")
    form = LoginForm(request.POST)

    print (request)
    if request.method == 'POST':

        print("******login 2 ******")
        username = request.POST.get('username')
        password = request.POST.get('password')

        print ("username",username)

        user = authenticate(request, username=username, password=password)
        print (user)

        if user is not None:
            print("******login 3 ******")
            login(request, user)
            return redirect('home')

    context = {'form':form}
    return render(request, 'template_login.html',context)

    


def vendor_list_view(request):
    queryset = Vendor.objects.all()
    context = {
        "object_list": queryset
    }

    return render(request, 'template_1.html',context)
    
#lisg of exams from given vendor v_id
def vendor_exam_list_view(request, v_id):
    
    #vendor_obj = Exam.objects.get(vendor_id = v_id),
    print (v_id),

    queryset = Exam.objects.filter(vendor_id = v_id)
    context = {
        "object_list": queryset
    }

    return render(request, 'template_exams.html',context)

# list of questions of the exam
@login_required(login_url='login')
def exam_question_list_view(request, v_id, e_id):

    qpp = 2 #questions per page
    page = int(request.GET.get('page', 1)) #requested page, if nothing provided in GET = 1
    queryset = Question.objects.filter(exam_id = e_id)[(page-1)*qpp:page*qpp] #questions for the requested page
    
    questions_count = Question.objects.filter(exam_id = e_id).count() #overall amout of questions
    pages_count = round(questions_count / qpp) #overall amount of pages based on amount of questions and questions per page (qpp)
    
    # if (page > 1) : previous_page = page - 1
    # else: previous_page = 1

    previous_page = (page - 1) if (page > 1) else 1
    next_page = (page + 1) if (page < pages_count) else pages_count 

    print ("page count ====",pages_count, "<===== ")
    
    gold_user =  is_user_role(request, 'gold')

    exam_access = user_exam_access_check(request, e_id)




    context = {
        "exam_slag": e_id,
        "object_list": queryset,
        "pages_count": pages_count,
        "current_page": page,
        "previous_page": previous_page,
        "next_page": next_page,
        "is_gold_user": gold_user,
        "has_access_to_exam": exam_access
    }

    print (context)

    return render(request, 'template_questions.html',context)


def create_order(request):
    body = json.loads(request.body)
    print ('BODY:', body)

    exam_url = body['ExamId']

    exam_obj = Exam.objects.get(exam_id = exam_url)


    print ('#######################')

    print (request.user)

    print ('#######################')

    print (exam_obj.exam_id)

    print ('#######################')

    print (exam_obj.id)

    print ('#######################')

    Order.objects.create(
        user_link = request.user,
        exam_link = exam_obj
    )
    return JsonResponse ('Payment Completted!', safe = False)





def admin_tools (request):

    func_id = int(request.GET.get('func', 0))


    
    if func_id == 0: 
        context = {}
        print ('option 0 - no tools')



    elif func_id == 1:
        queryset = Question.objects.all()

        print ('Queryset to make imagres = ', queryset.count())

        for question in queryset:

            img = Image.new('RGB', (800, 300), color = (255, 255, 254))
            img_name = 'static/q_images/'+question.exam_id+'_'+str(question.question_id)+'.png'
            print ('image name = ', img_name)

            fnt = ImageFont.truetype('/Library/Fonts/Arial.ttf', 15)
      

            draw = ImageDraw.Draw(img)
            draw.text((10,10), str(question.question_text),font=fnt, fill=(0,0,0))


            img.save(img_name)
        


        context = {}

    else: 
        context = {}
        print ('option Something else')
    

    
    return render(request, 'template_admin_tools.html', context)




# # list of questions of the exam
# def questions_view(request,*args, **kwargs):
#     #return HttpResponse("<h1>Hellow to ExamQuestions.com</h1>")
#     return render(request, 'template_1.html',{})
