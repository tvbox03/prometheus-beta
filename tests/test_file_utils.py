import os
import pytest
from src.file_utils import file_exists

def test_file_exists_with_existing_files():
    # Test existing files in the repository
    assert file_exists('.gitignore') is True
    assert file_exists('README.md') is True
    assert file_exists('requirements.txt') is True

def test_file_exists_with_non_existing_file():
    # Test non-existing file
    assert file_exists('non_existent_file.txt') is False

def test_file_exists_with_directory():
    # Test that directories return False
    assert file_exists('src') is False
    assert file_exists('tests') is False

def test_file_exists_with_none_input():
    # Test None input raises TypeError
    with pytest.raises(TypeError):
        file_exists(None)

def test_file_exists_with_empty_path():
    # Test empty path returns False
    assert file_exists('') is False