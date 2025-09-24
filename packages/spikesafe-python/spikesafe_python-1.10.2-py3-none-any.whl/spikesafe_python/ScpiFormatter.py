class ScpiFormatter():
    """
    Class for formatting SCPI command arguments.
    
    ...
    
    Methods
    -------
    ScpiFormatter.get_scpi_format_integer_for_bool(bool_value)
        Return the SCPI formatted value for a boolean value as an integer (1 for True, 0 for False).
    ScpiFormatter.get_scpi_format_on_state_for_bool(bool_value)
        Return the SCPI formatted value for a boolean value as a string ('ON' for True
    """

    @staticmethod
    def get_scpi_format_integer_for_bool(bool_value):
        """Return the SCPI formatted value for a boolean value.

        Returns
        -------
        int
            1 for True, 0 for False.
        """
        if bool_value:
            return 1
        else:
            return 0
        
    @staticmethod
    def get_scpi_format_on_state_for_bool(bool_value):
            """Return the SCPI formatted value for a boolean value. 

            Returns
            -------
            string
                'ON' for True, 'OFF' for False.
            """
            if bool_value:
                return 'ON'
            else:
                return 'OFF'
            
def get_scpi_format_integer_for_bool(bool_value):
     """
     Obsolete: Use ScpiFormatter.get_scpi_format_integer_for_bool(bool_value) instead.
     """
     return ScpiFormatter.get_scpi_format_integer_for_bool(bool_value)
     
def get_scpi_format_on_state_for_bool(bool_value):
     """
     Obsolete: Use ScpiFormatter.get_scpi_format_on_state_for_bool(bool_value) instead.
     """
     return ScpiFormatter.get_scpi_format_on_state_for_bool(bool_value)