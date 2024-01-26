from rest_framework.response import Response
from rest_framework.decorators import api_view

# python에서 @으로 시작하는 단어는 decorator라고 하는데
#실제 함수를 호출하면 특정 내용을 삽입해서 함수를 실행합니다,
# get 요청이 오면 함수를 호출
@api_view(['GET'])
def helloAPI(request):
  return Response('HELLO REST API')

from rest_framework import status
from rest_framework.generics import get_object_or_404

from .models import Book
from .serializers import BookSerializer

# 이방식은 GET 과 POST 모두를 처리
@api_view(['GET','POST'])
def booksAPI(request):
  # GET 방식의 처리 - 조회를 요청하는 경우
  if request.method == 'GET':
    books = Book.objects.all()
    # 출력하기 위해서 브라우저의 형식으로 데이터를 변환
    serializer = BookSerializer(books,many=True)
    return Response(serializer.data)
  # POST 방식의 처리 - 삽입하는 경우
  elif request.method == 'POST':
    # 클라이언트에서 전송된 데이터를 가지고 Model 인스턴스를 생성
    serializer =BookSerializer(data=request.data)
    # 유효성 검사를 수행해서 통과하면 삽입하고 아니면 에러를 출력함
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors)
  
@api_view(['GET'])
def oneBookAPI(request,bid):
  # Book 테이블에서 bid 컬럼값이 bid인 값을 찾아옵니다.
  book = get_object_or_404(Book,bid=bid)
  serializer = BookSerializer(book)
  return Response(serializer.data)