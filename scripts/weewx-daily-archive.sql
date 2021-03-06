--SQLite setup (i.e. CSV and headers)
.mode csv
.header on
-- Timestamp Temp    Chill   HIndex  Humid   Dewpt    Wind   HiWind  WindDir Rain    Barom   Solar    ET      UV
SELECT datetime(dateTime,'unixepoch') AS Timestamp,
	outTemp AS Temp,
	windchill AS Chill,
	heatindex AS HIndex,
	outHumidity AS Humid,
	dewpoint AS Dewpt,
	windSpeed AS Wind,
   windGust AS HiWind,
	windDir AS WindDir,
	rain AS Rain,
	rainRate AS RainRate,
	barometer AS Barom,
	radiation AS Solar,
	ET,
	UV,
	inTemp AS InsideTemp,
	inHumidity AS InsideHumid
	--pressure,
	--altimeter,
	--usUnits,
	--interval,
	--windGust,
	--windGustDir,
	--rain,
	--extraTemp1,
	--extraTemp2,
	--extraTemp3,
	--soilTemp1,
	--soilTemp2,
	--soilTemp3,
	--soilTemp4,
	--leafTemp1,
	--leafTemp2,
	--extraHumid1,
	--extraHumid2,
	--soilMoist1,
	--soilMoist2,
	--soilMoist3,
	--soilMoist4,
	--leafWet1,
	--leafWet2,
	--rxCheckPercent,
	--txBatteryStatus,
	--consBatteryVoltage,
	--hail,
	--hailRate,
	--heatingTemp,
	--heatingVoltage,
	--supplyVoltage,
	--referenceVoltage,
	--windBatteryStatus,
	--rainBatteryStatus,
	--outTempBatteryStatus,
	--inTempBatteryStatus
FROM archive WHERE DATETIME(dateTime,'unixepoch') > DATETIME('%%DATE%%','start of day','-1 seconds') AND DATETIME(dateTime,'unixepoch')  < DATETIME('%%DATE%%','+1 day','start of day') ORDER BY dateTime;
