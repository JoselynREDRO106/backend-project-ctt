from fastapi import APIRouter

from app.schemas.cliente_models import ClientCreate, ClientResponse, ClientUpdate
from app.services.cliente_services import ClientServices

client_router = APIRouter(prefix="/clients", tags=["Clients"])
client_service = ClientServices()


@client_router.get("/")
def get_all_clients_api() -> list[ClientResponse]:
    return client_service.get_all_clients()


@client_router.get("/{client_id}")
def get_client_api(client_id: int) -> ClientResponse | None:
    return client_service.get_client(client_id=client_id)


@client_router.post("/")
def create_client_api(client_data: ClientCreate) -> ClientResponse:
    return client_service.create_client(client_data=client_data)


@client_router.put("/{client_id}")
def update_client_api(client_id: int, client_data: ClientUpdate) -> ClientResponse | None:
    return client_service.update_client(client_id=client_id, client_data=client_data)


@client_router.delete("/{client_id}")
def delete_client_api(client_id: int) -> bool:
    return client_service.delete_client(client_id=client_id)