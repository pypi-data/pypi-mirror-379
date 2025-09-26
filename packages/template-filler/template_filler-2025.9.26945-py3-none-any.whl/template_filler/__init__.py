from string import Template
from typing import List, Dict, Any

def fill_template(template_string: str, variables: List[Dict[str, Any]]) -> List[str]:
    """
    Fills a template string with combinations of provided variables.

    Args:
        template_string: The template string containing placeholders like ${variable_name}.
        variables: A list of dictionaries. Each dictionary represents a set of possible
                   values for a variable. The keys of the dictionaries are the variable
                   names, and the values are lists of possible values for that variable.

    Returns:
        A list of strings, where each string is a result of filling the template
        with a unique combination of variables.

    Example:
        template = "Hello, ${name}! Your age is ${age}."
        vars_data = [
            {"name": ["Alice", "Bob"]},
            {"age": [30, 25]}
        ]
        results = fill_template(template, vars_data)
        # results will contain:
        # ["Hello, Alice! Your age is 30.", "Hello, Alice! Your age is 25.",
        #  "Hello, Bob! Your age is 30.", "Hello, Bob! Your age is 25."]
    """
    if not template_string or not variables:
        return []

    def generate_combinations(vars_list: List[Dict[str, Any]]) -> List[Dict[str, str]]:
        if not vars_list:
            return [{}]

        first_var_dict = vars_list[0]
        remaining_vars = vars_list[1:]

        combinations_from_remaining = generate_combinations(remaining_vars)

        all_combinations = []
        for key, values in first_var_dict.items():
            for value in values:
                for combo in combinations_from_remaining:
                    new_combo = {key: str(value)}
                    new_combo.update(combo)
                    all_combinations.append(new_combo)
        return all_combinations

    template = Template(template_string)
    filled_strings = []
    
    # Check if variables is a list of dictionaries, where each dictionary contains a list of values
    # e.g., [{"name": ["Alice", "Bob"]}, {"age": [30, 25]}]
    if all(isinstance(v, dict) and all(isinstance(val, list) for val in v.values()) for v in variables):
        # If the structure is as expected, proceed with combination generation
        variable_combinations = generate_combinations(variables)
    else:
        # If the structure is different (e.g., a single dict with lists), adapt it
        # This assumes the input might be a single dict like {"name": ["Alice", "Bob"], "age": [30, 25]}
        adapted_variables = []
        if isinstance(variables, dict):
            adapted_variables.append(variables)
        elif isinstance(variables, list) and all(isinstance(v, dict) for v in variables):
            # This case handles if the input was already [{"name": ["Alice", "Bob"], "age": [30, 25]}]
            # We need to ensure each dict is treated as a single 'set' of variables for combination
            # The current logic of generate_combinations expects list of dicts where each dict is a variable type
            # Let's flatten and then re-group if needed, or assume a simpler input structure for this branch.
            # For simplicity, we will assume a single dictionary input that needs to be processed.
            # A more robust solution would require more specific input format definition.
            # For now, let's assume if it's a list of dicts, each dict is a unique variable type with its values.
            # The `generate_combinations` function is designed for that.
            # If `variables` is `[{"name": ["Alice", "Bob"]}, {"age": [30, 25]}]`, the original `generate_combinations` works.
            # If `variables` is `[{"name": "Alice", "age": 30}, {"name": "Bob", "age": 25}]`, it's not a template filler in the described sense.
            # Let's stick to the specified example structure.
            pass # The first check handles the intended structure.
        
        if not variable_combinations: # If the initial check failed and no combinations were generated
             # Handle cases where variables might be a single dictionary of lists, e.g., {"name": ["A", "B"], "age": [1, 2]}
            if isinstance(variables, dict):
                variable_combinations = generate_combinations([variables])
            else:
                return [] # Or raise an error for unexpected format.

    for combo in variable_combinations:
        filled_strings.append(template.substitute(combo))

    return filled_strings