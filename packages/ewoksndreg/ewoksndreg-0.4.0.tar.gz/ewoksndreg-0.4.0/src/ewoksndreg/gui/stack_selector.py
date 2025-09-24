from typing import List
from typing import Optional

from silx.gui import qt


class HorizontalStackSelector(qt.QWidget):
    selectionChanged = qt.Signal(int)

    def __init__(self, parent: Optional[qt.QWidget] = None):
        super().__init__(parent)

        self._layout = qt.QHBoxLayout(self)
        self._layout.setContentsMargins(0, 0, 0, 0)
        self._layout.setSpacing(2)

        self._label = qt.QLabel("Select stack:")
        self._layout.addWidget(self._label)

        self._combobox = qt.QComboBox()
        self._layout.addWidget(self._combobox)
        self._layout.addStretch(1)

        self._combobox.currentIndexChanged.connect(self.selectionChanged)

    def setStackNames(self, names: List[str]) -> None:
        self._combobox.currentIndexChanged.disconnect(self.selectionChanged)
        try:
            index = max(min(0, self.getStackIndex()), len(names) - 1)
            self._combobox.clear()
            self._combobox.addItems(names)
            self.setStackIndex(index)
        finally:
            self._combobox.currentIndexChanged.connect(self.selectionChanged)

    def getStackNames(self) -> List[str]:
        return [self._combobox.itemText(i) for i in range(self._combobox.count())]

    def setStackName(self, name: str) -> None:
        index = self.getStackNames().index(name)
        self.setStackIndex(index)

    def getStackName(self, index: Optional[int] = None) -> str:
        if index is None:
            index = self.getStackIndex()
        n = self._combobox.count()
        if 0 <= index < n:
            return self._combobox.itemText(index)
        else:
            raise ValueError(f"index must be between {0} and {n-1}")

    def setStackIndex(self, index: int) -> None:
        self._combobox.setCurrentIndex(index)

    def getStackIndex(self) -> int:
        return self._combobox.currentIndex()
