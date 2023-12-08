from django.urls import path,include
# from profiles.api.views import ProfileList
from rest_framework.routers import DefaultRouter
from profiles.api.views import ProfileViewList,ProfileStatusViewList,AvatarUpdateView

# profile_list=ProfileViewList.as_view({'get':"list"})
# profile_detail=ProfileViewList.as_view({'get':"retrieve"})

router=DefaultRouter()
router.register('profiles',ProfileViewList)
router.register('status',ProfileStatusViewList,basename='status')

urlpatterns=[
    # path('profiles/',profile_list,
    #      name='profile-list'),
    # path('profiles/<int:pk>',profile_detail,
    #      name='profile-list'),
    path('',include(router.urls)),
    path('avatar/',AvatarUpdateView.as_view(),
         name='avatar-update'),
    
]