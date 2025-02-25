from django.shortcuts import render

# Create your views here.
from openai import OpenAI
from django.conf import settings

client = OpenAI(api_key=settings.OPENAI_API_KEY)
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Conversation
from .serializers import ConversationSerializer

# Set your OpenAI API key in settings.py

class ChatView(APIView):
    def post(self, request):
        user_message = request.data.get('message')
        if not user_message:
            return Response({"error": "Message is required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            response = client.chat.completions.create(model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_message}])
            bot_response = response.choices[0].message.content

            # Save conversation in the database
            conversation = Conversation.objects.create(user_message=user_message, bot_response=bot_response)
            serializer = ConversationSerializer(conversation)

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)