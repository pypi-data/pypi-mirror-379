# Copyright 2025 Enphase Energy, Inc.
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

from typing import Dict, Any, Optional, List, Tuple

from PySide6.QtGui import QColor, QAction
from PySide6.QtWidgets import QMenu, QColorDialog
from pydantic import BaseModel

from .multi_plot_widget import MultiPlotWidget
from .util import BaseTopModel, DataTopModel, HasSaveLoadDataConfig
from .signals_table import ContextMenuSignalsTable


class ColorPickerDataStateModel(DataTopModel):
    color: Optional[str] = None  # QColor name, e.g., '#ffea70' or 'red'


class ColorPickerPlotWidget(MultiPlotWidget, HasSaveLoadDataConfig):
    """Provides an API to set the color on signals, which overrides the color from show_data_items."""

    _DATA_MODEL_BASES = [ColorPickerDataStateModel]

    def __init__(self, *args: Any, **kwargs: Any):
        super().__init__(*args, **kwargs)
        self._colors: Dict[str, QColor] = {}  # only for save state

    def _write_model(self, model: BaseModel) -> None:
        assert isinstance(model, BaseTopModel)
        super()._write_model(model)
        for data_name, data_model in model.data.items():
            assert isinstance(data_model, ColorPickerDataStateModel)
            color = self._colors.get(data_name, None)
            if color is not None:
                data_model.color = color.name()

    def _load_model(self, model: BaseModel) -> None:
        assert isinstance(model, BaseTopModel)
        super()._load_model(model)
        for data_name, data_model in model.data.items():
            assert isinstance(data_model, ColorPickerDataStateModel)
            if data_model.color is not None:
                self.set_colors([data_name], QColor(data_model.color), update=False)

    def show_data_items(
        self, new_data_items: List[Tuple[str, QColor, MultiPlotWidget.PlotType]], **kwargs: Any
    ) -> None:
        # transforms data items to reflect the color settings
        colored_new_data_items = []
        for data_item_name, color, plot_type in new_data_items:
            changed_color = self._colors.get(data_item_name, None)
            if changed_color is not None:
                color = changed_color
            colored_new_data_items.append((data_item_name, color, plot_type))

        super().show_data_items(colored_new_data_items, **kwargs)

    def set_colors(self, data_names: List[str], color: QColor, update: bool = True) -> None:
        for data_name in data_names:
            self._colors[data_name] = color
        if update:
            self.show_data_items(
                [
                    (data_item_name, data_color, plot_type)
                    for data_item_name, (data_color, plot_type) in self._data_items.items()
                ]
            )
            self._update_plots()
            self.sigDataItemsUpdated.emit()


class ColorPickerSignalsTable(ContextMenuSignalsTable):
    """Mixin into SignalsTable that adds a context menu item for the user to change the color.
    This gets sent as a signal, and an upper must handle plumbing the colors through.
    """

    def __init__(self, *args: Any, **kwargs: Any):
        super().__init__(*args, **kwargs)

        self._set_color_action = QAction("Set Color", self)
        self._set_color_action.triggered.connect(self._on_set_color)

    def _populate_context_menu(self, menu: QMenu) -> None:
        super()._populate_context_menu(menu)
        menu.addAction(self._set_color_action)

    def _on_set_color(self) -> None:
        assert isinstance(self._plots, ColorPickerPlotWidget)
        data_names = list(self._data_items.keys())
        selected_data_names = [data_names[item.row()] for item in self.selectedItems()]
        color = QColorDialog.getColor()
        self._plots.set_colors(selected_data_names, color)
