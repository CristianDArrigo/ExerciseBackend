import json

class API:
    def __init__(self, db):
        """
        Initialize the API with a database instance.

        Args:
            db: An instance of the database to retrieve prize data.
        """
        self.db = db

    def list_prizes(self, catalog_id: int, filter: dict[str, str] | None = None, pagination: dict[str, int] | None = None):
        """
        List prizes by catalog.

        Args:
            catalog_id (int): The identifier of the catalog.
            filter (Optional[dict[str, str]]): A dictionary with filtering criteria.
            pagination (Optional[dict[str, int]]): A dictionary with pagination parameters.

        Returns:
            str: A JSON string containing the list of prizes.
        """
        try:
            prizes = self.db.get_prizes(catalog_id, filter, pagination)
            # return a JSON string containing the total number of prizes and then the list of prizes
            return json.dumps({"total": len(prizes), "prizes": prizes}) if prizes else None
        except Exception as e:
            # Log the error or handle it appropriately
            return json.dumps({"error": str(e)})
    
