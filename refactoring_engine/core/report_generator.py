# Generates before-after diff report

import difflib
import os
from datetime import datetime

class ReportGenerator:
    def __init__(self, settings):
        self.settings = settings
        self.report_dir = os.path.join('reports')
        os.makedirs(self.report_dir, exist_ok=True)

    def generate(self, results):
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        report_path = os.path.join(self.report_dir, f'report_{timestamp}.md')
        with open(report_path, 'w', encoding='utf-8') as f:
            for file, (before, after) in results.items():
                diff = difflib.unified_diff(
                    before.splitlines(), after.splitlines(),
                    fromfile=f'{file} (before)',
                    tofile=f'{file} (after)',
                    lineterm=''
                )
                f.write(f'## {file}\n')
                f.write('\n'.join(diff) + '\n\n')
        return report_path
