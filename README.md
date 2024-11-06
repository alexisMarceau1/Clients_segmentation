# Customer Segmentation Project

## Project Overview

This project was developed to provide the e-commerce team of Olist, a Brazilian online marketplace, with a robust customer segmentation model. The goal was to segment customers based on their purchasing behaviors and personal data to help the marketing team tailor communication campaigns more effectively. This segmentation analysis also includes a recommended maintenance schedule to ensure the model's accuracy over time.

## Business Context

Olist's e-commerce team requires actionable customer segments to inform daily communication strategies and campaigns. Our objective was to analyze customer data to identify distinct user types and deliver a comprehensive, data-driven segmentation model. This model is optimized for daily marketing use and includes maintenance insights to keep segments up-to-date.

## Key Insights

After thorough analysis and model testing, the final segmentation defines four customer labels with the following characteristics:

- **Label 0**: Satisfied but inactive customers who last ordered a long time ago.
- **Label 1**: Highly engaged, satisfied customers who frequently interact with the platform.
- **Label 2**: Regular but moderately engaged customers with average satisfaction.
- **Label 3**: Least satisfied customers, typically with lower review scores.

The segmentation showed that while recency and satisfaction were well-distinguished, total spend did not provide significant separation across clusters, likely due to most customers making only a single purchase.

## Model Stability

To ensure the segments remain accurate over time, a stability analysis was performed. Results indicate that the model should be retrained every 30 days to maintain a high Adjusted Rand Index (ARI) above 0.8, ensuring stable and reliable segmentation.

## Conclusion

The RFM-based segmentation model is particularly effective for categorizing customers by recency and satisfaction, with limited differentiation in spending patterns. The model is recommended for ongoing use with monthly updates to maintain segmentation quality.
