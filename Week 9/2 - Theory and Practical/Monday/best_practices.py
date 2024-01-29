"""
Descriptive Function Names:
Instead of foo() or bar(), let's name our functions 
so that anyone reading our code knows exactly what's going on.
"""

"""Single Responsibility Principle: 
One function, one responsibility. Break down your code into smaller, 
focused functions.
"""

"""Default Argument Values:
Be careful with default values. They're handy but watch out for mutable defaults.
"""

"""
Avoiding Global Variables:
Global variables can be tricky. Stick to local scope and keep your functions pure.
"""


# Input Validation & Sanity Checks ;)
"""
Input Sanity Checks: 
Input validation is like checking your ingredients before cooking. 
Ensure your functions get what they expect.
"""


"""
Exception Handling:
Expect the unexpected. Wrap your code in try-except blocks
and provide meaningful error messages.
"""


"""
Logging: 
Logging is your friend. Add informative logs to aid debugging.
"""
import logging

logging.basicConfig(filename="newfile.log")

logger = logging.getLogger()

logger.setLevel(logging.INFO)

logger.debug("Harmless debug Message")
logger.info("Just an information")
logger.warning("Its a Warning")
logger.error("Did you try to divide by zero")
logger.critical("Internet is down")