# from rest_framework.response import HttpResponseForbidden
# class BlockIPMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request):
#         # IP address to block
#         blocked_ip = '127.0.0.1'  # Replace with the IP address you want to block
        
#         # Get the client IP address
#         client_ip = request.META.get('REMOTE_ADDR')

#         # Check if the client IP matches the blocked IP
#         if client_ip == blocked_ip:
#             return HttpResponseForbidden("Access forbidden")

#         # Process the request
#         response = self.get_response(request)

#         return response
