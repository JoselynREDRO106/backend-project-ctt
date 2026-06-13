from app.models.cliente_models import ClientCreate, ClientResponse, ClientUpdate


class ClientServices():

    def __init__(self):
        self.clients: list[ClientResponse] = []
        self.next_id: int = 1

    def get_all_clients(self) -> list[ClientResponse]:
        return self.clients

    def get_client(self, client_id: int) -> ClientResponse | None:
        for client in self.clients:
            if client.id == client_id:
                return client

        return None

    def create_client(self, client_data: ClientCreate) -> ClientResponse:
        new_client = ClientResponse(
            id=self.next_id,
            name=client_data.name,
            lastname=client_data.lastname
        )

        self.clients.append(new_client)
        self.next_id += 1

        return new_client

    def update_client(self, client_id: int, client_data: ClientUpdate) -> ClientResponse | None:
        for index, client in enumerate(self.clients):
            if client.id == client_id:
                updated_client = ClientResponse(
                    id=client_id,
                    name=client_data.name,
                    lastname=client_data.lastname
                )
                self.clients[index] = updated_client
                return updated_client

        return None

    def delete_client(self, client_id: int) -> bool:
        for index, client in enumerate(self.clients):
            if client.id == client_id:
                self.clients.pop(index)
                return True

        return False