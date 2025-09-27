// src/components/variableInspectorSidebarWidget.tsx
import React from 'react';
import { ReactWidget } from '@jupyterlab/ui-components';
import { Message } from '@lumino/messaging';
import { pluginIcon } from '../icons/pluginIcon';
import { NotebookWatcher } from '../watchers/notebookWatcher';
import { CommandRegistry } from '@lumino/commands';
import { IStateDB } from '@jupyterlab/statedb';

import { NotebookPanelContextProvider } from '../context/notebookPanelContext';
import { NotebookKernelContextProvider } from '../context/notebookKernelContext';
import { VariableContextProvider } from '../context/notebookVariableContext';
import { VariableListComponent } from './variableListComponent';
import {
  PluginVisibilityContextValue,
  PluginVisibilityContext
} from '../context/pluginVisibilityContext';
import { ILabShell } from '@jupyterlab/application';
import { ISettingRegistry } from '@jupyterlab/settingregistry';
import { CodeExecutionContextProvider } from '../context/codeExecutionContext';
import { t } from '../translator';

export class VariableInspectorSidebarWidget extends ReactWidget {
  private notebookWatcher: NotebookWatcher;
  private commands: CommandRegistry;
  private isOpen = false;
  private labShell: ILabShell;
  private settingRegistry: ISettingRegistry | null = null;
  private _stateDB: IStateDB;

  constructor(
    notebookWatcher: NotebookWatcher,
    commands: CommandRegistry,
    labShell: ILabShell,
    settingRegistry: ISettingRegistry | null,
    stateDB: IStateDB,
  ) {
    super();
    this.notebookWatcher = notebookWatcher;
    this.commands = commands;
    this.id = 'mljar-variable-inspector::mljar-left-sidebar';
    this.title.icon = pluginIcon;
    this.title.caption = t('Your Variables');;
    this.addClass('mljar-variable-inspector-sidebar-widget');
    this.labShell = labShell;
    this.settingRegistry = settingRegistry;
    this._stateDB = stateDB;
  }

  protected onAfterShow(msg: Message): void {
    super.onAfterShow(msg);
    this.isOpen = true;
    this.update();
  }

  protected onAfterHide(msg: Message): void {
    super.onAfterHide(msg);
    this.isOpen = false;
    this.update();
  }

  render(): JSX.Element {
    const contextValue: PluginVisibilityContextValue = {
      isPluginOpen: this.isOpen,
      setPluginOpen: open => {
        this.isOpen = open;
        this.update();
      }
    };

    return (
      <div className="mljar-variable-inspector-sidebar-container">
        <PluginVisibilityContext.Provider value={contextValue}>
          <NotebookPanelContextProvider notebookWatcher={this.notebookWatcher}>
            <NotebookKernelContextProvider
              notebookWatcher={this.notebookWatcher}
            >
              <VariableContextProvider
                stateDB={this._stateDB}
                commands={this.commands}
              >
                <CodeExecutionContextProvider
                  settingRegistry={this.settingRegistry}
                >
                  <VariableListComponent
                    commands={this.commands}
                    labShell={this.labShell}
                    settingRegistry={this.settingRegistry}
                  />
                </CodeExecutionContextProvider>
              </VariableContextProvider>
            </NotebookKernelContextProvider>
          </NotebookPanelContextProvider>
        </PluginVisibilityContext.Provider>
      </div>
    );
  }
}

export function createVariableInspectorSidebar(
  notebookWatcher: NotebookWatcher,
  commands: CommandRegistry,
  labShell: ILabShell,
  settingRegistry: ISettingRegistry | null,
  stateDB: IStateDB,
): VariableInspectorSidebarWidget {
  return new VariableInspectorSidebarWidget(
    notebookWatcher,
    commands,
    labShell,
    settingRegistry,
    stateDB
  );
}
