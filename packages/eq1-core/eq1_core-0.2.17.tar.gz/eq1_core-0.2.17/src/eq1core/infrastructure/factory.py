from .db.services.core_data_service_impl import CoreDBService
from .api.services.core_data_service_impl import CoreAPIService


class DataServiceFactory:
    @staticmethod
    def get_service(service_type: str):
        if service_type.lower() == "db":
            return CoreDBService()
        elif service_type.lower() == "api":
            return CoreAPIService()
        else:
            raise ValueError(f"Unknown service type: {service_type}")
