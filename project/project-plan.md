# Project Plan

## Title

Climate Chaos: Understanding the Correlations between Atmospheric Pressure, Temperature and Precipitation with the Patterns of Extreme Weather
## Main Questions

1. How do changes in atmospheric pressure, temperature, and precipitation correlate with the occurrence of severe weather events (e.g., tornadoes, hail, lightning)?
2. How has the frequency and intensity of extreme weather events changed over the past century, and what is the potential link to climate change?

## Description

This project aims to explore the intricate relationships between atmospheric conditions and severe weather events, as well as to understand how these phenomena have evolved over the past century. Utilizing a combination of datasets, including the Integrated Surface Dataset (ISD), the Severe Weather Data Inventory (SWDI), Storm Data, this research addresses two critical questions:
Correlation of Atmospheric Conditions with Severe Weather Events: By analyzing changes in atmospheric pressure, temperature, and precipitation, we seek to determine how these factors correlate with the occurrence of severe weather events such as tornadoes, hail, and lightning. This involves detailed statistical analysis and pattern recognition to uncover the triggers and conditions that precede these extreme events.
Trends in Frequency and Intensity of Extreme Weather: This part of the project focuses on examining how the frequency and intensity of extreme weather events have changed over the past century. By leveraging long-term climate data, we aim to identify trends and potential links to climate change, providing insights into how a warming planet influences weather extremes.
The end goal of this project is to provide a comprehensive understanding of how climatic variables influence severe weather patterns and to highlight the impacts of climate change on weather extremities. This knowledge is crucial for improving predictive models, enhancing disaster preparedness, and informing policy decisions aimed at mitigating the effects of climate change.
## Datasources

<!-- Describe each datasources you plan to use in a section. Use the prefic "DatasourceX" where X is the id of the datasource. -->

### Datasource 1: Integrated Surface Dataset (ISD)
* Metadata URL: catalog.data.gov/harvest/object/74e329d1-945c-423e-a829-e1eb48f88ac8
* Data URL: Integrated Surface Dataset (Global) - Catalog
* Data Type: CSV

The ISD comprises worldwide surface weather observations from over 35,000 stations. Key parameters include air quality, atmospheric pressure, temperature, dew point, wind speed and direction, cloud cover, precipitation, and more. The dataset includes hourly, synoptic (3-hourly), and daily weather observations.

### Datasource 2: Severe Weather Data Inventory (SWDI)
* Metadata URL: catalog.data.gov/harvest/object/4fb59499-cb0b-43d3-bda1-9f059d63bd31
* Data URL: Severe Weather Data Inventory (SWDI) - Catalog
* Data Type: CSV

SWDI integrates severe weather records from various datasets in the National Centers for Environmental Information (NCEI) archive. It includes data on storm cells, hail signatures, mesocyclone signatures, tornado signatures, and lightning strikes, primarily derived from NEXRAD radar and NOAA's National Weather Service reports.

## Work Packages

<!-- List of work packages ordered sequentially, each pointing to an issue with more details. -->

This project is structured into six work packages, represented as [milestones in the GitHub repository](https://github.com/Hassan8725/advance_data_engineering/milestones).
Each work package contains at least one issue. 

1. **Choosing Data Sources** [WP1](https://github.com/TJSarhandi/MADE-01/milestone/1)
    1. Formulate the Research Question [issue](https://github.com/TJSarhandi/MADE-01/issues/3)
    2. Identify Potential Data Sources [issue](https://github.com/TJSarhandi/MADE-01/issues/4)
    3. Assess the Identified Data Sources [issue](https://github.com/TJSarhandi/MADE-01/issues/5)
2. **Data Collection and Processing Pipeline** [WP2](https://github.com/TJSarhandi/MADE-01/milestone/2)
    1. Select the Optimal Data Storage Format [issue](https://github.com/TJSarhandi/MADE-01/issues/6)
    2. Transform Data into the Selected Format [issue](https://github.com/TJSarhandi/MADE-01/issues/7)
    3. Data Pipeline [issue](https://github.com/TJSarhandi/MADE-01/issues/8)
3. **Data Analysis, Exploration, and Reporting** [WP3](https://github.com/TJSarhandi/MADE-01/milestone/3)
    1. Perform Exploratory Data Analysis and Initial Visualization [[issue](https://github.com/TJSarhandi/MADE-01/issues/9)]
    2. Develop Modules: Data Loader, Pipeline, Visualizations, Models, etc. [[issue](https://github.com/TJSarhandi/MADE-01/issues/10)]
    3. Execute Data Analysis and Modeling [[issue](https://github.com/TJSarhandi/MADE-01/issues/11)]
    4. Answer All Research Questions [issue](https://github.com/TJSarhandi/MADE-01/issues/12)
    5. Draw Insights from the Analysis [issue](https://github.com/TJSarhandi/MADE-01/issues/13)
4. **Tests** [WP4](https://github.com/TJSarhandi/MADE-01/milestone/4)
    1. Create Tests for each module [issue](https://github.com/TJSarhandi/MADE-01/issues/14)
5. **Continuous integration** [WP5](https://github.com/TJSarhandi/MADE-01/milestone/5)
    1.	Develop CI for Tests [issue](https://github.com/TJSarhandi/MADE-01/issues/15)
    2.	Set Up CI for Pre-Commit [issue](https://github.com/TJSarhandi/MADE-01/issues/16)
6. **Presenting Findings** [WP6](https://github.com/TJSarhandi/MADE-01/milestone/6)
    1.	Develop visual representations [issue](https://github.com/TJSarhandi/MADE-01/issues/17)
    2. Improve the Repository's Presentation [issue](https://github.com/TJSarhandi/MADE-01/issues/18)
    3. Prepare the Final Presentation [issue](https://github.com/TJSarhandi/MADE-01/issues/19)


Work packages must be completed sequentially as each one depends on the completion of all preceding ones. Dependencies within a work package are specified in the corresponding issues.
Since issues can change, the issue-ID should not be used to identify dependencies. Instead, refer to the dependency list provided in each issue.

## References and footnotes

[^r1]: [https://catalog.data.gov](https://catalog.data.gov/dataset/integrated-surface-dataset-global1)
[^r2]: [https://catalog.data.gov](https://catalog.data.gov/dataset/severe-weather-data-inventory-swdi2)


