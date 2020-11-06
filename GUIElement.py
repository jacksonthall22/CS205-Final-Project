"""
GUIElement objects represent the metadata of any object that is drawable on the GUI.

GUIElement extends ABC (stands for Abstract Base Class), a built-in Python library for creating abstract
classes. GUIElement is abstract by design so that its children must implement its single `@abstractmethod` 
called `display()`.

==========================
|||     Class Info     |||
==========================

Subclasses
==========
    - Game
    - Board
    - Tile
    - GamePiece

Fields
======
    Constant Class Vars
    -------------------
        TODO

    Regular Class Vars
    ------------------
        TODO

Methods
=======
    Constructor
    -----------
        TODO

    Magic Methods
    -------------
        TODO

    Static Methods
    --------------
        TODO

    Instance Methods
    ----------------
        TODO
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

    def __init__(self, texture_files=None, x_loc=0, y_loc=0, width=0, height=0):
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
            x_width: TODO
            y_width: TODO
        """

        # Make sure params are of correct type
        # TODO This fails because texture_files can be a NoneType
        # assert all((
        #     type(texture_files) in (dict, None),
        #     any((
        #         texture_files is None,
        #         all((is_valid_filename(filename, GUIElement.VALID_IMAGE_FILE_EXTENSIONS) for filename in
        #              texture_files.values()))
        #     )),
        # ))

        self.texture_files = texture_files
        self.x_loc = x_loc
        self.y_loc = y_loc
        self.width = width
        self.height = height

    ''' ========== Magic Methods ========== '''
    
    def __repr__(self):
        """ Create a formal string representation of this GUIElement. """

        r = f'<{self.__class__.__module__}.{self.__class__.__name__} object at {hex(id(self))}'

        # Builds string of names and values of all instance variables set in self
        r += ', vars: {'
        r += ', '.join([f'\'{i}\': {self.__dict__[i]}' for i in self.__dict__.keys()])
        r += '}>'

        return r

    ''' ========== Static Methods ========== '''

    @staticmethod
    def get_top_left_coord(gui_element):
        """ Return the coordinates of the top-right corner of the bounding box of the given GUIElement as a tuple. """

        return gui_element.x_loc, gui_element.y_loc

    @staticmethod
    def get_top_right_coord(gui_element):
        """ Return the coordinates of the top-right corner of the bounding box of the given GUIElement as a tuple. """

        return gui_element.x_loc + gui_element.x_width, gui_element.y_loc

    @staticmethod    
    def get_bottom_right_coord(gui_element):
        """
            Return the coordinates of the bottom-right corner of the bounding box of the given GUIElement as a tuple.
        """

        return gui_element.x_loc + gui_element.x_width, gui_element.y_loc + gui_element.y_width

    @staticmethod
    def get_bottom_left_coord(gui_element):
        """ Return the coordinates of the bottom-left corner of the bounding box of this GUIElement as a tuple. """

        return gui_element.x_loc, gui_element.y_loc + gui_element.y_width

    @staticmethod
    def click_is_inside(gui_element, x_click_loc, y_click_loc):
        """
            Return True iff the (x_click_loc, y_click_loc) pixel coordinate is located inside the bounding box of this
            GUIElement.
        """

        return gui_element.x_loc <= x_click_loc < gui_element.x_loc + gui_element.x_width \
            and gui_element.y_loc <= y_click_loc < gui_element.y_loc + gui_element.y_width

    ''' ========== Instance Methods ========== '''

    @abstractmethod
    def draw(self):
        # This method is abstract - don't implement here, only in subclasses

        # TODO : Can still change parameters ^ if needed (might need to add a parameter for the pygame screen object
        # TODO : on which the object should be drawn (not sure how that works -JH)

        # Important: Whatever changes in the signature here (def display(self))
        # will also need to be updated in signatures of display() in all child
        # classes. Interpreter does not seem to throw warnings if signatures do not
        # match so make sure to keep the same manually
        pass
    
    @abstractmethod
    def handle_click(self, x_click_loc, y_click_loc):
        # This method is abstract - don't implement here, only in subclasses
        pass
