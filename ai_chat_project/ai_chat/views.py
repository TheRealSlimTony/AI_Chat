from rest_framework import generics
from .models import Mensaje
from .serializers import MensajeSerializer, QuestionSerializer
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationSummaryMemory
from langchain.chains import ConversationalRetrievalChain
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from .vectorialdb import VectorialDatabase


class MensajeListCreate(generics.ListCreateAPIView):
    queryset = Mensaje.objects.all()
    serializer_class = MensajeSerializer
    print("MensajeListCreate: ", queryset, serializer_class)


class SearchQuestion(APIView):
    def post(self, request, *args, **kwargs):
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            question = serializer.validated_data["prompt"]

            # Crea una instancia de VectorialDatabase
            vectordb = VectorialDatabase()

            # Realiza la búsqueda de similitud para la pregunta dada
            response, source = vectordb.similarity_search(question)

            return Response({"result": response, "source": source})
        else:
            return Response(serializer.errors, status=400)


def home(request):
    return HttpResponse("Bienvenido al Chat AI")
