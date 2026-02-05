"""
Data Processing Examples - GitHub Copilot in PyCharm

This file demonstrates how Copilot can help with data processing tasks.
Includes examples of data transformation, analysis, and manipulation.
"""

from typing import List, Dict, Any
from collections import Counter, defaultdict
import statistics


# Example 1: CSV-like Data Processing
# ====================================

def parse_csv_line(line: str, delimiter: str = ',') -> List[str]:
    """Parse a CSV line into a list of fields."""
    return [field.strip() for field in line.split(delimiter)]


def csv_to_dict_list(csv_text: str, has_header: bool = True) -> List[Dict[str, str]]:
    """
    Convert CSV text to a list of dictionaries.
    
    Args:
        csv_text: CSV formatted text
        has_header: Whether first line contains headers
        
    Returns:
        List of dictionaries representing each row
    """
    lines = csv_text.strip().split('\n')
    
    if not lines:
        return []
    
    if has_header:
        headers = parse_csv_line(lines[0])
        data_lines = lines[1:]
    else:
        # Generate generic headers
        headers = [f"column_{i}" for i in range(len(parse_csv_line(lines[0])))]
        data_lines = lines
    
    result = []
    for line in data_lines:
        fields = parse_csv_line(line)
        row_dict = {headers[i]: fields[i] for i in range(min(len(headers), len(fields)))}
        result.append(row_dict)
    
    return result


# Example 2: Data Aggregation
# ============================

def group_by_field(data: List[Dict[str, Any]], field: str) -> Dict[Any, List[Dict[str, Any]]]:
    """
    Group data by a specific field.
    
    Args:
        data: List of dictionaries
        field: Field name to group by
        
    Returns:
        Dictionary with field values as keys and grouped items as values
    """
    groups = defaultdict(list)
    for item in data:
        if field in item:
            groups[item[field]].append(item)
    return dict(groups)


def calculate_statistics(numbers: List[float]) -> Dict[str, float]:
    """
    Calculate basic statistics for a list of numbers.
    
    Args:
        numbers: List of numeric values
        
    Returns:
        Dictionary with statistical measures
    """
    if not numbers:
        return {}
    
    return {
        'mean': statistics.mean(numbers),
        'median': statistics.median(numbers),
        'mode': statistics.mode(numbers) if len(set(numbers)) < len(numbers) else None,
        'stdev': statistics.stdev(numbers) if len(numbers) > 1 else 0,
        'min': min(numbers),
        'max': max(numbers),
        'sum': sum(numbers),
        'count': len(numbers)
    }


# Example 3: Data Filtering and Transformation
# =============================================

def filter_by_criteria(data: List[Dict[str, Any]], criteria: Dict[str, Any]) -> List[Dict[str, Any]]:
    """
    Filter data based on multiple criteria.
    
    Args:
        data: List of dictionaries to filter
        criteria: Dictionary of field names and values to match
        
    Returns:
        Filtered list of dictionaries
    """
    result = []
    for item in data:
        match = True
        for key, value in criteria.items():
            if key not in item or item[key] != value:
                match = False
                break
        if match:
            result.append(item)
    return result


def transform_fields(data: List[Dict[str, Any]], transformations: Dict[str, callable]) -> List[Dict[str, Any]]:
    """
    Apply transformations to specific fields in data.
    
    Args:
        data: List of dictionaries
        transformations: Dictionary mapping field names to transformation functions
        
    Returns:
        Transformed data
    """
    result = []
    for item in data.copy():
        new_item = item.copy()
        for field, transform_func in transformations.items():
            if field in new_item:
                new_item[field] = transform_func(new_item[field])
        result.append(new_item)
    return result


# Example 4: Data Analysis
# ========================

def find_duplicates(data: List[Any]) -> List[Any]:
    """
    Find duplicate items in a list.
    
    Args:
        data: List of items
        
    Returns:
        List of duplicate items
    """
    counts = Counter(data)
    return [item for item, count in counts.items() if count > 1]


def get_frequency_distribution(data: List[Any]) -> Dict[Any, int]:
    """
    Get frequency distribution of items.
    
    Args:
        data: List of items
        
    Returns:
        Dictionary with items and their counts
    """
    return dict(Counter(data))


def calculate_percentage_distribution(data: List[Any]) -> Dict[Any, float]:
    """
    Calculate percentage distribution of items.
    
    Args:
        data: List of items
        
    Returns:
        Dictionary with items and their percentages
    """
    counts = Counter(data)
    total = len(data)
    return {item: (count / total) * 100 for item, count in counts.items()}


# Example 5: Data Cleaning
# =========================

def remove_empty_values(data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Remove entries with empty or None values.
    
    Args:
        data: List of dictionaries
        
    Returns:
        Cleaned data with non-empty values
    """
    result = []
    for item in data:
        cleaned_item = {k: v for k, v in item.items() if v is not None and v != ''}
        if cleaned_item:
            result.append(cleaned_item)
    return result


def normalize_text_fields(data: List[Dict[str, str]], fields: List[str]) -> List[Dict[str, str]]:
    """
    Normalize text fields (lowercase, strip whitespace).
    
    Args:
        data: List of dictionaries
        fields: List of field names to normalize
        
    Returns:
        Data with normalized text fields
    """
    result = []
    for item in data:
        new_item = item.copy()
        for field in fields:
            if field in new_item and isinstance(new_item[field], str):
                new_item[field] = new_item[field].strip().lower()
        result.append(new_item)
    return result


# Example 6: Data Merging
# =======================

def merge_lists_by_key(list1: List[Dict[str, Any]], list2: List[Dict[str, Any]], key: str) -> List[Dict[str, Any]]:
    """
    Merge two lists of dictionaries based on a common key.
    
    Args:
        list1: First list of dictionaries
        list2: Second list of dictionaries
        key: Common key to merge on
        
    Returns:
        Merged list of dictionaries
    """
    # Create a lookup dictionary for list2
    lookup = {item[key]: item for item in list2 if key in item}
    
    result = []
    for item in list1:
        if key in item and item[key] in lookup:
            merged_item = item.copy()
            merged_item.update(lookup[item[key]])
            result.append(merged_item)
        else:
            result.append(item)
    
    return result


# Example Usage and Demonstration
if __name__ == "__main__":
    print("Data Processing Examples Demo")
    print("=" * 60)
    
    # Sample CSV data
    csv_data = """name,age,city,score
John Doe,25,New York,85
Jane Smith,30,Los Angeles,92
Bob Johnson,25,Chicago,78
Alice Brown,30,New York,88
Charlie Davis,35,Los Angeles,95"""
    
    # Parse CSV
    print("\n1. Parsing CSV Data:")
    parsed_data = csv_to_dict_list(csv_data)
    for row in parsed_data:
        print(f"   {row}")
    
    # Group by age
    print("\n2. Grouping by Age:")
    grouped = group_by_field(parsed_data, 'age')
    for age, people in grouped.items():
        print(f"   Age {age}: {len(people)} people")
    
    # Calculate statistics on scores
    print("\n3. Score Statistics:")
    scores = [float(row['score']) for row in parsed_data]
    stats = calculate_statistics(scores)
    for stat, value in stats.items():
        if value is not None:
            print(f"   {stat.capitalize()}: {value:.2f}")
    
    # Filter by city
    print("\n4. Filtering (City = New York):")
    filtered = filter_by_criteria(parsed_data, {'city': 'New York'})
    for row in filtered:
        print(f"   {row['name']} - Score: {row['score']}")
    
    # Find duplicate ages
    print("\n5. Duplicate Ages:")
    ages = [row['age'] for row in parsed_data]
    duplicates = find_duplicates(ages)
    print(f"   Ages appearing more than once: {duplicates}")
    
    # Frequency distribution of cities
    print("\n6. City Distribution:")
    cities = [row['city'] for row in parsed_data]
    distribution = get_frequency_distribution(cities)
    for city, count in distribution.items():
        print(f"   {city}: {count} people")
    
    print("\n" + "=" * 60)
    print("Demo completed!")
