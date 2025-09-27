import grpc
from Osdental.Models.Response import Response
from Osdental.Decorators.Retry import grpc_retry
from Osdental.Grpc.Generated import Common_pb2
from Osdental.Grpc.Generated import Portal_pb2_grpc
from Osdental.Shared.Config import Config
from Osdental.Exception.ControlledException import OSDException

class PortalClient:

    def __init__(self, host=Config.SECURITY_GRPC_HOST, port=Config.SECURITY_GRPC_PORT):
        if not host:
            raise OSDException('SECURITY_GRPC_HOST is not set')

        if port:
            url = f'{host}:{port}'
        else:
            url = host

        self.channel = grpc.aio.insecure_channel(url)
        self.stub = Portal_pb2_grpc.PortalStub(self.channel)

    @grpc_retry
    async def get_legacy(self) -> Response:
        request = Common_pb2.Empty()
        return await self.stub.GetLegacy(request)
    

    @grpc_retry
    async def validate_auth_token(self, request) -> Response:
        request = Common_pb2.Request(data=request)
        return await self.stub.ValidateAuthToken(request)
