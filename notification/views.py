import json

import requests
from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class Notifcationapi(APIView):
    def post(self, request):
        global r
        # sending_message_serializer = SendingMessageSerializer(data=message_serializer.data)
        # if sending_message_serializer.is_valid():
        # dK-WBgh96Hk:APA91bEv-M4YrmIm0qYnhgqf2viFKmNzYDKbGDiD3yEKPi7iKE_IfE-yKsPJiyPn1HLU_C7UmKVkHcTC68GW6HShp2ZHl8K6KSmmN3qgEJ86OOJGAcgUBI30brCXyPmRiTFBmTbMs7BT
        if(request.data):
            print(request.data)
            json_data = {'to': request.data['nameValuePairs']['to'],
                         'notification': {'body': request.data['nameValuePairs']['data']['nameValuePairs']['body'], 'title': request.data['nameValuePairs']['data']['nameValuePairs']['title']}, }
            print(json.dumps(json_data))
            jsondata = json.dumps(json_data)
            jsondataasbytes = jsondata.encode('UTF-8')
            r = requests.post("https://fcm.googleapis.com/fcm/send",
                              data=jsondataasbytes, headers={'Authorization': 'key=AIzaSyCty7NRhwhoEYn8hQQL79HxRtc_0paKMys',
                                                       'Content-Type': 'application/json; charset=UTF-8',
                                                       })
            if r.status_code == 200:
                print(r)
                return Response(r, status=status.HTTP_200_OK)
            else:
                return Response(r, status=status.HTTP_400_BAD_REQUEST)
