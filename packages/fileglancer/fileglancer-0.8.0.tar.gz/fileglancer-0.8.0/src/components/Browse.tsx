import React, { useEffect } from 'react';
import { useOutletContext } from 'react-router';
import { default as log } from '@/logger';
import type { OutletContextType } from '@/layouts/BrowseLayout';
import { useFileBrowserContext } from '@/contexts/FileBrowserContext';
import FileBrowser from './ui/BrowsePage/FileBrowser';
import Toolbar from './ui/BrowsePage/Toolbar';
import RenameDialog from './ui/Dialogs/Rename';
import Delete from './ui/Dialogs/Delete';
import ChangePermissions from './ui/Dialogs/ChangePermissions';
import ConvertFileDialog from './ui/Dialogs/ConvertFile';
import RecentDataLinksCard from './ui/BrowsePage/Dashboard/RecentDataLinksCard';
import RecentlyViewedCard from './ui/BrowsePage/Dashboard/RecentlyViewedCard';
import NavigationInput from './ui/BrowsePage/NavigateInput';
import FgDialog from './ui/Dialogs/FgDialog';

export default function Browse() {
  const {
    setShowPermissionsDialog,
    togglePropertiesDrawer,
    toggleSidebar,
    setShowConvertFileDialog,
    showPermissionsDialog,
    showPropertiesDrawer,
    showSidebar,
    showConvertFileDialog
  } = useOutletContext<OutletContextType>();

  const { fileBrowserState } = useFileBrowserContext();

  const [showDeleteDialog, setShowDeleteDialog] = React.useState(false);
  const [showRenameDialog, setShowRenameDialog] = React.useState(false);
  const [showNavigationDialog, setShowNavigationDialog] = React.useState(false);
  const [pastedPath, setPastedPath] = React.useState<string>('');

  // Auto-focus the container when component mounts so it can receive paste events
  useEffect(() => {
    const container = document.querySelector(
      '[data-browse-container]'
    ) as HTMLElement;
    if (container) {
      container.focus();
    }
  }, []);

  return (
    <div
      className="flex flex-col h-full min-w-fit max-h-full"
      tabIndex={0}
      data-browse-container
      onPaste={async event => {
        log.debug('React paste event fired!', event);

        // Check if any input, textarea, or contenteditable element is focused
        const activeElement = document.activeElement;
        log.debug('Active element:', activeElement);

        const isTextInputFocused =
          activeElement &&
          (activeElement.tagName === 'INPUT' ||
            activeElement.tagName === 'TEXTAREA' ||
            activeElement.getAttribute('contenteditable') === 'true');

        log.debug('Is text input focused:', isTextInputFocused);

        // Only handle paste if no text input is focused
        if (!isTextInputFocused) {
          log.debug('Handling paste event');
          event.preventDefault();

          try {
            const clipboardText = await navigator.clipboard.readText();
            log.debug('Clipboard text (API):', clipboardText);
            setPastedPath(clipboardText);
            setShowNavigationDialog(true);
          } catch (error) {
            log.debug('Clipboard API failed, using fallback:', error);
            // Fallback to event.clipboardData if clipboard API fails
            const clipboardText = event.clipboardData?.getData('text') || '';
            log.debug('Clipboard text (fallback):', clipboardText);
            setPastedPath(clipboardText);
            setShowNavigationDialog(true);
          }
        } else {
          log.debug('Text input is focused, ignoring paste');
        }
      }}
    >
      <Toolbar
        showPropertiesDrawer={showPropertiesDrawer}
        togglePropertiesDrawer={togglePropertiesDrawer}
        showSidebar={showSidebar}
        toggleSidebar={toggleSidebar}
      />
      <div
        className={`relative grow shrink-0 max-h-[calc(100%-55px)] flex flex-col overflow-y-auto px-2 ${!fileBrowserState.currentFileSharePath ? 'grid grid-cols-2 grid-rows-[60px_1fr] bg-surface-light gap-6 p-6' : ''}`}
      >
        {!fileBrowserState.currentFileSharePath ? (
          <>
            <div className="col-span-2">
              <NavigationInput location="dashboard" />
            </div>
            <RecentlyViewedCard />
            <RecentDataLinksCard />
          </>
        ) : (
          <FileBrowser
            showPropertiesDrawer={showPropertiesDrawer}
            togglePropertiesDrawer={togglePropertiesDrawer}
            setShowRenameDialog={setShowRenameDialog}
            setShowDeleteDialog={setShowDeleteDialog}
            setShowPermissionsDialog={setShowPermissionsDialog}
            setShowConvertFileDialog={setShowConvertFileDialog}
          />
        )}
      </div>
      {showRenameDialog ? (
        <RenameDialog
          showRenameDialog={showRenameDialog}
          setShowRenameDialog={setShowRenameDialog}
        />
      ) : null}
      {showDeleteDialog ? (
        <Delete
          showDeleteDialog={showDeleteDialog}
          setShowDeleteDialog={setShowDeleteDialog}
        />
      ) : null}
      {showPermissionsDialog ? (
        <ChangePermissions
          showPermissionsDialog={showPermissionsDialog}
          setShowPermissionsDialog={setShowPermissionsDialog}
        />
      ) : null}
      {showConvertFileDialog ? (
        <ConvertFileDialog
          showConvertFileDialog={showConvertFileDialog}
          setShowConvertFileDialog={setShowConvertFileDialog}
        />
      ) : null}
      {showNavigationDialog ? (
        <FgDialog
          open={showNavigationDialog}
          onClose={() => {
            setShowNavigationDialog(false);
            setPastedPath('');
          }}
        >
          <NavigationInput
            location="dialog"
            setShowNavigationDialog={setShowNavigationDialog}
            initialValue={pastedPath}
            onDialogClose={() => setPastedPath('')}
          />
        </FgDialog>
      ) : null}
    </div>
  );
}
