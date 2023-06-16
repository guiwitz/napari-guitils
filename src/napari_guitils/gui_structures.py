from qtpy.QtWidgets import (QTabWidget, QWidget, QVBoxLayout,
                            QHBoxLayout, QGridLayout, QGroupBox)


class TabSet(QTabWidget):
    """Multi-tab widget with named tabs.
    
    Parameters
    ----------
    tab_names : list of str
        The names of the tabs to create.
    tab_layouts : list of layouts, optional
        box layouts to use e.g QVBoxLayout, QHBoxLayout, QGridLayout, optional

    """
    def __init__(self, tab_names, tab_layouts=None):
        super().__init__()

        self.tab_names = tab_names
        tab_widgets = [QWidget() for _ in tab_names]
        if tab_layouts is None:
            tab_layouts = [None for _ in tab_names]
        tab_layouts = [QVBoxLayout() if tl is None else tl for tl in tab_layouts]
        
        for t_layout, t_widget, t_name in zip(tab_layouts, tab_widgets, tab_names):
            t_widget.setLayout(t_layout)
            self.addTab(t_widget, t_name)

    def add_named_tab(self, tab_name, widget, grid_pos=None):
        """Add a widget to a named tab.
        
        Parameters
        ----------
        tab_name : str
            The name of the tab to add the widget to.
        widget : QWidget
            The widget to add to the tab.
        grid_pos : tuple of four int, optional for grid layout

        """
        
        if grid_pos is not None:
            self.widget(self.tab_names.index(tab_name)).layout().addWidget(widget, *grid_pos)
        else:
            self.widget(self.tab_names.index(tab_name)).layout().addWidget(widget)


def create_tabs(tab_names, tab_layouts=None):
    """Create a tab widget with the given tab names.

    Parameters
    ----------
    tab_names : list of str
        The names of the tabs to create.
    tab_layouts : list of Layouts, optional 
        layouts to use e.g QVBoxLayout, QHBoxLayout, QGridLayout, optional

    Returns
    -------
    QTabWidget
        The tab widget with the given tabs.
    """
    
    tabs = QTabWidget()
    tab_widgets = [QWidget() for _ in tab_names]
    if tab_layouts is None:
        tab_layouts = [None for _ in tab_names]
    tab_layouts = [QVBoxLayout() if tl is None else tl for tl in tab_layouts]
    
    for t_layout, t_widget, t_name in zip(tab_layouts, tab_widgets, tab_names):
        t_widget.setLayout(t_layout)
        tabs.addTab(t_widget, t_name)
    
    return tabs

class VHGroup():
    """Group box with specific layout.

    Parameters
    ----------
    name: str
        Name of the group box
    orientation: str
        'V' for vertical, 'H' for horizontal, 'G' for grid
    """

    def __init__(self, name, orientation='V'):
        self.gbox = QGroupBox(name)
        if orientation=='V':
            self.glayout = QVBoxLayout()
        elif orientation=='H':
            self.glayout = QHBoxLayout()
        elif orientation=='G':
            self.glayout = QGridLayout()
        else:
            raise Exception(f"Unknown orientation {orientation}") 

        self.gbox.setLayout(self.glayout)

