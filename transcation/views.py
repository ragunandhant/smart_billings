from django.shortcuts import render,redirect, get_object_or_404
from whatsapp import sendMessage
# Create your views h
from cart.models import Cart,CartItem
from .models import Transcation
from user.models import userProfile
from django.contrib import messages

import qrcode
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.conf import settings
import os
import cipher

import cv2
from pyzbar import pyzbar
def getDetails(id):
    id = int(id)
    trans = Transcation.objects.get(id = id)
    cartitem = CartItem.objects.filter(cart = trans.cart)
    trans.save()
    return cartitem,trans
def getqr(request):
    # Initialize the camera
    cap = cv2.VideoCapture(0)

    while True:
        # Capture a frame from the camera
        ret, frame = cap.read()

        # Decode any QR codes in the frame
        decoded_objs = pyzbar.decode(frame)

        # Print the content of any QR codes found
        found = False
        for obj in decoded_objs:
            print(f'QR Code content: {obj.data.decode()}')
            s = cipher.decrypt_message(obj.data.decode())
            cap.release()
            cv2.destroyAllWindows()
            messages.success(request,s)
            cartitem ,trans= getDetails(s)
            context = {'cart':cartitem}

            if trans.is_printed:
                context['error'] = 'You have billed it'
                del context['cart']
            trans.is_printed = True
            trans.save()
            return render(request,'bill_details.html',context)
        # Display the frame
        cv2.imshow('frame', frame)

        # Exit if the user presses the 'q' key
        if cv2.waitKey(1) & 0xFF == ord('q') :
            break

    # Release the camera and close the window
    cap.release()
    cv2.destroyAllWindows()
    return redirect('core:index')

def download_image(request):
    # Get the path to the image file
    image_path = os.path.join(settings.MEDIA_ROOT, 'images', 'qr.png')
    
    # Check that the image file exists
    if not os.path.exists(image_path):
        return HttpResponse('File not found', status=404)
    
    # Open the image file in binary mode
    with open(image_path, 'rb') as f:
        response = HttpResponse(f.read(), content_type='image/png')
        response['Content-Disposition'] = 'attachment; filename=qr.png'
        return response

def checkout(request):
    if request.user.is_authenticated:
        cart = get_object_or_404(Cart,user=request.user,is_active = True)
        #cartitem = CartItem.objects.get(cart = cart)
        user = get_object_or_404(userProfile,user=request.user)
        total = cart.total
        success = False
        if user.wallet_amount >= total:
            trans = Transcation.objects.create(cart=cart,user=user.user,amount = total)
            trans.transcate(cart)
            print(user.wallet_amount)
            user.wallet_amount -= total
            print(user.wallet_amount)

            user.save()
            trans.save()
            success = True 
            #encryption
            encryption  = cipher.encrpyt_message(str(trans.id))
            img= qrcode.make(encryption)
            img.save('media/images/qr.png')

        if success:
            while not sendMessage(user.phone_number):
                pass
            messages.success(request,"completed")
            return render(request,'download.html',{'path':"F:\smart_billing_try\qr.png"})
        else:
            messages.error(request,"insufficient money")      
            return redirect('core:index')
    else:
        messages.error(request,"pls login in")
        return redirect('user:login')
def mytranscation(request):
    if request.user.is_authenticated:
        transcation = Transcation.objects.filter(user=request.user).order_by('created_at').values
        """for i in transcation:
            print(i.created_at,i.cart.total_amt)"""
        return render(request,'transcation.html',{'trans':transcation})
    else:
        messages.error(request,"pls login in")
        return redirect('user:login')

