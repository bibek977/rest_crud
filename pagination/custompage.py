from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination

# class MyPagePagination(PageNumberPagination):
#     page_size = 5
#     page_query_param = 'p'
#     page_size_query_param = 'records'
#     max_page_size = 7
#     # last_page_strings ="end"
#     last_page_strings =["end",'ends']


class MyLimitOffset(LimitOffsetPagination):
    default_limit = 5
    # limit_query_param = 'mylimit'
    # offset_query_param = "myoffset"
    max_limit = 10