import pandas as pd
import psycopg2
import json
from typing import List, Dict


class DatapointDB:
    """
    Class for accessing datapoints via a database.
    """

    def __init__(self, device_names: List[str], db_user: str, db_pass: str, db_host: str, output_path: str = "data", required_uuid_list: List[str] = None, filter_enabled: bool = True):
        """
        Initialize the DatapointDB class.

        :param device_names: List of device names to retrieve metadata for.
        :param db_user: Database user.
        :param db_pass: Database password.
        :param db_host: Database host.
        :param output_path: Directory to save JSON files.
        :param required_uuid_list: List of UUIDs to filter the metadata (optional).
        :param filter_enabled: Whether to filter metadata by "enabled == True" and "archived == False" (default is True).
        """
        self.device_names = device_names
        self.db_user = db_user
        self.db_pass = db_pass
        self.db_host = db_host
        self.output_path = output_path
        self.required_uuid_list = required_uuid_list or []
        self.filter_enabled = filter_enabled
        self.device_metadata: Dict[str, pd.DataFrame] = {}  # Store metadata for each device
        self.device_uuids: Dict[str, List[str]] = {}  # Store UUIDs for each device
        self._db_access()

    def _db_access(self) -> None:
        """Connect to the database and retrieve metadata for each device."""
        conn = psycopg2.connect(
            dbname="config_repository",
            user=self.db_user,
            password=self.db_pass,
            host=self.db_host,
            port=5432
        )
        cursor = conn.cursor()

        for device_name in self.device_names:
            query = """
                SELECT dp.uuid, dp.label, dp.config
                FROM data_points dp
                INNER JOIN devices dev ON dev.id = dp.device_id
                WHERE dev.name = %s
            """
            if self.filter_enabled:
                query += " AND dp.enabled = true AND dp.archived = false"

            cursor.execute(query, (device_name,))
            data_points = [{"uuid": r[0], "label": r[1], "config": r[2]} for r in cursor.fetchall()]

            # Convert to DataFrame and filter by required UUIDs if necessary
            metadata_df = pd.DataFrame(data_points)
            if not metadata_df.empty and self.required_uuid_list:
                metadata_df = metadata_df[metadata_df["uuid"].isin(self.required_uuid_list)]

            # Store metadata and UUIDs for the device
            self.device_metadata[device_name] = metadata_df
            self.device_uuids[device_name] = metadata_df["uuid"].tolist()

            # Export to JSON file
            self._export_json(metadata_df.to_dict(orient="records"), device_name)

        conn.close()

    def _export_json(self, data_points: List[Dict[str, str]], device_name: str) -> None:
        """Export data points to a JSON file for the specified device."""
        file_name = f"{self.output_path}/{device_name.replace(' ', '_')}_data_points.json"
        with open(file_name, 'w') as f:
            json.dump(data_points, f, indent=2)

    def get_all_uuids(self) -> Dict[str, List[str]]:
        """Return a dictionary of UUIDs for each device."""
        return self.device_uuids

    def get_all_metadata(self) -> Dict[str, List[Dict[str, str]]]:
        """Return a dictionary of metadata for each device."""
        return {device: metadata.to_dict(orient="records") for device, metadata in self.device_metadata.items()}

    def display_dataframe(self, device_name: str = None, aggregate: bool = False) -> None:
        """
        Display metadata as a DataFrame for a specific device or all devices.

        :param device_name: Name of the device to display metadata for (optional).
        :param aggregate: If True, combine metadata from all devices into a single DataFrame.
        """
        if aggregate:
            combined_df = pd.concat(self.device_metadata.values(), keys=self.device_metadata.keys())
            print("Aggregated metadata for all devices:")
            print(combined_df)
        elif device_name:
            if device_name in self.device_metadata:
                print(f"Metadata for device: {device_name}")
                print(self.device_metadata[device_name])
            else:
                print(f"No metadata found for device: {device_name}")
        else:
            for device, metadata in self.device_metadata.items():
                print(f"\nMetadata for device: {device}")
                print(metadata)