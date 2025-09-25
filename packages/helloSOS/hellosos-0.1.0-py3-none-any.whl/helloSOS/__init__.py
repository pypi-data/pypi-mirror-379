# # final__init__.py content will go here

# # Import ALL executable functions
# from .exact_prac1 import prac1, neural_network_visualization
# from .exact_prac3 import prac3, iris_classification
# from .exact_prac4 import prac4, titanic_survival_prediction
# from .exact_prac5 import prac5, mnist_cnn_classification
# from .exact_prac7 import prac7, banknote_authentication
# from .exact_prac8 import prac8, mnist_denoising_autoencoder

# # Import all your exact code strings for books/documentation
# from .exact_code_strings import (
#     PRAC1_CODE,
#     PRAC3_CODE, 
#     PRAC4_CODE,
#     PRAC5_CODE,
#     PRAC7_CODE,
#     PRAC8_CODE,
#     get_code,
#     get_all_codes,
#     save_code_to_file,
#     print_code,
#     execute_code
# )

# __version__ = "0.1.0"
# __author__ = "kiras"

# __all__ = [
#     # ALL Executable functions
#     "prac1",
#     "prac3",
#     "prac4",
#     "prac5", 
#     "prac7",
#     "prac8",
    
#     # Aliases for backward compatibility
#     "neural_network_visualization",     # alias for prac1
#     "iris_classification",             # alias for prac3
#     "titanic_survival_prediction",     # alias for prac4
#     "mnist_cnn_classification",        # alias for prac5
#     "banknote_authentication",         # alias for prac7
#     "mnist_denoising_autoencoder",     # alias for prac8
    
#     # Code strings for documentation/books
#     "PRAC1_CODE",
#     "PRAC3_CODE",
#     "PRAC4_CODE", 
#     "PRAC5_CODE",
#     "PRAC7_CODE",
#     "PRAC8_CODE",
#     "get_code",
#     "get_all_codes",
#     "save_code_to_file",
#     "print_code",
#     "execute_code"
# ]









































# Import ML/DL executable functions
from .exact_prac1 import prac1, neural_network_visualization
from .exact_prac3 import prac3, iris_classification
from .exact_prac4 import prac4, titanic_survival_prediction
from .exact_prac5 import prac5, mnist_cnn_classification
from .exact_prac7 import prac7, banknote_authentication
from .exact_prac8 import prac8, mnist_denoising_autoencoder

# Import all ML/DL code strings for books/documentation
from .exact_code_strings import (
    PRAC1_CODE,
    PRAC3_CODE, 
    PRAC4_CODE,
    PRAC5_CODE,
    PRAC7_CODE,
    PRAC8_CODE,
    get_code,
    get_all_codes,
    save_code_to_file,
    print_code,
    execute_code
)

# Import RPA code strings for UiPath workflows
from .rpa_code_strings import (
    RPA_PRAC1_CODE,
    RPA_PRAC2_CODE,
    RPA_PRAC3_CODE,
    RPA_PRAC4_CODE,
    RPA_PRAC5_CODE,
    RPA_PRAC6_CODE,
    get_rpa_code,
    get_all_rpa_codes,
    print_rpa_code
)

__version__ = "0.2.0"  # Updated version for RPA addition
__author__ = "Manny"

__all__ = [
    # ML/DL Executable functions
    "prac1", "prac3", "prac4", "prac5", "prac7", "prac8",
    
    # ML/DL Aliases for backward compatibility
    "neural_network_visualization",
    "iris_classification",
    "titanic_survival_prediction",
    "mnist_cnn_classification",
    "banknote_authentication",
    "mnist_denoising_autoencoder",
    
    # ML/DL Code strings for documentation/books
    "PRAC1_CODE", "PRAC3_CODE", "PRAC4_CODE", 
    "PRAC5_CODE", "PRAC7_CODE", "PRAC8_CODE",
    "get_code", "get_all_codes", "save_code_to_file",
    "print_code", "execute_code",
    
    # RPA Code strings for UiPath workflows
    "RPA_PRAC1_CODE", "RPA_PRAC2_CODE", "RPA_PRAC3_CODE",
    "RPA_PRAC4_CODE", "RPA_PRAC5_CODE", "RPA_PRAC6_CODE",
    "get_rpa_code", "get_all_rpa_codes", "print_rpa_code"
]