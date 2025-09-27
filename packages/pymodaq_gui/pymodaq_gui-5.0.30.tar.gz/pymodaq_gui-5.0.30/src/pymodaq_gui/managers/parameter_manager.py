import numbers
from pathlib import Path
from typing import List, Union, Dict, Optional, Tuple, Any

from qtpy import QtWidgets, QtCore
from pymodaq_gui.managers.action_manager import ActionManager
from pymodaq_gui.parameter import Parameter, ParameterTree, ioxml, utils
from pymodaq_gui.utils.file_io import select_file
from pymodaq_utils.config import get_set_config_dir

from pymodaq_utils.logger import set_logger, get_module_name


logger = set_logger(get_module_name(__file__))


class ParameterTreeWidget(ActionManager):

    def __init__(self, action_list: tuple = ('save', 'update', 'load')):
        super().__init__()

        self.widget = QtWidgets.QWidget()
        self.widget.setLayout(QtWidgets.QVBoxLayout())

        toolbar = QtWidgets.QToolBar()
        self.set_toolbar(toolbar)
        self.tree: ParameterTree = ParameterTree()

        self.widget.header = self.tree.header  # for back-compatibility, widget behave a bit like a ParameterTree
        self.widget.listAllItems = self.tree.listAllItems  # for back-compatibility

        #self.tree.setMinimumWidth(150)
        #self.tree.setMinimumHeight(300)
        
        # Making the buttons
        self.setup_actions(action_list) 
        # Making the splitter
        self.splitter = QtWidgets.QSplitter(QtCore.Qt.Vertical)
        # Adding the toolbar + the parameter tree
        self.splitter.addWidget(toolbar)
        self.splitter.addWidget(self.tree)
        # Hiding toolbar
        self.splitter.setSizes([0, 300])
        # Adding splitter to layout
        self.widget.layout().addWidget(self.splitter)
        self.widget.layout().setContentsMargins(0, 0, 0, 0)

    def setup_actions(self, action_list: tuple = ('save', 'update', 'load')):
        """
        See Also
        --------
        ActionManager.add_action
        """
        # Saving action
        self.add_action('save_settings', 'Save Settings', 'saveTree',
                        "Save current settings in an xml file", 
                        visible = 'save' in action_list)
        # Update action
        self.add_action('update_settings', 'Update Settings', 'updateTree',
                        "Update the settings from an xml file, the settings structure loaded must be identical to the current one",
                        visible = 'update' in action_list)                
        # Load action
        self.add_action('load_settings', 'Load Settings', 'openTree',
                        "Load current settings from an xml file, the current settings structure is erased and is replaced by the new one",
                         visible = 'load' in action_list)


class ParameterManager:
    """Class dealing with Parameter and ParameterTree

    Attributes
    ----------
    params: list of dicts
        Defining the Parameter tree like structure
    settings_name: str
        The particular name to give to the object parent Parameter (self.settings)
    settings: Parameter
        The higher level (parent) Parameter
    settings_tree: QWidget
        widget Holding a ParameterTree and a toolbar for interacting with the tree
    tree: ParameterTree
        the underlying ParameterTree
    """
    settings_name = 'custom_settings'
    params = []

    def __init__(self, settings_name: Optional[str] = None,
                 action_list: tuple = ('save', 'update', 'load'),
                 ):
        if settings_name is None:
            settings_name = self.settings_name
        # create a settings tree to be shown eventually in a dock
        # object containing the settings defined in the preamble
        # create a settings tree to be shown eventually in a dock
        self._settings_tree = ParameterTreeWidget(action_list)
        
        self._settings_tree.get_action(f'save_settings').connect_to(self.save_settings_slot)
        self._settings_tree.get_action(f'update_settings').connect_to(self.update_settings_slot)
        self._settings_tree.get_action(f'load_settings').connect_to(self.load_settings_slot)
                                                                        
        self.settings = Parameter.create(name=settings_name, type='group', children=self.params,
                                         showTop=False)  # create a Parameter
        # object containing the settings defined in the preamble
        self._settings_tree.tree.header().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)

    @property
    def settings_tree(self):
        return self._settings_tree.widget

    @property
    def tree(self):
        return self._settings_tree.tree

    @property
    def settings(self) -> Parameter:
        return self._settings

    @settings.setter
    def settings(self, settings: Union[Parameter, List[Dict[str, str]], Path]):
        settings = self.create_parameter(settings)
        self._settings = settings
        self.tree.setParameters(self._settings, showTop=False)  # load the tree with this parameter object
        self._settings.sigTreeStateChanged.connect(self.parameter_tree_changed)

    @staticmethod
    def create_parameter(settings: Union[Parameter, List[Dict[str, str]], Path]) -> Parameter:

        if isinstance(settings, List):
            _settings = Parameter.create(title='Settings', name='settings', type='group',
                                         children=settings, showTop=False)
        elif isinstance(settings, Path) or isinstance(settings, str):
            settings = Path(settings)
            _settings = Parameter.create(title='Settings', name='settings',
                                         type='group', showTop=False,
                                         children=ioxml.XML_file_to_parameter(str(settings)))
        elif isinstance(settings, Parameter):
            _settings = Parameter.create(title='Settings', name=settings.name(),
                                         type='group', showTop=False)
            _settings.restoreState(settings.saveState())
        else:
            raise TypeError(f'Cannot create Parameter object from {settings}')
        return _settings

    def parameter_tree_changed(self, param, changes):
        for param, change, data in changes:
            path = self._settings.childPath(param)
            if change == 'childAdded':
                self.child_added(param, data)

            elif change == 'value':
                self.value_changed(param)

            elif change == 'parent':
                self.param_deleted(param)

            elif change == 'options':
                self.options_changed(param, data)

            elif change == 'limits':
                self.limits_changed(param, data)

    def value_changed(self, param: Parameter):
        """Non-mandatory method  to be subclassed for actions to perform (methods to call) when one of the param's
        value in self._settings is changed

        For this to be triggered, the Parameter method: **setValue** should be used

        Parameters
        ----------
        param: Parameter
            the parameter whose value just changed

        Examples
        --------
        >>> if param.name() == 'do_something':
        >>>     if param.value():
        >>>         print('Do something')
        >>>         self.settings.child('main_settings', 'something_done').setValue(False)
        """
        ...

    def child_added(self, param: Parameter, data: Parameter):
        """Non-mandatory method to be subclassed for actions to perform when a param has been
        added in the attribute settings

        For this to be triggered, one of the Parameter methods: **addChild**, **addChildren**
        or **insertChildren** should be used

        Parameters
        ----------
        param: Parameter
            the parameter where child will be added
        data: Parameter
            the child parameter
        """
        pass

    def param_deleted(self, param: Parameter):
        """Non-mandatory method to be subclassed for actions to perform when one of the param in self.settings has been deleted

        For this to be triggered, the Parameter method: **removeChild** should be used

        Parameters
        ----------
        param: Parameter
            the parameter that has been deleted
        """
        pass

    def options_changed(self, param: Parameter, data: Dict[str, Any]):
        """Non-mandatory method to be subclassed for actions to perform when one of the options
        of any parameter in the settings attribute has been changed.

        For this to be triggered, the Parameter method: **setOpts** should be used

        Parameters
        ----------
        param: Parameter
            the parameter chose option has been changed
        data: dict
            the key is the string of the changed option
            the value depend on the type of option
        """
        pass

    def limits_changed(self, param: Parameter, data: Tuple[numbers.Number, numbers.Number]):
        """Non-mandatory method to be subclassed for actions to perform when the limits
        of any parameter in the *settings* attribute has been changed

        For this to be triggered, the Parameter method: **setLimits** should be used

        Parameters
        ----------
        param: Parameter
            the parameter chose option has been changed
        data: tuple of numbers
            tuple of float or int depending on the parameter type. For peculiar Parameter, could be
            a tuple of some other objects

        """
        pass


    def save_settings_slot(self, file_path: Path = None):
        """ Method to save the current settings using a xml file extension.

        The starting directory is the user config folder with a subfolder called settings folder

        Parameters
        ----------
        file_path: Path
            Path like object pointing to a xml file encoding a Parameter object
            If None, opens a file explorer window to save manually a file
        """
        if file_path is None or file_path is False:
            file_path = select_file(get_set_config_dir('settings', user=True), save=True, ext='xml', filter='*.xml',
                                    force_save_extension=True)
        else:
            file_path = Path(file_path)
            if '.xml' != file_path.suffix:
                return
        if file_path:
            ioxml.parameter_to_xml_file(self.settings, file_path.resolve())
            logger.info(f'The settings have been successfully saved at {file_path}')

    def _get_settings_from_file(self):
        return select_file(get_set_config_dir('settings', user=True), save=False, ext='xml', filter='*.xml',
                           force_save_extension=True)

    def load_settings_slot(self, file_path: Path = None):
        """ Method to load settings into the parameter using a xml file extension.

        The starting directory is the user config folder with a subfolder called settings folder

        Parameters
        ----------
        file_path: Path
            Path like object pointing to a xml file encoding a Parameter object
            If None, opens a file explorer window to pick manually a file
        """
        if file_path is None or file_path is False:
            file_path = self._get_settings_from_file()
        if file_path:
            self.settings = file_path.resolve()
            logger.info(f'The settings from {file_path} have been successfully loaded')            

    def update_settings_slot(self, file_path: Path = None):
        """ Method to update settings using a xml file extension.

        The file should define the same settings structure (names and children)

        The starting directory is the user config folder with a subfolder called settings folder

        Parameters
        ----------
        file_path: Path
            Path like object pointing to a xml file encoding a Parameter object
            If None, opens a file explorer window to pick manually a file
        """
        if file_path is None or file_path is False:
            file_path = self._get_settings_from_file()
        if file_path:
            _settings = self.create_parameter(file_path.resolve())
            # Checking if both parameters have the same structure
            sameStruct = utils.compareStructureParameter(self.settings,_settings)
            if sameStruct:  # Update if true
                self.settings = _settings
                logger.info(f'The settings from {file_path} have been successfully applied')                            
            else:
                logger.info(f'The loaded settings from {file_path} do not match the current settings structure and cannot be applied.')

