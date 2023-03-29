from qtpy.QtWidgets import (QTabWidget, QWidget, QVBoxLayout)


def create_tabs(tab_names, main_layout):
    """Create a tab widget with the given tab names.

    Parameters
    ----------
    tab_names : list of str
        The names of the tabs to create.
    main_layout : QWidget, optional
        main layout to add the tabs to

    Returns
    -------
    QTabWidget
        The tab widget with the given tabs.
    """
    
    tabs = QTabWidget()
    tab_widgets = [QWidget() for _ in tab_names]
    tab_layouts = [QVBoxLayout() for _ in tab_names]
    for t_layout, t_widget, t_name in zip(tab_layouts, tab_widgets, tab_names):
        t_widget.setLayout(t_layout)
        tabs.addTab(t_widget, t_name)
    
    main_layout.addWidget(tabs)