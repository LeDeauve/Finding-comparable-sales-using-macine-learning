# Features

Feature type explanation
NC: Non-ordinal categorical  
OC: Ordinal categorical  
N: Numerical (float/integer)  
B: Boolean  

| Name                                           | Datatype | Type (NC/OC/N/B)* |  Description |
| ---------------------------------------------- | -------- | -- | ----------- |
| **Object features**                            |          | | |
| TransactionId                                  | string   | -  | Transaction ID, unique key. Good to have when debugging. |
| SalePrice                                      | integer  | Target | Sale Price at EstimatedContractDate. |
| LogSalePrice                                   | float    | Target | Log of SalePrice |
| AdjSalePrice202006                             | float    | Target | Adjusted Sale Price to 2020-06 |
| LogAdjSalePrice202006                          | float    | Target | Log of AdjSalePrice202006 |
| BuildingAge                                    | integer  | OC/N | Building age - years since construction or significant renovation, AT TIME OF SALE. |
| UtilityArea                                    | integer  | N | 'Värdeyta', Living area + min(Auxilary area, 0.2*LivingArea, 20) |
| LotArea                                        | integer  | N | Lot area |
| QualityScore                                   | integer  | OC/N | Tax authority defined scoring for the quality of the property |
| CloseToBeach                                   | integer  | OC/B | Close to beach? , if STRAND in [1, 2] True else False |
| EnergyPerformance                              | integer  | N | How much energy per square meter the property uses |
| EnergyClass                                    | string   | OC | EPC-rating. Missing for roughly 30% of transactions. |
| HasWater                                       | integer  | C/B | Communal water access |
| HasSewer                                       | integer  | C/B | Communal sewage access |
| BuildingStyle                                  | integer  | C | Building style (1: friliggande villa, 2:kedjehus, 3:radhus) |
| STRAND                                         | integer  | N/OC | Tax authority beach classification (changed in 2004), 1, 2, 3, 4 and 1 is closest to beach |
| LivingArea                                     | integer  | N | Living area of property |
| AuxilaryArea                                   | integer  | N | Auxilary area of the property - areas not deemed livable (cieling height, heating, insulation, etc) |
| SecondHome                                     | integer  | C/B | Is it a second home? |
| NSalesPast1yr                                  | integer  | N | Number of sales of the same property the past year |
| NSalesPast2yr                                  | integer  | N | Number of sales of the same property the past 2 years |
| NSalesPast4yr                                  | integer  | N | Number of sales of the same property the past 4 years |
| NSalesPast6yr                                  | integer  | N | Number of sales of the same property the past 6 years |
| NSalesPast8yr                                  | integer  | N | Number of sales of the same property the past 8 years |
| NSalesPast10yr                                 | integer  | N | Number of sales of the same property the past 10 years |
| MonthsAgoLastSale                              | integer  | N | Number of months since the last sale, max 120 months.|
| **Neighborhood features**                      |  | |  |
| DesoClass                                      | string   | C | Deso Class (A: Rural, B: Suburb, C: City center) |
| SpMedianSqCorrBaseAreaId                       | float    | N | Sale price median corrected for living area of base area |
| SpVarianceSqCorrBaseAreaId                     | float    | N | Sale price variance corrected for living area of base area |
| SpMedianBaseAreaId                             | float    | N | Sale price median of base area |
| NBaseAreaId                                    | integer  | N | Number of properties of base area |
| MedianConstructionYear                         | float    |  | Median construction year in Deso area |
| UnknownConstructionYearFrac                    | float    |  | Fraction of unknown construction year in Deso area |
| MedianConstructionYear2yrChangeMean            | float    |  | Median construction year 2 year mean change in Deso area |
| UnknownConstructionYearFrac2yrChangeMean       | float    |  | Unknown construction year 2 year mean change in Deso area |
| PopLt20Frac                                    | float    |  | Fraction of population age <20 in Deso area |
| PopFrom20to64Frac                              | float    |  | Fraction of population age 20-64 in Deso area |
| PopGt64Frac                                    |float     |  | Fraction of population age >64 in Deso area |
| MedianAge                                      | float    |  | Median age of population in Deso area |
| PopLt20Frac2yrChangeMean                       | float    |  | PopLt20Frac 2 year mean change in Deso area |
| PopFrom20to64Frac2yrChangeMean                 | float    |  | PopFrom20to64Frac 2 year mean change DeSo area |
| PopGt64Frac2yrChangeMean                       | float    |  | PopGt64Frac 2 year mean change DeSo area |
| MedianAge2yrChangeMean                         | float    |  | MedianAge 2 year mean change  DeSo area |
| SingleWoKidsFrac                               | float    |  | Fraction of single without kids in Deso area |
| CohabitWoKidsFrac                              | float    |  | Fraction of cohabit without kids in Deso area |
| CohabitWithKidsFrac                            | float    |  | Fraction of cohabit with kids in Deso area |
| SingleWoKidsFrac2yrChangeMean                  | float    |  | SingleWoKidsFrac 2 year mean change in Deso area |
| CohabitWoKidsFrac2yrChangeMean                 | float    |  | CohabitWoKidsFrac2 year mean change in Deso area |
| CohabitWithKidsFrac2yrChangeMean               | float    |  | CohabitWithKidsFrac 2 year mean change in Deso area |
| OnBenefitsFrac                                 | float    |  | Fraction on benefits in Deso area |
| OnBenefitsFrac2yrChangeMean                    | float    |  | OnBenefitsFrac 2 year mean change in Deso area  |
| LowIncomePct                                   | float    |  | Low income percentage in Deso area  |
| HighIncomePct                                  | float    |  | High income percentage in Deso area |
| LowIncomePct2yrChangeMean                      | float    |  | LowIncomePct 2 year mean change in Deso area |
| HighIncomePct2yrChangeMean                     | float    |  | HighIncomePct 2 year mean change in Deso area |
| RentalPopFrac                                  | float    |  | Fraction of population in rentals in Deso area |
| CoopPopFrac                                    | float    |  | Fraction of population in coop apartments in Deso area |
| OwnershipPopFrac                               | float    |  | Fraction of population in ownership housing in Deso area |
| RentalPopFrac2yrChangeMean                     | float    |  | RentalPopFrac2 year mean change in Deso area |
| CoopPopFrac2yrChangeMean                       | float    |  | CoopPopFrac 2 year mean change in Deso area |
| OwnershipPopFrac2yrChangeMean                  | float    |  | OwnershipPopFrac 2 year mean change in Deso area |
| MeanIncomeSEK                                  | float    |  | Mean income in Deso area |
| MedianIncomeSEK                                | float    |  | Median income in Deso area |
| DiffMeanIncomeSEK                              | float    |  | Mean income difference to national mean in Deso area |
| DiffMedianIncomeSEK                            | float    |  | Median income difference to national median in Deso area |
| MeanIncomeSEK2yrChangeMean                     | float    |  | MeanIncomeSEK 2 year mean change in Deso area |
| MedianIncomeSEK2yrChangeMean                   | float    |  | MedianIncomeSEK 2 year mean change in Deso area |
| DiffMeanIncomeSEK2yrChangeMean                 | float    |  | DiffMeanIncomeSEK 2 year mean change in Deso area |
| DiffMedianIncomeSEK2yrChangeMean               | float    |  | DiffMedianIncomeSEK 2 year mean change in Deso area |
| PostGymnasiumLongFrac                          | float    |  | Fraction of population with post gymnasium edu >2 years in Deso area |
| PostGymnasiumShortFrac                         | float    |  | Fraction of population with post gymnasium edu <=2 years in Deso area |
| PreGymnasiumFrac                               | float    |  | Fraction of population with pre gymnasium edu in Deso area |
| GymnasiumFrac                                  | float    |  | Fraction of population with gymnasium edu in Deso area |
| GroupPostGymnasiumFrac                         | float    |  | Fraction of population with any post gymnasium edu in Deso area |
| PostGymnasiumLongFrac2yrChangeMean             | float    |  | PostGymnasiumLongFrac 2 year mean change in Deso area |
| PostGymnasiumShortFrac2yrChangeMean            | float    |  | PostGymnasiumShortFrac2 year mean change in Deso area |
| PreGymnasiumFrac2yrChangeMean                  | float    |  | PreGymnasiumFrac2 year mean change in Deso area |
| GymnasiumFrac2yrChangeMean                     | float    |  | GymnasiumFrac 2 year mean change in Deso area |
| GroupPostGymnasiumFrac2yrChangeMean            | float    |  | GroupPostGymnasiumFrac2 year mean change in Deso area |
| UnemploymentPctCounty                          | float    |  | Percentage unemployment in County |
| UnemploymentPctCounty2yrChangeMean             | float    |  | UnemploymentPctCounty 2 year mean change in County |
| MunicipalityPopulation                         | integer  |  | Population in Municipality |
| MunicipalityPopulation2yrFracChangeMean        | float    |  | MunicipalityPopulation2 year mean change in Municipality |
| MunicipalityMoveInFrac                         | float    |  | Pop fraction moved into Municipality |
| MunicipalityMoveOutFrac                        | float    |  | Pop fraction moved out of Municipality |
| MunicipalityMoveInFromCountyFrac               | float    |  | Pop fraction moved into into Municipality from County |
| MunicipalityMoveOutToCountyFrac                | float    |  | Pop fraction moved out of Municipality but within same County |
| MunicipalityMoveInFrac2yrChangeMean            | float    |  | MunicipalityMoveInFrac2 year mean change in Municipality |
| MunicipalityMoveOutFrac2yrChangeMean           | float    |  | MunicipalityMoveOutFrac 2 year mean change in Municipality |
| MunicipalityMoveInFromCountyFrac2yrChangeMean  | float    |  | MunicipalityMoveInFromCountyFrac 2 year mean change in Municipality |
| MunicipalityMoveOutToCountyFrac2yrChangeMean   | float    |  | MunicipalityMoveOutToCountyFrac 2 year mean change in Municipality |
| MunicipalityPopulationMeanDeviation            | float    |  | Deviation of municipality population from the national mean |
| MedianRentMunicipality                         | float    |  | Median rent in Municipality |
| MedianRentMunicipality2yrFracChangeMean        | float    |  | MedianRentMunicipality 2 year mean change in Municipality |
| MedianRentMunicipalityMeanDeviation            | float    |  | Devation from national mean of median rent in Municipality |
| **Makro economical features**     |  |  |  |
| KPIF                                           | float    |  | Core inflation |
| KPIF6MthChangeMean                             | float    |  | KPIF 6 month change |
| KPIF3MthChangeMean                             | float    |  | KPIF 3 month change |
| AverageInterestRate                            | float    |  | Average interest rate (Styrränta) |
| AverageInterestRate3MthChange                  | float    |  | AverageInterestRate 3 month change |
| AverageInterestRate6MthChange                  | float    |  | AverageInterestRate 6 month change |
| AverageInterestRate12MthChange                 | float    |  | AverageInterestRate 12 month change |
| BRP                                            | float    | N | Regional GDP |
| BRP2yrFracChangeMean                           | float    | N | Regional GDP 2 year mean fractional change |
| BRPMeanDeviation                               | float    | N | Regional GDP Mean deviation for each year wrt national mean |
| BRPMeanDeviation2YrChangeMean                  | float    | N | Regional GDP 2 year mean fractional change of BRPMeanDeviation  |
| **Spatial/Geographic features** | | |  |
| Lat                                            | float    | N | Latitude coordinate |
| Lon                                            | float    | N | Longitude coordinate |
| TaxRegionIdTp10                                | integer  | C | Tax region ID (Värdeområde) from taxation period 10 |
| BaseAreaId                                     | integer  | C | GrundområdesID |
| BaseAreaName                                   | string   | C | Base area name, more easily identifiable, XX_YYY_ZZ where XX is Model Area (Sweden divided into 8 of them), YYY is what building type (100 villa, 023 chain-linked + terraced) and ZZ a number |
| MunicipalityCode                               | integer  | C | Municipality code 0180: stockholm, see [wikipedia page on Sveriges Kommuner](https://sv.wikipedia.org/wiki/Lista_%C3%B6ver_Sveriges_kommuner) |
| CountyCode                                     | integer  | C | County code 1: stockholm, 2: dalarna, 3: ... see [wikipedi page on Sveriges Län](https://sv.wikipedia.org/wiki/Sveriges_l%C3%A4n) |
| DesoArea                                       | string   | C | Deso area - demographic statistic area |
| MunicipalityCodeStr                            | string   | C | 4 position string coding of MunicipalityCode  |
| CountyCodeStr                                  | string   | C | 4 position string coding of CountyCode |
|                                  |  |  |  |
| DistTinyCity                                   | float    |  | Distance to tiny city (pop 0-2_000) |
| DistSmallCity                                  | float    |  | Distance to small city (pop 2_000-20_000) |
| DistMediumCity                                 | float    |  | Distance to medium city (pop 20_000-200_000) |
| DistLargeCity                                  | float    |  | Distance to large city (pop  200_000-) |
| DistAnyCity                                    | float    |  | Distance to any city |
|                                  |  |  |  |
| DistRiver                                      | float    |  | Distance to river |
| DistStream                                     | float    |  | Distance to stream (smaller than river) |
| DistLakeTiny                                   | float    |  | Distance to tiny lakes (10_000-2e5 sqm) |
| DistLakeSmall                                  | float    |  | Distance to small lakes (2e5-1e7 sqm) |
| DistLakeMedium                                 | float    |  | Distance to medium lakes (1e7-1e8 sqm) |
| DistLakeLarge                                  | float    |  | Distance to large lakes (1e8- sqm)|
| DistCoast                                      | float    |  | Distance to coast |
| DistWaterAny                                   | float    |  | Distance to any water body |
|                                  |  |  |  |
| DistRailAnyKm                                  | float    |  | Distance to any rail |
| DistRailLe50Km                                 | float    |  | Distance to rail with max speed 50 km/h |
| DistRailGt50Le100Km                            | float    |  | Distance to rail with max speed 50-100 km/h  |
| DistRailGt100Km                                | float    |  | Distance to rail with max speed >100 km/h  |
|                                  |  |  |  |
| DistNearestRoadTpl                             | float    |  | Distance to nearest road trafikplats (roughly highway entry) |
|                                  |  |  |  |
| HTH5t30Pct                                     | float    |  | Fraction of max speed <30 km/h roads within 500 m radi |
| HTH40t60Pct                                    | float    |  | Fraction of max speed 40-60 km/h roads within 500 m radi |
| HTH70t90Pct                                    | float    |  | Fraction of max speed 70-90 km/h roads within 500 m radi |
| HTHgt100Pct                                    | float    |  | Fraction of max speed >100 km/h roads within 500 m radi |
|                                  |  |  |  |
| DistCampingKm                                  | float    |  | Distance to camping site (km) |
| DistGolfKm                                     | float    |  | Distance to golf course (km) |
| DistBeachKm                                    | float    |  | Distance to beach (km) |
| DistSkiSmallKm                                 | float    |  | Distance to small downhill ski restort (0-3 sqkm) |
| DistSkiMediumKm                                | float    |  | Distance to medium downhill ski restort ( 3-9 sqkm) |
| DistSkiLargeKm                                 | float    |  | Distance to large downhill ski restort ( >9 sqkm) |
| DistSkiAnyKm                                   | float    |  | Distance to any downhill ski restort |
| DistIntlAirportKm                              | float    |  | Distance to international airport |
| DistAnyAirportKm                               | float    |  | Distance to any airport |
| DistNordicSmallKm                              | float    |  | Distance to small nordic ski tracks (first 33 percentiles) |
| DistNordicMediumKm                             | float    |  | Distance to medium nordic ski tracks (middle 33 percentiles) |
| DistNordicLargeKm                              | float    |  | Distance to large nordic ski tracks (top 33 percentiles) |
| DistNordicAnyKm                                | float    |  | Distance to any nordic ski tracks |
| DistCommerceKm                                 | float    |  | Distance to commercial area |
| DistIndustryKm                                 | float    |  | Distance to industrial area |
|                                  |  |  |  |
| InCitySize                                     | string   |  | Within city of a certain size (tiny: <2_000, small:2e3-2e4, medium:2e4-2e5, large:>2e5, InRural:outside a city) |
|                                  |  |  |  |
| DistStopRailKm                                 | float    |  | Distance to rail stop (km) |
| DistStopBusKm                                  | float    |  | Distance to bus stop (km) |
| DistStopCommunaltaxiKm                         | float    |  | Distance to communal taxi (km) |
| DistStopTramKm                                 | float    |  | Distance to tram stop (km) |
| DistStopWaterKm                                | float    |  | Distance to water transport (km) |
| DistStopMetroKm                                | float    |  | Distance to metro stop (km) |
| **Temporal features**                          |       |  |  |
| SaleYear                                       | integer  |  | sale year |
| SaleDaySince1990                               | integer  |  | sale day in days since 1990  |
| SaleMonthOfYear                                | integer  |  | month of the year |
| SaleQuarterOfYear                              | integer  |  | quarter of the year |
| SaleDayOfYear                                  | integer  |  | day of year |
| SaleDayOfMonth                                 | integer  |  | day of month |
| SaleDayOfWeek                                  | integer  |  | day of week |
| **Other supporting columns**                   |          | |  |
| AdjFactorYYYYMM                                | float |  | Adjustment Factor to get Sale Price to 2020-06 (YYYY-MM) |
| geometry                                       | - |  | GIS-info |
| YearMonth                                      | date |   |  |
| EstimatedContractDate                          | date |   | (Predikterat) kontraktsdatum |
| EstimatedContractPeriod                        | date |   | Predikterad försäljningsdatum, som period månad |
| DatePeriod                                     | date |   |   |
| CityRefYear                                    | integer  |  | Used to join statistics from a year to the right corresponding year of transaction. |

