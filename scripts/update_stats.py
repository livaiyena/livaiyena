#!/usr/bin/env python3
"""
GitHub Language Statistics Calculator
Updates README.md with repository language statistics using GitHub API.

Usage:
    python update_stats.py --token YOUR_GITHUB_TOKEN --username YOUR_USERNAME

Requirements:
    - requests library (pip install requests)
    - GitHub Personal Access Token with 'repo' scope
"""

import argparse
import os
import sys
from typing import Dict, List, Tuple
from collections import defaultdict

try:
    import requests
except ImportError:
    print("Error: requests library not found. Install with: pip install requests")
    sys.exit(1)

try:
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
except ImportError:
    print("Error: matplotlib library not found. Install with: pip install matplotlib")
    sys.exit(1)


class GitHubStatsCalculator:
    """Calculate language statistics across all user repositories."""
    
    def __init__(self, username: str, token: str):
        """
        Initialize calculator with GitHub credentials.
        
        Args:
            username: GitHub username
            token: GitHub Personal Access Token
        """
        self.username = username
        self.token = token
        self.session = requests.Session()
        self.session.headers.update({
            'Authorization': f'token {token}',
            'Accept': 'application/vnd.github.v3+json',
            'User-Agent': 'GitHub-Stats-Calculator'
        })
        self.base_url = 'https://api.github.com'
    
    def check_rate_limit(self) -> Tuple[int, int]:
        """
        Check GitHub API rate limit status.
        
        Returns:
            Tuple of (remaining requests, limit reset timestamp)
        """
        response = self.session.get(f'{self.base_url}/rate_limit')
        if response.status_code == 200:
            data = response.json()
            core = data['resources']['core']
            return core['remaining'], core['reset']
        return 0, 0
    
    def get_repositories(self) -> List[Dict]:
        """
        Fetch all repositories for the user.
        
        Returns:
            List of repository dictionaries
        """
        repos = []
        page = 1
        per_page = 100
        
        while True:
            remaining, _ = self.check_rate_limit()
            if remaining < 10:
                print(f"Warning: Only {remaining} API requests remaining")
            
            url = f'{self.base_url}/users/{self.username}/repos'
            params = {
                'page': page,
                'per_page': per_page,
                'type': 'owner', 
                'sort': 'updated'
            }
            
            response = self.session.get(url, params=params)
            
            if response.status_code == 404:
                print(f"Error: User '{self.username}' not found")
                sys.exit(1)
            elif response.status_code == 401:
                print("Error: Invalid GitHub token")
                sys.exit(1)
            elif response.status_code != 200:
                print(f"Error fetching repositories: {response.status_code}")
                print(response.text)
                sys.exit(1)
            
            batch = response.json()
            if not batch:
                break
            
            repos.extend(batch)
            page += 1
        
        return repos
    
    def get_language_stats(self, repo_name: str) -> Dict[str, int]:
        """
        Get language statistics for a specific repository.
        
        Args:
            repo_name: Name of the repository
            
        Returns:
            Dictionary mapping language names to byte counts
        """
        url = f'{self.base_url}/repos/{self.username}/{repo_name}/languages'
        response = self.session.get(url)
        
        if response.status_code == 200:
            return response.json()
        return {}
    
    def calculate_total_stats(self, include_forks: bool = False) -> Dict[str, int]:
        """
        Calculate total language statistics across all repositories.
        
        Args:
            include_forks: Whether to include forked repositories
            
        Returns:
            Dictionary mapping language names to total byte counts
        """
        repos = self.get_repositories()
        
        if not include_forks:
            repos = [repo for repo in repos if not repo['fork']]
        
        print(f"Analyzing {len(repos)} repositories...")
        
        total_stats = defaultdict(int)
        
        for i, repo in enumerate(repos, 1):
            repo_name = repo['name']
            print(f"[{i}/{len(repos)}] Processing: {repo_name}")
            
            lang_stats = self.get_language_stats(repo_name)
            for language, bytes_count in lang_stats.items():
                total_stats[language] += bytes_count
        
        return dict(total_stats)
    
    def format_statistics(self, stats: Dict[str, int]) -> str:
        """
        Format statistics as markdown with progress bars.
        
        Args:
            stats: Dictionary of language statistics
            
        Returns:
            Formatted markdown string with progress bars
        """
        # Filter out web development languages
        excluded_languages = {'HTML', 'CSS', 'JavaScript', 'TypeScript', 'SCSS', 'Less'}
        filtered_stats = {
            lang: bytes_count 
            for lang, bytes_count in stats.items() 
            if lang not in excluded_languages
        }
        
        if not filtered_stats:
            return "No language data available.\n"
        
        total_bytes = sum(filtered_stats.values())
        sorted_stats = sorted(filtered_stats.items(), key=lambda x: x[1], reverse=True)
        
        # Take top 8 languages to avoid clutter
        top_languages = sorted_stats[:8]
        
        lines = []
        
        for language, bytes_count in top_languages:
            percentage = (bytes_count / total_bytes) * 100
            formatted_bytes = self._format_bytes(bytes_count)
            
            # Create progress bar (50 characters wide)
            bar_length = 50
            filled_length = int(bar_length * percentage / 100)
            bar = '█' * filled_length + '░' * (bar_length - filled_length)
            
            # Format: Language name (padded), bar, percentage, bytes
            lines.append(f"**{language:<12}** `{bar}` {percentage:5.1f}% ({formatted_bytes})")
        
        lines.append(f"\n**Total Code:** {self._format_bytes(total_bytes)}")
        
        return '\n'.join(lines)
    
    def create_chart(self, stats: Dict[str, int], output_path: str = 'stats-chart.svg') -> None:
        """
        Create a modern, compact chart with colored legend.
        
        Args:
            stats: Dictionary of language statistics
            output_path: Path to save the chart
        """
        excluded_languages = {'HTML', 'CSS', 'JavaScript', 'TypeScript', 'SCSS', 'Less'}
        filtered_stats = {
            lang: bytes_count 
            for lang, bytes_count in stats.items() 
            if lang not in excluded_languages
        }
        
        if not filtered_stats:
            print("No language data available for chart")
            return
        
        total_bytes = sum(filtered_stats.values())
        sorted_stats = sorted(filtered_stats.items(), key=lambda x: x[1], reverse=True)
        top_languages = sorted_stats[:8]
        
        languages = [lang for lang, _ in top_languages]
        percentages = [(bytes_count / total_bytes) * 100 for _, bytes_count in top_languages]
        
        # Vibrant color scheme
        color_map = {
            'Python': '#3572A5',
            'C': '#555555',
            'C++': '#f34b7d',
            'Java': '#b07219',
            'JavaScript': '#f1e05a',
            'Shell': '#89e051',
            'Bash': '#89e051',
            'PLpgSQL': '#336791',
            'SQL': '#e38c00',
            'Dockerfile': '#384d54',
            'Batchfile': '#C1F12E',
        }
        colors = [color_map.get(lang, '#8b949e') for lang in languages]
        
        # Create compact figure
        fig = plt.figure(figsize=(10, 5), facecolor='#0d1117', dpi=100)
        
        # Main layout - single horizontal bar at top, legend below
        ax_bar = plt.subplot2grid((10, 1), (0, 0), rowspan=2, fig=fig)
        ax_legend = plt.subplot2grid((10, 1), (3, 0), rowspan=7, fig=fig)
        
        # Create stacked horizontal bar
        left = 0
        for i, (pct, color) in enumerate(zip(percentages, colors)):
            ax_bar.barh(0, pct, left=left, height=0.8, 
                       color=color, edgecolor='none')
            left += pct
        
        # Style bar axes
        ax_bar.set_xlim(0, 100)
        ax_bar.set_ylim(-0.5, 0.5)
        ax_bar.axis('off')
        ax_bar.set_facecolor('#0d1117')
        
        # Title
        ax_bar.text(0, 1.2, 'Most Used Languages', 
                   color='#e6edf3', fontsize=16, 
                   fontweight='700', va='bottom',
                   fontfamily='sans-serif')
        
        # Legend area - create grid layout
        ax_legend.axis('off')
        ax_legend.set_xlim(0, 2)
        ax_legend.set_ylim(0, 4)
        ax_legend.set_facecolor('#0d1117')
        
        # Display legend items in 2 columns
        col_width = 1.0
        row_height = 0.5
        items_per_col = 4
        
        for i, (lang, pct, color) in enumerate(zip(languages, percentages, colors)):
            col = i // items_per_col
            row = i % items_per_col
            
            x = col * col_width
            y = 3.5 - (row * row_height)
            
            # Color dot
            ax_legend.plot(x + 0.02, y, 'o', color=color, 
                          markersize=10, markeredgecolor='none')
            
            # Language name and percentage
            ax_legend.text(x + 0.08, y, f'{lang} {pct:.1f}%', 
                          color='#e6edf3', fontsize=11,
                          va='center', fontweight='500',
                          fontfamily='sans-serif')
        
        # Tight layout
        plt.tight_layout(pad=1)
        
        # Save
        plt.savefig(output_path, format='svg', 
                   facecolor='#0d1117', 
                   edgecolor='none', 
                   bbox_inches='tight',
                   pad_inches=0.2)
        plt.close()
        print(f"✓ Chart saved to: {output_path}")
    
    
    @staticmethod
    def _format_bytes(bytes_count: int) -> str:
        """Format byte count with appropriate unit."""
        for unit in ['B', 'KB', 'MB', 'GB']:
            if bytes_count < 1024.0:
                return f"{bytes_count:.2f} {unit}"
            bytes_count /= 1024.0
        return f"{bytes_count:.2f} TB"


def update_readme(stats_markdown: str, readme_path: str = 'README.md') -> None:
    """
    Update README.md with new statistics.
    
    Args:
        stats_markdown: Formatted statistics markdown
        readme_path: Path to README.md file
    """
    marker_start = '<!-- STATS_START -->'
    marker_end = '<!-- STATS_END -->'
    
    if not os.path.exists(readme_path):
        print(f"Error: {readme_path} not found")
        sys.exit(1)
    
    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if marker_start not in content or marker_end not in content:
        print(f"Error: Markers {marker_start} and {marker_end} not found in README")
        sys.exit(1)
    
    # Find positions of markers
    start_idx = content.find(marker_start) + len(marker_start)
    end_idx = content.find(marker_end)
    
    # Construct new content
    new_content = (
        content[:start_idx] +
        '\n' + stats_markdown + '\n' +
        content[end_idx:]
    )
    
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"\n✓ Successfully updated {readme_path}")


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description='Calculate and update GitHub language statistics'
    )
    parser.add_argument(
        '--username',
        required=True,
        help='GitHub username'
    )
    parser.add_argument(
        '--token',
        help='GitHub Personal Access Token (or set GITHUB_TOKEN env var)'
    )
    parser.add_argument(
        '--include-forks',
        action='store_true',
        help='Include forked repositories in statistics'
    )
    parser.add_argument(
        '--readme',
        default='README.md',
        help='Path to README.md file (default: README.md)'
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Print statistics without updating README'
    )
    
    args = parser.parse_args()
    
    # Get token from args or environment
    token = args.token or os.environ.get('GITHUB_TOKEN')
    if not token:
        print("Error: GitHub token required (--token or GITHUB_TOKEN env var)")
        sys.exit(1)
    
    # Initialize calculator and fetch stats
    calculator = GitHubStatsCalculator(args.username, token)
    
    print(f"Fetching repository data for user: {args.username}\n")
    stats = calculator.calculate_total_stats(include_forks=args.include_forks)
    
    # Generate chart
    chart_path = os.path.join(os.path.dirname(args.readme) or '.', 'stats-chart.svg')
    calculator.create_chart(stats, chart_path)
    
    # Format text output
    stats_markdown = calculator.format_statistics(stats)
    
    if args.dry_run:
        print("\n=== Statistics Preview ===\n")
        print(stats_markdown)
    else:
        update_readme(stats_markdown, args.readme)


if __name__ == '__main__':
    main()
