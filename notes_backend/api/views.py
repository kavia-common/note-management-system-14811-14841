from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.request import Request
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, ListModelMixin
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from .models import Note
from .serializers import NoteSerializer


@api_view(['GET'])
def health(request: Request):
    """
    Health check endpoint.

    Returns:
        200 OK with {"message": "Server is up!"}
    """
    return Response({"message": "Server is up!"})


# PUBLIC_INTERFACE
class NoteViewSet(CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, ListModelMixin, viewsets.GenericViewSet):
    """
    A ViewSet for performing CRUD operations on notes.

    Endpoints:
    - GET /api/notes/           -> list notes
    - POST /api/notes/          -> create note
    - GET /api/notes/{id}/      -> retrieve note
    - PUT /api/notes/{id}/      -> full update
    - PATCH /api/notes/{id}/    -> partial update
    - DELETE /api/notes/{id}/   -> delete note
    """
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    @swagger_auto_schema(
        operation_id="listNotes",
        operation_summary="List notes",
        operation_description="Retrieve a list of all notes ordered by last updated.",
        responses={200: NoteSerializer(many=True)},
        tags=["Notes"],
    )
    def list(self, request: Request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_id="createNote",
        operation_summary="Create a note",
        operation_description="Create a new note with title and optional content.",
        request_body=NoteSerializer,
        responses={201: NoteSerializer},
        tags=["Notes"],
    )
    def create(self, request: Request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_id="retrieveNote",
        operation_summary="Retrieve a note",
        operation_description="Get a single note by its ID.",
        responses={200: NoteSerializer},
        tags=["Notes"],
    )
    def retrieve(self, request: Request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_id="updateNote",
        operation_summary="Update a note",
        operation_description="Update all fields of a note.",
        request_body=NoteSerializer,
        responses={200: NoteSerializer},
        tags=["Notes"],
    )
    def update(self, request: Request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_id="partialUpdateNote",
        operation_summary="Partially update a note",
        operation_description="Update one or more fields of a note.",
        request_body=NoteSerializer,
        responses={200: NoteSerializer},
        tags=["Notes"],
    )
    def partial_update(self, request: Request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_id="deleteNote",
        operation_summary="Delete a note",
        operation_description="Delete a note by its ID.",
        responses={204: openapi.Response("No Content")},
        tags=["Notes"],
    )
    def destroy(self, request: Request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
