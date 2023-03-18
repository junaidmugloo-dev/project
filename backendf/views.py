import json
from django.http import JsonResponse
from django.http import HttpResponse
from pymongo import MongoClient
import pymongo
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets,status
from .serializer import *

railway ="mongodb://mongo:NKwMj4MdAXfZMsmXsJWe@containers-us-west-169.railway.app:8009"

def getadmin(request):
    client = pymongo.MongoClient(railway)
    db = client['project']
    collection = db['admin']

    details = list(collection.find({},{
        '_id':0,
        'user':1,
        'password':1
    }))
    return JsonResponse(details,safe=False)

def getappo(request):
    client= pymongo.MongoClient(railway)
    ab = client['project']
    collection = ab['meetings']

    details = list(collection.find({},{
        '_id':0,
        'name':1,
        'patient':1,
        'sent':1,
        'category':1,
        'slot':1,
        'report':1,
        'doc':1
    }))
    return JsonResponse(details,safe=False)

def getdocx(request):
    client = pymongo.MongoClient(railway)
    db = client['project']
    collection = db['doctor']

    details = list(collection.find({},{
        '_id':0,
        'name':1,
        'category':1,
        'place':1,
        'password':1
    }))
    return JsonResponse(details,safe=False)


def getdocs(request):
    client = pymongo.MongoClient(railway)
    db = client['project']
    collection = db['category']

    details = list(collection.find({},{
        '_id':0,
        'service':1,
        'image':1
    }))
    return JsonResponse(details,safe=False)

def getlog(request):
    client = pymongo.MongoClient(railway)
    db = client['project']
    collection = db['log']

    details = list(collection.find({},{
        '_id':0,
        'Email':1,
        'city':1,
        'phone':1,
        'password':1
    }))
    return JsonResponse(details,safe=False)


class registerviewset(viewsets.ViewSet):
    @action(methods=['post'],detail=False)
    def setlog(self,request):
        serializer = RegisterSerial(data=request.data)
        if serializer.is_valid():
            Email = serializer.validated_data['Email']
            city = serializer.validated_data['city']
            phone = serializer.validated_data['phone']
            password = serializer.validated_data['password']

            client = pymongo.MongoClient(railway)
            db = client['project']
            details = db['log']

            details.insert_one({
                'Email':Email,
                'city':city,
                'phone':phone,
                'password':password
            })
            return Response({'status':'success'})
        return Response({},status=status.HTTP_204_NO_CONTENT)
        


class addDoctorviewset(viewsets.ViewSet):
    @action(methods=['post'],detail=False)
    def adddoc(self,request):
        serializer = doctorserial(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data['name']
            category = serializer.validated_data['category']
            place = serializer.validated_data['place']
            password = serializer.validated_data['password']

            client = pymongo.MongoClient(railway)
            db = client['project']
            collection = db['doctor']

            collection.insert_one({
                'name':name,
                'category':category,
                'place':place,
                'password':password
            })
            return Response({'status':'success'})
        return Response({},status=status.HTTP_204_NO_CONTENT)


class deletes(viewsets.ViewSet):
    @action(methods=['post'],detail=False)
    def delslot(self,request):
        serializer = deleteslot(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data['name']
            category = serializer.validated_data['category']

            client = pymongo.MongoClient(railway)
            db = client['project']
            collection = db['meetings']

            collection.delete_one({
                'name':name,
                'category':category
            })
            return Response({'status':'success'})
        return Response({},status=status.HTTP_204_NO_CONTENT)



class removeDoctorviewset(viewsets.ViewSet):
    @action(methods=['post'],detail=False)
    def deldoc(self,request):
        serializer = deletedoctorserial(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data['name']
            category = serializer.validated_data['category']
          

            client = pymongo.MongoClient(railway)
            db = client['project']
            collection = db['doctor']

            collection.delete_one({
                'name':name,
                'category':category,
               
            })
            return Response({'status':'success'})
        return Response({},status=status.HTTP_204_NO_CONTENT)

class meetingviewset(viewsets.ViewSet):
    @action(methods =['post'],detail=False)
    def meeting(self,request):
        serializer = meetingsSerial(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data['name']
            patient = serializer.validated_data['patient']
            sent = serializer.validated_data['sent']
            category = serializer.validated_data['category']
            slot = serializer.validated_data['slot']
            report = serializer.validated_data['report']
            doc =serializer.validated_data['doc']
            
            client = pymongo.MongoClient(railway)
            db = client['project']
            details = db['meetings']

            details.insert_one({
                'name':name,
                'patient':patient,
                'sent':sent,
                'category':category,
                'slot':slot,
                'report':report,
                'doc':doc
            })
            return Response({'status':'success'})
        return Response({},status=status.HTTP_204_NO_CONTENT)



class updatepass(viewsets.ViewSet):
    @action(methods=['post'],detail=False)
    def update(self,request):
        serializer = passwordSerial(data=request.data)
        if serializer.is_valid():
            Email = serializer.validated_data['Email']
            password = serializer.validated_data['password']

            client = pymongo.MongoClient(railway)
            db = client['project']
            details = db['log']

            details.update_one({
                'Email':Email,
            },{
                '$set':{
                    'password':password
                }
            })
            return Response({'status':'success'})
        return Response({},status=status.HTTP_204_NO_CONTENT)



class updateservice(viewsets.ViewSet):
    @action(methods=['post'],detail=False)
    def addservice(self,request):
        serializer = serviceSerial(data=request.data)
        if serializer.is_valid():
            service = serializer.validated_data['service']
            image = serializer.validated_data['image']

            client = pymongo.MongoClient(railway)
            db = client['project']
            collection = db['category']

            collection.insert_one({
                'service':service,
                'image':image
            })
            return Response({'status':'success'})
        return Response({},status=status.HTTP_204_NO_CONTENT)
    



class delcateview(viewsets.ViewSet):
    @action(methods=['post'],detail=False)
    def delcategory(self,request):
        serializer = delcat(data=request.data)
        if serializer.is_valid():
            service = serializer.validated_data['service']

            client = pymongo.MongoClient(railway)
            db = client['project']
            collection = db['category']

            collection.delete_one({
                'service':service
            })
            return Response({'status':'success'})
        return Response({},status=status.HTTP_204_NO_CONTENT)