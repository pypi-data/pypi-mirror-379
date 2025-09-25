import { Card, List, Typography } from '@material-tailwind/react';
import { TbBrandGithub } from 'react-icons/tb';
import { SiClickup, SiSlack } from 'react-icons/si';
import { IconType } from 'react-icons/lib';

import useVersionNo from '@/hooks/useVersionState';
import useCentralVersion from '@/hooks/useCentralVersion';
import { FgStyledLink } from './ui/widgets/FgLink';

type HelpLink = {
  icon: IconType;
  title: string;
  url: string;
};

export default function Help() {
  const { versionNo } = useVersionNo();
  const { centralVersionState } = useCentralVersion();

  const helpLinks: HelpLink[] = [
    {
      icon: TbBrandGithub,
      title: `View ${versionNo} release notes`,
      url: `https://github.com/JaneliaSciComp/fileglancer/releases/tag/${versionNo}`
    },
    {
      icon: SiClickup,
      title: 'Submit feedback, bug reports, or feature requests',
      url: `https://forms.clickup.com/10502797/f/a0gmd-713/NBUCBCIN78SI2BE71G?Version=${versionNo}&URL=${window.location}`
    },
    {
      icon: SiSlack,
      title: 'Get help on the #fileglancer-support Slack channel',
      url: 'https://hhmi.enterprise.slack.com/archives/C0938N06YN8'
    }
  ];

  return (
    <>
      <div className="flex justify-between mb-6">
        <Typography type="h5" className="text-foreground font-bold">
          Help
        </Typography>
        <div className="text-right">
          <Typography type="lead" className="text-foreground font-bold">
            {`Fileglancer Version ${versionNo}`}
          </Typography>
          {centralVersionState.status === 'loaded' ? (
            <Typography type="small" className="text-muted-foreground">
              {`Fileglancer Central Version ${centralVersionState.version}`}
            </Typography>
          ) : centralVersionState.status === 'loading' ? (
            <Typography type="small" className="text-muted-foreground">
              Loading Fileglancer Central version...
            </Typography>
          ) : centralVersionState.status === 'error' ? (
            <Typography type="small" className="text-muted-foreground">
              Fileglancer Central version unavailable
            </Typography>
          ) : centralVersionState.status === 'not-configured' ? (
            <Typography type="small" className="text-muted-foreground">
              Fileglancer Central server not configured
            </Typography>
          ) : null}
        </div>
      </div>
      <Card className="min-h-max shrink-0">
        <List className="w-fit gap-2 p-4">
          {helpLinks.map(({ icon: Icon, title, url }) => (
            <List.Item
              key={url}
              className="hover:bg-transparent focus:bg-transparent"
            >
              <List.ItemStart>
                <Icon className="icon-large" />
              </List.ItemStart>
              <Typography
                as={FgStyledLink}
                target="_blank"
                rel="noopener noreferrer"
                textSize="large"
                to={url}
              >
                {title}
              </Typography>
            </List.Item>
          ))}
        </List>
      </Card>
    </>
  );
}
