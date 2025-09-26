"""
Test Data for Assistant UI Tests

This module provides test data generation and management for assistant-related UI tests.
Following best practices by separating test data from test logic and providing
reusable data factories for consistent testing.
"""

from dataclasses import dataclass
from typing import Optional, List
import pytest

from codemie_test_harness.tests.utils.base_utils import get_random_name


@dataclass
class AssistantTestData:
    """
    Data class for assistant test data.

    This class encapsulates all the data needed for assistant creation tests,
    providing a clean and type-safe way to manage test data.
    """

    name: str
    description: str
    system_prompt: str
    icon_url: Optional[str] = None
    shared: bool = False


class AssistantTestDataFactory:
    """
    Factory class for generating assistant test data.

    This factory provides various methods to create different types of
    assistant test data for different testing scenarios.
    """

    @staticmethod
    def create_minimal_assistant_data() -> AssistantTestData:
        """
        Create minimal assistant data with only required fields.

        This represents the most basic assistant creation scenario
        with minimal required information.

        Returns:
            AssistantTestData: Minimal assistant test data
        """
        return AssistantTestData(
            name=f"QA Test Assistant {get_random_name()}",
            description="Minimal test assistant for QA automation.",
            system_prompt=(
                "You are a test assistant created for QA validation purposes. "
                "Provide helpful and accurate responses to user queries."
            ),
            shared=False,
            icon_url=ICON_URL,
        )

    @staticmethod
    def create_shared_assistant_data() -> AssistantTestData:
        """
        Create shared assistant data for public/shared testing scenarios.

        Returns:
            AssistantTestData: Shared assistant test data
        """
        return AssistantTestData(
            name=f"QA Shared Assistant {get_random_name()}",
            description="Shared QA assistant available to all team members",
            system_prompt=(
                "You are a shared QA assistant available to the entire team. "
                "Provide collaborative testing support, knowledge sharing, and "
                "help maintain consistent quality standards across projects."
            ),
            icon_url=ICON_URL,
            shared=True,
        )

    @staticmethod
    def create_validation_test_data() -> List[AssistantTestData]:
        """
        Create a list of assistant data for validation testing scenarios.

        This includes data for testing various validation scenarios,
        edge cases in form validation, and error handling.

        Returns:
            List[AssistantTestData]: List of validation test data
        """
        return [
            # Empty name scenario
            AssistantTestData(
                name="",
                description="Test description",
                system_prompt="Test prompt",
            ),
            # Long name scenario
            AssistantTestData(
                name="A" * 100,  # Very long name
                description="Test description for long name validation",
                system_prompt="Test prompt for long name scenario",
            ),
            # Empty description scenario
            AssistantTestData(
                name="Test Assistant",
                description="",
                system_prompt="Test prompt",
            ),
            # Empty system prompt scenario
            AssistantTestData(
                name="Test Assistant",
                description="Test description",
                system_prompt="",
            ),
        ]


class AssistantValidationRules:
    """
    Validation rules and constraints for assistant data.

    This class defines the validation rules that should be applied
    to assistant data during testing.
    """

    # Field length constraints
    MAX_NAME_LENGTH = 100
    MAX_DESCRIPTION_LENGTH = 1000
    MAX_ICON_URL_LENGTH = 500

    # Required fields
    REQUIRED_FIELDS = ["name", "description", "system_prompt"]

    # Validation error messages (expected messages for testing)
    ERROR_MESSAGES = {
        "name_required": "Name is required",
        "name_too_long": f"Name must be less than {MAX_NAME_LENGTH} characters",
        "description_required": "Description is required",
        "description_too_long": f"Description must be less than {MAX_DESCRIPTION_LENGTH} characters",
        "system_prompt_required": "System prompt is required",
        "invalid_url": "Please enter a valid URL",
        "invalid_type": "Please select a valid assistant type",
    }


# ==================== CONVENIENCE FUNCTIONS ====================


def get_minimal_assistant_data() -> AssistantTestData:
    """Convenience function to get minimal assistant data."""
    return AssistantTestDataFactory.create_minimal_assistant_data()


def get_shared_assistant_data() -> AssistantTestData:
    """Convenience function to get shared assistant data."""
    return AssistantTestDataFactory.create_shared_assistant_data()


def get_validation_test_data() -> List[AssistantTestData]:
    """Convenience function to get validation test data."""
    return AssistantTestDataFactory.create_validation_test_data()


# ==================== TEST DATA CONSTANTS ====================

# Common test values for reuse
COMMON_TEST_PROMPTS = {
    "qa_assistant": (
        "You are a QA testing assistant. Your primary role is to help with "
        "quality assurance tasks, test automation, and ensuring software quality. "
        "Provide detailed and actionable guidance."
    ),
    "general_assistant": (
        "You are a helpful assistant. Provide clear, accurate, and helpful "
        "responses to user queries. Always be polite and professional."
    ),
    "specialist_assistant": (
        "You are a specialist assistant with deep expertise in your domain. "
        "Provide expert-level guidance and detailed technical solutions."
    ),
}

COMMON_TEST_DESCRIPTIONS = {
    "qa_assistant": "QA testing assistant for automation and quality assurance tasks",
    "general_assistant": "General purpose assistant for various tasks and queries",
    "specialist_assistant": "Specialist assistant with domain-specific expertise",
}

COMMON_ICON_URLS = {
    "qa_icon": "https://example.com/qa-assistant-icon.png",
    "general_icon": "https://example.com/general-assistant-icon.png",
    "specialist_icon": "https://example.com/specialist-assistant-icon.png",
}

ICON_URL = "https://raw.githubusercontent.com/epam-gen-ai-run/ai-run-install/main/docs/assets/ai/AQAUiTestGenerator.png"

# ==================== EXCEL TOOL EXTENDED FUNCTIONALITY TEST DATA ====================

# Test data for Excel tool extended functionality covering EPMCDME-7877 requirements
EXCEL_TOOL_TEST_DATA = [
    pytest.param(
        "Analyze the data in test_extended.xlsx and extract information from visible sheets only",
        """
            The analysis of the visible sheets in the file **test_extended.xlsx** yields the following data:
            
            ### First Sheet
            | Column 1 | Column 2 | Column 3 |
            | --- | --- | --- |
            | Cars | Test | 222 |
            | Data | Cats | 111 |
            |  |  | Travellers |
            | Tree | Forest |  |
            | Tree | Forest |  |
            | Tree | Forest |  |
            | Tree | Forest |  |
            | Bykes | Red | 877 |
            
            ### Second Sheet
            | Column 1 | Column 2 | Column 3 | Column 4 |
            | --- | --- | --- | --- |
            | Cars | Test | 222 | Second |
            | Data | Cats | 111 | Second |
            |  |  | Travellers | Second |
            | Tree | Forest |  | Second |
            | Tree | Forest |  | Second |
            | Tree | Forest |  | Second |
            | Tree | Forest |  | Second |
            | Bykes | Red | 877 | Second |
            
            The hidden sheet data has been excluded based on the request for visible sheets only. If you need further analysis on specific data or another request, feel free to ask!
        """,
        id="visible_sheets_only",
    ),
    pytest.param(
        "Extract all data from test_extended.xlsx including hidden sheets",
        """
            Here is the extracted data from the `test_extended.xlsx` file, including data from hidden sheets:
            
            ### First Sheet
            | Column 1 | Column 2 | Column 3 |
            | --- | --- | --- |
            | Cars | Test | 222 |
            | Data | Cats | 111 |
            |  |  | Travellers |
            |  |  |  |
            | Tree | Forest |  |
            | Tree | Forest |  |
            | Tree | Forest |  |
            | Tree | Forest |  |
            |  |  |  |
            | Bykes | Red | 877 |
            
            ### Second Sheet
            | Column 1 | Column 2 | Column 3 | Column 4 |
            | --- | --- | --- | --- |
            | Cars | Test | 222 | Second |
            | Data | Cats | 111 | Second |
            |  |  | Travellers | Second |
            |  |  |  |  |
            | Tree | Forest |  | Second |
            | Tree | Forest |  | Second |
            | Tree | Forest |  | Second |
            | Tree | Forest |  | Second |
            |  |  |  |  |
            | Bykes | Red | 877 | Second |
            
            ### Hidden Sheet
            | Column 1 | Column 2 | Column 3 | Column 4 |
            | --- | --- | --- | --- |
            | Cars | Test | 222 | Hidden |
            | Data | Cats | 111 | Hidden |
            |  |  | Travellers | Hidden |
            |  |  |  |  |
            | Tree | Forest |  | Hidden |
            | Tree | Forest |  | Hidden |
            | Tree | Forest |  | Hidden |
            | Tree | Forest |  | Hidden |
            |  |  |  |  |
            | Bykes | Red | 877 | Hidden |
        """,
        id="all_sheets_including_hidden",
    ),
    pytest.param(
        "List all sheet names in test_extended.xlsx",
        """
            The Excel file `test_extended.xlsx` contains the following sheets:

            - First sheet
            - Second sheet
            - Hidden sheet
        """,
        id="all_sheet_names",
    ),
    pytest.param(
        "Get only visible sheet names from test_extended.xlsx",
        """
            The visible sheets in the `test_extended.xlsx` file are:
            
            - First sheet
            - Second sheet
        """,
        id="visible_sheet_names_only",
    ),
    pytest.param(
        "Get comprehensive statistics about test_extended.xlsx file structure",
        """
            The Excel file `test_extended.xlsx` contains the following structure:
            
            - **Total Sheets:** 3
            
            ### Sheet: First sheet
            - **Columns:**
              - Column 1: string, Sample Values: `Cars`, `Data`, ``, ...
              - Column 2: string, Sample Values: `Test`, `Cats`, ``, ...
              - Column 3: string, Sample Values: `222`, `111`, `Travellers`, ...
            
            ### Sheet: Second sheet
            - **Columns:**
              - Column 1: string, Sample Values: `Cars`, `Data`, ``, ...
              - Column 2: string, Sample Values: `Test`, `Cats`, ``, ...
              - Column 3: string, Sample Values: `222`, `111`, `Travellers`, ...
              - Column 4: string, Sample Values: `Second`
            
            ### Sheet: Hidden sheet
            - **Columns:**
              - Column 1: string, Sample Values: `Cars`, `Data`, ``, ...
              - Column 2: string, Sample Values: `Test`, `Cats`, ``, ...
              - Column 3: string, Sample Values: `222`, `111`, `Travellers`, ...
              - Column 4: string, Sample Values: `Hidden`
            
            This summary provides an overview of the column names, data types, and sample values for each sheet within the Excel file.
        """,
        id="file_statistics",
    ),
    pytest.param(
        "Extract data from the first sheet only using sheet index from test_extended.xlsx",
        """
            Here is the extracted data from the first sheet of the file `test_extended.xlsx`:
            
            | Column 1 | Column 2 | Column 3   |
            |:---------|:---------|:-----------|
            | Cars     | Test     | 222        |
            | Data     | Cats     | 111        |
            |          |          | Travellers |
            | Tree     | Forest   |            |
            | Tree     | Forest   |            |
            | Tree     | Forest   |            |
            | Tree     | Forest   |            |
            | Bykes    | Red      | 877        |        
        """,
        id="single_sheet_by_index",
    ),
    pytest.param(
        "Extract data only from 'Second sheet' in test_extended.xlsx",
        """
            The data extracted from the "Second sheet" in `test_extended.xlsx` is as follows:
            
            | Column 1 | Column 2 | Column 3   | Column 4 |
            |----------|----------|------------|----------|
            | Cars     | Test     | 222        | Second   |
            | Data     | Cats     | 111        | Second   |
            |          |          | Travellers | Second   |
            | Tree     | Forest   |            | Second   |
            | Tree     | Forest   |            | Second   |
            | Tree     | Forest   |            | Second   |
            | Tree     | Forest   |            | Second   |
            | Bykes    | Red      | 877        | Second   |        
        """,
        id="single_sheet_by_name",
    ),
    pytest.param(
        "Process test_extended.xlsx with data cleaning to remove empty rows and columns",
        """
            The file `test_extended.xlsx` was processed with data cleaning to remove empty rows and columns. Here is a representation of the cleaned Excel sheets:
            
            ### First Sheet
            | Column 1 | Column 2 | Column 3 |
            |----------|----------|----------|
            | Cars     | Test     | 222      |
            | Data     | Cats     | 111      |
            |          |          | Travellers|
            | Tree     | Forest   |          |
            | Tree     | Forest   |          |
            | Tree     | Forest   |          |
            | Tree     | Forest   |          |
            | Bykes    | Red      | 877      |
            
            ### Second Sheet
            | Column 1 | Column 2 | Column 3 | Column 4 |
            |----------|----------|----------|----------|
            | Cars     | Test     | 222      | Second   |
            | Data     | Cats     | 111      | Second   |
            |          |          | Travellers| Second   |
            | Tree     | Forest   |          | Second   |
            | Tree     | Forest   |          | Second   |
            | Tree     | Forest   |          | Second   |
            | Tree     | Forest   |          | Second   |
            | Bykes    | Red      | 877      | Second   |
            
            ### Hidden Sheet
            | Column 1 | Column 2 | Column 3 | Column 4 |
            |----------|----------|----------|----------|
            | Cars     | Test     | 222      | Hidden   |
            | Data     | Cats     | 111      | Hidden   |
            |          |          | Travellers| Hidden   |
            | Tree     | Forest   |          | Hidden   |
            | Tree     | Forest   |          | Hidden   |
            | Tree     | Forest   |          | Hidden   |
            | Tree     | Forest   |          | Hidden   |
            | Bykes    | Red      | 877      | Hidden   |
            
            The visible sheets have been cleaned, taking away rows and columns that were completely empty. Hidden sheets have been processed but are not visible by default.        
        """,
        id="data_cleaning",
    ),
    pytest.param(
        "Analyze test_extended.xlsx with visible_only=False to include hidden sheets",
        """
            The Excel file `test_extended.xlsx` contains three sheets, including a hidden one. Here's a summary of each sheet's content:
            
            ### First Sheet
            | Column 1 | Column 2 | Column 3 |
            | --- | --- | --- |
            | Cars | Test | 222 |
            | Data | Cats | 111 |
            |   |   | Travellers |
            |   |   |   |
            | Tree | Forest |   |
            | Tree | Forest |   |
            | Tree | Forest |   |
            | Tree | Forest |   |
            |   |   |   |
            | Bykes | Red | 877 |
            
            ### Second Sheet
            | Column 1 | Column 2 | Column 3 | Column 4 |
            | --- | --- | --- | --- |
            | Cars | Test | 222 | Second |
            | Data | Cats | 111 | Second |
            |   |   | Travellers | Second |
            |   |   |   |   |
            | Tree | Forest |   | Second |
            | Tree | Forest |   | Second |
            | Tree | Forest |   | Second |
            | Tree | Forest |   | Second |
            |   |   |   |   |
            | Bykes | Red | 877 | Second |
            
            ### Hidden Sheet
            | Column 1 | Column 2 | Column 3 | Column 4 |
            | --- | --- | --- | --- |
            | Cars | Test | 222 | Hidden |
            | Data | Cats | 111 | Hidden |
            |   |   | Travellers | Hidden |
            |   |   |   |   |
            | Tree | Forest |   | Hidden |
            | Tree | Forest |   | Hidden |
            | Tree | Forest |   | Hidden |
            | Tree | Forest |   | Hidden |
            |   |   |   |   |
            | Bykes | Red | 877 | Hidden |
            
            ### Observations:
            - Each sheet has a similar structure, with `Column 1` and `Column 2` containing repeated entries.
            - The hidden sheet appears to be similar to the second sheet but with the label 'Hidden' in `Column 4`.
            - The first sheet doesn't have a `Column 4` like the other two sheets.
            - There are several rows with missing values, especially in `Column 1` and `Column 2`. 
            
            Let me know if you need more in-depth analysis or specific insights from these sheets!
        """,
        id="hidden_sheet_visibility",
    ),
    pytest.param(
        "Analyze column structure and data types in test_extended.xlsx",
        """
            The Excel file `test_extended.xlsx` contains a total of 3 sheets: "First sheet", "Second sheet", and a "Hidden sheet". Here's an overview of the column structure and data types for each sheet:
            
            ### Sheet: First sheet
            - **Columns:**
              - **Column 1**: string (Sample Values: `Cars`, `Data`, ...)
              - **Column 2**: string (Sample Values: `Test`, `Cats`, ...)
              - **Column 3**: string (Sample Values: `222`, `111`, `Travellers`, ...)
            
            ### Sheet: Second sheet
            - **Columns:**
              - **Column 1**: string (Sample Values: `Cars`, `Data`, ...)
              - **Column 2**: string (Sample Values: `Test`, `Cats`, ...)
              - **Column 3**: string (Sample Values: `222`, `111`, `Travellers`, ...)
              - **Column 4**: string (Sample Value: `Second`)
            
            ### Sheet: Hidden sheet
            - **Columns:**
              - **Column 1**: string (Sample Values: `Cars`, `Data`, ...)
              - **Column 2**: string (Sample Values: `Test`, `Cats`, ...)
              - **Column 3**: string (Sample Values: `222`, `111`, `Travellers`, ...)
              - **Column 4**: string (Sample Value: `Hidden`)
            
            All columns across the sheets predominantly contain string data types. If you have any further questions or need additional analysis, feel free to ask!
        """,
        id="column_structure_analysis",
    ),
    pytest.param(
        "Normalize test_extended.xlsx data to standard tabular structure with markdown format",
        """
            Here is the normalized content from the `test_extended.xlsx`, structured in markdown tables:
            
            ### First Sheet
            ```markdown
            | Column 1 | Column 2 | Column 3 |
            |----------|----------|----------|
            | Cars     | Test     | 222      |
            | Data     | Cats     | 111      |
            |          |          | Travellers|
            | Tree     | Forest   |          |
            | Tree     | Forest   |          |
            | Tree     | Forest   |          |
            | Tree     | Forest   |          |
            | Bykes    | Red      | 877      |
            ```
            
            ### Second Sheet
            ```markdown
            | Column 1 | Column 2 | Column 3 | Column 4 |
            |----------|----------|----------|----------|
            | Cars     | Test     | 222      | Second   |
            | Data     | Cats     | 111      | Second   |
            |          |          | Travellers| Second  |
            | Tree     | Forest   |          | Second   |
            | Tree     | Forest   |          | Second   |
            | Tree     | Forest   |          | Second   |
            | Tree     | Forest   |          | Second   |
            | Bykes    | Red      | 877      | Second   |
            ```
            
            ### Hidden Sheet
            ```markdown
            | Column 1 | Column 2 | Column 3 | Column 4 |
            |----------|----------|----------|----------|
            | Cars     | Test     | 222      | Hidden   |
            | Data     | Cats     | 111      | Hidden   |
            |          |          | Travellers| Hidden  |
            | Tree     | Forest   |          | Hidden   |
            | Tree     | Forest   |          | Hidden   |
            | Tree     | Forest   |          | Hidden   |
            | Tree     | Forest   |          | Hidden   |
            | Bykes    | Red      | 877      | Hidden   |
            ```
            
            Each sheet has been normalized into a standard tabular markdown format.
        """,
        id="tabular_normalization",
    ),
    pytest.param(
        "Perform comprehensive analysis of all sheets in test_extended.xlsx including data summary",
        """
            The file `test_extended.xlsx` contains the following information:
            
            ### Overall Summary
            - **Total Sheets:** 3
            
            ### Detailed Sheet Information
            
            #### 1. First Sheet
            - **Columns:**
              | Column Name | Data Type | Sample Values     |
              |-------------|-----------|-------------------|
              | Column 1    | string    | `Cars`, `Data`, ...|
              | Column 2    | string    | `Test`, `Cats`, ...|
              | Column 3    | string    | `222`, `111`, ...  |
            
            #### 2. Second Sheet
            - **Columns:**
              | Column Name | Data Type | Sample Values     |
              |-------------|-----------|-------------------|
              | Column 1    | string    | `Cars`, `Data`, ...|
              | Column 2    | string    | `Test`, `Cats`, ...|
              | Column 3    | string    | `222`, `111`, ...  |
              | Column 4    | string    | `Second`           |
            
            #### 3. Hidden Sheet
            - **Columns:**
              | Column Name | Data Type | Sample Values     |
              |-------------|-----------|-------------------|
              | Column 1    | string    | `Cars`, `Data`, ...|
              | Column 2    | string    | `Test`, `Cats`, ...|
              | Column 3    | string    | `222`, `111`, ...  |
              | Column 4    | string    | `Hidden`           |
            
            These sheets include a variety of string data across the columns with consistent format among the visible and hidden sheets.
        """,
        id="comprehensive_analysis",
    ),
]
