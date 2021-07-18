# Create distance matrix using Google API&nbsp;&nbsp;![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)
This project is built using `Python` and allows you to create a distance matrix in an array between multiple coordinate points from Google Maps and export it to a `.csv` file.

## Requirements
* Coordinate
List of place name, latitude, and longitude provided on coordinate.xlsx file, or you can edit file [coordinate.xlsx](https://github.com/bismaanassuka/distance-matrix-api/blob/master/coordinate.xlsx).

|No|Place                |latitude    |longitude  |
|--|---------------------|------------|-----------|
|1 |Bhayangkara Hospital |-7,813091268|112,0182431|
|2 |DKT Hospital         |-7,808506414|112,0098232|
|3 |Baptis Hospital      |-7,826937415|112,0328038|
|4 |Ahmad Dahlan Hospital|-7,788513467|112,0013828|
|5 |Gambiran Hospital    |-7,838808068|112,031257 |

>I used as an example the coordinates to calculate the distance from several hospitals in Kediri, Indonesia.
Preview: [coordinate.xlsx](https://github.com/bismaanassuka/distance-matrix-api/blob/master/coordinate.xlsx)

* Python 3
* Python Package
  * googlemaps `pip install googlemaps`
  * pandas `pip install pandas`

* API key
You can get the API key at [Google Cloud Platform](https://developers.google.com/maps/documentation/distance-matrix/get-api-key).

>Put your API key in the distance-matrix-api.py file into the API_key variable on line 5.
```python
API_key = 'AIzaSyAF......' #your API here
```

## Usage
To generate your matrix distance, run this file inside this project folder.
```python

distance-matrix-api.py

```

## Result
The result of the completed process will be as below as `.csv` file with semicolon `;` separator.

|     |  1  |  2  |  3  |  4  |  5  |
|  -  |  -  |  -  |  -  |  -  |  -  |
|**1**| 0.0 |1.925|3.442|5.212|4.617|
|**2**|1.53 | 0.0 |4.77 |3.604|5.945|
|**3**|2.992|4.437| 0.0 |7.724|1.461|
|**4**|4.814|3.601|8.055| 0.0 |8.605|
|**5**|4.167|5.612|1.461|8.899| 0.0 |

Preview: [calculated_distances.csv](https://github.com/bismaanassuka/distance-matrix-api/blob/master/calculated_distances.csv)

Enjoy it!:sunglasses:

**bismaanassuka**

[![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/for-you.svg)](https://forthebadge.com)
---
