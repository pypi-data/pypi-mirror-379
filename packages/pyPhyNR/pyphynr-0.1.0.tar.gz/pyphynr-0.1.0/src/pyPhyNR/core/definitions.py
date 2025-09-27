"""
5G NR definitions and constants
"""

# Resource Block (RB) definitions
N_SC_PER_RB = 12  # Number of subcarriers per RB

# OFDM and CP parameters from 3GPP TS 38.211
BASE_SCS = 15_000  # 15 kHz base subcarrier spacing
BASE_FFT = 4096    # Base FFT size
TC_SCALE = 32      # Tc = 1/(Δf_ref * N_f_ref) where Δf_ref = 15kHz * 32
K_SCALE = 64       # k = tc * 64 (scaling factor)

# Normal CP lengths from 3GPP (ratio to FFT size):
# - First symbol: 160/2048 ≈ 7.81%
# - Other symbols: 144/2048 ≈ 7.03%
CP_RATIO_FIRST = 160/2048  # First symbol in slot
CP_RATIO_OTHER = 144/2048  # Other symbols

# Maximum carrier configurations
MAX_PRB_FR1 = 273  # Maximum PRBs in FR1 (100 MHz at 15kHz SCS)
MAX_PRB_FR2_1 = 264  # Maximum PRBs in FR2-1 (400 MHz at 120kHz SCS)
MAX_PRB_FR2_2 = 1320  # Maximum PRBs in FR2-2 (2000 MHz at 120kHz SCS)

# Maximum DMRS REs per symbol
MAX_DMRS_RE = 3276 // 2  # 1638 REs

# Slot and frame definitions
N_SYMBOLS_PER_SLOT = 14  # Number of OFDM symbols per slot
N_SLOTS_PER_FRAME = 20   # Number of slots per 10ms frame

# Subcarrier spacing definitions (kHz)
SCS_15 = 15
SCS_30 = 30
SCS_60 = 60
SCS_120 = 120
SCS_240 = 240

# Bandwidth definitions (MHz)
BW_5 = 5
BW_10 = 10
BW_15 = 15
BW_20 = 20
BW_25 = 25
BW_30 = 30
BW_40 = 40
BW_50 = 50
BW_60 = 60
BW_80 = 80
BW_100 = 100

# Frequency Range definitions (in Hz)
FR1_FREQ_RANGE = (410e6, 7125e6)  # 410 MHz - 7.125 GHz
FR2_1_FREQ_RANGE = (24.25e9, 52.6e9)  # 24.25 GHz - 52.6 GHz
FR2_2_FREQ_RANGE = (52.6e9, 114.25e9)  # 52.6 GHz - 114.25 GHz

# Resource block configuration for each channel bandwidth and numerology (μ)
# Format: (bandwidth_mhz, numerology): rb_count
RB_TABLE = {
    # FR1 configurations
    (5, 0): 25,
    (5, 1): 11,
    (10, 0): 52,
    (10, 1): 24,
    (10, 2): 11,
    (15, 0): 79,
    (15, 1): 38,
    (15, 2): 18,
    (20, 0): 106,
    (20, 1): 51,
    (20, 2): 24,
    (25, 0): 133,
    (25, 1): 65,
    (25, 2): 31,
    (30, 0): 160,
    (30, 1): 78,
    (30, 2): 38,
    (40, 0): 216,
    (40, 1): 106,
    (40, 2): 51,
    (50, 0): 270,
    (50, 1): 133,
    (50, 2): 65,
    (60, 0): 324,
    (60, 1): 162,
    (60, 2): 79,
    (70, 0): 378,
    (70, 1): 189,
    (70, 2): 93,
    (80, 0): 432,
    (80, 1): 217,
    (80, 2): 107,
    (90, 0): 486,
    (90, 1): 245,
    (90, 2): 121,
    (100, 0): 540,
    (100, 1): 273,
    (100, 2): 135,
    
    # FR2-1 configurations (μ = 2,3)
    (50, 2): 66,
    (50, 3): 32,
    (100, 2): 132,
    (100, 3): 66,
    (200, 2): 264,
    (200, 3): 132,
    (400, 2): 528,
    (400, 3): 264,
    
    # FR2-2 configurations (μ = 3,4)
    (400, 3): 264,
    (400, 4): 132,
    (800, 3): 528,
    (800, 4): 264,
    (1600, 3): 1056,
    (1600, 4): 528,
    (2000, 3): 1320,
    (2000, 4): 660
}

def get_rb_count(bandwidth_mhz: float, numerology: int) -> int:
    """
    Get number of resource blocks for given bandwidth and numerology
    
    Args:
        bandwidth_mhz: Channel bandwidth in MHz (can be float for custom bandwidths)
        numerology: μ value (0-4)
        
    Returns:
        Number of resource blocks
        
    Raises:
        ValueError: If combination of bandwidth and numerology is not valid
    """
    # First try exact match in RB_TABLE
    key = (int(bandwidth_mhz), numerology)
    if key in RB_TABLE:
        return RB_TABLE[key]
    
    # For custom bandwidths, calculate RBs based on subcarrier spacing
    scs_hz = 15e3 * (2 ** numerology)  # Subcarrier spacing in Hz
    total_subcarriers = bandwidth_mhz * 1e6 / scs_hz
    n_rb = int(total_subcarriers / 12)  # 12 subcarriers per RB
    
    # Validate the calculated RB count is reasonable
    if n_rb < 1 or n_rb > 1000:
        raise ValueError(
            f"Calculated RB count ({n_rb}) for bandwidth ({bandwidth_mhz} MHz) "
            f"and numerology (μ={numerology}) is out of reasonable range"
        )
    
    return n_rb

def get_frequency_range(frequency_hz: float) -> str:
    """
    Determine the frequency range (FR1, FR2-1, or FR2-2) for a given frequency
    
    Args:
        frequency_hz: Frequency in Hz
        
    Returns:
        String indicating frequency range ('FR1', 'FR2-1', or 'FR2-2')
        
    Raises:
        ValueError: If frequency is outside defined ranges
    """
    if FR1_FREQ_RANGE[0] <= frequency_hz <= FR1_FREQ_RANGE[1]:
        return 'FR1'
    elif FR2_1_FREQ_RANGE[0] <= frequency_hz <= FR2_1_FREQ_RANGE[1]:
        return 'FR2-1'
    elif FR2_2_FREQ_RANGE[0] <= frequency_hz <= FR2_2_FREQ_RANGE[1]:
        return 'FR2-2'
    else:
        raise ValueError(f"Frequency {frequency_hz/1e6:.2f} MHz is outside defined ranges") 