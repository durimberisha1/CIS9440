--Dimension/Fact Table Creation

--Create Dim_Date
CREATE TABLE `cis9440-nyc-traffic.nyc_crashes_dataset.Dim_Date` (
    Date_PK INT64 NOT NULL,
    CRASH_DATE DATE NOT NULL,
    CRASH_TIME TIME NOT NULL,
    CRASH_HOUR INT64,
    CRASH_DAY_OF_WEEK STRING
);

--Create Dim_Location
CREATE TABLE `cis9440-nyc-traffic.nyc_crashes_dataset.Dim_Location` (
    Location_PK INT64 NOT NULL,
    BOROUGH STRING,
    ZIP_CODE STRING,
    LOCATION STRING,
    ON_STREET_NAME STRING
);

--Create Dim_Contributin_Factor
CREATE TABLE `cis9440-nyc-traffic.nyc_crashes_dataset.Dim_Contributing_Factor` (
    Factor_PK INT64 NOT NULL,
    CONTRIBUTING_FACTOR STRING
);

--Create Dim_Vehicle
CREATE TABLE `cis9440-nyc-traffic.nyc_crashes_dataset.Dim_Vehicle` (
    Vehicle_PK INT64 NOT NULL,
    VEHICLE_TYPE_CODE STRING
);

--Create Fact_Crashes
CREATE TABLE `cis9440-nyc-traffic.nyc_crashes_dataset.Fact_Crashes` (
    Collision_ID STRING NOT NULL,
    Date_FK INT64,
    Location_FK INT64,
    NUMBER_OF_PERSONS_INJURED INT64,
    NUMBER_OF_PERSONS_KILLED INT64,
    NUMBER_OF_PEDESTRIANS_INJURED INT64,
    NUMBER_OF_PEDESTRIANS_KILLED INT64,
    NUMBER_OF_CYCLIST_INJURED INT64,
    NUMBER_OF_CYCLIST_KILLED INT64,
    NUMBER_OF_MOTORIST_INJURED INT64,
    NUMBER_OF_MOTORIST_KILLED INT64,
    Factor_1_FK INT64,
    Vehicle_Type_1_FK INT64
);





