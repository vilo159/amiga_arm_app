from connections import *

def gps_test():
    print("\n **********Beginning GPS Test********** \n")



    # Initialize the GPS module by changing what data it sends and at what rate.
    # These are NMEA extensions for PMTK_314_SET_NMEA_OUTPUT and
    # PMTK_220_SET_NMEA_UPDATERATE but you can send anything from here to adjust
    # the GPS module behavior:
    #   https://cdn-shop.adafruit.com/datasheets/PMTK_A11.pdf

    # Turn on the basic GGA and RMC info (what you typically want)
    # gps.send_command(b'PMTK314,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0')
    # Turn on just minimum info (RMC only, location):
    #gps.send_command(b'PMTK314,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0')
    # Turn off everything:
    #gps.send_command(b'PMTK314,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0')
    # Tuen on everything (not all of it is parsed!)
    #gps.send_command(b'PMTK314,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0')

    # Set update rate to once a second (1hz) which is what you typically want.
    # gps.send_command(b'PMTK220,1000')
    # Or decrease to once every two seconds by doubling the millisecond value.
    # Be sure to also increase your UART timeout above!
    #gps.send_command(b'PMTK220,2000')
    # You can also speed up the rate, but don't go too fast or else you can lose
    # data during parsing.  This would be twice a second (2hz, 500ms delay):
    #gps.send_command(b'PMTK220,500')

    # Main loop runs forever printing the location, etc. every second.
    last_print = time.monotonic()
    cnt = 0
    while cnt < 10:
        cnt = cnt + 1
        # Make sure to call gps.update() every loop iteration and at least twice
        # as fast as data comes from the GPS unit (usually every second).
        # This returns a bool that's true if it parsed new data (you can ignore it
        # though if you don't care and instead look at the has_fix property).
        gps.update()
        # Every second print out current location details if there's a fix.
        current = time.monotonic()
        if current - last_print >= 1.0:
            last_print = current
            if not gps.has_fix:
                # Try again if we don't have a fix yet.
                print('Waiting for fix...')
                print('cnt: ', cnt)
                continue
            # We have a fix! (gps.has_fix is true)
            # Print out details about the fix like location, date, etc.
            print('=' * 40)  # Print a separator line.
            print('Fix timestamp: {}/{}/{} {:02}:{:02}:{:02}'.format(
                gps.timestamp_utc.tm_mon,   # Grab parts of the time from the
                gps.timestamp_utc.tm_mday,  # struct_time object that holds
                gps.timestamp_utc.tm_year,  # the fix time.  Note you might
                gps.timestamp_utc.tm_hour,  # not get all data like year, day,
                gps.timestamp_utc.tm_min,   # month!
                gps.timestamp_utc.tm_sec))
            print('Latitude: {0:.6f} degrees'.format(gps.latitude))
            print('Longitude: {0:.6f} degrees'.format(gps.longitude))
            print('Fix quality: {}'.format(gps.fix_quality))
            # Some attributes beyond latitude, longitude and timestamp are optional
            # and might not be present.  Check if they're None before trying to use!
            if gps.satellites is not None:
                print('# satellites: {}'.format(gps.satellites))
            if gps.altitude_m is not None:
                print('Altitude: {} meters'.format(gps.altitude_m))
            if gps.speed_knots is not None:
                print('Speed: {} knots'.format(gps.speed_knots))
            if gps.track_angle_deg is not None:
                print('Track angle: {} degrees'.format(gps.track_angle_deg))
            if gps.horizontal_dilution is not None:
                print('Horizontal dilution: {}'.format(gps.horizontal_dilution))
            if gps.height_geoid is not None:
                print('Height geo ID: {} meters'.format(gps.height_geoid))

            # print('{0:.6f}, {1:.6f}, sample_{2:d}, #FF0000'.format(gps.latitude, gps.longitude, cnt))
            # print('{0:.6f}, {1:.6f}'.format(gps.latitude, gps.longitude))
    print("\n **********Ending GPS Test********** \n")


if __name__ == "__main__":
    gps_test()
