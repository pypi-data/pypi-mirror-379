#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""Class for managing database of simulated AFBF with random topothesy
and Hurst functions.

.. codeauthor:: Frédéric Richard <frederic.richard_at_univ-amu.fr>
"""
import os
import time
import yaml
import pickle
from afbf.utilities import seed, set_state, get_state
from afbf.utilities import zeros
from afbf import tbfield, perfunction, sdata, coordinates
from afbf.Classes.SpatialData import LoadSdata
from afbf.Simulation.TurningBands import LoadTBField


class protocol:
    """This class enables to manage and build database.

    :param str rep: Path to the data directory.
    :param int M:
        Number of parameters for the Hurst and topothesy functions.
    :param str smode_cst:
        Mode of simulation of the Hurst and topothesy function.
    :param float Hmin:
        Minimal value of the Hurst index in :math:`(0, 1)`.
    :param float Hmax:
        Maximal value of the Hurst index in :math:`(0, 1)`.
    :param str smode_int:
        Mode of simulation of the intervals of the Hurst function.
    :param float dint:
        Minimal interval lenght of the Hurst function steps.
    :param int K: Number of turning bands.
    :param int N: image size.
    """

    def __init__(self, rep="../data/SimulationSet_001"):
        """Set the protocol.

        :param str rep: Path to the data directory.
        """
        self.rep = rep
        if os.path.isfile(self.rep + "/setting.yaml"):
            self.LoadSetting()
        else:
            raise Exception("Configuration file is missing.")

        if "step" not in self.params_model['ftype']:
            raise Exception("Only step functions are supported.")

        if self.params_model['fname'] == 'efbf' or\
                self.params_model['fname'] == 'fbf':
            # Predefined fields.
            self.field = tbfield(self.params_model['fname'])
            self.params_model['M'] = self.field.hurst.fparam.size
        else:
            # Customed fields.
            hurst = perfunction(self.params_model['ftype'],
                                self.params_model['M'],
                                'Hurst')
            topo = perfunction(self.params_model['ftype'],
                               self.params_model['M'],
                               'Topothesy')
            self.field = tbfield("Field", topo, hurst)
        # Turning band initialization.
        self.field.InitTurningBands(self.params_images['K'])
        # Image definition.
        self.coord = coordinates(self.params_images['N'])  # Image coordinates.
        self.X = sdata()
        self.X.coord = self.coord
        self.X.name = "Example"

        # Set Random state
        self.SetRandomState()
        # Check the database consistency and repair.
        self.CheckConsistency()
        # Display the setting.
        self.DisplaySetting()

        # Feature dictionary
        self.feature_names = {
            0: "H",
            1: "Hurst_argmin_length",
            2: "Hurst_argmin_center",
            3: "Hmax"
        }

    def DisplaySetting(self):
        """Display the setting of the protocol.
        """
        print("Protocol:")
        print("Directory:" + self.rep)
        print("Number of examples: %d" % (self.nbexpe))
        print("Image size: %d x %d" % (self.params_images['N'],
                                       self.params_images['N']))
        print("Hurst function:")
        print("Type:" + self.params_model['ftype'])
        print("Number of parameters: %d" % (self.params_model['M']))
        print("Step constant sampling: " + self.params_model['smode_cst'])
        print("Step interval sampling: " + self.params_model['smode_int'])
        print("Minimal Hurst value: %-3.2f" % (self.params_model['Hmin']))
        print("Maximal Hurst value: %-3.2f" % (self.params_model['Hmax']))
        print("Minimal inter-step lenght: %3.2f" % (self.params_model['dint']))

    def LoadSetting(self):
        """Load the protocol setting.
        """
        with open(self.rep + "/setting.yaml", 'r') as stream:
            config = yaml.safe_load(stream)
        self.params_model = config['model']
        self.params_images = config['images']

    def MissingData(self, n):
        """Check if data is missing for an example.

        :param int n:
            Number of the example.
        """
        filename = self.SetFileName(n)
        if os.path.isfile(filename + "-hurst.pickle") and\
            os.path.isfile(filename + "-topo.pickle") and\
                os.path.isfile(filename + "-features.pickle"):
            return False
        else:
            return True

    def CheckConsistency(self):
        """Check the consistency of the database.
        """
        examples = []
        files = os.listdir(self.rep)
        # List of examples.
        for j in range(len(files)):
            file = files[j]
            if file.find("example") >= 0:
                n = int(file[8:14])
                examples.append(n)

        self.nbexpe = max(examples)
        # Check if data is missing and, if so, complete the database.
        for ex in range(self.nbexpe):
            if self.MissingData(ex):
                print('Warning: missing example ', n)
                self.CreateFields(expe_start=ex, expe_end=ex+1)

    def SetExampleNumberStr(self, n):
        """Set the number of the example in an str format.
        """
        return str(1000000 + n)[1:]

    def SetFileName(self, n):
        """Set the name of the file of an example.
        """
        numberstr = self.SetExampleNumberStr(n)
        filename = self.rep + "/example-" + numberstr

        return filename

    def LoadExample(self, n):
        """Load an example.

        :param int n: The index of the example.
        """
        if n >= self.nbexpe:
            raise Exception(f"LoadExample: index {n} out of bounds.")

        self.n = n
        filename = self.SetFileName(n)
        self.field = LoadTBField(filename)
        self.X = LoadSdata(filename + "-image")
        with open(filename + "-features.pickle", "rb") as f:
            Z = pickle.load(f)
        self.field.H = Z[0]
        self.field.hurst_argmin_lenght = Z[1]
        self.field.hurst_argmin_center = Z[2]
        self.field.Hmax = Z[3] + Z[0]

    def SaveExample(self, n):
        """Save an example in pickle file.

        :param int n: The index of the example.
        """
        filename = self.SetFileName(n)
        self.X.Save(filename + "-image")
        self.field.Save(filename)
        with open(filename + "-features.pickle", "wb") as f:
            pickle.dump([self.field.H,
                         self.field.hurst_argmin_lenght,
                         self.field.hurst_argmin_center,
                         self.field.Hmax - self.field.H], f)

    def ShowExample(self, n):
        """Show an example.

        :param int n: The index of the example.
        """
        self.LoadExample(n)
        self.field.DisplayParameters(3 * n + 1)
        self.X.Display(3 * n + 3)
        print("Example %d" % (self.n))
        print("Hurst-related parameters:")
        print("min=%3.2f, argmin length=%3.2f, center=%3.2f, Hmax=%3.2f"
              % (self.field.H, self.field.hurst_argmin_lenght,
                 self.field.hurst_argmin_center, self.field.Hmax))

    def SetRandomState(self):
        """Set the random state used for simulations.
        """
        filename = self.rep + "/randomstate.pickle"
        if os.path.isfile(filename):
            with open(filename, "rb") as f:
                Z = pickle.load(f)
                set_state(Z[0])
        else:
            rs = get_state()
            with open(self.rep + "/randomstate.pickle", "wb") as f:
                pickle.dump([rs], f)
            set_state(rs)

    def IterateFields(self, expe_start=None, expe_end=None, _create=True):
        """Iterate to create new examples or visualize existing ones.
        """
        if expe_start is None:
            expe_start = 0
        if expe_end is None:
            expe_end = self.nbexpe
        if _create:
            # Create new examples.
            print('Field creation.')
            # Set the mode of simulation.
            self.field.hurst.SetStepSampleMode(self.params_model['smode_cst'],
                                               self.params_model['Hmin'],
                                               self.params_model['Hmax'],
                                               self.params_model['smode_int'],
                                               self.params_model['dint'])
        else:
            # Visualize existing examples.
            print('Field visualization.')
            expe_end = min(expe_end, self.nbexpe)
            expe_end = min(expe_end, self.nbexpe)

        start = time.time()
        for n in range(expe_start, expe_end):
            filename = self.SetFileName(n)
            radname = filename[-6:]
            if self.MissingData(n):
                # Creating a new sample.
                seed(n)
                # Name of the field.
                self.field.name = "Field " + radname
                # Define a new model.
                self.field.hurst.ChangeParameters()
                self.field.NormalizeModel()
                self.field.hurst.fname =\
                    "Hurst function - field " + radname
                self.field.topo.fname =\
                    "Topothesy function - field " + radname
                # Compute some model features.
                self.field.ComputeFeatures_Hurst()
                # Simulate the field
                seed(n)
                start = time.time()
                self.X = self.field.Simulate(self.coord)
                self.X.name = "Example - field " + radname
                print("Example %d: %4.3f sec." % (n, time.time() - start))
                self.SaveExample(n)
                self.nbexpe += 1
            elif not _create:
                self.ShowExample(n)

    def DisplayFields(self, expe_start=0, expe_end=None):
        """Show several examples.
        """
        self.IterateFields(expe_start, expe_end, _create=False)

    def CreateFields(self, expe_start=0, expe_end=None):
        """Create several examples.
        """
        self.IterateFields(expe_start, expe_end, _create=True)

    def ExportData(self, n):
        """Export an example in a numpy format.

        :param int n: the index of the example to export.
        :returns: (images, features)
        :rtype: (ndarrays, ndarrays)

        .. note::
            - image is an array of size N x N:
            - features is an array of size 4 containing

              * features[0] is the Hurst index.
              * features[1] is the length of the Hurst argmin set.
              * features[2] is the center of the Hurst argmin set.
              * features[3] is the maximum of the Hurst function.
        """
        image = zeros((self.params_images['N'], self.params_images['N']),
                      dtype=float)
        features = zeros(4, dtype=float)
        self.LoadExample(n)
        image[:, :] = self.X.values.reshape(self.X.M)[:, :]
        features[0] = self.field.H
        features[1] = self.field.hurst_argmin_lenght
        features[2] = self.field.hurst_argmin_center
        features[3] = self.field.Hmax - self.field.H

        return image, features

    def ExportDataset(self, n_start=0, n_end=None):
        """Export the database in numpy format.

        :param int n_start: first example.
        :param int n_end: last example.

        :returns: (images, features)
        :rtype: (ndarrays, ndarrays)

        .. note::
            - images is an array of size (n_end - n_start + 1) x N x N:
              images[j, :, :] is the image of the (n_start + j)th example.
            - features, an array of size  (n_end - n_start + 1) X 4:
              features[j, :] are the features of the (n_start +j)th examples.

              * features[j, 0] is the Hurst index.
              * features[j, 1] is the length of the Hurst argmin set.
              * features[j, 2] is the center of the Hurst argmin set.
              * features[j, 3] is the range length of the Hurst function.

        """
        if n_end is None:
            n_end = self.nbexpe - 1

        nbexamples = n_end - n_start + 1
        images = zeros((nbexamples, self.params_images['N'],
                        self.params_images['N']), dtype=float)
        features = zeros((nbexamples, 4), dtype=float)
        for j in range(n_start, n_end + 1):
            j0 = j - n_start
            image, feature = self.ExportData(j)
            images[j, :, :] = image[:, :]
            features[j0, 0] = feature[0]
            features[j0, 1] = feature[1]
            features[j0, 2] = feature[2]
            features[j0, 3] = feature[3]

        return images, features
