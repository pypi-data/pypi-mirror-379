import json

import numpy as np
import pyqtgraph as pg
from pyqtgraph.widgets.PlotWidget import PlotItem, PlotWidget
from pyqtgraph.widgets.RemoteGraphicsView import RemoteGraphicsView

from microEye.hardware.stages.stabilizer import *
from microEye.qt import QtWidgets
from microEye.utils.gui_helper import GaussianOffSet


class focusWidget(QtWidgets.QDockWidget):
    def __init__(self):
        '''
        Initialize the focusWidget instance.

        Set up the GUI layout, including the ROI settings, buttons, and graph widgets.
        '''
        super().__init__('Focus Stabilization')

        # Remove close button from dock widgets
        self.setFeatures(
            QtWidgets.QDockWidget.DockWidgetFeature.DockWidgetFloatable
            | QtWidgets.QDockWidget.DockWidgetFeature.DockWidgetMovable
        )

        self.focusStabilizerView = FocusStabilizerView()

        self.init_layout()

        self.connectUpdateGui()

        self.focusStabilizerView.setRoiActivated.connect(self.set_roi)

        # We need to store a reference to the plotted line
        # somewhere, so we can apply the new data to it.
        self.__plot_ref = None
        self.__plotfit_ref = None
        self.__center_ref = None

    def init_layout(self):
        # display tab
        self.labelStyle = {'color': '#FFF', 'font-size': '10pt'}
        graphs_layout = QtWidgets.QGridLayout()

        # Graphics Layout
        self.graphicsLayoutWidget = pg.GraphicsLayoutWidget()
        graphicsLayout = self.graphicsLayoutWidget.ci
        pg.setConfigOptions(antialias=True, imageAxisOrder='row-major')
        pg.setConfigOption('imageAxisOrder', 'row-major')

        # IR Camera GraphView
        self.remote_plt = graphicsLayout.addViewBox(0, 0, invertY=True)
        self.remote_plt.setAspectLocked()
        self.remote_img = pg.ImageItem(axisOrder='row-major')
        self.remote_img.setImage(np.random.normal(size=(512, 512)))
        # IR LineROI
        self.roi = pg.ROI(pg.Point(25.5, 25.5), pg.Point(0, 256), angle=0, pen='r')
        self.roi.addTranslateHandle([0, 0], [0, 1])
        self.roi.addScaleRotateHandle([0, 1], [0, 0])
        self.roi.updateFlag = False

        # IR LineROI Graph
        self.graph_IR = graphicsLayout.addPlot(1, 0)
        self.graph_IR.setLabel('bottom', 'Pixel', **self.labelStyle)
        self.graph_IR.setLabel('left', 'Signal', 'V', **self.labelStyle)
        # IR Peak Position Graph
        self.graph_Peak = graphicsLayout.addPlot(2, 0)
        self.graph_Peak.setLabel('bottom', 'Frame', **self.labelStyle)
        self.graph_Peak.setLabel('left', 'Center Pixel Error', **self.labelStyle)

        # self.roi.maxBounds = QRectF(0, 0, 513, 513)
        def roiChanged(cls):
            if not self.roi.updateFlag:
                pos = self.roi.pos()
                self.focusStabilizerView.set_param_value(
                    FocusStabilizerParams.X1, pos[0]
                )
                self.focusStabilizerView.set_param_value(
                    FocusStabilizerParams.Y1, pos[1]
                )
                self.focusStabilizerView.set_param_value(
                    FocusStabilizerParams.LENGTH, self.roi.size()[1]
                )
                self.focusStabilizerView.set_param_value(
                    FocusStabilizerParams.ANGLE, self.roi.angle() % 360
                )
                x, y = self.getRoiCoords()
                self.focusStabilizerView.set_param_value(FocusStabilizerParams.X2, x[1])
                self.focusStabilizerView.set_param_value(FocusStabilizerParams.Y2, y[1])
                if self.roi.size()[0] > 0:
                    self.roi.setSize((0, self.roi.size()[1]))

        # self.lr_proxy = pg.multiprocess.proxy(
        #     roiChanged, callSync='off', autoProxy=True)
        self.roi.sigRegionChangeFinished.connect(roiChanged)
        self.remote_plt.addItem(self.remote_img)
        self.remote_plt.addItem(self.roi)

        graphs_layout.addWidget(self.graphicsLayoutWidget, 0, 1, 3, 1)
        graphs_layout.addWidget(self.focusStabilizerView, 0, 3)

        container = QtWidgets.QWidget(self)
        container.setLayout(graphs_layout)
        self.setWidget(container)

    @property
    def buffer(self):
        return FocusStabilizer.instance().buffer

    def connectUpdateGui(self):
        FocusStabilizer.instance().updateViewBox.connect(self.updateViewBox)
        FocusStabilizer.instance().updatePlots.connect(self.updatePlots)

    def updateViewBox(self, data: np.ndarray):
        self.remote_img.setImage(data, _callSync='off')

    def updatePlots(self, data: np.ndarray, method: str):
        '''Updates the graphs.'''
        xdata = np.arange(len(data))

        if method == 'reflection':
            # updates the IR graph with data
            if self.__plot_ref is None:
                # create plot reference when None
                self.__plot_ref = self.graph_IR.plot(xdata, data, pen='r')
            else:
                # use the plot reference to update the data for that line.
                self.__plot_ref.setData(xdata, data)

            if FocusStabilizer.instance().fit_params is not None:
                # updates the IR graph with data fit
                if self.__plotfit_ref is None:
                    # create plot reference when None
                    self.__plotfit_ref = self.graph_IR.plot(
                        xdata,
                        GaussianOffSet(xdata, *FocusStabilizer.instance().fit_params),
                        pen='b',
                    )
                else:
                    # use the plot reference to update the data for that line.
                    self.__plotfit_ref.setData(
                        xdata,
                        GaussianOffSet(xdata, *FocusStabilizer.instance().fit_params),
                    )
        elif method == 'beads' or method == 'beads astigmatic':
            self.graph_IR.setLabel('bottom', 'Drift', **self.labelStyle)
            self.graph_IR.setLabel('left', 'Pixel', **self.labelStyle)
            # updates the IR graph with data
            if self.__plot_ref is None:
                # create plot reference when None
                self.__plot_ref = self.graph_IR.plot(xdata, data[:, 0], pen='r')
            else:
                # use the plot reference to update the data for that line.
                self.__plot_ref.setData(xdata, data[:, 0])

            if self.__plotfit_ref is None:
                # create plot reference when None
                self.__plotfit_ref = self.graph_IR.plot(xdata, data[:, 1], pen='b')
            else:
                # use the plot reference to update the data for that line.
                self.__plotfit_ref.setData(xdata, data[:, 1])

        if self.__center_ref is None:
            # create plot reference when None
            self.__center_ref = self.graph_Peak.plot(
                FocusStabilizer.instance().time_points,
                FocusStabilizer.instance().parameter_buffer,
            )
        else:
            # use the plot reference to update the data for that line.
            self.__center_ref.setData(
                FocusStabilizer.instance().time_points,
                FocusStabilizer.instance().parameter_buffer,
            )

    def updateRoiParams(self, params: dict):
        if 'ROI_x' in params:
            self.focusStabilizerView.set_param_value(
                FocusStabilizerParams.X1, float(params['ROI_x'])
            )
        if 'ROI_y' in params:
            self.focusStabilizerView.set_param_value(
                FocusStabilizerParams.Y1, float(params['ROI_y'])
            )
        if 'ROI_length' in params:
            self.focusStabilizerView.set_param_value(
                FocusStabilizerParams.LENGTH, int(params['ROI_length'])
            )
        if 'ROI_angle' in params:
            self.focusStabilizerView.set_param_value(
                FocusStabilizerParams.ANGLE, float(params['ROI_angle'])
            )
        if 'ROI_Width' in params:
            self.focusStabilizerView.set_param_value(
                FocusStabilizerParams.LINE_WIDTH, int(params['ROI_Width'])
            )
        x, y = self.getRoiCoords()
        self.focusStabilizerView.set_param_value(FocusStabilizerParams.X2, x[1])
        self.focusStabilizerView.set_param_value(FocusStabilizerParams.Y2, y[1])

        if 'PixelCalCoeff' in params:
            self.focusStabilizerView.set_param_value(
                FocusStabilizerParams.CAL_COEFF, float(params['PixelCalCoeff'])
            )
        if 'UseCal' in params:
            self.focusStabilizerView.set_param_value(
                FocusStabilizerParams.USE_CAL, bool(params['UseCal'])
            )
        if 'Inverted' in params:
            self.focusStabilizerView.set_param_value(
                FocusStabilizerParams.INVERTED, bool(params['Inverted'])
            )
        if 'PID' in params:
            _P, _I, _D, _tau, _err_th = params['PID']
            self.focusStabilizerView.set_param_value(
                FocusStabilizerParams.FT_P, float(_P)
            )
            self.focusStabilizerView.set_param_value(
                FocusStabilizerParams.FT_I, float(_I)
            )
            self.focusStabilizerView.set_param_value(
                FocusStabilizerParams.FT_D, float(_D)
            )
            self.focusStabilizerView.set_param_value(
                FocusStabilizerParams.FT_TAU, float(_tau)
            )
            self.focusStabilizerView.set_param_value(
                FocusStabilizerParams.FT_ERROR_TH, float(_err_th)
            )

    def getRoiCoords(self):
        dy = self.roi.state['size'][1] * np.cos(np.pi * self.roi.state['angle'] / 180)
        dx = self.roi.state['size'][1] * np.sin(np.pi * self.roi.state['angle'] / 180)
        x = self.roi.x()
        y = self.roi.y()
        return [x, x - dx], [y, y + dy]

    def set_roi(self):
        '''
        Set the ROI based on the current spin box values.
        '''
        self.roi.updateFlag = True
        self.roi.setPos(
            self.focusStabilizerView.get_param_value(FocusStabilizerParams.X1),
            self.focusStabilizerView.get_param_value(FocusStabilizerParams.Y1),
        )
        self.roi.setSize(
            [0, self.focusStabilizerView.get_param_value(FocusStabilizerParams.LENGTH)]
        )
        self.roi.setAngle(
            self.focusStabilizerView.get_param_value(FocusStabilizerParams.ANGLE)
        )

        x, y = self.getRoiCoords()
        self.focusStabilizerView.set_param_value(FocusStabilizerParams.X2, x[1])
        self.focusStabilizerView.set_param_value(FocusStabilizerParams.Y2, y[1])

        self.roi.updateFlag = False

    def get_config(self) -> dict:
        return {
            'ROI_x': self.roi.x(),
            'ROI_y': self.roi.y(),
            'ROI_length': self.roi.state['size'][1],
            'ROI_angle': self.roi.state['angle'] % 360,
            'ROI_Width': FocusStabilizer.instance().line_width,
            'PID': FocusStabilizer.instance().getPID(),
            'PixelCalCoeff': FocusStabilizer.instance().calCoeff(),
            'UseCal': FocusStabilizer.instance().useCal(),
            'Inverted': FocusStabilizer.instance().isInverted(),
        }

    def load_config(self, config: dict) -> None:
        if not isinstance(config, dict):
            raise TypeError('Configuration must be a dictionary.')

        self.updateRoiParams(config)
        self.set_roi()

    def __str__(self):
        return 'Focus Stabilization Widget'
