#AzimuthConverterFinal.py
#Steven Wagner 02/07/2025
#
#Takes any magnetic declination rounded to
#nearest degree, takes any azimuth and converts
#from magnetic to grid or grid to magnetic and
#returns a bearing between 0-360⁰


def convert_azimuth(azimuth, declination, direction, conversion_type):
    """
    Convert azimuth between Magnetic and Grid North based on declination.
    """
    if direction.lower() == "west":
        if conversion_type == 1:  # Magnetic to Grid
            return azimuth + declination
        elif conversion_type == 2:  # Grid to Magnetic
            return azimuth - declination
    elif direction.lower() == "east":
        if conversion_type == 1:  # Magnetic to Grid
            return azimuth - declination
        elif conversion_type == 2:  # Grid to Magnetic
            return azimuth + declination
    return None  # Invalid input handling

while True:
    try:
        # Get magnetic declination
        declination_input = input("Enter magnetic declination in decimal format (e.g., 7 West or 5 East): ").strip()
        if declination_input.lower() == "q":
            break
        
        # Parse declination
        parts = declination_input.split()
        if len(parts) != 2 or not parts[0].replace('.', '', 1).isdigit() or parts[1].lower() not in ["east", "west"]:
            print("Invalid declination format. Please enter in the format '7 West' or '5 East'.")
            continue
        
        declination = float(parts[0])
        direction = parts[1]

        while True:  # Loop for multiple azimuth calculations with the same declination
            # Get azimuth
            azimuth_input = input("Enter azimuth between 0 and 360 (or press 'q' to quit): ").strip()
            if azimuth_input.lower() == "q":
                break

            if not azimuth_input.replace('.', '', 1).isdigit():
                print("Invalid azimuth. Please enter a numeric value between 0 - 360.")
                continue
            
            azimuth = float(azimuth_input)

            # Get conversion type
            conversion_input = input("Convert (1) Magnetic to Grid or (2) Grid to Magnetic? Enter 1 or 2 (or 'q' to quit): ").strip()
            if conversion_input.lower() == "q":
                break

            if conversion_input not in ["1", "2"]:
                print("Invalid choice. Enter 1 for Magnetic to Grid or 2 for Grid to Magnetic.")
                continue
            
            conversion_type = int(conversion_input)

            # Perform conversion 
            result = convert_azimuth(azimuth, declination, direction, conversion_type)
            
            # Ensures azimuth returned is not a negative number
            while result < 0:
                result+=360 
           
            # Ensures azimuth returned is not greater than 360 degrees
            while result > 360:
                result -= 360  
            if result is not None:
                conversion_text = "Magnetic to Grid" if conversion_type == 1 else "Grid to Magnetic"
                print(f"Converted azimuth ({conversion_text}): {result:.2f}°\n")
            else:
                print("Error in conversion. Please check inputs.\n")

        # Ask if the user wants to enter a new declination or quit
        restart = input("Enter a new declination? (y/n): ").strip().lower()
        if restart != "y":
            break

    except Exception as e:
        print(f"An error occurred: {e}. Please try again.")

print("Program exited.")
