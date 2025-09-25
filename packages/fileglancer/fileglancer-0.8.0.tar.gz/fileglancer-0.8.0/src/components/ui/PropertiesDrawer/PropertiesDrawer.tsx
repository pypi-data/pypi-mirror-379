import * as React from 'react';
import {
  Button,
  Card,
  IconButton,
  Switch,
  Typography,
  Tabs
} from '@material-tailwind/react';
import toast from 'react-hot-toast';
import { HiOutlineDocument, HiOutlineDuplicate, HiX } from 'react-icons/hi';
import { HiOutlineFolder } from 'react-icons/hi2';

import PermissionsTable from '@/components/ui/PropertiesDrawer/PermissionsTable';
import OverviewTable from '@/components/ui/PropertiesDrawer/OverviewTable';
import TicketDetails from '@/components/ui/PropertiesDrawer/TicketDetails';
import FgTooltip from '@/components/ui/widgets/FgTooltip';
import DataLinkDialog from '@/components/ui/Dialogs/DataLink';
import { getPreferredPathForDisplay } from '@/utils';
import { copyToClipboard } from '@/utils/copyText';
import { useFileBrowserContext } from '@/contexts/FileBrowserContext';
import { usePreferencesContext } from '@/contexts/PreferencesContext';
import { useTicketContext } from '@/contexts/TicketsContext';
import { useProxiedPathContext } from '@/contexts/ProxiedPathContext';
import { useExternalBucketContext } from '@/contexts/ExternalBucketContext';
import useDataToolLinks from '@/hooks/useDataToolLinks';

type PropertiesDrawerProps = {
  togglePropertiesDrawer: () => void;
  setShowPermissionsDialog: React.Dispatch<React.SetStateAction<boolean>>;
  setShowConvertFileDialog: React.Dispatch<React.SetStateAction<boolean>>;
};

function CopyPathButton({
  path,
  isDataLink
}: {
  path: string;
  isDataLink?: boolean;
}): JSX.Element {
  return (
    <div className="group flex justify-between items-center min-w-0 max-w-full">
      <FgTooltip label={path} triggerClasses="block truncate">
        <Typography className="text-foreground text-sm truncate">
          <span className="!font-bold">
            {isDataLink ? 'Data Link: ' : 'Path: '}
          </span>
          {path}
        </Typography>
      </FgTooltip>
      <IconButton
        variant="ghost"
        isCircular
        className="text-transparent group-hover:text-foreground shrink-0"
        onClick={async () => {
          const result = await copyToClipboard(path);
          if (result.success) {
            toast.success(
              `${isDataLink ? 'Data link' : 'Path'} copied to clipboard!`
            );
          } else {
            toast.error(
              `Failed to copy ${isDataLink ? 'data link' : 'path'}. Error: ${result.error}`
            );
          }
        }}
      >
        <HiOutlineDuplicate className="icon-small" />
      </IconButton>
    </div>
  );
}

export default function PropertiesDrawer({
  togglePropertiesDrawer,
  setShowPermissionsDialog,
  setShowConvertFileDialog
}: PropertiesDrawerProps): JSX.Element {
  const [showDataLinkDialog, setShowDataLinkDialog] =
    React.useState<boolean>(false);

  const { fileBrowserState } = useFileBrowserContext();
  const { pathPreference, areDataLinksAutomatic } = usePreferencesContext();
  const { ticket } = useTicketContext();
  const { proxiedPath, dataUrl } = useProxiedPathContext();
  const { externalDataUrl } = useExternalBucketContext();
  const {
    handleDialogConfirm,
    handleDialogCancel,
    handleCreateDataLink,
    handleDeleteDataLink
  } = useDataToolLinks(setShowDataLinkDialog);

  const fullPath = getPreferredPathForDisplay(
    pathPreference,
    fileBrowserState.currentFileSharePath,
    fileBrowserState.propertiesTarget?.path
  );

  const tooltipTriggerClasses = 'max-w-[calc(100%-2rem)] truncate';

  return (
    <>
      <Card className="overflow-auto w-full h-full max-h-full p-3 rounded-none shadow-none flex flex-col border-0">
        <div className="flex items-center justify-between gap-4 mb-1 shrink-0">
          <Typography type="h6">Properties</Typography>
          <IconButton
            size="sm"
            variant="ghost"
            color="secondary"
            className="h-8 w-8 rounded-full text-foreground hover:bg-secondary-light/20 shrink-0"
            onClick={() => {
              togglePropertiesDrawer();
            }}
          >
            <HiX className="icon-default" />
          </IconButton>
        </div>

        {fileBrowserState.propertiesTarget ? (
          <div className="shrink-0 flex items-center gap-2 mt-3 mb-4 max-h-min">
            {fileBrowserState.propertiesTarget.is_dir ? (
              <HiOutlineFolder className="icon-default" />
            ) : (
              <HiOutlineDocument className="icon-default" />
            )}
            <FgTooltip
              label={fileBrowserState.propertiesTarget.name}
              triggerClasses={tooltipTriggerClasses}
            >
              <Typography className="font-semibold truncate max-w-min">
                {fileBrowserState.propertiesTarget?.name}
              </Typography>
            </FgTooltip>
          </div>
        ) : (
          <Typography className="mt-3 mb-4">
            Click on a file or folder to view its properties
          </Typography>
        )}
        {fileBrowserState.propertiesTarget ? (
          <Tabs
            key="file-properties-tabs"
            defaultValue="overview"
            className="flex flex-col flex-1 min-h-0 "
          >
            <Tabs.List className="justify-start items-stretch shrink-0 min-w-fit w-full py-2 bg-surface dark:bg-surface-light">
              <Tabs.Trigger
                className="!text-foreground h-full"
                value="overview"
              >
                Overview
              </Tabs.Trigger>

              <Tabs.Trigger
                className="!text-foreground h-full"
                value="permissions"
              >
                Permissions
              </Tabs.Trigger>

              <Tabs.Trigger className="!text-foreground h-full" value="convert">
                Convert
              </Tabs.Trigger>
              <Tabs.TriggerIndicator className="h-full" />
            </Tabs.List>

            {/*Overview panel*/}
            <Tabs.Panel
              value="overview"
              className="flex-1 flex flex-col gap-4 max-w-full p-2"
            >
              <CopyPathButton path={fullPath} />
              <OverviewTable file={fileBrowserState.propertiesTarget} />
              {fileBrowserState.propertiesTarget.is_dir ? (
                <div className="flex flex-col gap-2 min-w-[175px] max-w-full pt-2">
                  <div className="flex items-center gap-2 max-w-full">
                    <Switch
                      id="share-switch"
                      className="before:bg-primary/50 after:border-primary/50 checked:disabled:before:bg-surface checked:disabled:before:border checked:disabled:before:border-surface-dark checked:disabled:after:border-surface-dark"
                      onChange={async () => {
                        if (areDataLinksAutomatic && !proxiedPath) {
                          await handleCreateDataLink();
                        } else {
                          setShowDataLinkDialog(true);
                        }
                      }}
                      checked={externalDataUrl || proxiedPath ? true : false}
                      disabled={externalDataUrl ? true : false}
                    />
                    <Typography
                      as="label"
                      htmlFor="share-switch"
                      className={`${externalDataUrl ? 'cursor-default' : 'cursor-pointer'} text-foreground font-semibold`}
                    >
                      {proxiedPath ? 'Delete data link' : 'Create data link'}
                    </Typography>
                  </div>
                  <Typography
                    type="small"
                    className="text-foreground whitespace-normal w-full"
                  >
                    {externalDataUrl
                      ? 'Public data link already exists since this data is on s3.janelia.org.'
                      : proxiedPath
                        ? 'Deleting the data link will remove data access for collaborators with the link.'
                        : 'Creating a data link allows you to share the data at this path with internal collaborators or use tools to view the data.'}
                  </Typography>
                </div>
              ) : null}
              {externalDataUrl ? (
                <CopyPathButton path={externalDataUrl} isDataLink={true} />
              ) : dataUrl ? (
                <CopyPathButton path={dataUrl} isDataLink={true} />
              ) : null}
            </Tabs.Panel>

            {/*Permissions panel*/}
            <Tabs.Panel
              value="permissions"
              className="flex flex-col max-w-full gap-4 flex-1 p-2"
            >
              <PermissionsTable file={fileBrowserState.propertiesTarget} />
              <Button
                variant="outline"
                onClick={() => {
                  setShowPermissionsDialog(true);
                }}
                className="!rounded-md !text-primary !text-nowrap !self-start"
              >
                Change Permissions
              </Button>
            </Tabs.Panel>

            {/*Task panel*/}
            <Tabs.Panel
              value="convert"
              className="flex flex-col gap-4 flex-1 w-full p-2"
            >
              {ticket ? (
                <TicketDetails />
              ) : (
                <>
                  <Typography className="min-w-64">
                    Scientific Computing can help you convert images to OME-Zarr
                    format, suitable for viewing in external viewers like
                    Neuroglancer.
                  </Typography>
                  <Button
                    variant="outline"
                    onClick={() => {
                      setShowConvertFileDialog(true);
                    }}
                  >
                    Open conversion request
                  </Button>
                </>
              )}
            </Tabs.Panel>
          </Tabs>
        ) : null}
      </Card>
      {showDataLinkDialog && !proxiedPath && !externalDataUrl ? (
        <DataLinkDialog
          tools={false}
          action="create"
          onConfirm={handleDialogConfirm}
          onCancel={handleDialogCancel}
          showDataLinkDialog={showDataLinkDialog}
          setShowDataLinkDialog={setShowDataLinkDialog}
        />
      ) : showDataLinkDialog && proxiedPath ? (
        <DataLinkDialog
          action="delete"
          proxiedPath={proxiedPath}
          handleDeleteDataLink={handleDeleteDataLink}
          showDataLinkDialog={showDataLinkDialog}
          setShowDataLinkDialog={setShowDataLinkDialog}
        />
      ) : null}
    </>
  );
}
