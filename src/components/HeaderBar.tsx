import { Brain, Zap } from "lucide-react";
import { Button } from "@/components/ui/button";
import { ThemeToggle } from "@/components/theme-toggle";

interface HeaderBarProps {
  stats: { totalEpisodes: number; avgReward: number; epsilon: number; qTableSize: number };
  onTrainBatch: () => void;
  isTraining: boolean;
}

const HeaderBar = ({ stats, onTrainBatch, isTraining }: HeaderBarProps) => {
  return (
    <header className="flex items-center justify-between border-b border-border px-4 py-3">
      <div className="flex items-center gap-3">
        <div className="flex items-center gap-2">
          <Brain className="h-6 w-6 text-primary" />
          <h1 className="text-lg font-semibold font-mono text-foreground">
            RL Code Reviewer
          </h1>
        </div>
        <span className="rounded-sm bg-primary/10 px-2 py-0.5 text-xs font-mono text-primary">
          Q-Learning Agent
        </span>
      </div>

      <div className="flex items-center gap-4">
        <div className="flex gap-4 text-xs font-mono text-muted-foreground">
          <span>Episodes: <span className="text-foreground">{stats.totalEpisodes}</span></span>
          <span>Avg Reward: <span className={stats.avgReward >= 0 ? "text-success" : "text-destructive"}>{stats.avgReward}</span></span>
          <span>ε: <span className="text-accent">{stats.epsilon}</span></span>
          <span>Q-States: <span className="text-foreground">{stats.qTableSize}</span></span>
        </div>
        <Button
          size="sm"
          variant="outline"
          onClick={onTrainBatch}
          disabled={isTraining}
          className="gap-1 font-mono text-xs"
        >
          <Zap className="h-3 w-3" />
          Train ×10
        </Button>
        <ThemeToggle />
      </div>
    </header>
  );
};

export default HeaderBar;
