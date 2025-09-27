from enum import StrEnum

class App:
    class AzureStorageAccount:
        class Containers(StrEnum):
            NAME_TO_CREATE_DELETE="testlib"
            NAME_WITH_DATA="tmp"