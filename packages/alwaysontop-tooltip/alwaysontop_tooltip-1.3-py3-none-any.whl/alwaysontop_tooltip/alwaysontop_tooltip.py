import tkinter as tk
from tkinter import font

class AlwaysOnTopToolTip:
    """ A tooltip that appears when hovering over a widget, remains on top, and can be styled """
    def __init__(
            self,
            widget: tk.Widget,
            msg: str,
            delay: int = 500,
            bg: str = "#ffffe0",
            font: tuple = ( "Calibri", 10 ),
            wraplength: int = 300,
            borderstyle: str = 'solid',
            borderwidth: int = 1,
            stationary: bool = False,
            blink: dict | None = None ) -> None:
        """ Initialize the tooltip attached to widget

        Args:
            widget - The widget to attach the tooltip to
            message (msg) - The text to display in the tooltip
            delay - Delay in milliseconds before showing the tooltip
            background color (bg) - Background color of the tooltip
            font - Font used for the tooltip text
            wraplength - Maximum width of the tooltip text before wrapping
            borderstyle - Style of the tooltip border (e.g., 'solid', 'flat', 'raised', 'sunken', 'groove', 'ridge')
            borderwidth - Width of the tooltip border
            stationary - If True, the tooltip does not follow the mouse cursor
            blink - Configuration for blinking effect, a dictionary with options:
            - enabled: bool, whether blinking is enabled
            - interval: int, time in milliseconds between blink updates
            - mode: str, 'visibility' or 'opacity' for blinking effect
            - min_alpha: float, minimum opacity for 'opacity' mode
            - max_alpha: float, maximum opacity for 'opacity' mode
            - step: float, change in opacity per blink for 'opacity' mode
            - duration: int, time in milliseconds after which blinking stops
        Raises:
            ValueError: If widget is None or msg is not a non-empty string
        """

        # Initial validation
        if widget is None:
            raise ValueError( "Tooltip requires a valid widget." )

        if not isinstance( msg, str ) or not msg.strip():
            raise ValueError( "Tooltip requires a non-empty message string." )

        self.widget = widget
        self.text = msg
        self.delay = delay
        self.bg = bg
        self.font = font
        self.wraplength = wraplength
        self.borderwidth = borderwidth

        # Blink config
        self.blink_config = blink or {}
        self.blink_enabled = self.blink_config.get( "enabled", False )
        self.blink_interval = self.blink_config.get( "interval", 500 )
        self.blink_mode = self.blink_config.get( "mode", "solid" )
        self.blink_duration = self.blink_config.get( "duration", None )
        self.blink_timeout_job = None

        # Opacity mode settings
        self.min_alpha = self.blink_config.get( "min_alpha", 0.3 )
        self.max_alpha = self.blink_config.get( "max_alpha", 1.0 )
        self.alpha_step = self.blink_config.get( "step", 0.1 )
        self.current_alpha = self.max_alpha
        self.alpha_direction = -1  # fading out

        self.blink_job = None
        self.blink_state = True

        if borderstyle in ( 'solid', 'flat', 'raised', 'sunken', 'groove', 'ridge' ):
            self.relief = borderstyle

            if borderstyle in ( 'groove', 'ridge', 'sunken', 'raised' ) and borderwidth < 3:
                # Use a minimum border width for the style to be visible
                self.borderwidth = 3

        else:
            self.relief = 'solid'

        self.tooltip_window = None
        self.after_id = None

        self.widget.bind( "<Enter>", self.schedule )
        self.widget.bind( "<Leave>", self.hide )
        if not stationary:
            self.widget.bind( "<Motion>", self.move )

    def schedule( self, event = None ) -> None:
        """ Schedule the tooltip to show after a delay

        Args:
            event: What event triggered the function. This is ignored
        """

        self.unschedule()
        self.after_id = self.widget.after( self.delay, self.show )

    def unschedule( self ) -> None:
        """ Cancel the scheduled tooltip display if it exists """

        if self.after_id:
            self.widget.after_cancel( self.after_id )
            self.after_id = None

    def move( self, event ) -> None:
        """ Move the tooltip to follow the mouse cursor
        
        Args:
            event: Event that triggered the function. This is ignored."""

        if self.tooltip_window:
            x, y = event.x_root + 20, event.y_root + 10
            self.tooltip_window.geometry( f"+{ x }+{ y }" )

    def show( self ) -> None:
        """ Show the tooltip at the current mouse position """

        if self.tooltip_window or not self.text:
            return

        x = self.widget.winfo_pointerx() + 20
        y = self.widget.winfo_pointery() + 10

        self.tooltip_window = tk.Toplevel( self.widget )
        self.tooltip_window.wm_overrideredirect( True )
        self.tooltip_window.attributes( "-topmost", True )
        self.tooltip_window.geometry( f"+{ x }+{ y }" )

        label = tk.Label(
            self.tooltip_window,
            text = self.text,
            background = self.bg,
            font = self.font,
            justify = 'left',
            padx = 5,
            pady = 5,
            relief = self.relief,
            borderwidth = self.borderwidth,
            wraplength = self.wraplength,
        )
        label.grid( column = 0, row = 0 )

        self.tooltip_window.grid_columnconfigure( index = 0 )
        self.tooltip_window.grid_rowconfigure( index = 0 )

        if self.blink_enabled:
            self.start_blink()

    def start_blink( self ) -> None:
        """ Start the blinking effect for the tooltip """

        if not self.tooltip_window:
            return

        # Blinking behavior: either visibility toggle or opacity fade
        if self.blink_mode == "visibility":
            self.blink_state = not self.blink_state

            if self.blink_state:
                self.tooltip_window.deiconify()

            else:
                self.tooltip_window.withdraw()

        elif self.blink_mode == "opacity":
            self.current_alpha += self.alpha_step * self.alpha_direction

            if self.current_alpha <= self.min_alpha:
                self.current_alpha = self.min_alpha
                self.alpha_direction = 1

            elif self.current_alpha >= self.max_alpha:
                self.current_alpha = self.max_alpha
                self.alpha_direction = -1

            self.tooltip_window.attributes( "-alpha", self.current_alpha )

        # Reschedule blink
        self.blink_job = self.tooltip_window.after( self.blink_interval, self.start_blink )

        # Start the timer to stop blinking after a fixed duration
        if self.blink_duration and not self.blink_timeout_job:
            self.blink_timeout_job = self.tooltip_window.after(
                self.blink_duration, self.stop_blink
            )

    def stop_blink( self ) -> None:
        """ Cancel the repeated blinking """

        if self.blink_job and self.tooltip_window:
            self.tooltip_window.after_cancel( self.blink_job )
            self.blink_job = None

        # Cancel the timeout that would stop blinking
        if self.blink_timeout_job and self.tooltip_window:
            self.tooltip_window.after_cancel( self.blink_timeout_job )
            self.blink_timeout_job = None

        # Reset state based on mode
        if self.tooltip_window:
            if self.blink_mode == "visibility":
                self.tooltip_window.deiconify()
            elif self.blink_mode == "opacity":
                self.tooltip_window.attributes( "-alpha", self.max_alpha )

    def hide( self, event = None ) -> None:
        """ Hide the tooltip and clean up

        Args:
            event: Event that triggered the function. This is ignored
        """

        self.unschedule()
        self.stop_blink()
        if self.tooltip_window:
            self.tooltip_window.destroy()
            self.tooltip_window = None

    def config( self,
               new_text: str = None,
               new_bg: str = None,
               new_font: tuple[ str, int ] = None,
               new_relief: str = None,
               new_borderwidth: int = None,
               new_wraplength: int = None
               ) -> None:
        """ Reconfigure tooltip

        Args:
            new_text (str): The new text in the tooltip
            new_bg (str): Color for the background
            new_font (tuble(str, int)): The font used for the text, (<fontname>, <fontsize>)
            new_relief (str): Borderstyle, must be one of 'solid', 'flat', 'raised', 'sunken', 'groove', 'ridge'
            new_borderwidth (int): New width of border
            new_wraplength (int): New character wraplength, this is the maximum length of text before it gets wraped to a new line
        """

        if new_text == None or len( new_text ) == 0:
            new_text = self.text
        self.text = new_text

        if new_bg != None:
            self.bg = self._normalize_color( new_bg )

        if new_font != None:
            self.font = self._normalize_font( new_font )

        if new_relief != None:
            self.relief, self.borderwidth = self._normalize_relief( new_relief, new_borderwidth if new_borderwidth else self.borderwidth )

        if new_borderwidth != None:
            self.borderwidth = self._normalize_borderwidth( new_borderwidth, new_relief if new_relief else self.relief )

        if new_wraplength == None or new_wraplength <= 0:
            self.wraplength = self.wraplength

    def _is_valid_color( self, color: str) -> bool:
        """ Check if the given color is valid

        Args:
            color (str): Color string to verify

        Returns:
            bool: If the color string is valid
        """

        try:
            self.root.winfo_rgb( color )
            return True

        except tk.TclError:
            return False

    def _normalize_borderwidth( self, borderwidth: int, relief: str ) -> int:
        """ Verify that the borderwidth is correct

        Args:
            borderwidth (int): Width of the border
            relief (string): Relief (borderstyle) to verify if the borderwidth is possible

        Returns:
            borderwidth (int): The entered borderwidth, or 3 if entered borderwidth does not match for relief
        """

        if not isinstance( borderwidth, int ) or borderwidth < 0:
            borderwidth = self.borderwidth
        elif relief in ( 'groove', 'ridge', 'sunken', 'raised' ) and borderwidth < 3:
            # Use a minimum border width for the style to be visible
            borderwidth = 3

        return borderwidth

    def _normalize_color( self, color: str | tuple ) -> str:
        """ Verify color string or transform to color string
        Can be string or tuple, if it is a StringVar, string will first be extracted
        If value is invalid, current color will remain

        Args:
            color (str | tuple): The color to verify

        Returns:
            color (str): a normalized string, representing a color
        """

        default = self.bg
        if isinstance( color, tk.StringVar ):
            color = color.get()

        if isinstance( color, str ):
            if self._is_valid_color( color ):
                pass
            else:
                color = default

        elif isinstance( color, tuple ) and len( color ) == 3 and all( isinstance( c, int ) and c >= 0 and c <= 255 for c in color ):
            color = f'#{ color[ 0 ]:02x }{ color[ 1 ]:02x }{ color[ 2 ]:02x }'

        else:
            color = default

        return color

    def _verify_font_name( self, name:str ) -> bool:
        """ Verify that the given name exists and can be used
        
        Args:
            name (str): Name to verify
            
        Returns:
            bool: True if name exists
        """
        
        return name in font.families()

    def _normalize_font( self, font: str | tuple ) -> tuple:
        """ Verify font

        Args:
            font (str | tuple): The font specification i.e. 'Arial, 12, normal' or ('Arial', 12, 'normal')

        Returns:
            font (tuple): A tuple representing a font """

        current = self.font

        if isinstance( font, str ):
            try:
                temptup =  tuple( font.split( ',' ) )
                if len( temptup ) < 3:
                    font = current

                else:
                    font = temptup[0].strip() if self._verify_font_name( temptup[0].strip() ) else 'Arial'
                    size = int( temptup[1].strip() ) if int( temptup[1].strip() ) > 0 else 18
                    style = temptup[2].strip() if temptup[2].strip() in ( 'normal', 'bold', 'italic' ) else 'normal'
                    font = ( font, size, style )

            except:
                font = ( 'Calibri', 18, 'normal' )

        elif isinstance( font, tuple ):
            if not self._verify_font_name( font[ 0 ] ):
                font[ 0 ] = 'Arial'

            if font[ 1 ] < 1:
                font[ 1 ] = 18

            if not font[ 2 ] in ( 'normal', 'bold', 'italic' ):
                font[ 2 ] = 'normal'

        return font

    def _normalize_relief( self, new_relief: str, new_borderwidth: int ) -> tuple[ str, int ]:
        """ Verify that relief (style) exists
        
        Args:
            new_relief (str): Given relief to test
            new_borderwidth (int): Given borderwidth, if it is too small for the relief, 3 will be used
            """

        if new_relief in ( 'solid', 'flat', 'raised', 'sunken', 'groove', 'ridge' ):
            if new_relief in ( 'groove', 'ridge', 'sunken', 'raised' ) and new_borderwidth < 3:
                # Use a minimum border width for the style to be visible
                new_borderwidth = 3
        else:
            new_relief = self.relief

        return new_relief, new_borderwidth

