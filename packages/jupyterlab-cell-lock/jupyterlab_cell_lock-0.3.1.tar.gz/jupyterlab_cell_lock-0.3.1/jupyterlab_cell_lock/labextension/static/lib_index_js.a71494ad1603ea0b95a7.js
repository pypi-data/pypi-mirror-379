"use strict";
(self["webpackChunkjupyterlab_cell_lock"] = self["webpackChunkjupyterlab_cell_lock"] || []).push([["lib_index_js"],{

/***/ "./lib/icon.js":
/*!*********************!*\
  !*** ./lib/icon.js ***!
  \*********************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   applyCellIcon: () => (/* binding */ applyCellIcon),
/* harmony export */   asBool: () => (/* binding */ asBool),
/* harmony export */   refreshIcons: () => (/* binding */ refreshIcons)
/* harmony export */ });
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/ui-components */ "webpack/sharing/consume/default/@jupyterlab/ui-components");
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0__);

const asBool = (v) => (typeof v === 'boolean' ? v : true);
const applyCellIcon = (cellModel, cellWidget, statusWidget, retryCount = 0) => {
    const editable = asBool(cellModel.getMetadata('editable'));
    const deletable = asBool(cellModel.getMetadata('deletable'));
    const promptNode = cellWidget.node.querySelector('.jp-InputPrompt.jp-InputArea-prompt');
    if (!promptNode) {
        if (retryCount < 10) {
            setTimeout(() => {
                applyCellIcon(cellModel, cellWidget, statusWidget, retryCount + 1);
            }, 10);
        }
        return;
    }
    const existing = promptNode.querySelector('.jp-CellLockIcon');
    if (existing) {
        existing.remove();
    }
    const iconNode = document.createElement('span');
    iconNode.className = 'jp-CellLockIcon';
    iconNode.setAttribute('role', 'button');
    iconNode.setAttribute('tabindex', '0');
    if (!editable || !deletable) {
        let tooltipMessage = 'This cell is ';
        const isReadOnly = !editable;
        const isUndeletable = !deletable;
        if (isReadOnly && isUndeletable) {
            tooltipMessage += 'read-only and undeletable.';
        }
        else if (isReadOnly) {
            tooltipMessage += 'read-only but can be deleted.';
        }
        else if (isUndeletable) {
            tooltipMessage += 'undeletable but can be edited.';
        }
        iconNode.title = tooltipMessage;
        iconNode.setAttribute('aria-label', 'Unlock cell');
        _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0__.lockIcon.element({
            container: iconNode,
            elementPosition: 'left',
            height: '14px',
            width: '14px'
        });
        const unlockAction = () => {
            cellModel.setMetadata('editable', true);
            cellModel.setMetadata('deletable', true);
            applyCellIcon(cellModel, cellWidget, statusWidget);
            if (statusWidget) {
                statusWidget.setTemporaryStatus('Cell unlocked.');
            }
        };
        iconNode.addEventListener('click', unlockAction);
        iconNode.addEventListener('keydown', event => {
            if (event.key === 'Enter' || event.key === ' ') {
                event.preventDefault();
                unlockAction();
            }
        });
    }
    else {
        iconNode.title = 'This cell is editable and deletable.';
        iconNode.setAttribute('aria-label', 'Lock cell');
        _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0__.editIcon.element({
            container: iconNode,
            elementPosition: 'left',
            height: '14px',
            width: '14px'
        });
        // Handle click and keyboard events to lock
        const lockAction = () => {
            cellModel.setMetadata('editable', false);
            cellModel.setMetadata('deletable', false);
            applyCellIcon(cellModel, cellWidget, statusWidget);
            if (statusWidget) {
                statusWidget.setTemporaryStatus('Cell locked.');
            }
        };
        iconNode.addEventListener('click', lockAction);
        iconNode.addEventListener('keydown', event => {
            if (event.key === 'Enter' || event.key === ' ') {
                event.preventDefault();
                lockAction();
            }
        });
    }
    promptNode.appendChild(iconNode);
};
const refreshIcons = (notebookPanel, statusWidget) => {
    if (!notebookPanel) {
        return;
    }
    const { content: notebook } = notebookPanel;
    if (notebook.model && notebook.widgets) {
        //console.log('Refreshing lock icons for', notebook.widgets.length, 'cells');
        requestAnimationFrame(() => {
            notebook.widgets.forEach((cellWidget, i) => {
                const cellModel = notebook.model.cells.get(i);
                if (cellModel) {
                    applyCellIcon(cellModel, cellWidget, statusWidget);
                }
            });
        });
    }
};


/***/ }),

/***/ "./lib/index.js":
/*!**********************!*\
  !*** ./lib/index.js ***!
  \**********************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var _jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/notebook */ "webpack/sharing/consume/default/@jupyterlab/notebook");
/* harmony import */ var _jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _jupyterlab_statusbar__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/statusbar */ "webpack/sharing/consume/default/@jupyterlab/statusbar");
/* harmony import */ var _jupyterlab_statusbar__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_statusbar__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @jupyterlab/apputils */ "webpack/sharing/consume/default/@jupyterlab/apputils");
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! @jupyterlab/ui-components */ "webpack/sharing/consume/default/@jupyterlab/ui-components");
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_3___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_3__);
/* harmony import */ var _status__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! ./status */ "./lib/status.js");
/* harmony import */ var _icon__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! ./icon */ "./lib/icon.js");
/* harmony import */ var _metadata__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! ./metadata */ "./lib/metadata.js");







const plugin = {
    id: 'jupyterlab-cell-lock:plugin',
    autoStart: true,
    requires: [_jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_0__.INotebookTracker],
    optional: [_jupyterlab_statusbar__WEBPACK_IMPORTED_MODULE_1__.IStatusBar],
    activate: (app, tracker, statusBar) => {
        console.log('jupyterlab-cell-lock extension activated!');
        let statusWidget;
        if (statusBar) {
            statusWidget = new _status__WEBPACK_IMPORTED_MODULE_4__.CellLockStatus();
            statusBar.registerStatusItem('cellLockStatus', {
                item: statusWidget,
                align: 'middle'
            });
        }
        // Define the lock command
        const lockCommand = 'jupyterlab-cell-lock:lock-cells';
        app.commands.addCommand(lockCommand, {
            label: 'Make All Current Cells Read-Only & Undeletable',
            execute: () => {
                (0,_metadata__WEBPACK_IMPORTED_MODULE_6__.toggleAllCellMetadata)(false, false, tracker, statusWidget);
            }
        });
        // Define the unlock command
        const unlockCommand = 'jupyterlab-cell-lock:unlock-cells';
        app.commands.addCommand(unlockCommand, {
            label: 'Make All Current Cells Editable & Deletable',
            execute: () => {
                (0,_metadata__WEBPACK_IMPORTED_MODULE_6__.toggleAllCellMetadata)(true, true, tracker, statusWidget);
            }
        });
        tracker.widgetAdded.connect((_, notebookPanel) => {
            var _a;
            const { content: notebook, context } = notebookPanel;
            const lockButton = new _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_2__.ToolbarButton({
                label: 'Lock all cells',
                icon: _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_3__.lockIcon,
                onClick: () => {
                    app.commands.execute(lockCommand);
                },
                tooltip: 'Make all current cells read-only & undeletable'
            });
            const unlockButton = new _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_2__.ToolbarButton({
                label: 'Unlock all cells',
                icon: _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_3__.editIcon,
                onClick: () => {
                    app.commands.execute(unlockCommand);
                },
                tooltip: 'Make all current cells editable & deletable'
            });
            notebookPanel.toolbar.insertItem(10, 'lockCells', lockButton);
            notebookPanel.toolbar.insertItem(11, 'unlockCells', unlockButton);
            // Apply icons once the notebook is fully loaded and revealed
            Promise.all([context.ready, notebookPanel.revealed]).then(() => {
                (0,_icon__WEBPACK_IMPORTED_MODULE_5__.refreshIcons)(notebookPanel, statusWidget);
            });
            // Function to add output area listeners to a code cell
            const addOutputListener = (cellWidget) => {
                if (cellWidget.model.type === 'code' && cellWidget.outputArea) {
                    const outputAreaModel = cellWidget.outputArea.model;
                    outputAreaModel.changed.connect(() => {
                        setTimeout(() => {
                            (0,_icon__WEBPACK_IMPORTED_MODULE_5__.applyCellIcon)(cellWidget.model, cellWidget, statusWidget);
                        }, 10);
                    });
                    outputAreaModel.stateChanged.connect((sender, args) => {
                        if (args.name === 'outputs' || args.name === 'length') {
                            setTimeout(() => {
                                (0,_icon__WEBPACK_IMPORTED_MODULE_5__.applyCellIcon)(cellWidget.model, cellWidget, statusWidget);
                            }, 10);
                        }
                    });
                }
            };
            // Add listeners to existing cells
            notebook.widgets.forEach(cellWidget => {
                addOutputListener(cellWidget);
            });
            // Handle new cells being added
            (_a = notebook.model) === null || _a === void 0 ? void 0 : _a.cells.changed.connect((_, change) => {
                if (change.type === 'add') {
                    change.newValues.forEach((cellModel, idx) => {
                        const cellWidget = notebook.widgets[change.newIndex + idx];
                        if (cellWidget) {
                            setTimeout(() => {
                                (0,_icon__WEBPACK_IMPORTED_MODULE_5__.applyCellIcon)(cellModel, cellWidget, statusWidget);
                                addOutputListener(cellWidget);
                            }, 10);
                        }
                    });
                }
            });
            // Refresh on metadata change
            notebook.widgets.forEach(cellWidget => {
                cellWidget.model.metadataChanged.connect(() => {
                    (0,_icon__WEBPACK_IMPORTED_MODULE_5__.applyCellIcon)(cellWidget.model, cellWidget, statusWidget);
                });
            });
            // Refresh on save
            context.saveState.connect((_, state) => {
                if (state === 'completed') {
                    (0,_icon__WEBPACK_IMPORTED_MODULE_5__.refreshIcons)(notebookPanel, statusWidget);
                }
            });
        });
        // Refresh when the active cell changes
        tracker.activeCellChanged.connect(() => {
            const current = tracker.currentWidget;
            if (current) {
                (0,_icon__WEBPACK_IMPORTED_MODULE_5__.refreshIcons)(current, statusWidget);
            }
        });
    }
};
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (plugin);


/***/ }),

/***/ "./lib/metadata.js":
/*!*************************!*\
  !*** ./lib/metadata.js ***!
  \*************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   toggleAllCellMetadata: () => (/* binding */ toggleAllCellMetadata)
/* harmony export */ });
/* harmony import */ var _icon__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ./icon */ "./lib/icon.js");

const toggleAllCellMetadata = (editable, deletable, tracker, statusWidget) => {
    var _a;
    const current = tracker.currentWidget;
    if (!current) {
        console.warn('No active notebook.');
        return;
    }
    const notebook = current.content;
    const cells = (_a = notebook.model) === null || _a === void 0 ? void 0 : _a.cells;
    if (!cells) {
        return;
    }
    let editedCellCount = 0;
    let nonEditedCellCount = 0;
    for (let i = 0; i < cells.length; i++) {
        const cellModel = cells.get(i);
        const isEditable = (0,_icon__WEBPACK_IMPORTED_MODULE_0__.asBool)(cellModel.getMetadata('editable'));
        const isDeletable = (0,_icon__WEBPACK_IMPORTED_MODULE_0__.asBool)(cellModel.getMetadata('deletable'));
        if (isEditable !== editable || isDeletable !== deletable) {
            cellModel.setMetadata('editable', editable);
            cellModel.setMetadata('deletable', deletable);
            const cellWidget = notebook.widgets[i];
            (0,_icon__WEBPACK_IMPORTED_MODULE_0__.applyCellIcon)(cellModel, cellWidget, statusWidget);
            editedCellCount++;
        }
        else {
            nonEditedCellCount++;
        }
    }
    const action = editable ? 'unlocked' : 'locked';
    let statusMessage = '';
    if (editedCellCount === 0) {
        statusMessage = `All cells were already ${action}.`;
    }
    else {
        statusMessage = `${editedCellCount} cell${editedCellCount > 1 ? 's' : ''} ${editedCellCount > 1 ? 'were' : 'was'} successfully ${action}.`;
        if (nonEditedCellCount > 0) {
            statusMessage += ` (${nonEditedCellCount} already ${action}).`;
        }
    }
    if (statusWidget) {
        statusWidget.setTemporaryStatus(statusMessage);
    }
};


/***/ }),

/***/ "./lib/status.js":
/*!***********************!*\
  !*** ./lib/status.js ***!
  \***********************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   CellLockStatus: () => (/* binding */ CellLockStatus)
/* harmony export */ });
/* harmony import */ var _lumino_widgets__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @lumino/widgets */ "webpack/sharing/consume/default/@lumino/widgets");
/* harmony import */ var _lumino_widgets__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_lumino_widgets__WEBPACK_IMPORTED_MODULE_0__);

class CellLockStatus extends _lumino_widgets__WEBPACK_IMPORTED_MODULE_0__.Widget {
    constructor() {
        super();
        this._timer = null;
        this.addClass('jp-CellLockStatus');
        this._statusNode = document.createElement('span');
        this.node.appendChild(this._statusNode);
        this.node.style.display = 'inline-flex';
        this.node.style.alignItems = 'center';
    }
    setTemporaryStatus(summary, timeoutMs = 2000) {
        this._statusNode.innerText = summary;
        if (this._timer) {
            window.clearTimeout(this._timer);
        }
        this._timer = window.setTimeout(() => {
            this._statusNode.innerText = '';
            this._timer = null;
        }, timeoutMs);
    }
}


/***/ })

}]);
//# sourceMappingURL=lib_index_js.a71494ad1603ea0b95a7.js.map