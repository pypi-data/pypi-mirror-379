"""Perform JV hysteresis simulations"""
######### Package Imports #########################################################################

import os,sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.integrate import trapezoid
# import pySIMsalabim
## Import pySIMsalabim, if not successful, add the parent directory to the system path
try :
    import pySIMsalabim as sim
except ImportError:
    # Add the parent directory to the system path
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
    import pySIMsalabim as sim
from pySIMsalabim.utils import general as utils_gen
from pySIMsalabim.plots import plot_functions as utils_plot
from pySIMsalabim.utils.utils import update_cmd_pars

######### Function Definitions ####################################################################

def build_tVG_arrays(Vmin,Vmax,scan_speed,direction,steps,G_frac):
    """Build the Arrays for time, voltage and Generation rate for a hysteresis experiment.

    Parameters
    ----------
    Vmin : float 
        minimum voltage
    Vmax : float
        maximum voltage
    scan_speed : float
        Voltage scan speed [V/s]
    direction : integer
        Perform a Vmin-Vmax-Vmin (1) or Vmax-Vmin-Vmax scan (-1)
    steps : integer
        Number of time steps
    G_frac : float
        Device Parameter | Fractional Generation rate

    Returns
    -------
    np.array
        Array of time points
    np.array
        Array of voltages
    np.array
        Array of generation rates
    """    
    # Determine max time point
    tmax = abs((Vmax - Vmin)/scan_speed)
    V, G = [], []
    Vmin_ = Vmin
    Vmax_ = Vmax

    if direction == -1:
        Vmin = Vmax_
        Vmax = Vmin_

    t_min_to_max = np.linspace(0,tmax,int(steps/2))
    t_max_to_min = np.linspace(tmax,2*tmax,int(steps/2))
    t_max_to_min = np.delete(t_max_to_min,[0]) # remove double entry
    t = np.append(t_min_to_max,t_max_to_min)

    for i in t:
        if i < tmax:
            # First  voltage sweep
            V.append(direction*scan_speed*i + Vmin)
        else: 
            # Second voltage sweep
            V.append(-direction*scan_speed*(i-tmax) + Vmax)
        # Append the generation rate
        G.append(G_frac)
    # convert to numpy arrays
    V, G = np.asarray(V), np.asarray(G)
    return t,V,G

def build_tVG_arrays_log(Vmin,Vmax,Vacc,scan_speed,direction,steps,G_frac):
    """Build the Arrays for time, voltage and Generation rate for a hysteresis experiment with an exponential voltage sweep.

    Parameters
    ----------
    Vmin : float 
        minimum voltage
    Vmax : float
        maximum voltage
    scan_speed : float
        Voltage scan speed [V/s]
    direction : integer
        Perform a Vmin-Vmax-Vmin (1) or Vmax-Vmin-Vmax scan (-1)
    steps : integer
        Number of time steps
    G_frac : float
        Device Parameter | Fractional Generation rate
    Vminexpo : float
        Voltage at which the exponential voltage steps start if Vmin or Vmax is 0

    Returns
    -------
    np.array
        Array of time points
    np.array
        Array of voltages
    np.array
        Array of generation rates
    """ 
    if Vacc >= Vmin and Vacc <= Vmax:
        raise ValueError('Vacc must not be between Vmin and Vmax')
    
    d = Vacc-Vmax
    V_min_to_max = [ Vacc - d * np.exp((1 - i/(steps/2 - 1)) * np.log((Vacc - Vmin)/d)) for i in range(steps//2) ]
    V_min_to_max = np.array(V_min_to_max)
    if Vmin == 0:
        # find idx of the min of Vmin_to_max and set it to 0
        min_idx = np.argmin(V_min_to_max)
        V_min_to_max[min_idx] = 0
    elif Vmax == 0:
        # find idx of the max of Vmin_to_max and set it to 0
        max_idx = np.argmax(V_min_to_max)
        V_min_to_max[max_idx] = 0

    V_max_to_min = V_min_to_max[::-1]
    if direction == 1:
        # forward -> backward
        V_max_to_min = np.delete(V_max_to_min,[0])# remove double entry
        V = np.append(V_min_to_max,V_max_to_min)
    elif direction == -1:
        # backward -> forward
        V_min_to_max = np.delete(V_min_to_max,[0])# remove double entry
        V = np.append(V_max_to_min,V_min_to_max)
    G = G_frac * np.ones(len(V))
    # calculate the time array based on the voltage array and the scan speed
    t = np.zeros(len(V))
    for i in range(1,len(V)):
        t[i] = t[i-1] + abs((V[i]-V[i-1])/scan_speed)

    return t,V,G

def create_tVG_hysteresis(session_path, Vmin, Vmax, scan_speed, direction, steps, G_frac, tVG_name, Vacc=None,Vdist=1,**kwargs):
    """Create a tVG file for hysteresis experiments. 

    Parameters
    ----------
    session_path : string
        working directory for zimt
    Vmin : float 
        Left voltage boundary
    Vmax : float
        Right voltage boundary
    scan_speed : float
        Voltage scan speed [V/s]
    direction : integer
        Perform a Vmin-Vmax-Vmin (1) or Vmax-Vmin-Vmax scan (-1)
    steps : integer
        Number of time steps
    G_frac : float
        Device Parameter | Fractional Generation rate
    Vacc : float, optional
        Point of accumulation of row of V's, note: Vacc should be slightly larger than Vmax or slightly lower than Vmin, only needed if Vdist=2, else ignored, default is None
    Vdist : integer, optional
        Voltage distribution type (1: linear, 2: exponential), default is 1
    tVG_name : string
        Device Parameter | Name of the tVG file
    **kwargs : dict
        Additional keyword arguments


    Returns
    -------
    integer
        Value to indicate the result of the process
    string
        A message to indicate the result of the process
    """
    # kwargs
    
    expo_mode = True if Vdist == 2 else False
    # Vminexpo = kwargs.get('Vminexpo', 1e-2) # Voltage at which the exponential voltage steps start if Vmin or Vmax is 0
    # # check that Vminexpo is positive
    # if Vminexpo <= 0:
    #     msg = 'Vminexpo must be strictly positive'
    #     retval = 1
    #     return retval, msg
    if expo_mode and Vacc is None:
        msg = 'When expo_mode is True, Vacc must be provided'
        retval = 1
        return retval, msg
    
    # check that direction is either 1 or -1
    if direction != 1 and direction != -1:
        msg = 'Incorrect scan direction, choose either 1 for a forward - backward scan or -1 for a backward - forward scan'
        retval = 1
        return retval, msg

    # check that Vmin < Vmax
    if Vmin >= Vmax:
        msg = 'Vmin must be smaller than Vmax'
        retval = 1
        return retval, msg    

    # Create two arrays for both time sweeps
    if expo_mode:
        t,V,G = build_tVG_arrays_log(Vmin,Vmax,Vacc,scan_speed,direction,steps,G_frac)
    else:
        t,V,G = build_tVG_arrays(Vmin,Vmax,scan_speed,direction,steps,G_frac)
        
    # Set the correct header for the tVG file
    tVG_header = ['t','Vext','G_frac']

    # Combine t,V,G arrays into a DataFrame
    tVG = pd.DataFrame(np.stack([t,np.asarray(V),np.asarray(G)]).T,columns=tVG_header)

    # Create tVG file
    tVG.to_csv(os.path.join(session_path,tVG_name),sep=' ',index=False,float_format='%.5e')

    # tVG file is created, msg a success
    msg = 'Success'
    retval = 0
    
    return retval, msg

def plot_hysteresis_JV(session_path, path2file = 'tj.dat'):
    """Plot the hysteresis JV curve

    Parameters
    ----------
    session_path : string
        working directory for zimt
    path2file : string
        Path to the tj file

    Returns
    -------
    Axes
        Axes object for the plot

    """
    # Read the data from tj-file
    data_tj = pd.read_csv(os.path.join(session_path,path2file), sep=r'\s+')
    
    fig, ax = plt.subplots()
    pars = {'Jext' : 'Simulation'} #'$J_{ext}$'}
    par_x = 'Vext'
    xlabel = '$V_{ext}$ [V]'
    ylabel = 'Current density [Am$^{-2}$]'
    xscale = 'linear'
    yscale = 'linear'
    title = 'JV curve'
    plot_type = plt.plot

    ax = utils_plot.plot_result(data_tj, pars, list(pars.keys()), par_x, xlabel, ylabel, xscale, yscale, title, ax, plot_type)
    plt.tight_layout() # make it fit in the window
    
    return ax

def tVG_exp(session_path, expJV_Vmin_Vmax, expJV_Vmax_Vmin, scan_speed, direction, G_frac, tVG_name):
    """Create a tVG file for hysteresis experiments where Vext is the same as the voltages in the experimental JV file

    Parameters
    ----------
    session_path : string
        working directory for zimt
    expJV_Vmin_Vmax : string
        Name of the file of the Vmin-Vmax JV scan
    expJV_Vmax_Vmin : string
        Name of the file of the Vmax-Vmin JV scan
    scan_speed : float
        Voltage scan speed [V/s]
    direction : integer
        Perform a Vmin-Vmax-Vmin (1) or Vmax-Vmin-Vmax scan (-1)
    G_frac : float
        Fractional Generation rate
    tVG_name : string
        Name of the tVG file

    Returns
    -------
    integer
        Value to indicate the result of the process
    string
        A message to indicate the result of the process
    """
    
    if direction == 1:
        JV_forward, JV_backward = read_Exp_JV(session_path, expJV_Vmin_Vmax, expJV_Vmax_Vmin)
    elif direction == -1:
        JV_backward, JV_forward = read_Exp_JV(session_path, expJV_Vmin_Vmax, expJV_Vmax_Vmin)
    else:
        # Illegal value for direction given
        msg = 'Incorrect scan direction, choose either 1 for Vmin-Vmax-Vmin scan or -1 for a Vmax-Vmin-Vmax scan'
        retval = 1
        return retval, msg

    V_forward = JV_forward.Vext
    V_backward = JV_backward.Vext

    # Create the time array
    t=np.empty(len(V_forward) + len(V_backward))
    t[0]=0

    # First half
    for i in range(1,len(V_forward)):
        t[i]= t[i-1] + abs((V_forward[i]-V_forward[i-1])/scan_speed)

    # Turning point
    t[len(V_forward)]=t[len(V_forward)-1] + abs((V_backward[0]-V_forward.iloc[-1])/scan_speed)

    # Second half
    for i in range(len(V_forward)+1,len(V_forward) + len(V_backward)):
        t[i]= t[i-1] + abs((V_backward[i-len(V_forward)]-V_backward[i-len(V_forward)-1])/scan_speed)

    # Voltage array
    V = np.concatenate([V_forward, V_backward])

    # Set the correct header for the tVG file
    tVG_header = ['t','Vext','G_frac']

    G = G_frac * np.ones(len(t))

    # Combine t,V,G arrays into a DataFrama
    tVG = pd.DataFrame(np.stack([t,np.asarray(V),G]).T,columns=tVG_header)

    # Create tVG file
    tVG.to_csv(os.path.join(session_path,tVG_name),sep=' ',index=False,float_format='%.3e')

    # tVG file is created, msg a success
    msg = 'Success'
    retval = 0
    return retval, msg

def read_Exp_JV(session_path, expJV_Vmin_Vmax, expJV_Vmax_Vmin):
    """Read experimental forward and backward JV files

    Parameters
    ----------
    session_path : string
        working directory for zimt
    expJV_Vmin_Vmax : string
        Name of the file of the forward JV scan
    expJV_Vmax_Vmin : string
        Name of the file of the backward JV scan

    Returns
    -------
    np.array
        Array of current and voltage of experimental JV from Vmin to Vmax
    np.array
        Array of current and voltage of experimental JV from Vmax to Vmin
    """
    
    expJV_min_max = os.path.join(session_path, expJV_Vmin_Vmax)
    expJV_max_min = os.path.join(session_path, expJV_Vmax_Vmin)
    
    # Determine time corresponding to each voltage V_i
    JV_min_max = pd.read_csv(expJV_min_max, sep=r'\s+')
    JV_max_min = pd.read_csv(expJV_max_min, sep=r'\s+')
    
    return JV_min_max, JV_max_min

def concatJVs(session_path, expJV_Vmin_Vmax, expJV_Vmax_Vmin, direction):
    """Put the experimental forward and backward JV arrays together

    Parameters
    ----------
    session_path : string
        working directory for zimt
    expJV_Vmin_Vmax : string
        Name of the file of the forward JV scan
    expJV_Vmax_Vmin : string
        Name of the file of the backward JV scan
    direction : integer
        Perform a Vmin-Vmax-Vmin (1) or Vmax-Vmin-Vmax scan (-1)
    
    Returns
    -------
    np.array
        Array of current and voltage of experimental JV
    """
    
    if direction == 1:
        JV_forward, JV_backward = read_Exp_JV(session_path, expJV_Vmin_Vmax, expJV_Vmax_Vmin)
    elif direction == -1:
        JV_backward, JV_forward = read_Exp_JV(session_path, expJV_Vmin_Vmax, expJV_Vmax_Vmin)
    else:
        # Illegal value for direction given
        print('Incorrect scan direction, choose either 1 for Vmin-Vmax-Vmin scan or -1 for a Vmax-Vmin-Vmax scan')
        sys.exit()
    
    expJV = pd.concat([JV_forward, JV_backward], ignore_index=True)   
    return expJV

def read_tj_file(session_path, tj_file_name='tj.dat'):
    """ Read relevant parameters for admittance of the tj file

    Parameters
    ----------
    session_path : string
        Path of the simulation folder for this session
    data_tj : dataFrame
        Pandas dataFrame containing the tj output file from ZimT

    Returns
    -------
    DataFrame
        Pandas dataFrame of the tj_file containing the time, current density, numerical error in the current density and the photogenerated current density
    """

    data = pd.read_csv(os.path.join(session_path,tj_file_name), sep=r'\s+')

    return data

def Compare_Exp_Sim_JV(session_path, expJV_Vmin_Vmax, expJV_Vmax_Vmin, rms_mode, direction, tj_file_name='tj.dat'):
    """ Calculate the root-mean-square (rms) error of the simulated data compared to the experimental data. The used formulas are
    described in the Manual (see the variable rms_mode in the section 'Description of simulated device parameters').

    Parameters
    ----------
    session_path : string
        Path of the simulation folder for this session
    expJV_Vmin_Vmax : string
        Name of the file of the forward JV scan
    expJV_Vmax_Vmin : string
        Name of the file of the backward JV scan
    rms_mode : string
        Indicates how the normalised rms error should be calculated: either in linear or logarithmic form
    direction : integer
        Perform a Vmin-Vmax-Vmin (1) or Vmax-Vmin-Vmax scan (-1)
    tj_file_name : dataFrame
        Pandas dataFrame containing the tj output file from ZimT

    Returns
    -------
    Float
        Calculated rms-error
    """
        
    JVExp = concatJVs(session_path, expJV_Vmin_Vmax, expJV_Vmax_Vmin, direction)
    JVSim = read_tj_file(session_path, tj_file_name)[['t', 'Vext', 'Jext']]
    
    # Make an array of voltages that did not converge in simulation
    V_array_not_in_JVSim = np.setdiff1d(JVExp.Vext, JVSim.Vext)
    
    # Remove voltages of experimental data that did not converge in the simulation
    # As the rms-value cannot be calculated, when the voltages of the simulation and experimental data do not overlap
    if len(V_array_not_in_JVSim) > 0:
        disgardedPoints = True
        indices = []
        
        for i in range(len(V_array_not_in_JVSim)):
            # Find indices where voltages do not overlap for every V_i
            index_array = np.where((JVExp.Vext == V_array_not_in_JVSim[i]))[0]
            
            # Add the to-slice-indices to a list
            for j in range(len(index_array)):
                indices.append(index_array[j])
        
        # Delete the indices and convert JVExp from a numpy array in a DataFrame again
        JVExp = np.delete(JVExp, np.sort(indices), axis=0)
        JVExp = pd.DataFrame(JVExp, columns=['Vext', 'Jext'])
    
    rms = 0
    count = 0
    disgardedPoints = False
    
    # Look for the interval [Jmin,Jmax] in both the simulated and experiment data
    Jmin = min(min(JVExp.Jext), min(JVSim.Jext))
    Jmax = max(max(JVExp.Jext), max(JVSim.Jext))
    
    if rms_mode == 'lin' or 'linear':
        # Calculate the sum of squared residuals
        for i in range(len(JVExp)):
            rms = rms + (JVExp.Jext[i] - JVSim.Jext[i])**2
            count += 1
        
        # Calculate the root mean square error and normalise with respect to the interval [Jmin,Jmax]
        rms = np.sqrt(rms/count)/(Jmax-Jmin)
        
    elif rms_mode == 'log' or 'logarithmic':
        # Calculate the sum of squared residuals
        for i in range(len(JVExp)):
            if JVExp.Jext[i]*JVSim.Jext[i]>=0: # We can only calc rms if both are <> 0 and they have the same sign
                rms = rms + np.log(JVExp.Jext[i]/JVSim.Jext[i])**2
            else:
                disgardedPoints = True
            
        # Calculate the root mean square error and normalise with respect to the interval [Jmin,Jmax]
        rms = np.sqrt(rms/count)/abs(np.log(abs(Jmax/Jmin))) # Note: Jmax > Jmin, of course, but ABS(Jmin) can be larger than ABS(Jmax) so we need to use ABS(LN(...)) to get a positive rms

    if disgardedPoints:
        print('Not all JV points were used in computing the rms-error.')
        print('Delete voltages are: ', V_array_not_in_JVSim)
    
    return rms

def calc_hysteresis_index(session_path, tj_file_name = 'tj.dat', tVG_file_ame='tVG.txt', plot_hyst_index = False):
    """
    Calculate the hysteresis index from the simulated JV curve using the difference area between the forward and backward scan
    
    Parameters
    ----------
    session_path : string
        working directory for zimt
    tj_file_name : string
        Name of the tj file
    tVG_file_ame : string
        Name of the tVG file
    plot_hyst_index : bool
        If True, plot the JV curves with the normalisation and difference area

    Returns
    -------
    float
        Hysteresis index
    """

    sign_dum = 0 # dummy value for sign change in voltage array

    # Read data from files. tj file for the JV curve and tVG file to get all possible voltage steps. 
    # This is needed as not all voltages might be present in the tj file.
    data_tj = pd.read_csv(os.path.join(session_path,tj_file_name), sep=r'\s+')
    data_tVG = pd.read_csv(os.path.join(session_path,tVG_file_ame), sep=r'\s+')

    # Store Vinput, Vext and Jext in arrays
    Vinput = np.array(data_tVG['Vext'])
    Vext = np.array(data_tj['Vext'])
    Jext = np.array(data_tj['Jext'])

    # Find the min and max values of Vext and Jext to span the normalisation area 
    Jmin = min(Jext)
    Jmax = max(Jext)
    Vmin = min(Vext)
    Vmax = max(Vext)

    # As the forward and backward scan are in the same array, 
    # we need to find the point where the JV curve changes direction, i.e. the turning point and split into two seperate arrays
    # Vext,Jext array
    diff = np.diff(Vext)
    sign_change = np.where(np.diff(np.sign(diff)))
    
    if len(sign_change[0]) == 0:
        print('Hysteresis index could not be calculated. No sign change in the voltage array')
        return 0
    elif len(sign_change[0]) ==2:
        # Check if they are consecutive. If so, we might just be missing the 'flip'' point, as it could have not converged, so we need to correct for this.
        if sign_change[0][1] - sign_change[0][0] == 1:
            idx_change = sign_change[0][0] + 2
            sign_dum = 1
        else:
            print('Hysteresis index could not be calculated. Multiple sign changes in the voltage array')
            return 0
    elif len(sign_change[0]) > 2:
        print('Hysteresis index could not be calculated. Multiple sign changes in the voltage array')
        return 0
    else:
        # Need to correct for the index change between Vinput and the sign_change array
        idx_change = sign_change[0][0] + 2

    # split the Vext and Jext arrays into two arrays
    Vext_1 = Vext[:idx_change]
    Jext_1 = Jext[:idx_change]
    Vext_2 = Vext[idx_change:]
    Jext_2 = Jext[idx_change:]

    if sign_dum != 1:
        # append the last value of the first array to the first position of the second array to be able to include the turning point
        Vext_2 = np.insert(Vext_2,0,Vext_1[-1])
        Jext_2 = np.insert(Jext_2,0,Jext_1[-1])

    # Vinput array
    diff = np.diff(Vinput)
    sign_change = np.where(np.diff(np.sign(diff)))

    if len(sign_change[0]) == 0:
        print('Hysteresis index could not be calculated. No sign change in the voltage array')
        return 0
    elif len(sign_change[0]) > 1:
        print('Hysteresis index could not be calculated.. Multiple sign changes in the voltage array')
        return 0
    else:
        # Need to correct for the index change between Vinput and the sign_change array
        sign_change_Vinput = sign_change[0][0] + 2

    # We only need one of the arrays, as we will only use this as a reference
    Vinput_1 = Vinput[:sign_change_Vinput]


    # To calculate the difference area between the two curves, we need to reverse the order of the second arrays to match the order of the applied voltage
    # reverse the second array
    Vext_2 = Vext_2[::-1]
    Jext_2 = Jext_2[::-1]

    # Create empty arrays to store the final V,J values
    Vfinal = []
    Jfinal_1 = []
    Jfinal_2 = []

    # Loop over Vinput and check if the voltage exist in both V arrays
    # If it does, add the current to the corresponding J array, else we cannot use it so we discard it
    for i in range(len(Vinput_1)):
        if (Vinput_1[i] in Vext_1) and (Vinput_1[i] in Vext_2):
            # Get the index of the voltage in the corresponding V arrays
            idx1 = np.where(Vext_1 == Vinput_1[i])[0][0]
            idx2 = np.where(Vext_2 == Vinput_1[i])[0][0] 

            # Append the values to the final arrays
            Vfinal.append(Vext_1[idx1])
            Jfinal_1.append(Jext_1[idx1])
            Jfinal_2.append(Jext_2[idx2])

    # Calculate the hysteresis index
    hysteresis_index_num = abs(trapezoid(np.abs(np.array(Jfinal_1) - np.array(Jfinal_2)),Vfinal)) # Use abs around trapezoid to avoid negative values when Vfinal is flipped
    hysteresis_index_denom = (Jmax - Jmin) * (Vmax - Vmin)
    hysteresis_index = hysteresis_index_num / hysteresis_index_denom

    if plot_hyst_index == True:

        # Plot JV traces together with normalisation and difference area
        fig, ax = plt.subplots()

        # Normalisation area
        ax.vlines(x = Vmin,ymin =  Jmin, ymax = Jmax, color='#919191',linestyles='dashed',label='Normalisation area')
        ax.vlines(x = Vmax,ymin =  Jmin, ymax = Jmax, color='#919191',linestyles='dashed')
        ax.hlines(y = Jmin,xmin =  Vmin, xmax = Vmax, color='#919191',linestyles='dashed')
        ax.hlines(y = Jmax,xmin =  Vmin, xmax = Vmax, color='#919191',linestyles='dashed')

        # Difference area
        ax.fill_between(Vfinal,Jfinal_1,Jfinal_2, color='#b1f997',label='Difference area')
    
        # JV traces
        ax.plot(Vfinal,Jfinal_2,label='Backward', color='r', linewidth=4)
        ax.plot(Vfinal,Jfinal_1,label='Forward', color = 'b', linewidth=4)

        ax.set_xlabel('$V_{ext}$ [V]')
        ax.set_ylabel('$J_{ext}$ [Am$^{-2}$]')

        # Reverse the legend order. Curves should be listed first, then norm/diff area. 
        handles, labels = ax.get_legend_handles_labels()
        ax.legend(handles[::-1], labels[::-1],framealpha=1, loc='center left', bbox_to_anchor=(0.07, 0.75))
        plt.tight_layout()

        plt.show()

    return hysteresis_index

def Hysteresis_JV(zimt_device_parameters, session_path, UseExpData, scan_speed, direction, G_frac, tVG_name='tVG.txt', tj_name = 'tj.dat',varFile='none',
                  run_mode=False, Vmin=0.0, Vmax=0.0, steps =0, expJV_Vmin_Vmax='', expJV_Vmax_Vmin='',rms_mode='lin', **kwargs ):
    """Create a tVG file and perform a JV hysteresis experiment.

    Parameters
    ----------
    zimt_device_parameters : string
        name of the zimt device parameters file
    session_path : string
        working directory for zimt
    UseExpData : integer
        If 1, use experimental JV curves. If 0, Use Vmin, Vmax as boundaries
    scan_speed : float
        Voltage scan speed [V/s]
    direction : integer
        Perform a forward-backward (1) or backward-forward scan (-1).
    G_frac : float
        Device Parameter | Fractional generation rate
    run_mode : bool, optional
        Indicate whether the script is in 'web' mode (True) or standalone mode (False). Used to control the console output, by default False  
    tVG_name : string, optional
        Device Parameter | Name of the tVG file, by default 'tVG.txt'
    tj_name : string, optional
        Name of the tj file, by default 'tj.dat'
    varFile : string, optional
        Name of the var file, by default 'none'
    run_mode : bool, optional
        indicate whether the script is in 'web' mode (True) or standalone mode (False). Used to control the console output, by default False
    Vmin : float, optional
        Left voltage boundary, by default 0.0
    Vmax : float, optional
        Right voltage boundary, by default 0.0
    steps : int, optional
        Number of time steps, by default 0
    expJV_Vmin_Vmax : str, optional
        file name of the first expJV curve, by default ''
    expJV_Vmax_Vmin : str, optional
        file name of the second expJV curve, by default ''
    rms_mode : str, optional
        Either 'lin' or 'log' to specify how the rms error is calculated

    Returns
    -------
    CompletedProcess
        Output object of with returncode and console output of the simulation
    string
        Return message to display on the UI, for both success and failed
    dict
        Dictionary containing the special output values of the simulation. In this case, the rms error ('rms') and the hysteresis index ('hyst_index')
    """
    verbose = kwargs.get('verbose', False) # Check if the user wants to see the console output
    UUID = kwargs.get('UUID', '') # Check if the user wants to add a UUID to the tj file name
    cmd_pars = kwargs.get('cmd_pars', None) # Check if the user wants to add additional command line parameters
    Vdist = kwargs.get('Vdist', 1) # Voltage distribution type (1: linear, 2: exponential)
    Vacc = kwargs.get('Vacc', None) # Point of accumulation of row of V's, note: Vacc should be slightly larger than Vmax or slightly lower than Vmin, only needed if Vdist=2, else ignored

    # Check if the user wants to force the use of thread safe mode, necessary for Windows with parallel simulations
    if os.name == 'nt':  
        threadsafe = kwargs.get('threadsafe', True) # Check if the user wants to force the use of threads instead of processes
    else:
        threadsafe = kwargs.get('threadsafe', False) # Check if the user wants to force the use of threads instead of processes

    turnoff_autoTidy = kwargs.get('turnoff_autoTidy', None) # Check if the user wants to turn off the autoTidy function in SIMsalabim
    if turnoff_autoTidy is None: 
        if not threadsafe:
            turnoff_autoTidy = True
        else:
            turnoff_autoTidy = False

    # tVG file generation additional parameters
    # expo_mode = kwargs.get('expo_mode', False) # whether to use exponential time steps
    # Vminexpo = kwargs.get('Vminexpo', 1e-2) # minimum voltage after 0 to start the log steps

    # Update the JV file name with the UUID
    if UUID != '':
        dum_str = f'_{UUID}'
    else:
        dum_str = ''

    # Update the filenames with the UUID
    tj_name = os.path.join(session_path, tj_name)
    tVG_name = os.path.join(session_path, tVG_name)
    if UUID != '':
        tj_file_name_base, tj_file_name_ext = os.path.splitext(tj_name)
        tj_name = tj_file_name_base + dum_str + tj_file_name_ext 
        tVG_name_base, tVG_name_ext = os.path.splitext(tVG_name)
        tVG_name = tVG_name_base + dum_str + tVG_name_ext
        if varFile != 'none':
            var_file_base, var_file_ext = os.path.splitext(varFile)
            varFile = var_file_base + dum_str + var_file_ext
            varFile = os.path.join(session_path, varFile)
    # varFile = 'none' # we don't use a var file for the hysteresis JV simulation

    # Init output_vals rms & hyst_index
    rms = 0.0
    hyst_index = 0.0

    if UseExpData == 1:
        # When fitting to experimental data, create a tVG file where Vext is the same as the voltages in the experimental JV file
        if os.path.exists(os.path.join(session_path, expJV_Vmin_Vmax)) and os.path.exists(os.path.join(session_path, expJV_Vmax_Vmin)):
            result, message = tVG_exp(session_path, expJV_Vmin_Vmax, expJV_Vmax_Vmin, scan_speed, direction, G_frac, tVG_name)
        else:
            result = 1
            message = 'Experimental JV files not found'
    else:
        result, message = create_tVG_hysteresis(session_path, Vmin, Vmax, scan_speed, direction, steps, G_frac, tVG_name, Vacc=Vacc, Vdist=Vdist)

    if result == 0:
        # tVG file created
        Hysteresis_JV_args = [{'par':'dev_par_file','val':zimt_device_parameters},
                              {'par':'tVGFile','val':tVG_name},
                              {'par':'tJFile','val':tj_name},
                              {'par':'varFile','val':varFile},
                              {'par':'logFile','val':'log'+dum_str+'.txt'}
                              ]
        
        if turnoff_autoTidy:
            Hysteresis_JV_args.append({'par':'autoTidy','val':'0'})

        if cmd_pars is not None:
            Hysteresis_JV_args = update_cmd_pars(Hysteresis_JV_args, cmd_pars)

        if threadsafe:
            result, message = utils_gen.run_simulation_filesafe('zimt', Hysteresis_JV_args, session_path, run_mode, verbose=verbose)
        else:
            result, message = utils_gen.run_simulation('zimt', Hysteresis_JV_args, session_path, run_mode, verbose=verbose)

        if result == 0 or result == 95:
            if UseExpData == 1:
                rms = Compare_Exp_Sim_JV(session_path, expJV_Vmin_Vmax, expJV_Vmax_Vmin, rms_mode, direction, tj_name)
            hyst_index = calc_hysteresis_index(session_path, tj_name, tVG_name)
        else:
            message = message
        
        result = result

        # Put all the output values in a dictionary to be returned. 
        # By putting it in a dictionary we can add any number of values without breaking return arguments
        output_vals = {'rms': rms, 'hyst_index': hyst_index}
    
    return result, message, output_vals

## Running the function as a standalone script
if __name__ == "__main__":
    ## Manual Hysteresis input parameters. These are overwritten by command line arguments if provided
    scan_speed = 1e1 # V/s
    direction = 1 # Scan direction: 1 for Vmin-Vmax-Vmin, -1 for Vmax-Vmin-Vmax
    G_frac = 1 # amount of suns
    UseExpData = 0 # integer, if 1 read experimental data
    Vmin = 0 # lower voltage boundary
    Vmax = 1.15 # upper voltage boundary
    steps = 200 # Number of voltage steps
    expJV_Vmin_Vmax = 'od05_f.txt' # Forward (direction=1)/Backward (direction=-1) JV scan file
    expJV_Vmax_Vmin = 'od05_b.txt' # Backward (direction=1)/Forward (direction=-1) JV scan file

    # Define folder and file paths
    session_path = os.path.join('../../','SIMsalabim','ZimT')

    zimt_device_parameters = 'simulation_setup.txt'

    tVGFile = 'tVG.txt'
    tJFile = 'tj.dat'
    varFile = 'none'

    # UUID = str(uuid.uuid4()) # Add a UUID to the simulation
    UUID = ''

    # Not user input
    rms_mode = 'log' # lin or log

    ############## Command line arguments  ##############
    ## Notes
    ## - The command line arguments are optional and can be provided in any order
    ## - Each command line argument must be provided in the format -par_name value
    ## - Possible arguments include all SIMsalabim parameters and Hysteresis JV specific parameters as listed before
    ## - Special arguments
    ##   - sp : string
    ##     - The session path, i.e. the working directory for the simulation
    ##   - simsetup : string
    ##     - The name of the zimt simulation setup parameters file
    ##   - UUID : string
    ##     - An UUID to add to the simulation (output)

    cmd_pars_dict = {}
    cmd_pars = []

    # Check if any arguments are provided.
    if len(sys.argv) >= 2:
        # Each arguments should be in the format -par val, i.e. in pairs of two. Skip the first argument as this is the script name
        if not len(sys.argv[1:]) % 2 == 0:
            print('Error in command line parameters. Please provide arguments in the format -par_name value -par_name value ...')
            sys.exit(1)
        else:
            input_list = sys.argv[1:]
            # Loop over the input list and put pairs into a dictionary with the first argument as key and the second argument as value
            for i in range(0,len(input_list),2):
                # Check if the key already exists, if not, add it to the cmd_pars_dict
                if str(input_list[i][1:]) in cmd_pars_dict:
                    print(f'Duplicate parameter found in the command line parameters: {str(input_list[i][1:])}')
                    sys.exit(1)
                else:
                    cmd_pars_dict[str(input_list[i][1:])] = str(input_list[i+1])

    # Check and process specific keys/arguments that are not native SIMsalabim arguments
    # Handle the session_path/sp argument separately, as the other parameters depend on this
    if 'sp' in cmd_pars_dict:
        session_path = cmd_pars_dict['sp']
        # remove from cmd_pars
        cmd_pars_dict.pop('sp')

    # Define mappings for keys and variables
    key_action_map = {
        'zimt_device_parameters': lambda val: {'zimt_device_parameters': val},
        'scan_speed': lambda val: {'scan_speed': float(val)},
        'direction': lambda val: {'direction': int(val)},
        'G_frac': lambda val: {'G_frac': float(val)},
        'UseExpData': lambda val: {'UseExpData': int(val)},
        'Vmin': lambda val: {'Vmin': float(val)},
        'Vmax': lambda val: {'Vmax': float(val)},
        'steps': lambda val: {'steps': int(val)},
        'expJV_Vmin_Vmax': lambda val: {'expJV_Vmin_Vmax': val},
        'expJV_Vmax_Vmin': lambda val: {'expJV_Vmax_Vmin': val},
        'tVGFile': lambda val: {'tVGFile':  val},
        'tJFile': lambda val: {'tJFile': val},
        'varFile': lambda val: {'varFile': val},
        'UUID': lambda val: {'UUID': val},
    }

    for key in list(cmd_pars_dict.keys()):  # Use list to avoid modifying the dictionary while iterating
        if key in key_action_map:
            # Apply the corresponding action
            result = key_action_map[key](cmd_pars_dict[key])
            globals().update(result)  # Dynamically update global variables
            cmd_pars_dict.pop(key)

    # Handle remaining keys in `cmd_pars_dict` and add them to the cmd_pars list
    cmd_pars.extend({'par': key, 'val': value} for key, value in cmd_pars_dict.items())
    
    if UseExpData == 1:
        result, message, output_vals = Hysteresis_JV(zimt_device_parameters, session_path, UseExpData, scan_speed, direction, G_frac, tVG_name = tVGFile, tj_name = tJFile,
                                             run_mode = False, expJV_Vmin_Vmax = expJV_Vmin_Vmax, expJV_Vmax_Vmin = expJV_Vmax_Vmin, rms_mode = rms_mode, cmd_pars = cmd_pars, UUID=UUID)
    else:
        result, message, output_vals = Hysteresis_JV(zimt_device_parameters, session_path, UseExpData, scan_speed, direction, G_frac, tVG_name = tVGFile, tj_name = tJFile, 
                                              run_mode = False, Vmin=Vmin, Vmax=Vmax, steps =steps, rms_mode = rms_mode, cmd_pars = cmd_pars, UUID=UUID)
    
    if result == 0 or result == 95:
        if UseExpData == 1:
            print('Rms-value: ', "{:.5f}".format(round(output_vals['rms'], 5)))

        print(f'hyst-index: {output_vals["hyst_index"]:.3f}')

        ax = plot_hysteresis_JV(session_path, tJFile)
        if UseExpData == 1:
            JVExp = concatJVs(session_path, expJV_Vmin_Vmax, expJV_Vmax_Vmin, direction)
            ax.scatter(JVExp.Vext, JVExp.Jext, label='Experimental', color='r')
        
        ax.legend()
        plt.show()
    else:
        print(message) #'Convergence issues, no plot is printed')
