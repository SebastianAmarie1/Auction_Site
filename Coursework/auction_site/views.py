
from django.http import JsonResponse, HttpRequest, HttpResponse
import json
from . import models
from datetime import datetime
from django.contrib.auth import authenticate,login,logout
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail



'''posting and getting individual user'''
@csrf_exempt
def users_api_indv(request: HttpRequest) -> JsonResponse:
    if request.method == "POST":
        
        user = models.User.objects.get(id=request.POST['userId'])  
        user.email = request.POST['email']
        user.dob = request.POST['dob']
        user.city = request.POST['city']
        if (request.FILES.get('picture')):
            user.profile_picture = request.FILES.get('picture')
        user.save()  

        selectedUser: models.User = models.User.objects.get(id=request.POST['userId'])

        return JsonResponse({"user": selectedUser.to_dict()})


'''for signing in'''
@csrf_exempt
def sign_in(request: HttpRequest) -> JsonResponse:

    POST: request = json.loads(request.body)
    username: str = POST['username']
    password: str = POST['password']
    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        print("Login successful")
        selected_user: models.User = models.User.objects.get(username=request.user)
        return JsonResponse(selected_user.to_dict())
    else:
        return JsonResponse({"Message": 'Unsuccessful login'})


'''for signing up'''
@csrf_exempt
def sign_up(request: HttpRequest) -> JsonResponse:
    POST: request = json.loads(request.body)
    if request.method == 'POST':
        if POST['password'] == POST['confirm_password']:
            new_user: models.User = models.User.objects.create_user(email=POST['email'], username=POST['username'] ,first_name=POST['first_name'], last_name=POST['last_name'], password=POST['password'], dob=POST['dob'])
            send_mail('Registration Successful!','Welcome, you have sucessfully signed in to YouBid!', 'webbycw3@gmail.com', [POST['email']])
            print('Successfully created account')
        else:
            print('Passwords did not match')
        return JsonResponse(new_user.to_dict())


'''for signing out'''
@csrf_exempt
def sign_out(request: HttpRequest) -> JsonResponse:
    logout(request)
    return JsonResponse({"Message": 'Successful logout'})


@csrf_exempt
def check_logged_in(request: HttpRequest) -> JsonResponse:
    if request.user.is_authenticated:
        print("logged in")
        return JsonResponse(request.user.to_dict())
    else:
        print("Not logged in")
        return JsonResponse({"Message": 'Not Logged In'})

#PRODUCTS
'''for getting all products and posting products'''
@csrf_exempt
def products_api(request: HttpRequest) -> JsonResponse:
    if request.method == "POST":
        selectedUser: models.User = models.User.objects.get(id=request.POST['sender_id'])
        
        models.Products.objects.create(
            name= request.POST['name'],
            owner = selectedUser, 
            description = request.POST['description'],
            picture = request.FILES.get('image'),
            start_date = request.POST['start_date'],
            finish_date = request.POST['finish_date'],
        )

    return JsonResponse({
        'products': [
            products.to_dict()
            for products in models.Products.objects.filter(finish_date__gt=datetime.today())
        ]
    })
        

'''This function is to get a specific Product'''
@csrf_exempt
def product_api_indv(request: HttpRequest, product_id: int) -> JsonResponse:
    if request.method == "GET":
        product: models.Products = models.Products.objects.get(id=product_id)
        return JsonResponse({
            'product': [
                product.to_dict() 
            ]
        }) 



#REVIEWS
''' posting of reviews'''
@csrf_exempt
def reviews_api(request: HttpRequest) -> JsonResponse:
    if request.method == "POST":
        body: request = json.loads(request.body)
        
        selectedUser: models.User = models.User.objects.get(id=body['sender_id'])
        selectedItem: models.Products = models.Products.objects.get(id=body['item_id'])

        models.Review.objects.create(
            message= body['message'],
            sender_id= selectedUser,
            item_id= selectedItem,
            date_posted= body['date_posted'],
        )
    
        return JsonResponse({
            'reviews': [
                reviews.to_dict()
                for reviews in models.Review.objects.all()
            ]
        })

'''Getting a specific Review'''
@csrf_exempt
def reviews_api_indv(request: HttpRequest, rev_id: int) -> JsonResponse:
    if request.method == "POST":
        body: request = json.loads(request.body)

        selectedUser: models.User = models.User.objects.get(id=body['sender_id'])
        product: models.Products = models.Products.objects.get(id=rev_id)

        models.Review.objects.create(
            message= body['message'],
            sender= selectedUser,
            item=product,
        )

    product: models.Products = models.Products.objects.get(id=rev_id)
    reviewsTable: models.Review = models.Review.objects.filter(item = product)

    reviews: list[object] = []
    for r in reviewsTable:
        reviews.append(r.to_dict())

    if (reviews):
        return JsonResponse({
            'reviews': reviews
        })
    else :
        return JsonResponse({"message": "No Reviews"})
            

'''Gets the Replies for a reviews and allows posting of replies'''
@csrf_exempt
def replies_api(request: HttpRequest) -> JsonResponse:
    if request.method == "POST":
        body = json.loads(request.body)
        
        selectedUser: models.User = models.User.objects.get(id=body['sender_id'])
        selectedReview: models.Review = models.Review.objects.get(id=body['replying_id'])

        models.Replies.objects.create(
            replying_id= selectedReview,
            message= body['message'],
            sender_id= selectedUser,
            date_posted= body['date_posted'],
        )
    
        return JsonResponse({
            'reviews': [
                reviews.to_dict()
                for reviews in models.Replies.objects.all()
            ]
        })


@csrf_exempt
def replies_api_indv(request: HttpRequest, rep_id: int) -> JsonResponse:
    if request.method == "POST":
        body = json.loads(request.body)

        selectedUser: models.User = models.User.objects.get(id=body['sender_id'])
        product: models.Products = models.Products.objects.get(id=rep_id)
        replying: models.Review = models.Review.objects.get(id=body['replying'])

        models.Replies.objects.create(
            message= body['message'],
            sender= selectedUser,
            item=product,
            replying=replying,
        )

    product: models.Products = models.Products.objects.get(id=rep_id)
    repliessTable: models.Replies = models.Replies.objects.filter(item = product)
    replies: list[object] = []

    for r in repliessTable:
        replies.append(r.to_dict())

    if (replies):
        return JsonResponse({
            'replies': replies
        })
    else :
        return JsonResponse({"message": "No Reviews"})

@csrf_exempt
def bids_api(request: HttpRequest) -> JsonResponse:
    if request.method == "GET":
        products: models.Products = models.Products.objects.filter(finish_date__gt=datetime.today())
        bidsList: list[object] = []
        for p in products:
            bids: models.Bids = models.Bids.objects.filter(product=p)
            highest: int = 0
            cSet: models.Bids = None
            if (len(bids) != 0):
                for b in bids:
                    if (highest < b.amount):
                        highest = b.amount
                        cSet = b
                bidsList.append(cSet.to_dict())

        if (bidsList):
            return JsonResponse({
                'bids': bidsList
            })
        else :
            return JsonResponse({"message": "No Reviews"})

    if request.method == "POST":
        body: request = json.loads(request.body)

        selectedUser: models.User = models.User.objects.get(id=body['sender_id'])
        product: models.Products = models.Products.objects.get(id=body["product_id"])

        bid: models.Bids = models.Bids.objects.create(
            amount= body['amount'],
            user= selectedUser,
            product= product,
        )

        return JsonResponse({
            'bid': bid.to_dict()
        })

@csrf_exempt
def bids_api_indv(request: HttpRequest, pro_id: int) -> JsonResponse:
    if request.method == "GET":
        product: models.Products = models.Products.objects.filter(id=pro_id)

        bids: models.Bids = models.Bids.objects.filter(product=product[0])
        highest: int = 0
        cSet: models.Bids = None
        for bid in bids:
            if (highest < bid.amount):
                highest = bid.amount
                cSet = bid

        if cSet != None:
            return JsonResponse({
                    'bids': [
                        cSet.to_dict()
                    ]
                })
        else:
            return JsonResponse({"amount": 0})

