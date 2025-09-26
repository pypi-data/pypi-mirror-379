# ChemCalc

A Python library for chemical mixture calculations and composition conversions.

## Features

- Convert between different amount types (mass, volume, moles, concentrations, fractions, etc.)
- Calculate mole fractions from various mixture specifications  
- Handle complex mixture compositions including entities and stoichiometry
- Support for recursive mixture calculations
- Unit cell population calculations for molecular simulation
- Support for molality calculations with multiple solutes

## Installation

```bash
pip install chemcalc
```

## Quick Start

### Basic Example: Water/Ethanol/Salt Solution

```python
import chemcalc as cc

# Define the mixture components
names             = ["Water", "Ethanol", "NaCl"        ]
amounts           = [70.0   , 30.0     , 1.0           ]
amount_types      = ["φ"    , "φ"      , "c"           ]  # volume fractions and molarity
units             = ["%"    , "%"      ,"mol/L"        ]
molar_weights     = [18.02  , 46.07    , 58.44         ]  # g/mol
molar_volumes     = [18.0   , 58.5     , 27.0          ]  # mL/mol
entities          = [[]     , []       , ["Na+", "Cl-"]]  # NaCl dissociates            
stoichiometries   = [[]     , []       , [1.0  , 1.0  ]]  # 1:1 ratio

# Create mixture data structure
component_data = cc.create_mixture(
    names, amounts, amount_types, units, Mw=molar_weights, 
    Vm=molar_volumes, entities=entities, stoichiometries=stoichiometries
)

# Get mole fractions
result = cc.get_mole_fractions(component_data, include_entities=True)
print("Mole fractions       :", result["mole_fractions"])
print("Entity mole fractions:", result["entity_mole_fractions"])

# Convert to practical amounts for preparing 1L solution
target_types = ["V", "V", "m"]  # volumes for solvents, mass for salt
conversion = cc.convert(component_data, target_types, 1.0, "V")  # 1L total

print("To prepare 1L solution:")
for comp_name, data in conversion["converted_amounts"].items():
    if data["amount_type"] == "V":
        print(f"{comp_name}: {data['amount']:.3f} L")
    elif data["amount_type"] == "m":
        print(f"{comp_name}: {data['amount']:.3f} g")
```

### Advanced Example: Molality Calculations

```python
# Multiple solutes with molalities
names             = ["Water", "Ethanol", "NaCl", "Urea", "Hydroxybenzoic acid"]
amounts           = [70.0   , 30.0     , 1.0   , 0.5   , 0.8                  ]
amount_types      = ["φ"    , "φ"      , "c"   , "b"   , "b"                  ]  # b = molality
units             = ["%"    , "%"      ,"mol/L", "mol/kg", "mol/kg"           ]

component_data = cc.create_mixture(names, amounts, amount_types, units, ...)
result = cc.get_mole_fractions(component_data)

# Returns separate results for each molal solute
for i, res in enumerate(result):
    print(f"Solution {i+1} mole fractions:", res["mole_fractions"])
```

### Recursive Mixtures

For complex solutions prepared in multiple steps:

```python
# Define base components
components = {
    "Water": {"name": "Water", "mw": 18.015, "vm": 18.0},
    "Ethanol": {"name": "Ethanol", "mw": 46.07, "vm": 58.0},
    "NaCl": {
        "name": "NaCl", "mw": 58.44, "vm": 27.0,
        "properties": {
            "entities": [
                {"name": "Na⁺", "stoichiometry": 1.0},
                {"name": "Cl⁻", "stoichiometry": 1.0}
            ]
        }
    }
}

# Define intermediate mixtures
water_ethanol = {
    "name": "Water-Ethanol", 
    "parents": [
        {"name": "Water", "amount": 70, "amount_type": "φ", "unit": "%"},
        {"name": "Ethanol", "amount": 30, "amount_type": "φ", "unit": "%"}
    ]
}

# Define final mixture
saline_solution = {
    "name": "Saline-Solution",
    "parents": [
        {"name": "Water-Ethanol", "amount": 95, "amount_type": "V", "unit": "mL"},
        {"name": "NaCl", "amount": 0.9, "amount_type": "m", "unit": "g"}
    ]
}

# Combine all nodes
all_nodes = {**components, "Water-Ethanol": water_ethanol, "Saline-Solution": saline_solution}

# Calculate terminal mixtures
results = cc.get_mole_fractions_recursive(all_nodes, include_entities=True)
```

## Supported Amount Types

| Symbol | Type | Standard Unit |
|--------|------|---------------|
| `m` | Mass | g |
| `V` | Volume | L |
| `n` | Moles | mol |
| `w` | Weight fraction | - (0-1) |
| `φ` | Volume fraction | - (0-1) |  
| `x` | Mole fraction | - (0-1) |
| `c` | Molarity | mol/L |
| `b` | Molality | mol/kg |
| `ρ` | Mass concentration | g/L |
| `v` | Specific volume | L/g |

## Unit Conversions

The library automatically handles unit conversions:
- Mass: kg, g, mg, μg
- Volume: m³, L, mL, μL, cc, cm³  
- Amount: mol, mmol, μmol
- Concentrations: M, mM, μM, mol/L, etc.
- Fractions: decimal (0-1) or percentage (%)

## API Reference

### Main Functions

- `create_mixture()`: Create mixture data structure
- `get_mole_fractions()`: Calculate mole fractions from mixture
- `convert()`: Convert to target amount types
- `get_mole_fractions_recursive()`: Handle recursive mixtures
- `populate_unit_cell()`: Calculate entities in unit cell

### Utilities

- `create_amount_matrix()`: Convert mixture to matrix format
- `entities_mole_fraction_algebra()`: Calculate entity mole fractions  
- `amount_conversion_algebra()`: Core conversion calculations

## Requirements

- Python >= 3.8
- NumPy >= 1.19.0

## License

MIT License

## Contributing

Contributions welcome! Please read our contributing guidelines and submit pull requests to our GitHub repository.

## Citation

If you use ChemCalc in your research, please cite:

```
ChemCalc: A Python library for chemical mixture calculations
GitHub: https://github.com/yourusername/chemcalc
```