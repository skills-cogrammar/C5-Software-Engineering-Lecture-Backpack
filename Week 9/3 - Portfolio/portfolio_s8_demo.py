
# Import libraries
from tabulate import tabulate   # pip install tabulate if not defined

# Declare functions
def init_system():
    """
    Initialize the backend system.
    """
    pass


# Print Dashboard
def print_dashboard(speed, indicators, analytic):
    """
    Display Dashboard.

    Parameters:
    - speed (int): Travelling speed.
	- indicators (lst): Left & Right indicator status.
	- analytic (lst): Analytic title and value.
	
    Returns:
    None
    """
    headers = ["LI", "Speed", analytic[0], "RI"]
    table = [[indicators[0], speed, analytic[1], indicators[1]]]
    table = tabulate(table, headers = headers, tablefmt = "grid", 
                     numalign = "center", stralign = "center")
    
    print("\n************ DASHBOARD ************\n")
    print(table)


# ==============  Navigation Functions  ==============
def navigate_to_destination(destination):
    """
    Navigate to a specified destination.

    Parameters:
    - destination (str): The destination to navigate to.

    Returns:
    None
    """
    # Code for navigating to a specified destination
    print(f"-- you have arrived at {destination} --")


def search_nearby_places(keyword):
    """
    Search for nearby places based on a keyword.

    Parameters:
    - keyword (str): The keyword for the search.

    Returns:
    None
    """
    # Code for searching nearby places based on a keyword
    pass


# ============== Media Functions ==============
def play_music(song):
    """
    Play a specific song.

    Parameters:
    - song (str): The title of the song to play.

    Returns:
    None
    """
    # Code for playing a specific song
    print(f"-- play - {song} --")


def show_playlist():
    """
    Display the current playlist.

    Returns:
    None
    """
    # Code for displaying the current playlist
    pass


def play_podcast(podcast):
    """
    Play a specific podcast.

    Parameters:
    - podcast (str): The title of the podcast to play.

    Returns:
    None
    """
    # Code for playing a specific podcast
    pass


# ============== Connectivity Functions  ==============
def connect_bluetooth(device):
    """
    Connect to a Bluetooth device.

    Parameters:
    - device (str): The name of the Bluetooth device to connect to.

    Returns:
    None
    """
    # Code for connecting to a Bluetooth device
    print(f"-- bluetooth connected to {device} --")


def pair_device(device):
    """
    Pair a new device.

    Parameters:
    - device (str): The name of the device to pair.

    Returns:
    None
    """
    # Code for pairing a new device
    pass


# ============== Vehicle Status Functions ==============
def check_fuel_level():
    """
    Check the fuel level.

    Returns:
    None
    """
    # Code for checking the fuel level
    pass


def check_engine_status():
    """
    Check the engine status.

    Returns:
    None
    """
    # Code for checking the engine status
    pass


# ============== Settings Functions  ==============
def adjust_volume(level):
    """
    Adjust the volume.

    Parameters:
    - level (int): The volume level (0 to 10).

    Returns:
    None
    """
    # Code for adjusting the volume
    print(f"-- volume adjusted to {level} --")


def set_display_brightness(level):
    """
    Set the display brightness.

    Parameters:
    - level (int): The brightness level (0 to 10).

    Returns:
    None
    """
    # Code for setting the display brightness
    pass


def customize_theme(theme):
    """
    Customize the dashboard theme.

    Parameters:
    - theme (str): The theme to apply.

    Returns:
    None
    """
    # Code for customizing the dashboard theme
    pass


# ============== Example Usage  ==============
print_dashboard(50, ["Off", "Off"], ["Range", 100])

print()

play_music("Always Look on the Bright Side of Life")
adjust_volume(7)
navigate_to_destination("Office")
connect_bluetooth("Smartphone")

