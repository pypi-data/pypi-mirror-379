# This file contains all SPRpy classes, and also methods and functions that depend on the class objects

import datetime
import os
import scipy
import pickle
import copy
import bottleneck
import multiprocessing
from SPRpy_functions import *
from fresnel_transfer_matrix import fresnel_calculation


class Session:

    """
    A base class for storing and loading a group of measurements for a particular session in one file. This should be
    the first thing that a user is prompted for before they start their analysis.
    """

    def __init__(self, version, name='Session', directory=os.getcwd(), current_data_path=None):
        self.version = version
        self.name = datetime.datetime.now().__str__()[0:16].replace(':', '_') + ' ' + name
        if not os.path.exists(directory + r'/SPRpy sessions'):
            os.mkdir(directory + r'/SPRpy sessions')
        self.location = directory + r'/SPRpy sessions' + r'/{name_}'.format(name_=self.name)
        if not os.path.exists(self.location):
            os.mkdir(self.location)
        if not os.path.exists(self.location + r'/Sensors'):
            os.mkdir(self.location + r'/Sensors')
        if not os.path.exists(self.location + r'/Analysis instances'):
            os.mkdir(self.location + r'/Analysis instances')
        self.sensor_instances = {}  # NOTE: The sessions in this list are also updated when modified as current sensor object
        self.sensor_ID_count = 0
        self.fresnel_analysis_instances = {}
        self.fresnel_analysis_ID_count = 0
        self.exclusion_height_analysis_instances = {}
        self.exclusion_height_analysis_ID_count = 0
        self.current_data_path = current_data_path
        self.log = datetime.datetime.now().__str__()[0:16] + ' >> ' + 'Welcome to SPRpy!' \
            + '\n' + datetime.datetime.now().__str__()[0:16] + ' >> ' + 'Start your session by defining your SPR sensor layers.'

    def update_name_and_location(self, new_name):
        """
        Updates the name and location of the session.
        :param new_name: string
        :return:
        """

        self.name = new_name
        # old_location = self.location
        os.rename(self.location, self.location.replace(self.location.split('/')[-1], new_name))
        self.location = self.location.replace(self.location.split('/')[-1], new_name)
        return

    def remove_sensor(self, sensor_object_id):
        """
        Remove a sensor object from the session.
        :return:
        """
        removed = self.sensor_instances.pop(sensor_object_id)
        removed_file_path = self.location + r'\Sensors' + r'\S{id} {name}.pickle'.format(id=removed.object_id, name=removed.name)
        os.remove(removed_file_path)
        print('Removed the following sensor object: S{id} {name}'.format(id=removed.object_id, name=removed.name))

        return

    def remove_fresnel_analysis(self, analysis_object_id):
        """
        Remove an analysis object from the session.
        :return:
        """
        removed = self.fresnel_analysis_instances.pop(analysis_object_id)
        removed_file_path = self.location + r'\Analysis instances' + r'\FM{id} {name}.pickle'.format(id=removed.object_id, name=removed.name)
        os.remove(removed_file_path)
        print('Removed the following analysis object: FM{id} {name}'.format(id=removed.object_id, name=removed.name))

        return

    def remove_exclusion_height_analysis(self, analysis_object_id):
        """
        Remove an analysis object from the session.
        :return:
        """
        removed = self.exclusion_height_analysis_instances.pop(analysis_object_id)
        removed_file_path = self.location + r'\Analysis instances' + r'\EH{id} {name}.pickle'.format(id=removed.object_id, name=removed.name)
        os.remove(removed_file_path)
        print('Removed the following analysis object: EH{id} {name}'.format(id=removed.object_id, name=removed.name))

        return

    def save_all(self):
        """
        Saves all objects stored in the session, and the session file itself.
        :return: None
        """

        # Save session object
        with open(self.location + r'\Session file (v{version_}).pickle'.format(version_=self.version.replace('.', '_')), 'wb') as save_file:
            pickle.dump(self, save_file)

        # Save sensor instances
        for sensor_id in self.sensor_instances:
            with open(self.location + r'\Sensors' + r'\S{id} {name}.pickle'.format(id=sensor_id, name=self.sensor_instances[sensor_id].name), 'wb') as save_file:
                pickle.dump(self.sensor_instances[sensor_id], save_file)

        # Save fresnel analysis instances
        for analysis_id in self.fresnel_analysis_instances:
            with open(self.location + r'\Analysis instances' + r'\FM{id} {name}.pickle'.format(id=analysis_id, name=self.fresnel_analysis_instances[analysis_id].name), 'wb') as save_file:
                pickle.dump(self.fresnel_analysis_instances[analysis_id], save_file)

        # Save exclusion height analysis instances
        for analysis_id in self.exclusion_height_analysis_instances:
            with open(self.location + r'\Analysis instances' + r'\FM{id} {name}.pickle'.format(id=analysis_id, name=self.exclusion_height_analysis_instances[analysis_id].name), 'wb') as save_file:
                pickle.dump(self.exclusion_height_analysis_instances[analysis_id], save_file)

        return

    def save_session(self):

        # Save session object
        with open(self.location + r'\Session file (v{version_}).pickle'.format(version_=self.version.replace('.', '_')), 'wb') as save_file:
            pickle.dump(self, save_file)

        return

    def save_sensor(self, sensor_id):
        """
        Saves a single sensor object to the session.
        :return: None
        """

        with open(self.location + r'\Sensors' + r'\S{id} {name}.pickle'.format(id=sensor_id, name=self.sensor_instances[
            sensor_id].name), 'wb') as save_file:
            pickle.dump(self.sensor_instances[sensor_id], save_file)

        return

    def save_fresnel_analysis(self, analysis_id):
        """
        Saves a single fresnel analysis object to the session.
        :return: None
        """

        with open(self.location + r'\Analysis instances' + r'\FM{id} {name}.pickle'.format(id=analysis_id, name=self.fresnel_analysis_instances[analysis_id].name), 'wb') as save_file:
            pickle.dump(self.fresnel_analysis_instances[analysis_id], save_file)

        return

    def save_exclusion_height_analysis(self, analysis_id):
        """
        Saves a single fresnel analysis object to the session.
        :return: None
        """

        with open(self.location + r'\Analysis instances' + r'\EH{id} {name}.pickle'.format(id=analysis_id, name=self.exclusion_height_analysis_instances[analysis_id].name), 'wb') as save_file:
            pickle.dump(self.exclusion_height_analysis_instances[analysis_id], save_file)

        return

    def import_sensor(self):

        file_path_ = select_file(prompt='Select the sensor object', prompt_folder=self.location + r'\Sensors')
        self.sensor_ID_count += 1

        with open(file_path_, 'rb') as import_file:
            sensor_object = pickle.load(import_file)

        sensor_object.object_id = self.sensor_ID_count
        self.sensor_instances[self.sensor_ID_count] = sensor_object

        return

    def import_fresnel_analysis(self):
        file_path_ = select_file(prompt='Select the analysis object', prompt_folder=self.location + r'\Analysis instances')
        self.fresnel_analysis_ID_count += 1

        with open(file_path_, 'rb') as import_file:
            analysis_object = pickle.load(import_file)

        analysis_object.object_id = self.fresnel_analysis_ID_count
        self.fresnel_analysis_instances[analysis_object.object_id] = analysis_object

        return

    def import_exclusion_height_analysis(self):
        file_path_ = select_file(prompt='Select the analysis object', prompt_folder=self.location + r'\Analysis instances')
        self.exclusion_height_analysis_ID_count += 1

        with open(file_path_, 'rb') as import_file:
            analysis_object = pickle.load(import_file)

        analysis_object.object_id = self.exclusion_height_analysis_ID_count
        self.exclusion_height_analysis_instances[analysis_object.object_id] = analysis_object

        return


class Sensor:

    """
      An SPR measurement typically have some things in common, such as the sensor layers, measured angles,
    measured reflectivity, measurement time, etc. This information can be shared between different analysis methods for
    one measurement. This class serves as a basis for describing the current sensor, containing information about its
    layers and their optical properties.
    """

    def __init__(self, data_path_, object_id_, object_name_='Gold sensor', sensor_metal='Au', data_type='R'):

        # Load sensor's default optical properties
        self.object_id = object_id_
        self.name = object_name_
        self.data_path = data_path_
        self.data_type = data_type
        self.wavelength = int(data_path_[-9:-6])
        self.channel = data_path_[-12:-4].replace('_', ' ')
        self.sensor_metal = sensor_metal
        self.set_default_optical_properties(self.sensor_metal)
        self.fitted_var = self.optical_parameters.iloc[self.fitted_layer_index]

    def set_default_optical_properties(self, sensor_metal):

        # These default parameters should be set based on material layer and wavelength from loaded .csv file

        match sensor_metal:
            case 'Au' | 'gold' | 'Gold' | 'GOLD':
                self.layer_thicknesses = np.array([np.nan, 2.00, 50.00, np.nan])
                self.fitted_layer_index = (2, 3)  # Tuple with index for df.iloc[fitted_layer_index]
                match self.wavelength:
                    case 670:
                        self.refractive_indices = np.array([1.5202, 3.5295, 0.2238, 1.0003])
                        self.extinction_coefficients = np.array([0, 4.2683, 3.9259, 0])
                    case 785:
                        self.refractive_indices = np.array([1.5162, 3.9729, 0.2580, 1.0003])
                        self.extinction_coefficients = np.array([0, 4.1895, 4.88,  0])
                    case 850:
                        self.refractive_indices = np.array([1.5149, 4.1254, 0.2653, 1.0003])
                        self.extinction_coefficients = np.array([0, 4.1383, 5.5002, 0])
                    case 980:
                        self.refractive_indices = np.array([1.5130, 4.2797, 0.2800, 1.0003])
                        self.extinction_coefficients = np.array([0, 4.0770, 6.7406, 0])
                self.optical_parameters = pd.DataFrame(data={'Layers': ['Prism', 'Cr', 'Au', 'Bulk'],  # NOTE: sensor_object.optical_parameters will auto-update when changing sensor_object.layer_thicknesses, sensor_object.refractive_indices or sensor_object.extinction_coefficients
                                                             'd [nm]': self.layer_thicknesses,
                                                             'n': self.refractive_indices,
                                                             'k': self.extinction_coefficients})

            case 'sio2' | 'SiO2' | 'SIO2' | 'Glass' | 'glass' | 'silica':
                # Fused silica values source: L. V. Rodríguez-de Marcos, J. I. Larruquert, J. A. Méndez, J. A. Aznárez. Self-consistent optical constants of SiO2 and Ta2O5 films. Opt. Mater. Express 6, 3622-3637 (2016)
                self.layer_thicknesses = np.array([np.nan, 2.00, 50.00, 14.00, np.nan])
                self.fitted_layer_index = (3, 1)  # Tuple with index for df.iloc[fitted_layer_index]
                match self.wavelength:
                    case 670:
                        self.refractive_indices = np.array([1.5202, 3.5295, 0.2238, 1.4628, 1.0003])
                        self.extinction_coefficients = np.array([0, 4.2683, 3.9259, 0, 0])
                    case 785:
                        self.refractive_indices = np.array([1.5162, 3.9729, 0.2580, 1.4610, 1.0003])
                        self.extinction_coefficients = np.array([0, 4.1895, 4.88, 0, 0])
                    case 850:
                        self.refractive_indices = np.array([1.5149, 4.1254, 0.2653, 1.4603, 1.0003])
                        self.extinction_coefficients = np.array([0, 4.1383, 5.5002, 0, 0])
                    case 980:
                        self.refractive_indices = np.array([1.5130, 4.2797, 0.2800, 1.4592, 1.0003])
                        self.extinction_coefficients = np.array([0, 4.0770, 6.7406, 0, 0])
                self.optical_parameters = pd.DataFrame(data={'Layers': ['Prism', 'Cr', 'Au', 'SiO2', 'Bulk'],
                                                             'd [nm]': self.layer_thicknesses,
                                                             'n': self.refractive_indices,
                                                             'k': self.extinction_coefficients})

            case 'Pd' | 'palladium' | 'Palladium' | 'PALLADIUM':
                # Source Pd 670nm : Andersson, John, et al. "Surface plasmon resonance sensing with thin films of palladium and platinum–quantitative and real-time analysis." Physical Chemistry Chemical Physics 24.7 (2022): 4588-4594.
                # Source Pd 785nm, 980nm: Similar procedure as Andersson, John et al., but these were not reported.
                self.layer_thicknesses = np.array([np.nan, 2.00, 20.00, np.nan])
                self.fitted_layer_index = (2, 3)  # Tuple with index for df.iloc[fitted_layer_index]
                match self.wavelength:
                    case 670:
                        self.refractive_indices = np.array([1.5202, 3.5295, 2.25, 1.0003])
                        self.extinction_coefficients = np.array([0, 4.2683, 4.60, 0])
                    case 785:
                        self.refractive_indices = np.array([1.5162, 3.9729, 2.5467, 1.0003])
                        self.extinction_coefficients = np.array([0, 4.1895, 5.1250, 0])
                    case 850:
                        self.refractive_indices = np.array([1.5149, 4.1254, 2.7, 1.0003])  # Estimated values for Pd
                        self.extinction_coefficients = np.array([0, 4.1383, 5.7, 0])  # Estimated values for Pd
                    case 980:
                        self.refractive_indices = np.array([1.5130, 4.2797, 3.0331, 1.0003])
                        self.extinction_coefficients = np.array([0, 4.0770, 6.1010, 0])
                self.optical_parameters = pd.DataFrame(data={'Layers': ['Prism', 'Cr', 'Pd', 'Bulk'],
                                                             'd [nm]': self.layer_thicknesses,
                                                             'n': self.refractive_indices,
                                                             'k': self.extinction_coefficients})

            case 'Pt' | 'platinum' | 'Platinum' | 'PLATINUM':
                # Source Pt 670 nm: Andersson, John, et al. "Surface plasmon resonance sensing with thin films of palladium and platinum–quantitative and real-time analysis." Physical Chemistry Chemical Physics 24.7 (2022): 4588-4594.
                # Source Pt 785, 850 and 980 nm: W. S. M. Werner, K. Glantschnig, C. Ambrosch-Draxl. Optical constants and inelastic electron-scattering data for 17 elemental metals, J. Phys Chem Ref. Data 38, 1013-1092 (2009)
                self.layer_thicknesses = np.array([np.nan, 2.00, 20.00, np.nan])
                self.fitted_layer_index = (2, 3)  # Tuple with index for df.iloc[fitted_layer_index]
                match self.wavelength:
                    case 670:
                        self.refractive_indices = np.array([1.5202, 3.5295, 2.47, 1.0003])
                        self.extinction_coefficients = np.array([0, 4.2683, 5.28, 0])
                    case 785:
                        self.refractive_indices = np.array([1.5162, 3.9729, 2.5254, 1.0003])
                        self.extinction_coefficients = np.array([0, 4.1895, 5.6380, 0])
                    case 850:
                        self.refractive_indices = np.array([1.5149, 4.1254, 2.7193, 1.0003])
                        self.extinction_coefficients = np.array([0, 4.1383, 5.9555, 0])
                    case 980:
                        self.refractive_indices = np.array([1.5130, 4.2797, 3.0598, 1.0003])
                        self.extinction_coefficients = np.array([0, 4.0770, 6.4912, 0])
                self.optical_parameters = pd.DataFrame(data={'Layers': ['Prism', 'Cr', 'Pt', 'Bulk'],
                                                             'd [nm]': self.layer_thicknesses,
                                                             'n': self.refractive_indices,
                                                             'k': self.extinction_coefficients})
        return


class FresnelModel:
    """
    This class defines how a modelled reflectivity trace behaves.

    TODO: Each object should also have a .csv export function.

    """

    def __init__(self, sensor_object_, data_path_, reflectivity_df_, TIR_range_, scanspeed_, object_id_, object_name_):
        self.name = object_name_
        self.object_id = object_id_
        self.sensor_object = sensor_object_
        self.sensor_object_label = ''
        self.initial_data_path = data_path_
        self.measurement_data = reflectivity_df_
        self.TIR_range = TIR_range_  # Default for air. For water: (60.8, 63)
        self.scanspeed = scanspeed_  # Scan speed from .spr2 file, 1 (slow), 5 (medium) or 10 (fast)
        self.angle_range = [40, 80]
        self.polarization = 1.0  # 0-1, for degree of s (=0) and p(=1) polarization,
        self.ini_guess = np.array(4)
        self.bounds = [0, 50]  # or [(lb1, lb2), (ub1, ub2)] etc
        self.extinction_correction = 0
        self.y_offset = 0
        self.fit_offset = True
        self.fit_prism_k = True
        self.fitted_data = None
        self.fitted_result = None
        self.fitted_layer_index = copy.deepcopy(self.sensor_object.fitted_layer_index)  # Deepcopy to not overwrite if fitting multiple layers in the same sensor object
        self.fitted_layer = copy.deepcopy(self.sensor_object.optical_parameters.iloc[self.fitted_layer_index[0], 0])

    def calculate_fresnel_trace(self):

        fresnel_coefficients_ = fresnel_calculation(None,
                                                    angles=self.angle_range,
                                                    fitted_layer_index=self.sensor_object.fitted_layer_index,
                                                    wavelength=self.sensor_object.wavelength,
                                                    layer_thicknesses=self.sensor_object.layer_thicknesses,
                                                    n_re=self.sensor_object.refractive_indices,
                                                    n_im=self.sensor_object.extinction_coefficients,
                                                    ydata=None,
                                                    ydata_type=self.sensor_object.data_type,
                                                    polarization=self.polarization)
        return fresnel_coefficients_

    def model_reflectivity_trace(self):

        xdata_ = self.measurement_data['angles']
        ydata_ = self.measurement_data['ydata']

        # Calculate TIR angle and bulk refractive index
        TIR_angle, TIR_fitted_angles, TIR_fitted_ydata = TIR_determination(xdata_, ydata_, self.TIR_range, self.scanspeed)
        self.sensor_object.refractive_indices[-1] = self.sensor_object.refractive_indices[0] * np.sin(np.pi / 180 * TIR_angle)

        # Add extinction correction to fitted surface layer extinction value
        self.sensor_object.extinction_coefficients[0] += self.extinction_correction  # Manually correct prism layer extinction

        # Selecting a range of measurement data to use for fitting, and including an offset in reflectivity (iterated 3 times)
        selection_xdata_ = xdata_[(xdata_ >= self.angle_range[0]) & (xdata_ <= self.angle_range[1])]
        selection_ydata_ = ydata_[(xdata_ >= self.angle_range[0]) & (xdata_ <= self.angle_range[1])]

        # Weighing options
        weights = None

        # weights_ = np.abs(np.diff(selection_ydata_))+1  # Highest derivative
        # weights = np.append(weights_, 0)

        # weights = 1/selection_ydata_

        # weights = np.ones(len(selection_ydata_))
        # weights[selection_ydata_.argmin():-1] = 2

        # Perform the first fitting
        result = scipy.optimize.least_squares(fresnel_calculation,
                                              self.ini_guess,
                                              bounds=self.bounds,
                                              kwargs={'fitted_layer_index': self.sensor_object.fitted_layer_index,
                                                      'wavelength': self.sensor_object.wavelength,
                                                      'layer_thicknesses': self.sensor_object.layer_thicknesses,
                                                      'n_re': self.sensor_object.refractive_indices,
                                                      'n_im': self.sensor_object.extinction_coefficients,
                                                      'angles': selection_xdata_,
                                                      'ydata': selection_ydata_,
                                                      'weights': weights,
                                                      'ydata_type': self.sensor_object.data_type,
                                                      'polarization': self.polarization,
                                                      'ydata_offset': self.y_offset},
                                              loss='huber',
                                              ftol=1e-12,
                                              xtol=1e-12,
                                              gtol=1e-12)

        # Collect the results from least_squares object and calculate corresponding fresnel coefficients
        self.fitted_result = np.array(result['x'])

        if self.fit_offset:
            self.y_offset = self.fitted_result[1]
        else:
            self.y_offset = 0

        fresnel_coefficients = fresnel_calculation(self.fitted_result,
                                                   fitted_layer_index=self.sensor_object.fitted_layer_index,
                                                   angles=selection_xdata_,
                                                   wavelength=self.sensor_object.wavelength,
                                                   layer_thicknesses=self.sensor_object.layer_thicknesses,
                                                   n_re=self.sensor_object.refractive_indices,
                                                   n_im=self.sensor_object.extinction_coefficients,
                                                   ydata=None,
                                                   weights=weights,
                                                   ydata_type='R',
                                                   polarization=self.polarization,
                                                   ydata_offset=self.y_offset
                                                   )

        # Compile into fresnel_coefficients data frame
        self.fitted_data = pd.DataFrame(data={'angles': selection_xdata_, 'ydata': fresnel_coefficients})

        return self.fitted_data

    def export_fitted_results(self):
        """
        Exporting the result (including parameters) of a particular analysis as a .csv file
        :return:
        """
        pass

    def export_calculated_results(self):
        """
        Exporting the calculated fresnel traces (including parameters) of a particular analysis as a .csv file
        :return:
        """
        pass


class ExclusionHeight:

    """
        This class defines an analysis object for determining the exclusion height from measurement data with probe
        injections. The underlying method is described as the "non-interacting probe method" in the literature.
    """

    def __init__(self, fresnel_object_, sensorgram_df_, data_path_,  object_id_, object_name_):
        self.name = object_name_
        self.object_id = object_id_
        self.fresnel_object = fresnel_object_
        self.fresnel_object_label = 'Fresnel background: FM{analysis_number} {analysis_name}'.format(
                                                                    analysis_number=fresnel_object_.object_id,
                                                                    analysis_name=fresnel_object_.name)
        self.sensor_object = fresnel_object_.sensor_object
        self.polarization = fresnel_object_.polarization
        self.initial_data_path = data_path_
        self.sensorgram_data = sensorgram_df_
        self.sensorgram_offset_ind = 0
        self.d_n_pair_resolution = 200
        self.height_steps = np.linspace(0, 200, self.d_n_pair_resolution)
        self.points_below_SPR_min_ind = None
        self.points_above_SPR_min_ind = None
        self.injection_points = []
        self.buffer_points = []
        self.probe_points = []
        self.SPR_vs_TIR_dfs = []  # List of dataframes with labels 'SPR angles' and 'TIR angles' for indexing each step result
        self.buffer_reflectivity_dfs = []  # Use labels 'buffer reflectivity' and 'buffer angles' (and likewise probe) for indexing
        self.buffer_bulk_RIs = []  # Calculated from TIR angle of each reflectivity DF
        self.probe_reflectivity_dfs = []  # Use labels 'buffer reflectivity' and 'buffer angles' (and likewise probe) for indexing
        self.probe_bulk_RIs = []  # Calculated from TIR angle of each reflectivity DF
        self.d_n_pair_dfs = []  # Use labels 'height' and 'buffer RI' and 'probe RI' for indexing
        self.all_exclusion_results = []
        self.mean_exclusion_height_result = None  # Tuple of mean value of exclusion height from all injection steps, and standard deviation
        self.mean_exclusion_RI_result = None  # Tuple of mean value of exclusion RI from all injection steps, and standard deviation
        self.abort_flag = False
        self.fit_offset = False
        self.fit_prism = False

    def initialize_model(self, ydata_df):

        # Calculate number of points above and below minimum point based on fresnel model background range
        background_reflectivity = self.fresnel_object.measurement_data['ydata']
        background_angles = self.fresnel_object.measurement_data['angles']
        selection_criterion = (background_angles >= self.fresnel_object.angle_range[0]) & (background_angles <= self.fresnel_object.angle_range[1])
        selection_ydata_series = background_reflectivity[selection_criterion]
        smoothened_selection = bottleneck.move_mean(selection_ydata_series.to_numpy(), window=4, min_count=1)  # Ensures closer fit to minimum position
        smoothened_selection_series = pd.Series(smoothened_selection)
        self.points_below_SPR_min_ind = len(smoothened_selection_series[(smoothened_selection_series.index < smoothened_selection_series.idxmin())])
        self.points_above_SPR_min_ind = len(smoothened_selection_series[(smoothened_selection_series.index > smoothened_selection_series.idxmin())])

        # Overwrite previous probe and buffer reflectivity data frames and bulk RI lists and SPR vs TIR data frames
        self.buffer_reflectivity_dfs = []
        self.buffer_bulk_RIs = []
        self.probe_reflectivity_dfs = []
        self.probe_bulk_RIs = []
        self.SPR_vs_TIR_dfs = []

        # Calculate average reflectivity traces based on selected points
        bufferpoint_index = 0
        for reflectivity_index in range(int(len(self.buffer_points) / 2)):

            sliced_buffer_reflectivity_spectras = ydata_df.iloc[self.buffer_points[bufferpoint_index][0]:self.buffer_points[bufferpoint_index + 1][0], :]  # Selecting all spectras between the pairwise selected buffer points
            mean_buffer_reflectivity = sliced_buffer_reflectivity_spectras.mean(axis=0).squeeze()

            # Calculate TIR and bulk RI for each mean spectra
            try:
                buffer_TIR_angle, _, _ = TIR_determination(background_angles.to_numpy(), mean_buffer_reflectivity.to_numpy(), self.fresnel_object.TIR_range, self.fresnel_object.scanspeed)
            except TypeError:
                raise TypeError('Something went wrong when selecting buffer points. Please clear and reselect them and avoid clicking other point markers.')
            self.buffer_bulk_RIs.append(self.sensor_object.refractive_indices[0] * np.sin(np.pi / 180 * buffer_TIR_angle))

            # Calculate appropriate range selection
            buffer_reflectivity_minimum_ind = pd.Series(bottleneck.move_mean(mean_buffer_reflectivity.to_numpy(), window=4, min_count=1)).idxmin()
            self.buffer_reflectivity_dfs.append(pd.DataFrame(data={'reflectivity': mean_buffer_reflectivity.iloc[buffer_reflectivity_minimum_ind - self.points_below_SPR_min_ind:buffer_reflectivity_minimum_ind + self.points_above_SPR_min_ind],
                                                                   'angles': background_angles.iloc[buffer_reflectivity_minimum_ind - self.points_below_SPR_min_ind:buffer_reflectivity_minimum_ind + self.points_above_SPR_min_ind]
                                                                   })
                                                )

            # Next pair of buffer point indices
            bufferpoint_index += 2

        probepoint_index = 0
        for reflectivity_index in range(int(len(self.probe_points) / 2)):
            sliced_probe_reflectivity_spectras = ydata_df.iloc[self.probe_points[probepoint_index][0]:self.probe_points[probepoint_index + 1][0], :]  # Selecting all spectras between the pairwise selected probe point
            mean_probe_reflectivity = sliced_probe_reflectivity_spectras.mean(axis=0).squeeze()

            # Calculate TIR and bulk RI for each mean spectra
            try:
                probe_TIR_angle, _, _ = TIR_determination(background_angles.to_numpy(), mean_probe_reflectivity.to_numpy(), self.fresnel_object.TIR_range, self.fresnel_object.scanspeed)
            except TypeError:
                raise TypeError('Something went wrong when selecting probe points. Please clear and reselect them and avoid clicking other point markers.')
            self.probe_bulk_RIs.append(self.sensor_object.refractive_indices[0] * np.sin(np.pi / 180 * probe_TIR_angle))

            # Calculate appropriate range selection
            probe_reflectivity_minimum_ind = pd.Series(bottleneck.move_mean(mean_probe_reflectivity.to_numpy(), window=4, min_count=1)).idxmin()
            self.probe_reflectivity_dfs.append(pd.DataFrame(data={'reflectivity': mean_probe_reflectivity.iloc[probe_reflectivity_minimum_ind - self.points_below_SPR_min_ind:probe_reflectivity_minimum_ind + self.points_above_SPR_min_ind],
                                                                  'angles': background_angles.iloc[probe_reflectivity_minimum_ind - self.points_below_SPR_min_ind:probe_reflectivity_minimum_ind + self.points_above_SPR_min_ind]
                                                                  })
                                               )

            # Next pair of probe point indices
            probepoint_index += 2

        # Create SPR vs TIR data frames
        injectionpoint_index = 0
        offset_SPR_sensorgram = self.sensorgram_data['SPR angle'] - self.sensorgram_data.loc[self.sensorgram_offset_ind, 'SPR angle']
        offset_TIR_sensorgram = self.sensorgram_data['TIR angle'] - self.sensorgram_data.loc[self.sensorgram_offset_ind, 'TIR angle']

        for reflectivity_index in range(int(len(self.injection_points) / 2)):

            self.SPR_vs_TIR_dfs.append(pd.DataFrame(data={'SPR angles': offset_SPR_sensorgram.iloc[self.injection_points[injectionpoint_index][0]:self.injection_points[injectionpoint_index + 1][0]],
                                                          'TIR angles': offset_TIR_sensorgram.iloc[self.injection_points[injectionpoint_index][0]:self.injection_points[injectionpoint_index + 1][0]],
                                                          })
                                       )

            # Next pair of injection point indices
            injectionpoint_index += 2

        return


def calculate_exclusion_height(exclusion_height_analysis_object_copy, buffer_or_probe_flag, data_frame_index):
    """
    This function calculates the exclusion height for a single injection step

    :param exclusion_height_analysis_object_copy: object containing all parameters and data
    :param buffer_or_probe_flag: either 'buffer' or 'probe'
    :param data_frame_index: index of dataframe and buffer or probe RI bulk value
    :return RI_results: list of calculated RI results for each height step
    """

    # Adapt new initial guess and bounds for refractive index range
    RI_results = []
    offset_results = []
    prism_k_results = []
    if not exclusion_height_analysis_object_copy.fit_offset:
        exclusion_new_fresnel_ini_guess = 1.38  # Swollen layer estimated hydration
        exclusion_new_fresnel_bounds = [1.0, 3.0]

    elif exclusion_height_analysis_object_copy.fit_offset and not exclusion_height_analysis_object_copy.fit_prism:
        exclusion_new_fresnel_ini_guess = exclusion_height_analysis_object_copy.fresnel_object.ini_guess[0:2]
        exclusion_new_fresnel_ini_guess[0] = 1.38  # Swollen layer estimated hydration
        exclusion_new_fresnel_bounds = [(1.0, -np.inf), (3.0, np.inf)]

    elif exclusion_height_analysis_object_copy.fit_offset and exclusion_height_analysis_object_copy.fit_prism:
        if len(exclusion_height_analysis_object_copy.fresnel_object.ini_guess) == 3:
            exclusion_new_fresnel_ini_guess = exclusion_height_analysis_object_copy.fresnel_object.ini_guess
        elif len(exclusion_height_analysis_object_copy.fresnel_object.ini_guess) == 2:
            exclusion_new_fresnel_ini_guess = [exclusion_height_analysis_object_copy.fresnel_object.ini_guess, 0.01]
        exclusion_new_fresnel_ini_guess[0] = 1.38  # Swollen layer estimated hydration
        exclusion_new_fresnel_bounds = [(1.0, -np.inf, 0), (3.0, np.inf, 0.1)]

    # Check if calculations should be performed on buffer or probe data
    if buffer_or_probe_flag == 'buffer':

        # Add bulk RI to layers
        refractive_indices = exclusion_height_analysis_object_copy.sensor_object.refractive_indices
        refractive_indices[-1] = exclusion_height_analysis_object_copy.buffer_bulk_RIs[data_frame_index]

        for height in exclusion_height_analysis_object_copy.height_steps:

            exclusion_height_analysis_object_copy.sensor_object.layer_thicknesses[-2] = height  # Surface layer height should be updated to current height step

            # Perform the fitting
            result = scipy.optimize.least_squares(fresnel_calculation,
                                                  exclusion_new_fresnel_ini_guess,
                                                  bounds=exclusion_new_fresnel_bounds,
                                                  kwargs={'fitted_layer_index': (-2, 2),  # Should always be the RI of the surface layer
                                                          'wavelength': exclusion_height_analysis_object_copy.sensor_object.wavelength,
                                                          'layer_thicknesses': exclusion_height_analysis_object_copy.sensor_object.layer_thicknesses,
                                                          'n_re': refractive_indices,
                                                          'n_im': exclusion_height_analysis_object_copy.sensor_object.extinction_coefficients,
                                                          'angles': exclusion_height_analysis_object_copy.buffer_reflectivity_dfs[data_frame_index]['angles'].to_numpy(),
                                                          'ydata': exclusion_height_analysis_object_copy.buffer_reflectivity_dfs[data_frame_index]['reflectivity'].to_numpy(),
                                                          'ydata_type': exclusion_height_analysis_object_copy.sensor_object.data_type,
                                                          'ydata_offset': exclusion_height_analysis_object_copy.fresnel_object.y_offset,
                                                          'polarization': exclusion_height_analysis_object_copy.polarization}
                                                  )
            # Collect the results from least_squares object
            RI_results.append(result['x'][0])

            if exclusion_height_analysis_object_copy.fit_offset and not exclusion_height_analysis_object_copy.fit_prism:
                offset_results.append(result['x'][1])

            elif exclusion_height_analysis_object_copy.fit_offset and exclusion_height_analysis_object_copy.fit_prism:
                offset_results.append(result['x'][1])
                prism_k_results.append(result['x'][2])

        return [RI_results, offset_results, prism_k_results]

    elif buffer_or_probe_flag == 'probe':

        # Add bulk RI to layers
        refractive_indices = exclusion_height_analysis_object_copy.sensor_object.refractive_indices
        refractive_indices[-1] = exclusion_height_analysis_object_copy.probe_bulk_RIs[data_frame_index]

        for height in exclusion_height_analysis_object_copy.height_steps:

            exclusion_height_analysis_object_copy.sensor_object.layer_thicknesses[-2] = height

            result = scipy.optimize.least_squares(fresnel_calculation,
                                                  exclusion_new_fresnel_ini_guess,
                                                  bounds=exclusion_new_fresnel_bounds,
                                                  kwargs={'fitted_layer_index': (-2, 2),  # Should always be the RI of the surface layer
                                                          'wavelength': exclusion_height_analysis_object_copy.sensor_object.wavelength,
                                                          'layer_thicknesses': exclusion_height_analysis_object_copy.sensor_object.layer_thicknesses,
                                                          'n_re': refractive_indices,
                                                          'n_im': exclusion_height_analysis_object_copy.sensor_object.extinction_coefficients,
                                                          'angles': exclusion_height_analysis_object_copy.probe_reflectivity_dfs[data_frame_index]['angles'].to_numpy(),
                                                          'ydata': exclusion_height_analysis_object_copy.probe_reflectivity_dfs[data_frame_index]['reflectivity'].to_numpy(),
                                                          'ydata_type': exclusion_height_analysis_object_copy.sensor_object.data_type,
                                                          'ydata_offset': exclusion_height_analysis_object_copy.fresnel_object.y_offset,
                                                          'polarization': exclusion_height_analysis_object_copy.polarization}
                                                  )
            # Collect the results from least_squares object
            RI_results.append(result['x'][0])

            if exclusion_height_analysis_object_copy.fit_offset and not exclusion_height_analysis_object_copy.fit_prism:
                offset_results.append(result['x'][1])

            elif exclusion_height_analysis_object_copy.fit_offset and exclusion_height_analysis_object_copy.fit_prism:
                offset_results.append(result['x'][1])
                prism_k_results.append(result['x'][2])

        return [RI_results, offset_results, prism_k_results]

    else:
        raise ValueError('Only buffer or probe allowed')


def exclusion_height_process(exclusion_height_analysis_object_copy, buffer_or_probe_flag, data_frame_index, connection):
    """
    This function initiates the calculations and sends back the result

    :param exclusion_height_analysis_object_copy: object containing all parameters and data
    :param buffer_or_probe_flag: either 'buffer' or 'probe'
    :param data_frame_index: index of dataframe
    :param connection: child pipe connection object from multiprocessing.Pipe()
    :return: None
    """

    result = calculate_exclusion_height(exclusion_height_analysis_object_copy, buffer_or_probe_flag, data_frame_index)
    connection.send(result)
    connection.close()


def process_all_exclusion_heights(exclusion_height_analysis_object, logical_cores):

    buffer_connections = []
    probe_connections = []
    buffer_processes = []
    probe_processes = []

    buffer_index = 0
    probe_index = 0
    process_step = 0
    required_processes = int(len(exclusion_height_analysis_object.injection_points) + len(exclusion_height_analysis_object.injection_points) / 2)

    while process_step < min(required_processes, logical_cores):

        # Setup buffer process
        buffer_parent_conn, buffer_child_conn = multiprocessing.Pipe()
        buffer_connections.append(buffer_parent_conn)
        buffer_process = multiprocessing.Process(target=exclusion_height_process, args=(copy.deepcopy(exclusion_height_analysis_object), 'buffer', buffer_index, buffer_child_conn))
        buffer_processes.append(buffer_process)
        buffer_process.start()
        buffer_index += 1
        process_step += 1

        # Setup probe process
        if buffer_index % 2 == 0:
            probe_parent_conn, probe_child_conn = multiprocessing.Pipe()
            probe_connections.append(probe_parent_conn)
            probe_process = multiprocessing.Process(target=exclusion_height_process, args=(copy.deepcopy(exclusion_height_analysis_object), 'probe', probe_index, probe_child_conn))
            probe_processes.append(probe_process)
            probe_process.start()
            probe_index += 1
            process_step += 1

    # If there are remaining processes, wait for the next two processes to finish and start new processes for the remaining steps
    process_index = 0
    while process_step < required_processes:
        buffer_processes[process_index].join()

        # Setup buffer process
        buffer_parent_conn, buffer_child_conn = multiprocessing.Pipe()
        buffer_connections.append(buffer_parent_conn)
        buffer_process = multiprocessing.Process(target=exclusion_height_process, args=(copy.deepcopy(exclusion_height_analysis_object), 'buffer', buffer_index, buffer_child_conn))
        buffer_processes.append(buffer_process)
        buffer_process.start()
        buffer_index += 1
        process_step += 1

        if buffer_index % 2 == 0:
            probe_processes[int(process_index/2)].join()

            # Setup probe process
            probe_parent_conn, probe_child_conn = multiprocessing.Pipe()
            probe_connections.append(probe_parent_conn)
            probe_process = multiprocessing.Process(target=exclusion_height_process, args=(copy.deepcopy(exclusion_height_analysis_object), 'probe', probe_index, probe_child_conn))
            probe_processes.append(probe_process)
            probe_process.start()
            probe_index += 1
            process_step += 1

        process_index += 1

    # Wait for each process to finish and collect and record results
    for process_index in range(len(buffer_processes)):

        # Check if user has aborted the analysis
        if exclusion_height_analysis_object.abort_flag:
            for buffer_process in buffer_processes:
                buffer_process.terminate()
            for probe_process in probe_processes:
                probe_process.terminate()

            exclusion_height_analysis_object.abort_flag = False

            return

        # Wait for processes to finish and collect results
        buffer_processes[process_index].join()
        full_buffer_result = buffer_connections[process_index].recv()
        buffer_RI_result = full_buffer_result[0]

        if process_index % 2 == 0:
            probe_processes[int(process_index/2)].join()
            full_probe_result = probe_connections[int(process_index/2)].recv()
            probe_RI_result = full_probe_result[0]

        if not exclusion_height_analysis_object.fit_offset:
            exclusion_height_analysis_object.d_n_pair_dfs[process_index] = pd.DataFrame(data={'height': exclusion_height_analysis_object.height_steps, 'buffer RI': buffer_RI_result, 'probe RI': probe_RI_result})
        elif exclusion_height_analysis_object.fit_offset and not exclusion_height_analysis_object.fit_prism:
            exclusion_height_analysis_object.d_n_pair_dfs[process_index] = pd.DataFrame(data={'height': exclusion_height_analysis_object.height_steps, 'buffer RI': buffer_RI_result, 'probe RI': probe_RI_result, 'buffer offsets': full_buffer_result[1], 'probe offsets': full_probe_result[1]})
        elif exclusion_height_analysis_object.fit_offset and exclusion_height_analysis_object.fit_prism:
            exclusion_height_analysis_object.d_n_pair_dfs[process_index] = pd.DataFrame(data={'height': exclusion_height_analysis_object.height_steps, 'buffer RI': buffer_RI_result, 'probe RI': probe_RI_result, 'buffer offsets': full_buffer_result[1], 'probe offsets': full_probe_result[1], 'buffer prism k': full_buffer_result[2], 'probe prism k': full_probe_result[2]})

        # Calculate exclusion height from buffer and probe height steps and RI result intersection and add to exclusion_height_analysis_object.all_exclusion_results
        for height_ind in range(len(exclusion_height_analysis_object.height_steps)):
            if buffer_RI_result[height_ind] < probe_RI_result[height_ind]:

                buffer_RI_zoom_range = np.linspace(buffer_RI_result[height_ind - 1], buffer_RI_result[height_ind], 200)
                probe_RI_zoom_range = np.linspace(probe_RI_result[height_ind - 1], probe_RI_result[height_ind], 200)
                height_zoom_range = np.linspace(exclusion_height_analysis_object.height_steps[height_ind - 1], exclusion_height_analysis_object.height_steps[height_ind], 200)

                # Zoom in on the intersection
                for index in range(200):
                    if buffer_RI_zoom_range[index] < probe_RI_zoom_range[index]:
                        exclusion_height_analysis_object.all_exclusion_results[0, process_index] = height_zoom_range[index]
                        exclusion_height_analysis_object.all_exclusion_results[1, process_index] = buffer_RI_zoom_range[index]
                        break

                # Stop looping through height steps
                break

    # Replace zeros with NaNs for non-intersecting results
    exclusion_height_analysis_object.all_exclusion_results = np.where(exclusion_height_analysis_object.all_exclusion_results == 0, np.nan, exclusion_height_analysis_object.all_exclusion_results)

    return


def add_sensor_backend(session_object, data_path_, sensor_metal='Au'):

    """
    Adds sensor objects to a session object.
    :return: a sensor object
    """
    session_object.sensor_ID_count += 1
    sensor_object = Sensor(data_path_, session_object.sensor_ID_count, sensor_metal=sensor_metal)
    session_object.sensor_instances[session_object.sensor_ID_count] = sensor_object

    return sensor_object


def copy_sensor_backend(session_object, sensor_object):

    """
    Copies sensor object to a session object.
    :return: a sensor object
    """
    session_object.sensor_ID_count += 1
    copied_sensor_object = copy.deepcopy(sensor_object)
    copied_sensor_object.object_id = session_object.sensor_ID_count
    session_object.sensor_instances[session_object.sensor_ID_count] = copied_sensor_object

    return copied_sensor_object


def add_fresnel_model_object(session_object, sensor_object, data_path_, reflectivity_df_, TIR_range_, scanspeed_, object_name_):
    """
    Adds analysis objects to a session object.
    :return: an analysis object
    """
    session_object.fresnel_analysis_ID_count += 1
    analysis_object = FresnelModel(sensor_object, data_path_, reflectivity_df_, TIR_range_, scanspeed_, session_object.fresnel_analysis_ID_count, object_name_)
    session_object.fresnel_analysis_instances[session_object.fresnel_analysis_ID_count] = analysis_object

    return analysis_object


def add_exclusion_height_object(session_object, fresnel_object, sensorgram_df_, data_path_, object_name_):
    """
    Adds analysis objects to a session object.
    :return: an analysis object
    """
    session_object.exclusion_height_analysis_ID_count += 1
    analysis_object = ExclusionHeight(fresnel_object, sensorgram_df_, data_path_, session_object.exclusion_height_analysis_ID_count, object_name_)
    session_object.exclusion_height_analysis_instances[session_object.exclusion_height_analysis_ID_count] = analysis_object

    return analysis_object
