from app.internal.config import settings
from app.utils.constants.settings import App
from logyca_azure_storage_blob import AzureStorageAccountBlobManagement, SetCredentialsConnectionString

asabm=AzureStorageAccountBlobManagement(SetCredentialsConnectionString(connection_string=settings.connection_string))
status=asabm.container_create(App.AzureStorageAccount.Containers.NAME_TO_CREATE_DELETE)
if status is True:
    print("Contenedor {} creado...".format(App.AzureStorageAccount.Containers.NAME_TO_CREATE_DELETE))
else:
    print(status)
