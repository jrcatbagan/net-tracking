/*
 * File: ip-to-geolocation.c
 * Created: 2015, May 28
 *
 *
 * AlphaGroup
 */

#include <stdio.h>
#include <stdlib.h>
#include <GeoIPCity.h>

int main(int argc, char **argv)
{
	if (argc != 2) {
		fprintf(stderr, "error: invalid number of arguments\n\n");
		fprintf(stderr, "usage: %s <IPv4 address>\n\n");
		exit(EXIT_FAILURE);
	}

	GeoIP *db_handle = GeoIP_open(GEOIP_DATABASE_NAME, GEOIP_STANDARD);
	if (db_handle == NULL) {
		fprintf(stderr, "error: failed to open database: %s\n", GEOIP_DATABASE_NAME);
		exit(EXIT_FAILURE);
	}

	GeoIPRecord *geoiprecord = GeoIP_record_by_addr(db_handle argv[1]);
	if (geoiprecord == NULL) {
		fprintf(stderr, "error: failed to retreive geographical information\n");
		exit(EXIT_FAILURE);
	}

	printf("country code: %s\n", geoiprecord->country_code);
	printf("3 character country code: %s\n", geoiprecord->country_code3);
	printf("country name: %s\n", geoiprecord->country_name);
	printf("region: %s\n", geoiprecord->region);
	printf("city: %s\n", geoiprecord->city);
	printf("postal code: %s\n", geoiprecord->postal_code);
	printf("longitude: %f\n", geoiprecord->longitude);
	printf("latitude: %f\n", geoiprecord->latitude);

	GeoIP_delete(db_handle);

	return 0;
}
