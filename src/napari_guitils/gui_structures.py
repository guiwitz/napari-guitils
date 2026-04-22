from qtpy.QtWidgets import (QTabWidget, QWidget, QVBoxLayout,
                            QHBoxLayout, QGridLayout, QGroupBox,
                            QScrollArea)
from qtpy.QtCore import Qt


class TabSet(QTabWidget):
    """Multi-tab widget with named tabs.
    
    Parameters
    ----------
    tab_names : list of str
        The names of the tabs to create.
    tab_layouts : list of layouts, optional
        box layouts to use e.g QVBoxLayout, QHBoxLayout, QGridLayout, optional
    scrollable : bool or list of bool, optional
        If True or a list of True values, wraps each tab in a vertical scroll
        area. Can be a single bool to apply to all tabs, or a list of bools
        with one entry per tab.

    """
    def __init__(self, tab_names, tab_layouts=None, scrollable=False):
        super().__init__()

        self.tab_names = tab_names
        tab_widgets = [QWidget() for _ in tab_names]
        if tab_layouts is None:
            tab_layouts = [None for _ in tab_names]
        tab_layouts = [QVBoxLayout() if tl is None else tl for tl in tab_layouts]
        if isinstance(scrollable, bool):
            scrollable = [scrollable for _ in tab_names]
        
        for t_layout, t_widget, t_name, t_scroll in zip(tab_layouts, tab_widgets, tab_names, scrollable):
            t_widget.setLayout(t_layout)
            if t_scroll:
                scroll = QScrollArea()
                scroll.setWidget(t_widget)
                scroll.setWidgetResizable(True)
                scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
                scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
                self.addTab(scroll, t_name)
            else:
                self.addTab(t_widget, t_name)

    def widget(self, index):
        """Return the content widget for the tab at index, unwrapping any scroll area."""
        w = super().widget(index)
        if isinstance(w, QScrollArea):
            return w.widget()
        return w

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

