from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from devices.models import Device

class DeviceSyncView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        devices = Device.objects.all().values(
            'serial', 'name', 'status', 'model', 'android_version'
        )
        return Response(list(devices))

    def post(self, request):
        # Desktop app registers a device
        data = request.data
        device, created = Device.objects.update_or_create(
            serial=data['serial'],
            defaults={
                'name': data.get('name', f"Device {data['serial'][:8]}"),
                'status': data.get('status', 'Unknown'),
                'model': data.get('model', ''),
                'android_version': data.get('android_version', ''),
            }
        )
        return Response({"id": device.id, "created": created})