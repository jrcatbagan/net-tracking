#
# File: makefile
# Created: 2015, May 28
#
#
# AlphaGroup
#

.PHONY: default prepare-database clean

default:
	@echo -e "error: no target(s) specified\n"
	@echo -e "specify target 'help' to see supported targets\n"
prepare-database:
	wget http://geolite.maxmind.com/download/geoip/database/GeoLiteCountry/GeoIP.dat.gz
	wget http://geolite.maxmind.com/download/geoip/database/GeoLiteCity.dat.gz
	gzip --decompress GeoIP.dat.gz
	gzip --decompress GeoLiteCity.dat.gz
	@mkdir database
	@mv GeoIP.dat ./database
	@mv GeoLiteCity.dat ./database
	@echo -e "databases stored in $PWD/database\n"
clean:
# current approach must take care that 'build' is not deleted; must find a more
# elegant solution
	rm -f build/*
help:
	@echo -e "targets supported:\n"
	@echo -e "\tprepare-db:\tretreives and prepares the necessary GeoIP databases\n"
