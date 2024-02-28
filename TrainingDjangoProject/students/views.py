from django.shortcuts import render
from django.http import Http404
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Standard, Student
from .serializers import StandardSerializer, StudentSerializer

class StandardList(APIView):
    def get(self, request):
        standards = Standard.objects.all()
        serializer = StandardSerializer(standards, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StandardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StandardDetail(APIView):
    def get_object(self, pk):
        try:
            return Standard.objects.get(pk=pk)
        except Standard.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        standard = self.get_object(pk)
        serializer = StandardSerializer(standard)
        return Response(serializer.data)

    def put(self, request, pk):
        standard = self.get_object(pk)
        serializer = StandardSerializer(standard, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        standard = self.get_object(pk)
        standard.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class StudentList(APIView):
    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StudentDetail(APIView):
    def get_object(self, pk):
        try:
            return Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        student = self.get_object(pk)
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    def put(self, request, pk):
        student = self.get_object(pk)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        student = self.get_object(pk)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#Pagination
def student_list(request, page=1, per_page=10):
    # Fetch all student records
    students = Student.objects.all()

    # Handle search functionality
    search_name = request.GET.get('search_name')
    if search_name:
        students = students.filter(name__icontains=search_name)

    # Create Paginator instance
    paginator = Paginator(students, per_page)

    # Get the records for the requested page
    page_obj = paginator.get_page(page)

    if search_name:
        return render(request, 'student_list.html', {'page_obj': page_obj, 'per_page': per_page, 'page': page,'search':search_name})

    return render(request, 'student_list.html', {'page_obj': page_obj, 'per_page': per_page, 'page': page})
@csrf_exempt
def insert_student_data(request):
    # JSON data containing student records
    student_data = [
    {
        "name": "John Smith",
        "rollno": 1001,
        "standard": 10,
        "course": "Mathematics"
    },
    {
        "name": "Alice Johnson",
        "rollno": 1002,
        "standard": 10,
        "course": "Physics"
    },
    {
        "name": "Bob Jones",
        "rollno": 1003,
        "standard": 10,
        "course": "Chemistry"
    },
    {
        "name": "Emma Brown",
        "rollno": 1004,
        "standard": 10,
        "course": "Biology"
    },
    {
        "name": "Michael Davis",
        "rollno": 1005,
        "standard": 10,
        "course": "English"
    },
    {
        "name": "Sophia Miller",
        "rollno": 1006,
        "standard": 10,
        "course": "History"
    },
    {
        "name": "William Wilson",
        "rollno": 1007,
        "standard": 10,
        "course": "Geography"
    },
    {
        "name": "Olivia Taylor",
        "rollno": 1008,
        "standard": 10,
        "course": "Computer Science"
    },
    {
        "name": "James Anderson",
        "rollno": 1009,
        "standard": 10,
        "course": "Art"
    },
    {
        "name": "Emily Thomas",
        "rollno": 1010,
        "standard": 10,
        "course": "Music"
    },
    {
        "name": "Daniel Hernandez",
        "rollno": 1011,
        "standard": 11,
        "course": "Mathematics"
    },
    {
        "name": "Amelia Martinez",
        "rollno": 1012,
        "standard": 11,
        "course": "Physics"
    },
    {
        "name": "Lucas Thompson",
        "rollno": 1013,
        "standard": 11,
        "course": "Chemistry"
    },
    {
        "name": "Mia Garcia",
        "rollno": 1014,
        "standard": 11,
        "course": "Biology"
    },
    {
        "name": "Aiden Robinson",
        "rollno": 1015,
        "standard": 11,
        "course": "English"
    },
    {
        "name": "Ella Clark",
        "rollno": 1016,
        "standard": 11,
        "course": "History"
    },
    {
        "name": "Logan Rodriguez",
        "rollno": 1017,
        "standard": 11,
        "course": "Geography"
    },
    {
        "name": "Avery Lewis",
        "rollno": 1018,
        "standard": 11,
        "course": "Computer Science"
    },
    {
        "name": "Evelyn Lee",
        "rollno": 1019,
        "standard": 11,
        "course": "Art"
    },
    {
        "name": "Jack Walker",
        "rollno": 1020,
        "standard": 11,
        "course": "Music"
    },
    {
        "name": "Liam Perez",
        "rollno": 1021,
        "standard": 12,
        "course": "Mathematics"
    },
    {
        "name": "Layla Scott",
        "rollno": 1022,
        "standard": 12,
        "course": "Physics"
    },
    {
        "name": "Nora Green",
        "rollno": 1023,
        "standard": 12,
        "course": "Chemistry"
    },
    {
        "name": "Jacob Adams",
        "rollno": 1024,
        "standard": 12,
        "course": "Biology"
    },
    {
        "name": "Grace Campbell",
        "rollno": 1025,
        "standard": 12,
        "course": "English"
    },
    {
        "name": "Isaac Flores",
        "rollno": 1026,
        "standard": 12,
        "course": "History"
    },
    {
        "name": "Mila King",
        "rollno": 1027,
        "standard": 12,
        "course": "Geography"
    },
    {
        "name": "Benjamin Hill",
        "rollno": 1028,
        "standard": 12,
        "course": "Computer Science"
    },
    {
        "name": "Hannah Mitchell",
        "rollno": 1029,
        "standard": 12,
        "course": "Art"
    },
    {
        "name": "Gabriel Carter",
        "rollno": 1030,
        "standard": 12,
        "course": "Music"
    },
    {
        "name": "Noah Evans",
        "rollno": 1031,
        "standard": 9,
        "course": "Mathematics"
    },
    {
        "name": "Victoria Rivera",
        "rollno": 1032,
        "standard": 9,
        "course": "Physics"
    },
    {
        "name": "Sofia Hall",
        "rollno": 1033,
        "standard": 9,
        "course": "Chemistry"
    },
    {
        "name": "Henry Ward",
        "rollno": 1034,
        "standard": 9,
        "course": "Biology"
    },
    {
        "name": "Harper Butler",
        "rollno": 1035,
        "standard": 9,
        "course": "English"
    },
    {
        "name": "Owen Foster",
        "rollno": 1036,
        "standard": 9,
        "course": "History"
    },
    {
        "name": "Stella Simmons",
        "rollno": 1037,
        "standard": 9,
        "course": "Geography"
    },
    {
        "name": "Jackson Powell",
        "rollno": 1038,
        "standard": 9,
        "course": "Computer Science"
    },
    {
        "name": "Aria Barnes",
        "rollno": 1039,
        "standard": 9,
        "course": "Art"
    },
    {
        "name": "Levi Hughes",
        "rollno": 1040,
        "standard": 9,
        "course": "Music"
    },
    {
        "name": "Emma Johnson",
        "rollno": 1041,
        "standard": 8,
        "course": "Mathematics"
    },
    {
        "name": "Alexander Roberts",
        "rollno": 1042,
        "standard": 8,
        "course": "Physics"
    },
    {
        "name": "Mason Turner",
        "rollno": 1043,
        "standard": 8,
        "course": "Chemistry"
    },
    {
        "name": "Scarlett Nelson",
        "rollno": 1044,
        "standard": 8,
        "course": "Biology"
    },
    {
        "name": "Aurora Wood",
        "rollno": 1045,
        "standard": 8,
        "course": "English"
    },
    {
        "name": "Zoe Coleman",
        "rollno": 1046,
        "standard": 8,
        "course": "History"
    },
    {
        "name": "Ethan Ward",
        "rollno": 1047,
        "standard": 8,
        "course": "Geography"
    },
    {
        "name": "Madison Richardson",
        "rollno": 1048,
        "standard": 8,
        "course": "Computer Science"
    },
    {
        "name": "Lucy Hughes",
        "rollno": 1049,
        "standard": 8,
        "course": "Art"
    },
    {
        "name": "Ryan Diaz",
        "rollno": 1050,
        "standard": 8,
        "course": "Music"
    }
]
    

    # Insert data into the database
    for data in student_data:
        standard_instance = Standard.objects.get(pk=data['standard'])
        student = Student(
            name=data['name'],
            rollno=data['rollno'],
            standard=standard_instance,
            course=data['course']
        )
        student.save()

    return JsonResponse({'message': 'Student data inserted successfully'})    