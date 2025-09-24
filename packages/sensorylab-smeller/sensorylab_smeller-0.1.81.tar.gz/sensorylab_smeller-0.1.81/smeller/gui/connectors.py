# smeller/gui/connectors.py

class SetupConnector:
    """
    SetupConnector отвечает за подключение сигналов/слотов между компонентами пользовательского
    интерфейса (ControlPanel, ChannelManager, PlotWidgetComponent, AromablocksList) и методами MainWindow.
    """

    def __init__(self, view_model, ui_manager):
        """
        Инициализация SetupConnector.

        Аргументы:
            view_model: Модель представления (ViewModel) приложения.
            ui_manager: Экземпляр UIManager, содержащий собранный интерфейс и его компоненты.
        """
        self.view_model = view_model
        self.ui = ui_manager

    def setup_connections(self):
        """
        Настраивает соединения (signals/slots) для основных компонентов интерфейса,
        используя методы connect_signals каждого компонента.
        """
        # Подключаем сигналы ControlPanel к соответствующим слотам MainWindow.
        self.ui.control_panel.connect_signals(self.ui)
        # Подключаем сигналы ChannelManager к соответствующим слотам MainWindow.
        self.ui.channel_manager.connect_signals(self.ui)
        # Подключаем сигналы PlotWidgetComponent (график) к слотам MainWindow.
        self.ui.plot_widget_component.connect_signals(self.ui)
        # Подключаем сигналы media_view к слотам MainWindow.
        self.ui.media_view.connect_signals(self.ui)
        # Подключаем сигналы view_model к слотам MainWindow.
        self.ui.view_model.connect_signals(self.ui)
        # Подключаем сигналы AromablocksList к слотам MainWindow.
        self.ui.aromablocks_list.connect_signals(self.ui)
        # Подключаем сигналы menu_bar_manager к слотам MainWindow.
        self.ui.menu_bar_manager.connect_signals(self.ui)        #  Соединение для открытия диалога настроек подключения
        self.ui.menu_bar_manager.device_connection_settings_action.triggered.connect(self.ui.open_device_connection_dialog) #  <--- Добавлено соединение