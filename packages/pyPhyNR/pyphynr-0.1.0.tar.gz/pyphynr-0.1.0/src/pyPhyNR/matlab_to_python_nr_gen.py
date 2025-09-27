"""
Python translation of genNR.m MATLAB script
Generates 5G NR 20MHz signal with PDSCH and DMRS

Original MATLAB: genNR(1).m
Translated to Python with numpy and scipy

Key parameters:
- 51 PRBs (20MHz)
- 280 symbols (20 slots)
- 64QAM modulation
- DMRS in symbols 2 and 11
- Cell ID 123
"""

import numpy as np
import scipy.io

def save_vsa_recording(fileName, data, sampleFreq, centerFreq=0):
    """
    Save VSA recording in a .mat file compatible with 89600 software.
    Simplified version from Neptune's signals.py
    """
    halfSpan = sampleFreq / 1.28 / 2
    InputCenter = centerFreq
    FreqValidMax = halfSpan + InputCenter
    FreqValidMin = -halfSpan + InputCenter
    InputRange = 1
    InputRefImped = 50
    InputZoom = np.uint8(1)
    XDelta = 1 / sampleFreq
    XDomain = np.int16(2)
    XStart = 0
    XUnit = 'Sec'
    YUnit = 'V'
    Y = np.complex64(data)

    # Save variables to a .mat file
    scipy.io.savemat(fileName, {
        'FreqValidMax': FreqValidMax,
        'FreqValidMin': FreqValidMin,
        'InputCenter': InputCenter,
        'InputRange': InputRange,
        'InputRefImped': InputRefImped,
        'InputZoom': InputZoom,
        'XDelta': XDelta,
        'XDomain': XDomain,
        'XUnit': XUnit,
        'XStart': XStart,
        'YUnit': YUnit,
        'Y': Y
    })

def f_randbtw(N, lo, hi, seed=None):
    """Generate N random numbers between lo and hi"""
    if seed is not None and seed > 0:
        np.random.seed(seed)
    return lo + (hi - lo) * np.random.rand(N)

def f_modulationmapper(x, modscheme):
    """
    Modulation mapper according to 3GPP TS 38.211
    Translates from MATLAB bitget logic to Python
    """
    x = np.round(np.abs(x)).astype(int)
    m = np.zeros(len(x), dtype=complex)
    
    for ii, val in enumerate(x):
        if 'QP' in modscheme.upper():  # QPSK
            # MATLAB: bitget(x,1) = LSB, bitget(x,2) = next bit
            b1 = (val >> 1) & 1  # Second bit (MATLAB bitget(x,2))
            b0 = val & 1         # First bit (MATLAB bitget(x,1))
            m[ii] = (1/np.sqrt(2)) * (
                (1 - 2*b1) + 1j*(1 - 2*b0)
            )
            
        elif '16' in modscheme:  # 16QAM
            b1 = val & 1
            b2 = (val >> 1) & 1
            b3 = (val >> 2) & 1
            b4 = (val >> 3) & 1
            m[ii] = (1/np.sqrt(10)) * (
                (1 - 2*b1) * (2 - (1 - 2*b3)) +
                1j * (1 - 2*b2) * (2 - (1 - 2*b4))
            )
            
        elif '64' in modscheme:  # 64QAM
            b1 = val & 1
            b2 = (val >> 1) & 1
            b3 = (val >> 2) & 1
            b4 = (val >> 3) & 1
            b5 = (val >> 4) & 1
            b6 = (val >> 5) & 1
            m[ii] = (1/np.sqrt(42)) * (
                (1 - 2*b1) * (4 - (1 - 2*b3) * (2 - (1 - 2*b5))) +
                1j * (1 - 2*b2) * (4 - (1 - 2*b4) * (2 - (1 - 2*b6)))
            )
            
        elif '256' in modscheme:  # 256QAM
            b1 = val & 1
            b2 = (val >> 1) & 1
            b3 = (val >> 2) & 1
            b4 = (val >> 3) & 1
            b5 = (val >> 4) & 1
            b6 = (val >> 5) & 1
            b7 = (val >> 6) & 1
            b8 = (val >> 7) & 1
            m[ii] = (1/np.sqrt(170)) * (
                (1 - 2*b1) * (8 - (1 - 2*b3) * (4 - (1 - 2*b5) * (2 - (1 - 2*b7)))) +
                1j * (1 - 2*b2) * (8 - (1 - 2*b4) * (4 - (1 - 2*b6) * (2 - (1 - 2*b8))))
            )
    
    return m

def f_genDMRS(CellID, slotno, symbno):
    """
    Generate DMRS according to 3GPP TS 38.211 Section 7.4.1.1.1
    """
    NoDMRSRE = 3276 // 2  # Max number of DMRS REs in one symbol
    
    # Calculate c_init according to 38.211: 5.2.1
    Cinit = ((2**17) * (14*slotno + symbno + 1) * (2*CellID + 1) + 2*CellID + 0) % (2**31)
    
    # Initialize x1 sequence
    x1_init = np.array([1] + [0]*30)
    x1 = x1_init.copy()
    
    # Initialize x2 sequence from Cinit
    x2_init = np.zeros(31)
    for ii in range(31):
        x2_init[ii] = (Cinit >> ii) & 1
    x2 = x2_init.copy()
    
    # Generate Gold sequence
    MPN = (2**16) - 1
    for n in range(MPN):
        x1 = np.append(x1, (x1[n+3] + x1[n]) % 2)
        x2 = np.append(x2, (x2[n+3] + x2[n+2] + x2[n+1] + x2[n]) % 2)
    
    # Generate c sequence with NC offset
    NC = 1600
    c = np.zeros(MPN - NC, dtype=int)
    for n in range(MPN - NC):
        c[n] = (x1[n + NC] + x2[n + NC]) % 2
    
    # Generate DMRS symbols according to 38.211: 7.4.1.1.1
    DMRS_cmplx = np.zeros(NoDMRSRE, dtype=complex)
    for n in range(NoDMRSRE):
        # MATLAB indexing starts at 1, so we adjust: c(2*n-1) and c(2*n+1-1)
        real_part = (1 - 2*c[2*n-1]) / np.sqrt(2)
        imag_part = (1 - 2*c[2*n+1-1]) / np.sqrt(2)
        DMRS_cmplx[n] = real_part + 1j * imag_part
    
    return DMRS_cmplx

def f_AddCPanddoiFFT(FDIQ, fs, num, Nfft):
    """
    Add cyclic prefix and perform IFFT
    FDIQ: Frequency domain grid (subcarriers x symbols)
    fs: Sample rate
    num: Numerology (0=15kHz, 1=30kHz, etc.)
    Nfft: FFT size
    """
    noSC, noSYM = FDIQ.shape
    r_TD_vector_cpincl = np.array([], dtype=complex)
    r_TD_vector = np.array([], dtype=complex)
    
    for symbcount in range(noSYM):
        # Zero-pad to FFT size
        FD_symb = np.concatenate([FDIQ[:, symbcount], np.zeros(Nfft - noSC)])
        
        # Circshift to center the data (equivalent to MATLAB circshift)
        shift_amount = round((Nfft - noSC) / 2)
        FD_symb = np.roll(FD_symb, shift_amount)
        
        # IFFT with ifftshift
        TD_symb = np.fft.ifft(np.fft.ifftshift(FD_symb))
        
        # Calculate CP length
        tc = 1 / (480e3 * 4096)
        k = tc * 64
        
        if symbcount % (7 * (2**num)) == 0:
            # First symbol in slot has longer CP
            cplength = (144 * k * 2**(-num)) + 16 * k
        else:
            # Normal CP
            cplength = 144 * k * 2**(-num)
        
        cplength_smpls = int(cplength * fs)
        
        # Add cyclic prefix
        TD_symb_cpincl = np.concatenate([
            TD_symb[-cplength_smpls:],  # CP from end of symbol
            TD_symb                     # Original symbol
        ])
        
        # Concatenate to output vectors
        r_TD_vector_cpincl = np.concatenate([r_TD_vector_cpincl, TD_symb_cpincl])
        r_TD_vector = np.concatenate([r_TD_vector, TD_symb])
    
    return r_TD_vector_cpincl, r_TD_vector

def generate_nr_signal():
    """
    Main function - Python translation of genNR.m
    """
    print("🚀 Generating 5G NR signal (Python translation of MATLAB genNR.m)")
    
    # Parameters from MATLAB script
    noofPrb = 51      # Number of PRBs (20MHz)
    noofSmbs = 280    # Number of symbols (20 slots × 14 symbols)
    cellID = 123      # Cell ID
    
    print(f"📊 Parameters:")
    print(f"   PRBs: {noofPrb}")
    print(f"   Symbols: {noofSmbs}")  
    print(f"   Cell ID: {cellID}")
    
    # Generate random data grid (64QAM)
    print("🎲 Generating random 64QAM data...")
    prbGrid = np.zeros((noofPrb * 12, noofSmbs), dtype=complex)
    
    for ii in range(noofSmbs):
        # Generate random data: random integers 0-63, then map to 64QAM
        random_bits = f_randbtw(noofPrb * 12, 0, 63).astype(int)
        prbGrid[:, ii] = f_modulationmapper(random_bits, '64QAM')
    
    print(f"   Grid shape: {prbGrid.shape}")
    
    # Insert DMRS symbols
    print("📡 Inserting DMRS symbols...")
    r_DMRSsymbs = [2, 11]  # DMRS symbol positions
    print(f"   DMRS symbols: {r_DMRSsymbs}")
    
    for iSmb in range(0, noofSmbs, 14):  # Every slot (14 symbols)
        slot_num = iSmb // 14
        for iDMRS in r_DMRSsymbs:
            if iSmb + iDMRS < noofSmbs:
                # Generate DMRS for this symbol
                DMRS_cmplx = f_genDMRS(cellID, slot_num, iDMRS)
                
                # Insert DMRS on even subcarriers, KEEP data on odd subcarriers
                # This matches what 89600 VSA expects for rate matching
                dmrs_length = min(len(DMRS_cmplx), (noofPrb * 12) // 2)
                prbGrid[::2, iSmb + iDMRS] = DMRS_cmplx[:dmrs_length]
                # Odd subcarriers keep their original data values
    
    print(f"   Final grid shape: {prbGrid.shape}")
    
    # Generate time domain signal
    print("⚡ Converting to time domain (IFFT + CP)...")
    TD, TDnocp = f_AddCPanddoiFFT(prbGrid, 30.72e6, 1, 1024)
    
    print(f"   Time domain samples: {len(TD)}")
    print(f"   Signal power: {np.mean(np.abs(TD)**2):.2e}")
    
    return TD, prbGrid

if __name__ == "__main__":
    TD, prbGrid = generate_nr_signal()
    print("✅ Signal generation complete!")
