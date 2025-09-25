import json
import unittest
from pathlib import Path

from aixtools.compliance.private_data import PrivateData, PRIVATE_DATA_FILE
from aixtools.server.path import get_workspace_path


class TestPrivateData(unittest.TestCase):
    """Test cases for PrivateData class without mocking or patching."""

    def setUp(self):
        """Set up test environment with temporary directory."""        
        # Create a test user and session context
        self.workspace_path = Path(get_workspace_path())
        self.workspace_path.mkdir(parents=True, exist_ok=True)
        self.private_data_file = self.workspace_path / PRIVATE_DATA_FILE

    def tearDown(self):
        """Clean up test environment."""
        self.private_data_file.unlink(missing_ok=True)

    def test_init_no_existing_file(self):
        """Test initialization when no private data file exists."""
        private_data = PrivateData()
        self.assertFalse(private_data.has_private_data)
        self.assertEqual(private_data.get_private_datasets(), [])
        self.assertEqual(private_data.get_idap_datasets(), [])

    def test_init_with_existing_file(self):
        """Test initialization when private data file exists."""
        # Create a test file
        private_data_path = self.workspace_path / PRIVATE_DATA_FILE
        test_data = {
            "_has_private_data": True,
            "_private_datasets": ["dataset1", "dataset2"],
            "_idap_datasets": ["dataset1"],
            "ctx": None
        }
        with open(private_data_path, "w") as f:
            json.dump(test_data, f)
        
        private_data = PrivateData()
        
        self.assertTrue(private_data.has_private_data)
        self.assertEqual(set(private_data.get_private_datasets()), {"dataset1", "dataset2"})
        self.assertEqual(private_data.get_idap_datasets(), ["dataset1"])

    def test_add_private_dataset_new(self):
        """Test adding a new private dataset."""
        private_data = PrivateData()
        
        private_data.add_private_dataset("test_dataset")
        
        self.assertTrue(private_data.has_private_data)
        self.assertIn("test_dataset", private_data.get_private_datasets())
        
        # Verify data is saved to file
        private_data_path = self.workspace_path / PRIVATE_DATA_FILE
        self.assertTrue(private_data_path.exists())
        
        with open(private_data_path, "r") as f:
            saved_data = json.load(f)
        
        self.assertTrue(saved_data["_has_private_data"])
        self.assertIn("test_dataset", saved_data["_private_datasets"])

    def test_add_private_dataset_duplicate(self):
        """Test adding a duplicate private dataset."""
        private_data = PrivateData()
        
        private_data.add_private_dataset("test_dataset")
        initial_count = len(private_data.get_private_datasets())
        
        private_data.add_private_dataset("test_dataset")
        final_count = len(private_data.get_private_datasets())
        
        self.assertEqual(initial_count, final_count)
        self.assertEqual(private_data.get_private_datasets().count("test_dataset"), 1)

    def test_add_idap_dataset_new(self):
        """Test adding a new IDAP dataset."""
        private_data = PrivateData()
        
        private_data.add_idap_dataset("idap_dataset")
        
        self.assertTrue(private_data.has_private_data)
        self.assertIn("idap_dataset", private_data.get_idap_datasets())
        self.assertIn("idap_dataset", private_data.get_private_datasets())
        
        # Verify data is saved to file
        private_data_path = self.workspace_path / PRIVATE_DATA_FILE
        self.assertTrue(private_data_path.exists())
        
        with open(private_data_path, "r") as f:
            saved_data = json.load(f)
        
        self.assertTrue(saved_data["_has_private_data"])
        self.assertIn("idap_dataset", saved_data["_idap_datasets"])
        self.assertIn("idap_dataset", saved_data["_private_datasets"])

    def test_add_idap_dataset_existing_private(self):
        """Test adding IDAP dataset when it already exists as private dataset."""
        private_data = PrivateData()
        
        private_data.add_private_dataset("existing_dataset")
        private_data.add_idap_dataset("existing_dataset")
        
        self.assertTrue(private_data.has_private_data)
        self.assertIn("existing_dataset", private_data.get_idap_datasets())
        self.assertIn("existing_dataset", private_data.get_private_datasets())
        self.assertEqual(private_data.get_private_datasets().count("existing_dataset"), 1)

    def test_add_idap_dataset_duplicate(self):
        """Test adding a duplicate IDAP dataset."""
        private_data = PrivateData()
        
        private_data.add_idap_dataset("idap_dataset")
        initial_idap_count = len(private_data.get_idap_datasets())
        initial_private_count = len(private_data.get_private_datasets())
        
        private_data.add_idap_dataset("idap_dataset")
        final_idap_count = len(private_data.get_idap_datasets())
        final_private_count = len(private_data.get_private_datasets())
        
        self.assertEqual(initial_idap_count, final_idap_count)
        self.assertEqual(initial_private_count, final_private_count)

    def test_has_private_dataset(self):
        """Test checking if a private dataset exists."""
        private_data = PrivateData()
        
        self.assertFalse(private_data.has_private_dataset("nonexistent"))
        
        private_data.add_private_dataset("test_dataset")
        
        self.assertTrue(private_data.has_private_dataset("test_dataset"))
        self.assertFalse(private_data.has_private_dataset("nonexistent"))

    def test_has_idap_dataset(self):
        """Test checking if an IDAP dataset exists."""
        private_data = PrivateData()
        
        self.assertFalse(private_data.has_idap_dataset("nonexistent"))
        
        private_data.add_idap_dataset("idap_dataset")
        
        self.assertTrue(private_data.has_idap_dataset("idap_dataset"))
        self.assertFalse(private_data.has_idap_dataset("nonexistent"))

    def test_get_datasets_returns_copies(self):
        """Test that get methods return copies to prevent external modification."""
        private_data = PrivateData()
        private_data.add_private_dataset("private_dataset")
        private_data.add_idap_dataset("idap_dataset")
        
        private_datasets = private_data.get_private_datasets()
        idap_datasets = private_data.get_idap_datasets()
        
        # Modify the returned lists
        private_datasets.append("external_modification")
        idap_datasets.append("external_modification")
        
        # Verify original data is unchanged
        self.assertNotIn("external_modification", private_data.get_private_datasets())
        self.assertNotIn("external_modification", private_data.get_idap_datasets())

    def test_has_private_data_setter_true(self):
        """Test setting has_private_data to True."""
        private_data = PrivateData()
        
        private_data.has_private_data = True
        
        self.assertTrue(private_data.has_private_data)
        
        # Verify data is saved to file
        private_data_path = self.workspace_path / PRIVATE_DATA_FILE
        self.assertTrue(private_data_path.exists())

    def test_has_private_data_setter_false(self):
        """Test setting has_private_data to False clears all data."""
        private_data = PrivateData()
        private_data.add_private_dataset("dataset1")
        private_data.add_idap_dataset("dataset2")
        
        private_data.has_private_data = False
        
        self.assertFalse(private_data.has_private_data)
        self.assertEqual(private_data.get_private_datasets(), [])
        self.assertEqual(private_data.get_idap_datasets(), [])
        
        # Verify file is deleted
        private_data_path = self.workspace_path / PRIVATE_DATA_FILE
        self.assertFalse(private_data_path.exists())

    def test_save_with_no_private_data(self):
        """Test saving when has_private_data is False deletes the file."""
        private_data = PrivateData()
        private_data.add_private_dataset("test_dataset")
        
        # Verify file exists
        private_data_path = self.workspace_path / PRIVATE_DATA_FILE
        self.assertTrue(private_data_path.exists())
        
        private_data.has_private_data = False
        
        # Verify file is deleted
        self.assertFalse(private_data_path.exists())

    def test_save_with_private_data(self):
        """Test saving when has_private_data is True creates/updates the file."""
        private_data = PrivateData()
        private_data.add_private_dataset("dataset1")
        private_data.add_idap_dataset("dataset2")
        
        private_data_path = self.workspace_path / PRIVATE_DATA_FILE
        self.assertTrue(private_data_path.exists())
        
        with open(private_data_path, "r") as f:
            saved_data = json.load(f)
        
        self.assertTrue(saved_data["_has_private_data"])
        self.assertIn("dataset1", saved_data["_private_datasets"])
        self.assertIn("dataset2", saved_data["_private_datasets"])
        self.assertIn("dataset2", saved_data["_idap_datasets"])
        self.assertIsNone(saved_data["ctx"])

    def test_load_from_corrupted_file(self):
        """Test loading from a corrupted JSON file."""
        private_data_path = self.workspace_path / PRIVATE_DATA_FILE
        with open(private_data_path, "w") as f:
            f.write("invalid json content")
        
        with self.assertRaises(json.JSONDecodeError):
            PrivateData()

    def test_load_from_file_with_missing_fields(self):
        """Test loading from a file with missing fields uses defaults."""
        private_data_path = self.workspace_path / PRIVATE_DATA_FILE
        test_data = {"_has_private_data": True}  # Missing other fields
        with open(private_data_path, "w") as f:
            json.dump(test_data, f)
        
        private_data = PrivateData()
        
        self.assertTrue(private_data.has_private_data)
        self.assertEqual(private_data.get_private_datasets(), [])
        self.assertEqual(private_data.get_idap_datasets(), [])

    def test_multiple_operations_persistence(self):
        """Test that multiple operations are properly persisted."""
        # Create first instance and add data
        private_data1 = PrivateData()
        private_data1.add_private_dataset("dataset1")
        private_data1.add_idap_dataset("dataset2")
        
        # Create second instance and verify data is loaded
        private_data2 = PrivateData()
        self.assertTrue(private_data2.has_private_data)
        self.assertIn("dataset1", private_data2.get_private_datasets())
        self.assertIn("dataset2", private_data2.get_private_datasets())
        self.assertIn("dataset2", private_data2.get_idap_datasets())
        
        # Add more data with second instance
        private_data2.add_private_dataset("dataset3")
        
        # Create third instance and verify all data is present
        private_data3 = PrivateData()
        expected_private = {"dataset1", "dataset2", "dataset3"}
        expected_idap = {"dataset2"}
        
        self.assertEqual(set(private_data3.get_private_datasets()), expected_private)
        self.assertEqual(set(private_data3.get_idap_datasets()), expected_idap)

    def test_str_and_repr(self):
        """Test string representation methods."""
        private_data = PrivateData()
        private_data.add_private_dataset("dataset1")
        private_data.add_idap_dataset("dataset2")
        
        str_repr = str(private_data)
        repr_repr = repr(private_data)
        
        self.assertEqual(str_repr, repr_repr)
        self.assertIn("has_private_data=True", str_repr)
        self.assertIn("dataset1", str_repr)
        self.assertIn("dataset2", str_repr)
        self.assertIn(str(self.workspace_path / PRIVATE_DATA_FILE), str_repr)

    def test_file_operations_create_directories(self):
        """Test that file operations create necessary directories."""
        # Remove the workspace directory
        import shutil
        shutil.rmtree(self.workspace_path)
        self.assertFalse(self.workspace_path.exists())
        
        # Create PrivateData instance and add data
        private_data = PrivateData()
        private_data.add_private_dataset("test_dataset")
        
        # Verify directory and file were created
        self.assertTrue(self.workspace_path.exists())
        private_data_path = self.workspace_path / PRIVATE_DATA_FILE
        self.assertTrue(private_data_path.exists())

    def test_concurrent_modifications_simulation(self):
        """Test simulation of concurrent modifications (without actual threading)."""
        # Create two instances with same context
        private_data1 = PrivateData()
        private_data2 = PrivateData()
        
        # Add data with first instance
        private_data1.add_private_dataset("dataset1")
        
        # Second instance should see the changes when reloaded
        private_data2.load()
        self.assertIn("dataset1", private_data2.get_private_datasets())
        
        # Add data with second instance
        private_data2.add_idap_dataset("dataset2")
        
        # First instance should see the changes when reloaded
        private_data1.load()
        self.assertIn("dataset2", private_data1.get_idap_datasets())
        self.assertIn("dataset2", private_data1.get_private_datasets())


if __name__ == "__main__":
    unittest.main()