{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e46a14fb-14c8-4522-9951-b699279908a1",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "\n",
    "#Define input and output filenames\n",
    "INPUT_FILE = \"https://storage.googleapis.com/cis_9440_fall25/Motor_Vehicle_Collisions_-_Crashes_20251117.csv\"\n",
    "OUTPUT_FILE = \"Motor_Vehicle_Collisions_CLEANED.csv\"\n",
    "\n",
    "#Columns that will be dropped\n",
    "COLUMNS_TO_DROP = [\n",
    "    'LATITUDE', \n",
    "    'LONGITUDE', \n",
    "    'CROSS STREET NAME', \n",
    "    'OFF STREET NAME',\n",
    "    'CONTRIBUTING FACTOR VEHICLE 2',\n",
    "    'CONTRIBUTING FACTOR VEHICLE 3',\n",
    "    'CONTRIBUTING FACTOR VEHICLE 4',\n",
    "    'CONTRIBUTING FACTOR VEHICLE 5',\n",
    "    'VEHICLE TYPE CODE 2',\n",
    "    'VEHICLE TYPE CODE 3',\n",
    "    'VEHICLE TYPE CODE 4',\n",
    "    'VEHICLE TYPE CODE 5',\n",
    "]\n",
    "\n",
    "#Key columns for row filtering\n",
    "NOT_NULL = [\n",
    "    'BOROUGH', \n",
    "    'CONTRIBUTING FACTOR VEHICLE 1', \n",
    "    'VEHICLE TYPE CODE 1'\n",
    "]\n",
    "\n",
    "#Load the Data\n",
    "try:\n",
    "    df = pd.read_csv(INPUT_FILE, low_memory=False)\n",
    "except Exception as e:\n",
    "    print(f\"Error loading data from the URL: {e}\")\n",
    "    exit()\n",
    "\n",
    "#Drop irrelevant columns\n",
    "df_dropped_cols = df.drop(columns=COLUMNS_TO_DROP, errors='ignore')\n",
    "\n",
    "### 3. Drop Rows with Null Values in Key Columns\n",
    "df_cleaned = df_dropped_cols.dropna(subset=NOT_NULL)\n",
    "\n",
    "#Save to New CSV File\n",
    "df_cleaned.to_csv(OUTPUT_FILE, index=False)\n",
    "print(f\"\\nCleaned data saved to {OUTPUT_FILE}\")"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
