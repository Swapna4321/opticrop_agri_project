# Entity Relationship Diagram (ERD)

## Overview

The Entity Relationship Diagram (ERD) represents the logical structure of the OptiCrop system and illustrates how user inputs are processed to generate crop recommendations.

## Entities

### User Input

Stores agricultural parameters entered by the user.

Attributes:
- Nitrogen (N)
- Phosphorus (P)
- Potassium (K)
- Temperature
- Humidity
- pH
- Rainfall

### Prediction Model

Processes the input data and predicts the most suitable crop.

Attributes:
- Model ID
- Model Name
- Accuracy

### Crop Recommendation

Stores the predicted crop information.

Attributes:
- Crop ID
- Crop Name
- Prediction Result

## Relationships

- User Input provides agricultural data.
- Prediction Model analyzes the data.
- Crop Recommendation is generated based on model prediction.

## Purpose

The ER Diagram helps visualize data flow and relationships within the OptiCrop system.
