from django.urls import path

from quizapp.views import instructions, showQuiz, showResult, signup, userLogin, userLogout
urlpatterns = [
    path('login-page/',userLogin,name="login"),
    path('logout/',userLogout,name="logout"),
    path('Instructions/',instructions,name="startquiz"),
    path('quiz-page/',showQuiz,name="quiz"),
    path('result/',showResult,name="result"),
    path('signup/',signup,name="signup"),
]