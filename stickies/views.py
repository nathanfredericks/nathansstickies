from django.views.generic import ListView
from django.db import Error
import json
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Sticky


class StickyListView(ListView):
    model = Sticky


class UploadView(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAdminUser]

    def post(self, request):
        # check if content-type is json
        if request.headers['Content-Type'] != 'application/json':
            response = {
                'detail': 'Content-Type not supported!',
            }
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

        try:
            # attempt to parse json
            data = json.loads(request.body, strict=False)
        except ValueError:
            response = {
                'detail': 'Error parsing JSON request body.',
            }
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

        try:
            # make a list of Sticky objects to add to database
            stickies = data['stickies']  # list of stickies
            sticky_objs = []
            for sticky in stickies:
                # add to columns list
                sticky_objs.append(
                    Sticky(window=sticky['window'], text=sticky['text'])
                )
        except KeyError:
            response = {
                'detail': 'JSON request body is missing required key(s).',
            }
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

        try:
            # delete all current stickies
            Sticky.objects.all().delete()

            # create new stickies
            bulk_sticky_objs = Sticky.objects.bulk_create(sticky_objs)
            bulk_sticky_objs.save()
        except Error:
            response = {
                'detail': 'Error saving to database.',
            }
            return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        finally:
            response = {
                'detail': 'Successfully uploaded stickies!'
            }
            return Response(response, status=status.HTTP_201_CREATED)
