import json

class MockDB:
    """
    A mock database that stores prize data, retrieved from a JSON file (mock_prizes.json).
    """
    def __init__(self, prizes_path: str = 'mock_prizes.json'):
        """
        Initialize the mock database with prize data from the specified JSON file.

        Args:
            prizes_path (str): The path to the JSON file containing prize data.
        """
        with open(prizes_path, 'r') as f:
            self.prizes = json.load(f)

    def get_prizes(self, 
                   catalog_id: int, 
                   filter: dict[str, str] | None = None, 
                   pagination: dict[str, int] | None = None):
        """
        Retrieve prizes by catalog, optionally filtering and paginating the results.

        Args:
            catalog_id (int): The identifier of the catalog.
            filter (Optional[dict[str, str]]): A dictionary with filtering criteria.
            pagination (Optional[dict[str, int]]): A dictionary with pagination parameters.

        Returns:
            list: A list of prizes matching the provided criteria.
        """
        # Filter prizes based on catalog_id
        catalog_prizes = [prize for prize in self.prizes if prize['catalog_id'] == catalog_id]

        # Apply filtering criteria
        if filter:
            catalog_prizes = self._apply_filter(catalog_prizes, filter)

        # Apply pagination
        if pagination:
            catalog_prizes = self._apply_pagination(catalog_prizes, pagination)

        return catalog_prizes

    def _apply_filter(self, prizes: list, filter: dict[str, str]) -> list:
        """
        Apply filtering criteria to a list of prizes.

        Args:
            prizes (list): The list of prizes to filter.
            filter (dict[str, str]): A dictionary with filtering criteria.

        Returns:
            list: The filtered list of prizes.
        """
        return [prize for prize in prizes if all(prize.get(key) == value for key, value in filter.items())]

    def _apply_pagination(self, prizes: list, pagination: dict[str, int]) -> list:
        """
        Apply pagination to a list of prizes.

        Args:
            prizes (list): The list of prizes to paginate.
            pagination (dict[str, int]): A dictionary with pagination parameters.

        Returns:
            list: The paginated list of prizes.
        """
        page = pagination.get('page', 1)
        per_page = pagination.get('per_page', 10)
        start_index = (page - 1) * per_page
        end_index = start_index + per_page
        return prizes[start_index:end_index]
