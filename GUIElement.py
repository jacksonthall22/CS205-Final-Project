"""
GUIElement objects represent the metadata of any object that is drawable on the GUI.

GUIElement extends ABC (stands for Abstract Base Class), a built-in Python library for creating abstract
classes. GUIElement is abstract by design so that its children must implement its single `@abstractmethod` 
called `display()`.

Subclasses of GUIElement 
------------------------
    Edit as needed if more get added    
    - Game
    - Board
    - Tile
    - GamePiece

"""

from abc import ABC, abstractmethod  # Builtin Python lib to declare abstract classes
from utility import is_valid_filename


class GUIElement(ABC):
    """
        GUIElement is an abstract class used to represent any object that is drawable in the GUI. All drawable objects
        extend GUIElement.
    """

    ''' ========== Constant Class Variables ========== '''

    # Textures of any GUIElement should have one of these extensions (case sensitive) - add as needed
    VALID_IMAGE_FILE_EXTENSIONS = ('png', 'jpg', 'jpeg', 'gif')

    ''' ========== Regular Class Variables ========== '''

    ''' ========== Constructor ========== '''

    def __init__(self, texture_files=None, x_loc=0, y_loc=0):
        """
            texture_files : Dictionary containing any image texture filenames related to the object. Keys in the dict
                            should be short, unique, and descriptive snake_case strings that describe the image or what
                            it's used for. The values should be the filename (actually the full filepath relative to 
                            main.py). For example, it might look like this for a GamePiece object:

                                texture_files = {
                                    'white_side': 'white-side-texture.png',
                                    'black_side': 'black-side-texture.png',
                                    'flip_to_black': 'flip-white-to-black-animation.gif',
                                    'flip_to_white': 'flip-black-to-white-animation.gif'
                                }
            x_loc : X-location coordinate of top-left corner of the bounding box of this GUIElement on the screen (units
                    = pixels). Defaults to 0 (traditionally x=0 is left).
            y_loc : Y-location coordinate of top-left corner of the bounding box of this GUIElement on the screen (units
                    = pixels). Defaults to 0 (traditionally y=0 is top).
        """

        # Make sure params are of correct type
        assert all([
            type(texture_files) in (dict, None),
            all([is_valid_filename(filename, GUIElement.VALID_IMAGE_FILE_EXTENSIONS) for filename in
                 texture_files.values()]),
        ])

        self.texture_files = texture_files
        self.x_loc = x_loc
        self.y_loc = y_loc

    ''' ========== Magic Methods ========== '''
    
    def __repr__(self):
        """ Create a formal string representation of this GUIElement. """

        r = f'<{self.__class__.__module__}.{self.__class__.__name__} object at {hex(id(self))}'

        # Builds string of names and values of all instance variables set in self
        r += ', vars: '
        if self.__dict__:
            r += ', '.join([f'(\'{i}\': {self.__dict__[i]})' for i in self.__dict__.keys()])
        else:
            r += '<no instance variables set>'
        r += '>'

        return r

    ''' ========== Static Methods ========== '''

    ''' ========== Instance Methods ========== '''

    @abstractmethod
    def draw(self):
        # This method is abstract - don't implement here, only in subclasses

        # TODO Can still change parameters ^ based on what makes sense (might
        # need to add things like x_screen_location, y_screen_location, etc. to
        # display object at specific location, up to the GUI team).

        # Important: Whatever changes in the signature here (def display(self))
        # will also need to be updated in signatures of display() in all child
        # classes. Interpreter does not seem to throw warnings if signatures do not
        # match so make sure to keep the same manually
        pass
